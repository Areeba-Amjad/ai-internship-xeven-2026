# Day 25 — Production-Ready RAG & FastAPI Integration

## 📌 Overview

Day 25 focuses on building a production-oriented Retrieval Augmented Generation (RAG) system and exposing it through a FastAPI REST API.

The project combines:

* FAISS semantic search
* BM25 keyword search
* Hybrid retrieval
* Re-ranking
* Query expansion concepts
* Document chunking
* Embeddings
* FastAPI
* Pydantic validation
* Async endpoints
* Error handling
* Logging
* CORS
* Environment variables

---

## 🏗️ Architecture

```text
                     User
                       │
                       ▼
                 FastAPI API
                       │
             ┌─────────┴─────────┐
             │                   │
          /search              /ask
             │                   │
             ▼                   ▼
       Hybrid Retrieval     Hybrid Retrieval
             │                   │
       ┌─────┴─────┐       Re-ranking
       │           │           │
     FAISS       BM25        Top 5
       │           │           │
       └─────┬─────┘           ▼
             │              Context
             ▼                 │
        Candidates             ▼
                         OpenAI LLM
                              │
                              ▼
                       Answer + Sources
```

---

## 🔎 Retrieval Strategy

### Dense Retrieval

FAISS is used for semantic vector search.

```text
Query → Embedding → FAISS → Relevant Chunks
```

### Sparse Retrieval

BM25 is used for keyword-based search.

```text
Query → Tokenization → BM25 → Relevant Chunks
```

### Hybrid Retrieval

Both methods are combined:

```text
70% Semantic Search
+
30% Keyword Search
=
Hybrid Search
```

Hybrid retrieval provides both semantic understanding and exact keyword matching.

---

## 🎯 Re-ranking

The retrieval pipeline can retrieve a larger candidate set before applying relevance scoring.

```text
Query
  ↓
Top 20 Candidates
  ↓
Relevance Scoring
  ↓
Top 5
  ↓
Final Context
```

This improves the precision of the context provided to the LLM.

---

## 📚 Document Processing

Uploaded documents follow this pipeline:

```text
File Upload
     ↓
Text Extraction
     ↓
Chunking
     ↓
Embedding Generation
     ↓
FAISS Index
     ↓
BM25 Index
     ↓
Metadata Storage
```

---

## 🚀 API Endpoints

| Method | Endpoint            | Purpose                        |
| ------ | ------------------- | ------------------------------ |
| POST   | `/documents/upload` | Upload and index a document    |
| GET    | `/documents`        | List indexed documents         |
| DELETE | `/documents/{id}`   | Delete a document              |
| POST   | `/search`           | Perform semantic/hybrid search |
| POST   | `/ask`              | Ask a RAG question             |
| GET    | `/health`           | Check system health            |

---

## ⚙️ Installation

Create and activate the Conda environment:

```bash
conda activate embeddings
```

Install required packages:

```bash
python -m pip install fastapi uvicorn openai python-dotenv rank-bm25 pypdf faiss-cpu
```

---

## 🔐 Environment Configuration

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key
```

Never commit `.env` to GitHub.

The `.gitignore` file should contain:

```text
.env
__pycache__/
.ipynb_checkpoints/
```

---

## ▶️ Run the API

From the Day25 directory:

```bash
python -m uvicorn main:app --reload --port 8000
```

The API runs at:

```text
http://127.0.0.1:8000
```

---

## ❤️ Health Check

```bash
curl http://127.0.0.1:8000/health
```

Example response:

```json
{
  "status": "healthy",
  "message": "Day 25 RAG API is running"
}
```

---

## 📄 Upload Document

```bash
curl -X POST \
"http://127.0.0.1:8000/documents/upload" \
-F "file=@test_document.txt"
```

The API extracts the text, creates chunks, generates embeddings, and updates the retrieval indexes.

---

## 📑 List Documents

```bash
curl http://127.0.0.1:8000/documents
```

---

## 🔍 Hybrid Search

```bash
curl -X POST \
"http://127.0.0.1:8000/search" \
-H "Content-Type: application/json" \
-d '{"query":"What is RAG?","top_k":5,"use_hybrid":true}'
```

The search endpoint returns relevant chunks and their metadata.

---

## 🤖 RAG Question Answering

```bash
curl -X POST \
"http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d '{"question":"What is Retrieval Augmented Generation?"}'
```

The RAG pipeline retrieves relevant context and uses the LLM to generate an answer with sources.

---

## 🛠️ Technologies

* Python 3.11
* FastAPI
* Uvicorn
* OpenAI API
* FAISS
* BM25
* rank-bm25
* Pydantic
* PyPDF
* python-dotenv
* NumPy

---

## 📁 Project Structure

```text
Day25/
│
├── main.py
├── .env
├── .gitignore
├── test_document.txt
├── README.md
├── LEARNINGS.md
└── __pycache__/
```

---

## 🧪 Testing

Basic validation:

```bash
python -m py_compile main.py
```

Import test:

```bash
python -c "import main; print('Day25 loaded successfully')"
```

Health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

---

## 📈 Learning Outcomes

By completing Day 25, I learned how to:

* Build a hybrid retrieval system.
* Combine semantic and keyword search.
* Work with FAISS vector indexes.
* Build BM25 indexes.
* Design a RAG retrieval pipeline.
* Apply re-ranking concepts.
* Build REST APIs with FastAPI.
* Validate requests using Pydantic.
* Use asynchronous API endpoints.
* Implement error handling and logging.
* Configure CORS.
* Secure API credentials using `.env`.
* Test APIs using curl.

---

## ✅ Day 25 Status

**Production-Ready RAG & FastAPI Integration — Completed**

The project demonstrates how advanced retrieval techniques can be integrated into a FastAPI-based RAG service.
