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
- Loaded MRPC training data as a regular cached `Dataset`: 3,668 rows with
  `sentence1`, `sentence2`, `label`, and `idx`; inspected the first five rows.
- The cached Arrow file path was printed. For this verification the cache was
  redirected to `/tmp/lesson09-datasets-cache`; normal local runs use the
  Hugging Face cache under the user's home directory.
- CSV export was 915,219 bytes; Parquet was 623,315 bytes. Reloading Parquet
  preserved all rows.
- MRPC split with seed 42: 2,567 train, 550 validation, 551 test. Repeating
  the seed produced identical assignments.
- C4 streamed without downloading the full corpus. After the first-row
  connection warm-up, attempts read 9,178 and 18,137 more examples in about
  ten seconds each. Exact timings and startup delays are in
  `../outputs/remaining-exercises.txt`.
- The readable IMDB preview and split summary are captured in
  `../outputs/streaming-preview-readable.txt`.

Evidence is saved in `../outputs/`.
