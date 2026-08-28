# Day 24 – Context Engineering & FastAPI Basics

## Overview

This project demonstrates the fundamentals of Context Engineering and FastAPI, with a focus on building a simple RAG API.

The application provides REST API endpoints for health checking, item management and asking questions using a retrieval-based RAG system.

---

## Objectives

* Understand context window limits.
* Learn dynamic context injection.
* Understand conversational memory.
* Learn context compression.
* Build a FastAPI application.
* Use Pydantic for validation.
* Build REST API endpoints.
* Integrate a RAG system with FastAPI.
* Load the RAG system during application startup.
* Test APIs using Curl and Python requests.
* Explore OpenAPI and ReDoc documentation.

---

## Project Structure

```text
Day24/
│
├── main.py
├── test_api.py
└── README.md
```

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic
* Requests
* RAG
* REST API
* OpenAPI

---

## FastAPI Endpoints

### 1. Health Check

```text
GET /health
```

Checks whether the API and RAG system are running.

Example:

```json
{
  "status": "healthy",
  "rag_loaded": true
}
```

---

### 2. Get Item

```text
GET /items/{id}
```

Retrieves an item using its ID.

Example:

```text
GET /items/1
```

Response:

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "MacBook Air",
  "price": 1200.0
}
```

---

### 3. Create Item

```text
POST /items
```

Creates a new item using a validated Pydantic request body.

Example:

```json
{
  "name": "Mouse",
  "description": "Wireless mouse",
  "price": 25
}
```

---

### 4. Ask RAG

```text
POST /ask
```

Accepts a question and retrieves relevant information from the RAG knowledge base.

Example request:

```json
{
  "question": "What is RAG?"
}
```

Example response:

```json
{
  "answer": "Retrieval Augmented Generation combines information retrieval with large language models...",
  "sources": [
    "rag_basics.txt",
    "vector_database.txt"
  ],
  "confidence": 0.8
}
```

---

## RAG Pipeline

The RAG API follows this general workflow:

```text
Question
   ↓
Document Retrieval
   ↓
Relevant Context
   ↓
Answer Generation
   ↓
Sources + Confidence
   ↓
API Response
```

---

## Context Management

The project also explores conversational context management.

Important concepts studied include:

### Context Window

Models have a limited amount of text they can process at once, such as 4K, 8K or larger token limits.

### Dynamic Context Injection

Relevant information is added to the model context when needed.

### Conversation Memory

Previous questions and answers can be maintained as conversation context.

### Context Compression

Older conversation information can be summarized while recent conversations remain detailed.

---

## Installation

Create and activate a virtual environment if required.

Install dependencies:

```bash
pip install fastapi uvicorn requests
```

---

## Run the API

From the `Day24` directory:

```bash
python -m uvicorn main:app --reload --port 8001
```

The API runs at:

```text
http://127.0.0.1:8001
```

---

## Testing

### Health Check

```bash
curl http://127.0.0.1:8001/health
```

### Get Item

```bash
curl http://127.0.0.1:8001/items/1
```

### Create Item

```bash
curl -X POST http://127.0.0.1:8001/items \
-H "Content-Type: application/json" \
-d '{"name":"Mouse","description":"Wireless mouse","price":25}'
```

### Ask RAG

```bash
curl -X POST http://127.0.0.1:8001/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is RAG?"}'
```

---

## Python Requests Testing

The `test_api.py` script sends a request to the RAG endpoint.

Run:

```bash
python test_api.py
```

Successful testing returns:

```text
Status Code: 200
```

along with the generated answer, sources and confidence score.

---

## API Documentation

FastAPI automatically generates API documentation.

### Swagger UI

```text
/docs
```

### ReDoc

```text
/redoc
```

### OpenAPI Schema

```text
/openapi.json
```

---

## Error Handling

The API supports error handling for:

* Invalid input
* Validation errors
* No relevant documents
* Server/LLM errors

Common HTTP status codes include:

```text
400 → Bad Request
404 → Not Found
422 → Validation Error
500 → Internal Server Error
```

---

## Learning Outcome

After completing Day 24, I learned how to:

* Manage AI context.
* Work with conversational memory concepts.
* Build REST APIs using FastAPI.
* Use Pydantic models.
* Create GET and POST endpoints.
* Integrate RAG with an API.
* Load systems during application startup.
* Return structured API responses.
* Handle API errors.
* Test APIs with Curl.
* Test APIs using Python requests.
* Use automatically generated OpenAPI documentation.

---

## Conclusion

Day 24 provided practical experience in combining **Context Engineering, RAG and FastAPI**.

The final application demonstrates how an AI/RAG system can be exposed through a structured REST API and tested using multiple API clients.
