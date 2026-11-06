# Data Management Verification

**Author:** Andrew.Nd

## Environment

- Python: 3.12.3
- `datasets`: 5.1.0
- `huggingface_hub`: 2.4.0
- `pyarrow`: 26.0.1
- Public Hub access worked without a token; the Hub warned that unauthenticated
  requests have lower rate limits.

## Practical checks

- Streamed and displayed three IMDB training examples.
- Exported the same sample to CSV, JSON, and Parquet; loaded Parquet back.
- Confirmed unsupported `.xlsx` output raises a clear `ValueError`.
- Split 20 rows into train/validation/test counts of 14/3/3.
- Repeated seed 42 and confirmed identical row assignments.
- Confirmed `.gitignore` matches lesson-local `data/` and `models/` paths.

Evidence is saved in `../outputs/`.
