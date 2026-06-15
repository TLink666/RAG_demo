import faiss
import numpy as np

def build_index(model, docs):
    embeddings = model.encode([d["text"] for d in docs])
    embeddings = np.array(embeddings).astype("float32")
    faiss.normalize_L2(embeddings)
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    return index
