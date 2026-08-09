from fastapi import FastAPI
from pydantic import BaseModel
from app.rag.llm_service import generate_answer

#Request and Response models for the query endpoint
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: float

# FastAPI application instance
app = FastAPI(
    title="Enterprise RAG Support Assistant",
    description="A deployment-ready RAG assistant for support knowledge-base queries.",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "message": "Enterprise RAG Support Assistant API is running",
        "docs": "/docs",
        "health": "/health"
    }

# Endpoint to handle user queries and return answers from the LLM
@app.post("/query", response_model=QueryResponse)
def query_assistant(request: QueryRequest):
    answer = generate_answer(request.question)

    return {
        "answer": answer,
        "sources": [],
        "confidence": 0.0
    }
