from collections import Counter
import numpy as np

def analyze_retrieval(results):
    all_conf = []
    sources = []
    chunks = []
    for r in results:
        retrieved = r["retrieved"]
        for x in retrieved:
            all_conf.append(x["confidence"])
            sources.append(x["source"])
            chunks.append(x["chunk_id"])
    return {
        "num_queries": len(results),
        "avg_confidence":
        round(
            np.mean(all_conf),
            3
        ),
        "min_confidence":
        round(
            min(all_conf),
            3
        ),
        "max_confidence":
        round(
            max(all_conf),
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
        f"Avg confidence: "
        f"{stats['avg_confidence']}"
    )
    print(
        f"Min confidence: "
        f"{stats['min_confidence']}"
    )
    print(
        f"Max confidence: "
        f"{stats['max_confidence']}"
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