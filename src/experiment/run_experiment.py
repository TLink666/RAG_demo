import os
from datetime import datetime
from src.experiment.save_experiment import save_experiment
from src.config import RESULT_DIR

def run_experiment(
    config,
    results,
    metrics,
    debug_stats
):

    save_dir = os.path.join(
        RESULT_DIR,
        datetime.now().strftime("%Y%m%d_%H%M%S")
    )

    save_experiment(
        config=config,
        results=results,
        metrics=metrics,
        debug_stats=debug_stats,
        save_dir=save_dir
    )