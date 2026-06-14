import os
from src.loaders.txt_loader import load_txt
from src.loaders.pdf_loader import load_pdf

def load_documents(folder):
    docs = []
    for file in os.listdir(folder):
        path = f"{folder}/{file}"
        if file.endswith(".txt"):
            docs.append({
                "source": file,
                "page": None,
                "text": load_txt(path)
            })
        elif file.endswith(".pdf"):
            pages = load_pdf(path)
            for page in pages:
                docs.append({
                    "source": file,
                    "page": page["page"],
                    "text": page["text"]
                })
    return docs