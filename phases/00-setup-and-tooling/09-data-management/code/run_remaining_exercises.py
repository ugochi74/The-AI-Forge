"""Run the remaining Lesson 09 checks on MRPC and a short C4 stream."""

from pathlib import Path
from tempfile import TemporaryDirectory
from time import perf_counter

from datasets import disable_progress_bars, load_dataset

from data_utils import (
    convert_format,
    load_cached_split,
    load_from_parquet,
    split_dataset,
)


def run_mrpc_exercises():
    print("=== MRPC: load, inspect, convert, and split ===")
    dataset = load_cached_split("nyu-mll/glue", "mrpc", "train")
    print(f"Rows: {len(dataset)}")
    print(f"Fields: {', '.join(dataset.column_names)}")
    for index, example in enumerate(dataset.select(range(5)), start=1):
        print(f"\nExample {index} (label {example['label']})")
        print(f"  Sentence 1: {example['sentence1'][:180]}")
        print(f"  Sentence 2: {example['sentence2'][:180]}")

    for cached in dataset.cache_files:
        print(f"Dataset cache: {cached['filename']}")

    with TemporaryDirectory() as folder:
        csv_path = convert_format(dataset, Path(folder) / "mrpc.csv")
        parquet_path = convert_format(dataset, Path(folder) / "mrpc.parquet")
        restored = load_from_parquet(parquet_path)
        print("\nFormat comparison:")
        print(f"  CSV: {csv_path.stat().st_size} bytes")
        print(f"  Parquet: {parquet_path.stat().st_size} bytes")
        print(f"  Parquet rows preserved: {len(restored) == len(dataset)}")

    first = split_dataset(dataset, seed=42)
    repeat = split_dataset(dataset, seed=42)
    print("\nSeeded 70/15/15 split:")
    for name, split in first.items():
        print(f"  {name}: {len(split)} rows")
    same = all(
        first[name][field] == repeat[name][field]
        for name in first
        for field in ("sentence1", "sentence2", "label")
    )
    print(f"  Same assignments with seed 42: {same}")


def count_c4_examples(seconds=10):
    stream = iter(load_dataset(
        "allenai/c4", "en", split="train", streaming=True
    ))
    warmup_started = perf_counter()
    first_example = next(stream, None)
    warmup_seconds = perf_counter() - warmup_started
    if first_example is None:
        return 0, 0.0, warmup_seconds

    started = perf_counter()
    count = 0
    for _ in stream:
        count += 1
        if perf_counter() - started >= seconds:
            break
    return count, perf_counter() - started, warmup_seconds


def run_c4_exercise():
    print("\n=== C4 streaming: two 10-second attempts ===")
    for attempt in (1, 2):
        try:
            count, elapsed, warmup = count_c4_examples(seconds=10)
            print(
                f"Attempt {attempt}: first row in {warmup:.1f}s; "
                f"then {count} more examples in {elapsed:.1f}s"
            )
        except Exception as error:
            print(f"Attempt {attempt} unavailable: {type(error).__name__}: {error}")


if __name__ == "__main__":
    disable_progress_bars()
    run_mrpc_exercises()
    run_c4_exercise()
