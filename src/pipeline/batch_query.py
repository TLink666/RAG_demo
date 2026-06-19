from src.rag.generate import ask_llm
from src.rag.prompt import build_context

def batch_query(queries, retrieve_fn):
    results=[]
    for query in queries:
        retrieved = retrieve_fn(query)
        context = build_context(retrieved)
        answer = ask_llm(context, query)
        results.append({
            "query": query,

            "retrieved": retrieved,

            "answer": answer
        })
    return results