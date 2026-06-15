from src.chunking import chunk_text

def build_docs(loaded_docs, chunk_size=200, overlap=50):

    docs = []
    chunk_id = 0

    for file in loaded_docs:
        chunks = chunk_text(
            file["text"],
            chunk_size,
            overlap
        )

        for chunk in chunks:
            docs.append({
                "chunk_id": chunk_id,
                "source": file["source"],
                "page": file["page"],
                "text": chunk
            })
            chunk_id += 1
    return docs