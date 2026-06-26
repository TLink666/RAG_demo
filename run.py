from src.pipeline.run_rag import run_rag

queries = [
    "What do users prefer in AI systems?",
    "What transformed computers into household devices?",
    "Which brewing method uses pressure to produce concentrated flavor?",
    "Who invented quantum mechanics?"
]

if __name__ == "__main__":
    results, metrics, *_ = (
        run_rag(queries)
    )

    print()

    print("Finished")

    print()

    print(metrics)