from app.rag.context_builder import build_context
from app.rag.retriever import retrieve_relevant_chunks


question = "Procedure to reset username and password"

results = retrieve_relevant_chunks(question)

context = build_context(results)


print("QUESTION:")
print(question)
print()
        
for index, result in enumerate(results, start=1):
    print(f"RESULT {index}")
    print("SOURCE:", result["source"])
    print("DISTANCE:", result["distance"])
    print("TEXT:")
    print(result["text"])
    print("-" * 50)