from fastapi import FastAPI
from pydantic import BaseModel


from app.rag.retriever import retrieve_relevant_chunks
from app.rag.context_builder import build_context
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

# Endpoint to handle user queries/questions and return generated answere from LLM supported by ground sources. 
@app.post("/query", response_model=QueryResponse)
def query_assistant(request: QueryRequest):

    retrieved_chunks = retrieve_relevant_chunks(
        request.question,
        top_k=3
    )

    context = build_context(retrieved_chunks)

    answer = generate_answer(
        question=request.question,
        context=context
    )

# using set{} here to eliminate duplicate sources 
    sources = list({
        chunk["source"]
        for chunk in retrieved_chunks
    })

    return {
        "answer": answer,
        "sources": sources,
        "confidence": 0.0
    }
