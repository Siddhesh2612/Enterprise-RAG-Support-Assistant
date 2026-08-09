import os
import requests
from dotenv import load_dotenv # Load environment variables from a .env file

load_dotenv()

# Constants for Ollama API configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")


# Function to generate an answer from the Ollama model
def generate_answer(question: str) -> str:
    """
    Sends a user question to a locally running Ollama model
    and returns the generated answer.
    """
# Prepare the payload for the Ollama API request
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