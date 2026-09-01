from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Day 27 Full-Stack RAG API is running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_analytics():
    response = client.get("/analytics")
    assert response.status_code == 200
    data = response.json()
    assert "total_documents" in data
    assert "total_conversations" in data
