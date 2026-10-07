# Enterprise RAG Support Assistant

A FastAPI prototype that answers customer-support questions from local Markdown knowledge-base files. It embeds document chunks with Sentence Transformers, retrieves them from ChromaDB, and asks a local Ollama model to answer using the retrieved context. The API returns the answer and source filenames.

## Current features

- `POST /query` retrieves relevant chunks and generates a source-grounded answer.
- `GET /health` provides a basic API health response.
- `scripts/build_vector_store.py` indexes Markdown files from `data/raw/` into a local ChromaDB collection.

## Run locally

1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`.
3. Start Ollama locally and make the configured model available. The default is `llama3.2:3b`; set `OLLAMA_BASE_URL` and `OLLAMA_MODEL` to change it.
4. Build the index: `python scripts/build_vector_store.py`.
5. Start the API: `uvicorn app.main:app --reload`.

Open http://127.0.0.1:8000/docs for the interactive API. Send a JSON request such as `{"question":"How do I reset my password?"}` to `POST /query`.

## Status and limits

This is a prototype, not a production deployment. The `confidence` response field is currently a placeholder (`0.0`). Automated evaluation, CI, and container deployment are not implemented yet; the corresponding files are scaffolds. The included knowledge-base files are examples.

**Stack:** Python, FastAPI, ChromaDB, Sentence Transformers, Ollama.
