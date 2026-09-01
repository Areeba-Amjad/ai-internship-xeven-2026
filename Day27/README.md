# Day 27: Weekend Integration — Full-Stack RAG Application

## Overview

Day 27 focused on integrating the RAG components developed during previous days into a production-style full-stack application.

The project combines **FastAPI, PostgreSQL, SQLAlchemy, FAISS, Sentence Transformers, JWT authentication, conversation management, analytics, testing, and API documentation** into a single RAG backend.

## Objectives

* Design a production-style RAG architecture
* Integrate FastAPI with PostgreSQL
* Create database models using SQLAlchemy ORM
* Store documents, chunks, and conversations
* Implement RAG functionality using FAISS and embeddings
* Add authentication and API security
* Implement conversation tracking
* Add analytics functionality
* Create automated API tests
* Prepare API documentation
* Organize the project for deployment

## System Architecture

```text
                    ┌─────────────────────┐
                    │       Client        │
                    │ Browser / API User  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │    REST API Layer   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │ PostgreSQL  │  │ RAG Engine  │  │    Auth     │
       │  Database   │  │ FAISS + ST  │  │    JWT      │
       └─────────────┘  └─────────────┘  └─────────────┘
              │                │
              ▼                ▼
       Documents /       Embeddings /
       Conversations     Semantic Search
```

## Data Flow

```text
User Query
    ↓
FastAPI Endpoint
    ↓
Authentication
    ↓
RAG Retrieval
    ↓
FAISS Vector Search
    ↓
Relevant Documents / Chunks
    ↓
Response Generation
    ↓
Conversation Stored in PostgreSQL
    ↓
Analytics Updated
```

## Project Structure

```text
Day27/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── rag.py
│   ├── services.py
│   └── analytics.py
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── data/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Database

PostgreSQL was integrated as the persistent database.

The following tables were created:

### Documents

Stores document metadata.

### Chunks

Stores document chunks and their associated information.

### Conversations

Stores user questions, answers, and conversation history.

Database verification:

```bash
psql -d rag_db -c "\dt"
```

Output confirmed:

```text
chunks
conversations
documents
```

## Technologies Used

| Technology            | Purpose                  |
| --------------------- | ------------------------ |
| Python 3.11           | Application development  |
| FastAPI               | REST API                 |
| Uvicorn               | ASGI server              |
| PostgreSQL            | Persistent database      |
| SQLAlchemy            | ORM                      |
| psycopg2              | PostgreSQL driver        |
| FAISS                 | Vector similarity search |
| Sentence Transformers | Text embeddings          |
| Transformers          | NLP model support        |
| NumPy                 | Numerical operations     |
| Pydantic              | Data validation          |
| JWT                   | Authentication           |
| Pytest                | Automated testing        |
| HTTPX                 | API testing              |
| Docker                | Containerization         |

## Environment

The project was developed in a Conda environment:

```bash
conda activate day27
```

Python version:

```bash
python --version
```

Python 3.11.5 was used.

## Installation

Create and activate the environment:

```bash
conda activate day27
```

Install dependencies:

```bash
pip install -r requirements.txt
```

PostgreSQL was installed and configured for the project.

Verify PostgreSQL:

```bash
psql --version
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload --port 8000
```

The API runs at:

```text
http://127.0.0.1:8000
```

## API Testing

### Root Endpoint

```bash
curl http://127.0.0.1:8000/
```

Response:

```json
{
  "message": "Day 27 Full-Stack RAG API is running"
}
```

### Health Endpoint

```bash
curl http://127.0.0.1:8000/health
```

Response:

```json
{
  "status": "healthy",
  "database": "connected"
}
```

### Analytics Endpoint

```bash
curl http://127.0.0.1:8000/analytics
```

Example response:

```json
{
  "total_documents": 1,
  "total_conversations": 1
}
```

## API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

## Testing

Automated tests were created using Pytest.

Run:

```bash
pytest -v
```

Final result:

```text
3 passed, 1 warning
```

Tests included:

* Root endpoint test
* Health endpoint test
* Analytics endpoint test

## Security

The application includes dependencies for:

* JWT-based authentication
* Password hashing
* Environment-based configuration
* Cryptographic security

Sensitive configuration should be stored in `.env` and should **not** be committed to GitHub.

## Docker

The project includes:

```text
Dockerfile
docker-compose.yml
```

These files provide the foundation for containerized deployment of the application and PostgreSQL database.

## Key Results

Day 27 successfully integrated the RAG application into a backend system with:

* FastAPI REST API
* PostgreSQL database
* SQLAlchemy ORM
* FAISS vector search
* Sentence Transformer embeddings
* Authentication infrastructure
* Conversation storage
* Analytics
* Automated testing
* API documentation
* Docker deployment configuration

## Conclusion

Day 27 completed the transition from individual RAG components to a structured full-stack RAG application.

The project now demonstrates how **retrieval, embeddings, vector search, databases, APIs, authentication, testing, and analytics** can work together as a production-style AI backend.
