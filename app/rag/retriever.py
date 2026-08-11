from app.rag.vector_store import get_collection
from sentence_transformers import SentenceTransformer 

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_relevant_chunks(question: str, top_k: int = 3):
    collection = get_collection()

    question_embedding = embedding_model.encode(question).tolist()

    results = collection.query(query_embeddings = [question_embedding], n_results = top_k )

    retrieved_chunks = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):
        retrieved_chunks.append({
            "text": document,
            "source": metadata["source"],
            "distance": distance
        })

    return retrieved_chunks



