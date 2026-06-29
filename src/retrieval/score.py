def calibrate_score(results):
    scores = [r["score"] for r in results]
    mx=max(scores)
    mn=min(scores)
    if mx==mn:
        for r in results:
            r["confidence"]=0.5
        return results
    for r in results:
        r["confidence"]=(r["score"]-mn)/(mx-mn)
    return results