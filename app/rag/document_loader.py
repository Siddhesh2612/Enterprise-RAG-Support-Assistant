from pathlib import Path

def load_documents(data_dir: str = "data/raw"):
    documents = []

    folder_path = Path(data_dir)

    for file_path in folder_path.glob("*.md"):
        file = open(file_path, "r", encoding="utf-8")
        file_content = file.read()
        documents.append({"source": file_path.name, "text": file_content}) 
        file.close()

    return documents



