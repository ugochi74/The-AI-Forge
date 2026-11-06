# Data Management Notes

**Author:** Andrew.Nd

## Concepts

- Hugging Face `datasets` loads data from the Hub, can stream rows, and caches
  downloaded dataset files under `~/.cache/huggingface/datasets/`.
- A streamed dataset is an iterable read in order; it is useful for previews or
  data too large to download at once. The IMDB preview read three rows.
- The utility formats preview fields on separate lines, truncates long values,
  and prints split counts with each split's purpose.
- CSV is easy to inspect as text. JSON supports nested records. Parquet uses
  columnar binary storage. For a three-row sample, Parquet was larger because
  its metadata overhead outweighed compression savings.
- A fixed split seed makes train/validation/test assignment reproducible. Keep
  test data for final evaluation; use validation data during model selection.
- Hugging Face model files cache under `~/.cache/huggingface/hub/`. Repeating
  the config download returned the same cached path.
- Lesson-local `.gitignore` rules exclude downloaded `data/` and `models/`
  paths from Git without deleting local files. `git check-ignore -v` verified
  both rules. Git LFS can share large files; DVC tracks data versions stored
  remotely. Ignore rules are sufficient for re-downloadable files in this
  personal learning workspace.

## Commands and results

The streaming preview and data format comparison are recorded under
`outputs/`. The 20-row split example produced 14 train, 3 validation, and
3 test rows, with identical assignments when seed 42 was reused. The utility
also exported and reloaded Parquet, then split the restored dataset.
