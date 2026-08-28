from typing import List
import re

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# ============================================================
# 1. FASTAPI APP
# ============================================================

app = FastAPI(
    title="Conversational RAG API",
    description="Day 24 FastAPI and RAG API",
    version="1.0.0"
)


# ============================================================
# 2. PYDANTIC MODELS
# ============================================================

class Item(BaseModel):
    name: str = Field(..., min_length=1)
    description: str
    price: float = Field(..., gt=0)


class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)


class AskResponse(BaseModel):
    answer: str
    sources: List[str]
    confidence: float


# ============================================================
# 3. SAMPLE ITEMS
# ============================================================

items = {
    1: {
        "id": 1,
        "name": "Laptop",
        "description": "MacBook Air",
        "price": 1200.0
    },
    2: {
        "id": 2,
        "name": "Keyboard",
        "description": "Wireless keyboard",
        "price": 50.0
    }
}


# ============================================================
# 4. RAG KNOWLEDGE BASE
# ============================================================

documents = [
    {
        "source": "rag_basics.txt",
        "text": """
        Retrieval Augmented Generation (RAG) combines information
        retrieval with large language models. Relevant documents
        are retrieved first and then provided to the language model
        as context for generating an answer.
        """
    },
    {
        "source": "vector_database.txt",
        "text": """
        Vector databases store embeddings and allow semantic
        similarity search. They are commonly used in RAG systems
        to retrieve relevant information.
        """
    },
    {
        "source": "fastapi_ai.txt",
        "text": """
        FastAPI is a modern Python web framework that is useful
        for building APIs for AI applications. It supports async
        programming, automatic documentation and Pydantic validation.
        """
    },
    {
        "source": "context_engineering.txt",
        "text": """
        Context engineering focuses on selecting and organizing
        relevant information before sending it to a language model.
        Conversation memory and context compression help control
        context size.
        """
    }
]


# ============================================================
# 5. LOAD RAG SYSTEM ON STARTUP
# ============================================================

rag_system = None


@app.on_event("startup")
async def startup_event():

    global rag_system

    print("Loading RAG system...")

    rag_system = {
        "documents": documents,
        "status": "loaded"
    }

    print("RAG system loaded successfully.")


# ============================================================
# 6. HEALTH ENDPOINT
# ============================================================

@app.get("/health")
async def health_check():

    return {
        "status": "healthy",
        "rag_loaded": rag_system is not None
    }


# ============================================================
# 7. GET ITEM
# ============================================================

@app.get(
    "/items/{id}",
    response_model=ItemResponse
)
async def get_item(id: int):

    if id not in items:

        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return items[id]


# ============================================================
# 8. CREATE ITEM
# ============================================================

@app.post(
    "/items",
    response_model=ItemResponse,
    status_code=201
)
async def create_item(item: Item):

    new_id = max(items.keys()) + 1

    new_item = {
        "id": new_id,
        "name": item.name,
        "description": item.description,
        "price": item.price
    }

    items[new_id] = new_item

    return new_item


# ============================================================
# 9. RETRIEVE DOCUMENTS
# ============================================================

def retrieve_documents(question: str):

    clean_question = re.sub(
        r"[^\w\s]",
        "",
        question.lower()
    )

    question_words = set(
        clean_question.split()
    )

    results = []

    for document in documents:

        clean_text = re.sub(
            r"[^\w\s]",
            "",
            document["text"].lower()
        )

        score = 0

        for word in question_words:

            if len(word) > 2 and word in clean_text:

                score += 1

        if score > 0:

            results.append({
                "source": document["source"],
                "text": document["text"],
                "score": score
            })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:3]


# ============================================================
# 10. GENERATE ANSWER
# ============================================================

def generate_answer(question: str, retrieved_documents):

    if not retrieved_documents:
        return None

    context = "\n".join(
        document["text"].strip()
        for document in retrieved_documents
    )

    answer = (
        f"Question: {question}\n\n"
        f"Answer based on retrieved context:\n\n"
        f"{context}"
    )

    return answer


# ============================================================
# 11. RAG /ASK ENDPOINT
# ============================================================

@app.post(
    "/ask",
    response_model=AskResponse
)
async def ask_question(request: AskRequest):

    try:

        question = request.question.strip()

        # Invalid input
        if not question:

            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )

        # Check RAG system
        if rag_system is None:

            raise HTTPException(
                status_code=500,
                detail="RAG system is not loaded"
            )

        # Retrieve
        retrieved_documents = retrieve_documents(
            question
        )

        # No results
        if not retrieved_documents:

            raise HTTPException(
                status_code=404,
                detail="No relevant documents found"
            )

        # Generate
        answer = generate_answer(
            question,
            retrieved_documents
        )

        if answer is None:

            raise HTTPException(
                status_code=500,
                detail="Failed to generate answer"
            )

        # Sources
        sources = [
            document["source"]
            for document in retrieved_documents
        ]

        # Confidence
        confidence = min(
            0.95,
            0.60 + len(retrieved_documents) * 0.10
        )

        return {
            "answer": answer,
            "sources": sources,
            "confidence": confidence
        }

    except HTTPException:
        raise

    except Exception as e:

        print("Error:", e)

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# ============================================================
# 12. ROOT ENDPOINT
# ============================================================

@app.get("/")
async def root():

    return {
        "message": "Conversational RAG API is running",
        "docs": "/docs",
        "redoc": "/redoc"
    }
