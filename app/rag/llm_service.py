import os
from dotenv import load_dotenv
import requests

load_dotenv()

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b"
)

def generate_answer(question: str, context: str) -> str:

    prompt = f"""
You are an enterprise customer support assistant. Use ONLY the provided context to answer the user's question.
If the answer cannot be found in the context, say: "I do not have enough information in the available knowledge base."

Context:
{context}

User Question:
{question}

Answer:
"""
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]
