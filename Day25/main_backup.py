from fastapi import FastAPI

app = FastAPI(
    title="Day 25 - Production RAG API",
    description="Hybrid Search + Re-ranking + RAG",
    version="1.0.0"
)


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "message": "Day 25 RAG API is running"
    }