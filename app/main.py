from fastapi import FastAPI

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