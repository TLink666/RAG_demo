def retrieval_guard(retrieved, threshold=0.5):

    if (len(retrieved) == 0):
        return False

    best=max(
        r["confidence"]
        for r
        in retrieved
    )
    return (best>= threshold)