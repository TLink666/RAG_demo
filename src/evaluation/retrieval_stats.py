from collections import Counter
import numpy as np

def analyze_retrieval(results):
    all_scores = []
    sources = []
    chunks = []
    for r in results:
        retrieved = r["retrieved"]
        for x in retrieved:
            all_scores.append(x["score"])
            sources.append(x["source"])
            chunks.append(x["chunk_id"])
    return {
        "num_queries": len(results),
        "avg_score":
        round(
            np.mean(all_scores),
            3
        ),
        "min_score":
        round(
            min(all_scores),
            3
        ),
        "max_score":
        round(
            max(all_scores),
            3
        ),
        "unique_sources":
        len(
            set(sources)
        ),
        "top_chunks":
        Counter(
            chunks
        ).most_common(5)
    }

def print_retrieval(stats):
    print("\n=== Retrieval Statistics ===")
    print(
        f"Queries: "
        f"{stats['num_queries']}"
    )
    print(
        f"Avg score: "
        f"{stats['avg_score']}"
    )
    print(
        f"Min score: "
        f"{stats['min_score']}"
    )
    print(
        f"Max score: "
        f"{stats['max_score']}"
    )
    print(
        f"Unique sources: "
        f"{stats['unique_sources']}"
    )
    print("\nTop reused chunks:")
    for cid, count in stats["top_chunks"]:
        print(
            f"Chunk {cid}: "
            f"{count}"
        )