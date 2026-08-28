import os
import io
import re
import json
import time
import uuid
import logging
import threading
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Optional

import numpy as np
import faiss
from rank_bm25 import BM25Okapi
from dotenv import load_dotenv

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from openai import AsyncOpenAI


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

CHAT_MODEL = os.getenv(
    "OPENAI_CHAT_MODEL",
    "gpt-4o-mini"
)

EMBEDDING_MODEL = os.getenv(
    "OPENAI_EMBEDDING_MODEL",
    "text-embedding-3-small"
)

SEMANTIC_WEIGHT = float(
    os.getenv("SEMANTIC_WEIGHT", "0.70")
)

BM25_WEIGHT = float(
    os.getenv("BM25_WEIGHT", "0.30")
)

CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", "800")
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", "120")
)

CANDIDATE_K = int(
    os.getenv("CANDIDATE_K", "20")
)

FINAL_K = int(
    os.getenv("FINAL_K", "5")
)


# ============================================================
# DATA DIRECTORIES
# ============================================================

DATA_DIR = Path(
    os.getenv("RAG_DATA_DIR", "./rag_data")
)

UPLOAD_DIR = DATA_DIR / "uploads"

METADATA_FILE = DATA_DIR / "metadata.json"

DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    ),
)

logger = logging.getLogger("day25-rag")


# ============================================================
# OPENAI CLIENT
# ============================================================

client: Optional[AsyncOpenAI] = None

if OPENAI_API_KEY:
    client = AsyncOpenAI(
        api_key=OPENAI_API_KEY
    )


# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="Day 25 - Production RAG API",
    description=(
        "Production-ready RAG API using "
        "FAISS + BM25 hybrid search, "
        "query expansion and LLM re-ranking."
    ),
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# PYDANTIC MODELS
# ============================================================

class AskRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )

    top_k: int = Field(
        default=FINAL_K,
        ge=1,
        le=10
    )

    use_query_expansion: bool = True

    use_reranking: bool = True


class SearchRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20
    )

    use_hybrid: bool = True


class Source(BaseModel):
    document_id: str
    filename: str
    chunk_id: int
    score: float
    retrieval_type: str
    text: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]
    processing_time_seconds: float


class SearchResponse(BaseModel):
    query: str
    results: list[Source]
    processing_time_seconds: float


class DocumentInfo(BaseModel):
    id: str
    filename: str
    size_bytes: int
    chunks: int
    uploaded_at: str


class DocumentListResponse(BaseModel):
    count: int
    documents: list[DocumentInfo]


class DeleteResponse(BaseModel):
    message: str
    document_id: str


class HealthResponse(BaseModel):
    status: str
    indexed_documents: int
    indexed_chunks: int
    memory_usage_mb: float
    openai_configured: bool

# ============================================================
# IN-MEMORY RAG STORAGE
# ============================================================

documents_store: dict[str, dict[str, Any]] = {}
chunks_store: list[dict[str, Any]] = []

faiss_index: Optional[faiss.IndexFlatIP] = None

bm25_index: Optional[BM25Okapi] = None

bm25_corpus: list[dict[str, Any]] = []

storage_lock = threading.Lock()


# ============================================================
# TEXT PROCESSING
# ============================================================

def normalize_text(text: str) -> str:
    """Clean and normalize extracted text."""
    text = text.replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize(text: str) -> list[str]:
    """Simple tokenizer for BM25."""
    return re.findall(
        r"\b\w+\b",
        text.lower()
    )


def chunk_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP
) -> list[str]:
    """
    Split text into overlapping word-based chunks.
    """

    text = normalize_text(text)

    if not text:
        return []

    words = text.split()

    if overlap >= chunk_size:
        raise ValueError(
            "CHUNK_OVERLAP must be smaller than CHUNK_SIZE."
        )

    chunks = []

    start = 0

    while start < len(words):

        end = min(
            start + chunk_size,
            len(words)
        )

        chunk = " ".join(
            words[start:end]
        )

        if chunk:
            chunks.append(chunk)

        if end >= len(words):
            break

        start = end - overlap

    return chunks


# ============================================================
# DOCUMENT TEXT EXTRACTION
# ============================================================

def extract_text_from_file(
    filename: str,
    file_bytes: bytes
) -> str:
    """
    Extract text from TXT, MD and PDF files.
    """

    extension = Path(
        filename
    ).suffix.lower()

    if extension in {
        ".txt",
        ".md",
        ".csv"
    }:
        return file_bytes.decode(
            "utf-8",
            errors="ignore"
        )

    if extension == ".pdf":

        from pypdf import PdfReader

        reader = PdfReader(
            io.BytesIO(file_bytes)
        )

        pages = []

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                pages.append(
                    page_text
                )

        return "\n".join(pages)

    raise ValueError(
        "Unsupported file type. "
        "Use PDF, TXT, MD or CSV."
    )


# ============================================================
# OPENAI EMBEDDINGS
# ============================================================

async def create_embeddings(
    texts: list[str]
) -> np.ndarray:

    if not client:
        raise RuntimeError(
            "OpenAI API key is not configured."
        )

    if not texts:
        return np.empty(
            (0, 1536),
            dtype="float32"
        )

    response = await client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )

    vectors = np.array(
        [
            item.embedding
            for item in response.data
        ],
        dtype="float32"
    )

    # Normalize vectors so inner product
    # behaves like cosine similarity.
    faiss.normalize_L2(vectors)

    return vectors


# ============================================================
# REBUILD BM25 INDEX
# ============================================================

def rebuild_bm25_index() -> None:

    global bm25_index
    global bm25_corpus

    bm25_corpus = list(
        chunks_store
    )

    if not bm25_corpus:

        bm25_index = None

        return

    tokenized_corpus = [
        tokenize(
            item["text"]
        )
        for item in bm25_corpus
    ]

    bm25_index = BM25Okapi(
        tokenized_corpus
    )


# ============================================================
# REBUILD FAISS INDEX
# ============================================================

def rebuild_faiss_index(
    embeddings: Optional[np.ndarray] = None
) -> None:

    global faiss_index

    if not chunks_store:

        faiss_index = None

        return

    if embeddings is None:

        raise ValueError(
            "Embeddings are required "
            "to rebuild FAISS index."
        )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(
        embeddings
    )

    faiss_index = index


# ============================================================
# HYBRID SCORE NORMALIZATION
# ============================================================

def min_max_normalize(
    scores: np.ndarray
) -> np.ndarray:

    if len(scores) == 0:
        return scores

    min_score = scores.min()
    max_score = scores.max()

    if max_score - min_score < 1e-12:

        return np.ones_like(
            scores,
            dtype="float32"
        )

    return (
        (scores - min_score)
        /
        (max_score - min_score)
    )


# ============================================================
# HYBRID SEARCH
# ============================================================

async def hybrid_search(
    query: str,
    top_k: int = CANDIDATE_K
) -> list[dict[str, Any]]:

    if not chunks_store:
        return []

    if not client:
        raise RuntimeError(
            "OpenAI API key is not configured."
        )

    query_embedding = await create_embeddings(
        [query]
    )

    # --------------------------------------------------------
    # SEMANTIC SEARCH
    # --------------------------------------------------------

    semantic_scores = np.zeros(
        len(chunks_store),
        dtype="float32"
    )

    if faiss_index is not None:

        search_k = min(
            top_k,
            len(chunks_store)
        )

        distances, indices = faiss_index.search(
            query_embedding,
            search_k
        )

        for score, idx in zip(
            distances[0],
            indices[0]
        ):

            if idx >= 0:
                semantic_scores[idx] = score

    # --------------------------------------------------------
    # BM25 SEARCH
    # --------------------------------------------------------

    keyword_scores = np.zeros(
        len(chunks_store),
        dtype="float32"
    )

    if bm25_index is not None:

        query_tokens = tokenize(
            query
        )

        scores = bm25_index.get_scores(
            query_tokens
        )

        keyword_scores = np.array(
            scores,
            dtype="float32"
        )

    # --------------------------------------------------------
    # NORMALIZE BOTH SCORE TYPES
    # --------------------------------------------------------

    semantic_normalized = (
        min_max_normalize(
            semantic_scores
        )
    )

    keyword_normalized = (
        min_max_normalize(
            keyword_scores
        )
    )

    # --------------------------------------------------------
    # 70% SEMANTIC + 30% KEYWORD
    # --------------------------------------------------------

    hybrid_scores = (
        SEMANTIC_WEIGHT
        *
        semantic_normalized
        +
        BM25_WEIGHT
        *
        keyword_normalized
    )

    # --------------------------------------------------------
    # TOP RESULTS
    # --------------------------------------------------------

    result_count = min(
        top_k,
        len(chunks_store)
    )

    top_indices = np.argsort(
        hybrid_scores
    )[::-1][:result_count]

    results = []

    for idx in top_indices:

        item = dict(
            chunks_store[idx]
        )

        item["score"] = float(
            hybrid_scores[idx]
        )

        item["semantic_score"] = float(
            semantic_normalized[idx]
        )

        item["keyword_score"] = float(
            keyword_normalized[idx]
        )

        item["retrieval_type"] = "hybrid"

        results.append(
            item
        )

    return results

# ============================================================
# DOCUMENT MANAGEMENT HELPERS
# ============================================================

def save_metadata() -> None:
    """Save document metadata to JSON."""

    data = {
        "documents": documents_store,
        "chunks": chunks_store
    }

    METADATA_FILE.write_text(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


async def index_document(
    document_id: str,
    filename: str,
    file_bytes: bytes
) -> dict[str, Any]:

    global chunks_store

    # Extract text
    text = extract_text_from_file(
        filename,
        file_bytes
    )

    text = normalize_text(text)

    if not text:
        raise ValueError(
            "No readable text found in the document."
        )

    # Create chunks
    chunks = chunk_text(text)

    if not chunks:
        raise ValueError(
            "Document could not be divided into chunks."
        )

    logger.info(
        "Creating embeddings for %s chunks",
        len(chunks)
    )

    # Create embeddings
    embeddings = await create_embeddings(
        chunks
    )

    # Document metadata
    uploaded_at = datetime.now(
        timezone.utc
    ).isoformat()

    documents_store[document_id] = {
        "id": document_id,
        "filename": filename,
        "size_bytes": len(file_bytes),
        "chunks": len(chunks),
        "uploaded_at": uploaded_at
    }

    # Add chunks
    new_chunks = []

    for index, chunk in enumerate(chunks):

        new_chunks.append({
            "document_id": document_id,
            "filename": filename,
            "chunk_id": index,
            "text": chunk
        })

    # Store chunks
    chunks_store.extend(
        new_chunks
    )

    # Rebuild complete FAISS index
    all_texts = [
        item["text"]
        for item in chunks_store
    ]

    all_embeddings = await create_embeddings(
        all_texts
    )

    rebuild_faiss_index(
        all_embeddings
    )

    # Rebuild BM25
    rebuild_bm25_index()

    # Save metadata
    save_metadata()

    # Save original file
    file_path = UPLOAD_DIR / (
        f"{document_id}_{filename}"
    )

    file_path.write_bytes(
        file_bytes
    )

    logger.info(
        "Document indexed successfully: %s",
        filename
    )

    return documents_store[
        document_id
    ]


# ============================================================
# DOCUMENT UPLOAD ENDPOINT
# ============================================================

@app.post(
    "/documents/upload",
    response_model=DocumentInfo
)
async def upload_document(
    file: UploadFile = File(...)
):

    start_time = time.perf_counter()

    try:

        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="Filename is required."
            )

        allowed_extensions = {
            ".pdf",
            ".txt",
            ".md",
            ".csv"
        }

        extension = Path(
            file.filename
        ).suffix.lower()

        if extension not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=(
                    "Unsupported file type. "
                    "Use PDF, TXT, MD or CSV."
                )
            )

        file_bytes = await file.read()

        if not file_bytes:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        document_id = str(
            uuid.uuid4()
        )

        logger.info(
            "Uploading document: %s",
            file.filename
        )

        with storage_lock:

            metadata = await index_document(
                document_id=document_id,
                filename=file.filename,
                file_bytes=file_bytes
            )

        processing_time = (
            time.perf_counter()
            - start_time
        )

        logger.info(
            "Upload completed in %.3f seconds",
            processing_time
        )

        return DocumentInfo(
            **metadata
        )

    except HTTPException:
        raise

    except Exception as exc:

        logger.exception(
            "Document upload failed"
        )

        raise HTTPException(
            status_code=500,
            detail=f"Upload failed: {str(exc)}"
        )


# ============================================================
# LIST DOCUMENTS
# ============================================================

@app.get(
    "/documents",
    response_model=DocumentListResponse
)
async def list_documents():

    try:
        documents = [
            DocumentInfo(**document)
            for document in documents_store.values()
        ]

        return DocumentListResponse(
            count=len(documents),
            documents=documents
        )

    except Exception as exc:

        logger.exception(
            "Failed to list documents"
        )

        raise HTTPException(
            status_code=500,
            detail=f"Could not list documents: {str(exc)}"
        )


# ============================================================
# DELETE DOCUMENT
# ============================================================

@app.delete(
    "/documents/{document_id}",
    response_model=DeleteResponse
)
async def delete_document(
    document_id: str
):

    global chunks_store

    try:

        if document_id not in documents_store:

            raise HTTPException(
                status_code=404,
                detail="Document not found."
            )

        filename = documents_store[
            document_id
        ]["filename"]

        logger.info(
            "Deleting document: %s",
            filename
        )

        # ----------------------------------------------------
        # Remove document metadata
        # ----------------------------------------------------

        del documents_store[
            document_id
        ]

        # ----------------------------------------------------
        # Remove document chunks
        # ----------------------------------------------------

        chunks_store = [
            chunk
            for chunk in chunks_store
            if chunk["document_id"] != document_id
        ]

        # ----------------------------------------------------
        # Rebuild indexes
        # ----------------------------------------------------

        if chunks_store:

            all_texts = [
                chunk["text"]
                for chunk in chunks_store
            ]

            all_embeddings = await create_embeddings(
                all_texts
            )

            rebuild_faiss_index(
                all_embeddings
            )

            rebuild_bm25_index()

        else:

            global faiss_index
            global bm25_index

            faiss_index = None
            bm25_index = None

        # ----------------------------------------------------
        # Delete saved file
        # ----------------------------------------------------

        for file_path in UPLOAD_DIR.glob(
            f"{document_id}_*"
        ):

            try:
                file_path.unlink()

            except Exception:
                logger.warning(
                    "Could not delete file: %s",
                    file_path
                )

        # ----------------------------------------------------
        # Save updated metadata
        # ----------------------------------------------------

        save_metadata()

        logger.info(
            "Document deleted successfully: %s",
            document_id
        )

        return DeleteResponse(
            message="Document deleted successfully.",
            document_id=document_id
        )

    except HTTPException:
        raise

    except Exception as exc:

        logger.exception(
            "Document deletion failed"
        )

        raise HTTPException(
            status_code=500,
            detail=f"Delete failed: {str(exc)}"
        )
