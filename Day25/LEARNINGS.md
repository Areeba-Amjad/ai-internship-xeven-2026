# Day 25 — Production-Ready RAG & FastAPI Integration

## Overview

Day 25 focused on building a production-style Retrieval Augmented Generation (RAG) system and exposing it through a FastAPI service.

The implementation combined semantic search, keyword search, hybrid retrieval, document processing, embeddings, vector storage, API validation, logging, error handling, CORS, and environment-based configuration.

---

## 1. Advanced RAG Techniques

### Dense Retrieval

Dense retrieval uses embeddings to represent documents and queries as numerical vectors.

The query is compared with document vectors using semantic similarity.

**Advantages:**

* Understands meaning and context
* Works well with natural language queries
* Can find relevant information even when exact keywords differ

**Example:**

Query:

> How does RAG work?

A dense retriever can find a document containing:

> Retrieval Augmented Generation retrieves relevant information and provides it to an LLM.

Even though the exact words are different.

---

### Sparse Retrieval — BM25

BM25 is a keyword-based retrieval algorithm.

It focuses on the occurrence and importance of words in documents.

**Advantages:**

* Excellent for exact keywords
* Useful for technical terms and names
* Does not require embeddings

BM25 was implemented using the `rank-bm25` package.

---

### Hybrid Search

Hybrid search combines dense semantic retrieval with sparse keyword retrieval.

The Day 25 implementation uses:

* **70% semantic similarity**
* **30% keyword similarity**

Conceptually:

```text
Hybrid Score =
0.70 × Semantic Score
+
0.30 × BM25 Score
```

Hybrid search provides a balance between understanding meaning and matching exact terminology.

---

## 2. Re-ranking

Re-ranking improves retrieval quality after the initial search.

Instead of directly using the first few retrieved chunks:

```text
Query
  ↓
Retrieve 20 candidates
  ↓
LLM relevance scoring
  ↓
Rank candidates
  ↓
Select Top 5
```

Each candidate can be evaluated according to its relevance to the user's query.

A 0–10 relevance score can be used.

This improves precision because the final context contains the most relevant chunks.

---

## 3. Query Expansion

Query expansion reformulates the original user query into multiple variations.

Example:

```text
Original:
What is RAG?

Variations:
1. What is Retrieval Augmented Generation?
2. How does a RAG system work?
3. What is retrieval augmented generation used for?
```

Each variation can be used for retrieval.

The results can then be combined and ranked.

### Benefits

* Handles different ways of asking the same question
* Improves recall
* Helps retrieve information when the original wording does not match the document

---

## 4. Self-Query Retrieval

Self-query retrieval allows an LLM to convert a natural-language query into structured filters.

For example:

```text
Find machine learning documents from 2025
```

can be interpreted as:

```text
topic = "machine learning"
year = 2025
```

This allows retrieval systems to use metadata filters in addition to semantic similarity.

---

## 5. Parent Document Retrieval

Parent document retrieval stores smaller chunks for efficient retrieval but returns the larger parent document or section.

Concept:

```text
Large Parent Document
        ↓
      Chunks
        ↓
   Vector Search
        ↓
Relevant Chunk
        ↓
Return Parent Context
```

This helps preserve context while keeping retrieval efficient.

---

# 6. FastAPI RAG Service

FastAPI was used to expose the RAG system as a REST API.

The service includes endpoints for:

```text
POST /documents/upload
GET  /documents
DELETE /documents/{id}
POST /search
POST /ask
GET  /health
```

---

## 7. Document Upload Pipeline

The document upload pipeline follows these steps:

```text
Upload File
    ↓
Read Document
    ↓
Extract Text
    ↓
Split Into Chunks
    ↓
Generate Embeddings
    ↓
Store Vectors in FAISS
    ↓
Update BM25 Index
    ↓
Store Metadata
```

Supported document processing can include text-based files and PDF documents.

---

## 8. FAISS Vector Search

FAISS was used for efficient similarity search over embeddings.

The general workflow is:

```text
Document
   ↓
Embedding
   ↓
FAISS Index

Query
   ↓
Embedding
   ↓
FAISS Similarity Search
   ↓
Relevant Chunks
```

FAISS provides fast vector similarity search.

---

## 9. BM25 Index

A BM25 index was maintained alongside the FAISS index.

Documents are tokenized before being indexed.

Example:

```python
tokens = text.lower().split()
```

The BM25 retriever then calculates keyword relevance for incoming queries.

---

## 10. Pydantic Validation

Pydantic models were used for request and response validation.

Benefits include:

* Structured API input
* Type validation
* Clear response formats
* Automatic FastAPI documentation
* Better error messages

---

## 11. Async API Endpoints

Async functions were used for endpoints that interact with external LLM or embedding APIs.

Example:

```python
async def ask(...):
    ...
```

Asynchronous programming allows the server to handle other requests while waiting for external API operations.

---

## 12. Error Handling

The API uses exception handling to prevent application crashes.

General pattern:

```python
try:
    ...
except Exception as exc:
    logger.exception("Operation failed")
    raise HTTPException(
        status_code=500,
        detail=str(exc)
    )
```

Appropriate HTTP status codes help API clients understand failures.

---

## 13. Logging

Logging was added to track:

* Incoming requests
* Search operations
* Upload operations
* Errors
* Processing time
* API failures

This is important for debugging and production monitoring.

---

## 14. CORS

Cross-Origin Resource Sharing (CORS) was enabled so that a frontend application can communicate with the FastAPI backend.

This is useful when frontend and backend applications run on different origins.

---

## 15. Environment Variables

API credentials are stored in `.env` instead of being hard-coded into Python files.

Example:

```text
OPENAI_API_KEY=your_api_key
```

The `.env` file is excluded from Git using `.gitignore`.

This prevents sensitive credentials from being accidentally committed to GitHub.

---

## 16. API Testing

The API was tested using `curl`.

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Document listing:

```bash
curl http://127.0.0.1:8000/documents
```

Document upload:

```bash
curl -X POST \
"http://127.0.0.1:8000/documents/upload" \
-F "file=@test_document.txt"
```

Hybrid search:

```bash
curl -X POST \
"http://127.0.0.1:8000/search" \
-H "Content-Type: application/json" \
-d '{"query":"What is RAG?","top_k":5,"use_hybrid":true}'
```

---

# 17. Key Learnings

Through Day 25, I learned:

1. How dense and sparse retrieval differ.
2. How to combine FAISS and BM25 into hybrid search.
3. Why hybrid retrieval can improve recall.
4. How re-ranking improves retrieval precision.
5. How query expansion can improve recall.
6. How self-query retrieval can use metadata filters.
7. How parent document retrieval preserves context.
8. How to build a RAG backend using FastAPI.
9. How to validate API requests with Pydantic.
10. How to use async endpoints for external API calls.
11. How to handle API errors safely.
12. How to implement logging and request monitoring.
13. How to configure CORS for frontend integration.
14. How to protect API keys using environment variables.
15. How to test REST APIs using curl.
16. How to structure a production-oriented RAG pipeline.

---

## Conclusion

Day 25 connected the previous RAG concepts with a practical backend service.

The final architecture combines:

```text
             User Query
                  ↓
           Query Processing
                  ↓
       ┌──────────┴──────────┐
       ↓                     ↓
   FAISS Search           BM25 Search
   Semantic 70%           Keyword 30%
       └──────────┬──────────┘
                  ↓
           Hybrid Results
                  ↓
            Re-ranking
                  ↓
              Top 5
                  ↓
          Context Assembly
                  ↓
               LLM
                  ↓
          Answer + Sources
```

This provides a foundation for building scalable and production-oriented RAG applications.

