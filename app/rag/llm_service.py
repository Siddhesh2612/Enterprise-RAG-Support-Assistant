import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")



def generate_answer(question: str) -> str:
    """
    Sends a user question to a locally running Ollama model
    and returns the generated answer.
    """

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": (
            "You are an enterprise customer support AI assistant. "
            "Answer clearly and professionally.\n\n"
            f"User question: {question}"
        ),
        "stream": False
    }

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()
    return data.get("response", "No response generated.")