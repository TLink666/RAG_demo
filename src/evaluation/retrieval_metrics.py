def recall_at_k(results, gold, k=5):
    hit = 0
    total = 0
    
    for item in results:
        q = item["query"]
        if q not in gold:
            continue
        total += 1
        target = gold[q]
        retrieved = item["retrieved"][:k]
        if any(
            r["source"] == target
            for r in retrieved
        ):
            hit += 1
    if total == 0:
        return None
    return round(hit / total, 3)

def mrr(results, gold):
    total_rr = 0
    total = 0

    for item in results:
        q = item["query"]
        if q not in gold:
            continue
        total += 1
        target = gold[q]
        rr = 0
        for rank, r in enumerate(
            item["retrieved"],
            1
        ):
            if r["source"] == target:
                rr = 1 / rank
                break

        total_rr += rr
    if total == 0:
        return None
    return round(
        total_rr / total,
        3
    )