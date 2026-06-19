import os
import json


def save_results(results, path):
    os.makedirs(
        os.path.dirname(
            path
        ),
        exist_ok=True
    )
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            results,
            f,
            indent=2,
            ensure_ascii=False
        )