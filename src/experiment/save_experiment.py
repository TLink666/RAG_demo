import os
import json

def save_experiment(
    config,
    results,
    metrics,
    debug_stats,
    save_dir
):

    os.makedirs(save_dir,exist_ok=True)
    
    with open(f"{save_dir}/config.json", "w") as f:
        json.dump(config, f, indent=2)

    with open(f"{save_dir}/result.json", "w") as f:
        json.dump(results, f, indent=2)

    with open(f"{save_dir}/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    
    with open(f"{save_dir}/retrieval_stats.json", "w") as f:
        json.dump(debug_stats,  f, indent=2)