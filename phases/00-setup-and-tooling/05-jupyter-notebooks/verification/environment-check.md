# Environment Check

## Current workspace check

- [x] Python is available: Python 3.12.3.
- [x] JupyterLab and ipykernel are installed in the project `.venv`.
- [x] NumPy, pandas, and Matplotlib import successfully from the project `.venv`.
- [x] The `ai-forge` kernel is registered under `.venv/share/jupyter/kernels`.
- [ ] Open `code/jupyter_basics.ipynb` and run all cells from a fresh kernel.
- [ ] Confirm the DataFrame and chart render and both timing cells complete.

## Evidence

During the tutoring exercise, the learner reported `Average: 6.0` for the
three-number calculation. The system Python does not have Jupyter, so use
`.venv/bin/python` and `.venv/bin/jupyter`, with the project-local Jupyter
directories shown in `notes.md`. Notebook execution and its output checks
remain unchecked until the notebook is run from a Jupyter kernel.
