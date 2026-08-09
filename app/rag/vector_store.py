import chromadb
from sentence_transformers import SentenceTransformer

from app.rag.document_loader import load_documents
from app.rag.chunker import chunk_text


EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "support_knowledge_base"

embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)


def build_vector_store():
    client = chromadb.PersistentClient(path="data/processed/chroma_db")

    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    documents = load_documents()

    ids = []
    texts = []
    metadatas = []

    for doc in documents:
        chunks = chunk_text(doc["text"])

        for index, chunk in enumerate(chunks):
            chunk_id = f"{doc['source']}_{index}"

            ids.append(chunk_id)
            texts.append(chunk)
            metadatas.append({
                "source": doc["source"],
                "chunk_index": index
            })

    embeddings = embedding_model.encode(texts).tolist()

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return collection


def get_collection():
    client = chromadb.PersistentClient(path="data/processed/chroma_db")
    return client.get_or_create_collection(name=COLLECTION_NAME)