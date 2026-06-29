from src.retrieval.bm25_store import *
from src.retrieval.faiss_retrieve import retrieve
from src.retrieval.score import calibrate_score
from src.config import TOP_K, HYBRID_ALPHA, RETRIEVAL_METHOD, RRF_K

def normalize_scores(results):
    scores = [r["score"] for r in results]
    mx = max(scores)
    mn = min(scores)
    if mx == mn:
        for r in results:
            r["score"] = 0.5
        return results
    for r in results:
        r["score"] = (r["score"]-mn) / (mx-mn)
    return results

def hybrid_retrieve(query, model, index, bm25, docs, k=TOP_K, alpha=HYBRID_ALPHA):
    faiss_results = retrieve(query, model, index, docs, k)
    bm25_results = search_bm25(bm25, docs, query, k)
    for r in faiss_results:
        r["faiss_raw_score"] = r["score"]
    faiss_results = normalize_scores(faiss_results)
    for r in bm25_results:
        r["bm25_raw_score"] = r["score"]
    bm25_results = normalize_scores(bm25_results)
    merged = {}
    for rank, r in enumerate(faiss_results, 1):
        cid = r["chunk_id"]
        merged[cid] = {
            **r,
            "faiss_rank": rank,
            "bm25_rank": None,
            "retriever": "faiss",
            "faiss_score": r["score"],
            "bm25_raw_score": None,
            "bm25_score": 0
        }
    for rank, r in enumerate(bm25_results, 1):
        cid = r["chunk_id"]
        if cid not in merged:
            merged[cid] = {
                **r,
                "faiss_rank": None,
                "bm25_rank": rank,
                "retriever": "bm25",
                "faiss_raw_score": None,
                "faiss_score": 0,
                "bm25_score": r["score"]
            }
        else:
            merged[cid]["bm25_rank"]=rank
            merged[cid]["bm25_raw_score"] = r["bm25_raw_score"]
            merged[cid]["bm25_score"] = r["score"]
            if (merged[cid]["faiss_score"]>0 and merged[cid]["bm25_score"]>0):
                merged[cid]["retriever"] = "hybrid"
    for cid in merged:
        if RETRIEVAL_METHOD == "weighted":
            merged[cid]["score"] = (alpha * merged[cid]["faiss_score"] + (1-alpha) * merged[cid]["bm25_score"])
        elif RETRIEVAL_METHOD == "rrf":
            score = 0
            if (merged[cid]["faiss_rank"]is not None):
                score += (1 /(RRF_K+merged[cid]["faiss_rank"]))
            if (merged[cid]["bm25_rank"]is not None):
                score += (1 /(RRF_K+merged[cid]["bm25_rank"]))
            merged[cid]["score"]=score
    results = sorted(
        merged.values(),
        key=lambda x:x["score"],
        reverse=True
    )[:k]
    results = calibrate_score(results)
    for i, r in enumerate(results, 1):
        r["rank"] = i
    return results