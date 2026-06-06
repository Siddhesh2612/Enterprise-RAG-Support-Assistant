# Enterprise RAG Support Assistant

A deployment-ready Retrieval-Augmented Generation (RAG) application that answers customer support queries using a structured knowledge base.

This project demonstrates production-oriented AI engineering skills including FastAPI APIs, vector search, Docker-based deployment, evaluation, and CI/CD readiness.

## Problem

Customer support teams often rely on large volumes of internal documentation (FAQs, policies, troubleshooting guides), making it difficult to quickly retrieve accurate answers.

Traditional keyword search systems fail to provide context-aware and reliable responses.

## Solution

This project builds a Retrieval-Augmented Generation (RAG) system that:

- Retrieves relevant documents from a knowledge base
- Generates context-aware answers using LLMs
- Returns source-backed responses to reduce hallucination
- Exposes the system via a FastAPI backend for real-world usage

## Features

- FastAPI backend with REST endpoints
- Document ingestion and vector-based retrieval (FAISS/Chroma)
- Source-grounded answer generation
- Dockerised application for reproducible deployment
- Basic evaluation framework for retrieval and answer quality
- Logging and error handling for reliability
- CI pipeline with GitHub Actions (planned)

## Tech Stack

- Python
- FastAPI
- LangChain / LlamaIndex (for RAG pipeline)
- FAISS / Chroma (vector database)
- Hugging Face / OpenAI-compatible models
- Docker
- Pytest
- GitHub Actions (CI)

## Project Structure

app/              → FastAPI app and RAG pipeline
data/             → Knowledge base documents
tests/            → Unit and API tests
evaluation/       → RAG evaluation datasets
docs/             → Documentation
Dockerfile        → Container setup
docker-compose.yml→ Local deployment

## How to Run Locally

### 1. Clone the repository

git clone https://github.com/Siddhesh2612/Enterprise-RAG-Support-Assistant.git  
cd Enterprise-RAG-Support-Assistant

### 2. Create virtual environment

python -m venv .venv  
source .venv/bin/activate   # Mac/Linux  
.venv\Scripts\activate      # Windows  

### 3. Install dependencies

pip install -r requirements.txt  

### 4. Run the application

uvicorn app.main:app --reload  

### 5. Access API

Docs: http://127.0.0.1:8000/docs  
Health: http://127.0.0.1:8000/health



