"""Reusable examples for the Phase 0 Jupyter Notebooks lesson."""

from __future__ import annotations

import gc
import random
import statistics
import timeit
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # Save figures when running as a script, without a GUI.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


LESSON_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = LESSON_DIR / "outputs"
CSV_PATH = OUTPUT_DIR / "model_metrics.csv"


def timing_comparison(size: int = 100_000, repeats: int = 5) -> None:
    """Compare list and NumPy random-number generation with repeated timings."""
    random_times = timeit.repeat(
        lambda: [random.random() for _ in range(size)], number=1, repeat=repeats
    )
    numpy_times = timeit.repeat(
        lambda: np.random.random(size), number=1, repeat=repeats
    )

    print("=== Random-number generation ===")
    print(f"Python list median: {statistics.median(random_times):.4f} s")
    print(f"NumPy array median: {statistics.median(numpy_times):.4f} s")
    print("Use %timeit in a notebook for a more careful microbenchmark.")


def dataframe_display() -> pd.DataFrame:
    """Load and print the lesson's small CSV fixture."""
    frame = pd.read_csv(CSV_PATH)
    print("=== Model metrics ===")
    print(frame.to_string(index=False))
    print(f"\nHighest accuracy: {frame.loc[frame['accuracy'].idxmax(), 'model']}")
    return frame


def save_accuracy_plot(frame: pd.DataFrame | None = None) -> Path:
    """Save an accuracy chart; notebooks can instead display it inline."""
    if frame is None:
        frame = pd.read_csv(CSV_PATH)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plot_path = OUTPUT_DIR / "notebook_tips_plot.png"
    axis = frame.plot(x="model", y="accuracy", kind="bar", legend=False)
    axis.set_title("Model accuracy")
    axis.set_ylabel("Accuracy")
    axis.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig(plot_path, dpi=120)
    plt.close()
    print(f"Saved chart to {plot_path}")
    print("In a notebook, display the plot inline with `display(fig)` or `plt.show()`.")
    return plot_path


def memory_check(size: int = 1_000_000) -> None:
    """Show array memory use and explicitly release the temporary array."""
    values = np.random.standard_normal(size)
    print(f"Array elements: {values.size:,}")
    print(f"Array data size: {values.nbytes / 1_000_000:.2f} MB")
    del values
    gc.collect()
    print("Deleted the temporary array; a kernel restart clears remaining state.")


def gpu_status() -> None:
    """Report GPU availability when PyTorch is installed (for the Colab exercise)."""
    try:
        import torch
    except ImportError:
        print("PyTorch is not installed in this environment; GPU check skipped.")
        return

    print(f"PyTorch CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")


def main() -> None:
    timing_comparison()
    frame = dataframe_display()
    save_accuracy_plot(frame)
    memory_check()
    gpu_status()


if __name__ == "__main__":
    main()
