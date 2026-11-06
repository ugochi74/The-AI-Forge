from pathlib import Path
from tempfile import TemporaryDirectory

from datasets import Dataset, disable_progress_bars, load_dataset


def load_and_inspect(dataset_name, config=None, split="train", limit=3):
    dataset = load_dataset(dataset_name, name=config, split=split, streaming=True)
    label_names = {"0": "negative", "1": "positive"}
    print(f"\n=== Dataset preview: {dataset_name} ({split}) ===")
    for index, example in enumerate(dataset.take(limit), start=1):
        print(f"\nExample {index}")
        for field, value in example.items():
            display = str(value).replace("\n", " ")
            if len(display) > 180:
                display = display[:180].rstrip() + "..."
            if dataset_name == "stanfordnlp/imdb" and field == "label":
                meaning = label_names.get(display)
                if meaning:
                    display = f"{display} ({meaning})"
            print(f"  {field.title()}: {display}")
    return dataset


def convert_format(dataset, output_path):
    output_path = Path(output_path)
    exporters = {
        ".csv": dataset.to_csv,
        ".json": dataset.to_json,
        ".parquet": dataset.to_parquet,
    }
    try:
        export = exporters[output_path.suffix.lower()]
    except KeyError:
        raise ValueError("Choose .csv, .json, or .parquet") from None
    export(str(output_path))
    return output_path


def split_dataset(dataset, seed=42):
    holdout = dataset.train_test_split(test_size=0.30, seed=seed)
    validation_test = holdout["test"].train_test_split(test_size=0.50, seed=seed)
    return {
        "train": holdout["train"],
        "validation": validation_test["train"],
        "test": validation_test["test"],
    }


def load_from_parquet(path):
    return Dataset.from_parquet(str(path))


if __name__ == "__main__":
    disable_progress_bars()
    load_and_inspect("stanfordnlp/imdb", limit=3)

    sample = Dataset.from_dict(
        {
            "text": [f"review {i}" for i in range(20)],
            "label": [i % 2 for i in range(20)],
        }
    )
    with TemporaryDirectory() as folder:
        path = convert_format(sample, Path(folder) / "sample.parquet")
        restored = load_from_parquet(path)

    purposes = {
        "train": "model learns from these rows",
        "validation": "compare choices while developing",
        "test": "final evaluation on held-out rows",
    }
    print("\n=== Synthetic 20-row split (seed 42) ===")
    print(f"{'Split':<12} {'Rows':>4}  Purpose")
    for name, split in split_dataset(restored, seed=42).items():
        print(f"{name:<12} {len(split):>4}  {purposes[name]}")
