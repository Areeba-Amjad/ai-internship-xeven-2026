from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Document, Conversation

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Day 27 Full-Stack RAG API",
    description="Production RAG API with PostgreSQL",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Day 27 Full-Stack RAG API is running"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected"
    }


@app.post("/documents")
def create_document(
    title: str,
    content: str,
    db: Session = Depends(get_db)
):
    document = Document(title=title, content=content)
    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "id": document.id,
        "title": document.title,
        "message": "Document created successfully"
    }


@app.get("/documents")
def get_documents(db: Session = Depends(get_db)):
    documents = db.query(Document).all()

    return [
        {
            "id": doc.id,
            "title": doc.title,
            "version": doc.version
        }
        for doc in documents
    ]


@app.post("/conversations")
def create_conversation(
    session_id: str,
    question: str,
    answer: str,
    db: Session = Depends(get_db)
):
    conversation = Conversation(
        session_id=session_id,
        question=question,
        answer=answer
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return {
        "id": conversation.id,
        "message": "Conversation saved successfully"
    }


@app.get("/conversations/{session_id}")
def get_conversations(
    session_id: str,
    db: Session = Depends(get_db)
):
    conversations = (
        db.query(Conversation)
        .filter(Conversation.session_id == session_id)
        .all()
    )

    return [
        {
            "id": conv.id,
            "question": conv.question,
            "answer": conv.answer
        }
        for conv in conversations
    ]


@app.get("/analytics")
def analytics(db: Session = Depends(get_db)):
    return {
        "total_documents": db.query(Document).count(),
        "total_conversations": db.query(Conversation).count()
    }
