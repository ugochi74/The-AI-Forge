# Notebook Troubleshooting Helper

When a notebook fails, identify the symptom first. Do not assume the visible
cell order matches the order the kernel actually ran.

| Symptom | Check | Fix |
|---|---|---|
| `NameError` for a variable | Was its setup cell run in this kernel? | Use **Restart and Run All** from the top. |
| Works only after clicking cells in a certain order | Does a later cell depend on a variable created by an earlier cell? | Restart the kernel and run every cell top to bottom. |
| A deleted variable still seems to exist | Is the old value still in kernel memory? | Restart the kernel, then rerun the notebook. |
| Notebook uses too much memory | Are large arrays, dataframes, or models still referenced? | Delete unused variables; call `gc.collect()` if needed, or restart the kernel. |
| `ModuleNotFoundError` | Is the notebook kernel using the environment where the package was installed? | Install the package in the active environment and select that environment's kernel. |
| A plot does not appear | Did the cell create/show a plot, and is Matplotlib installed? | Run the plotting cell; use `%matplotlib inline` if needed. |
| Slow operation timing changes between runs | Is this a small operation or a long cell? | Use `%timeit` for repeated microbenchmarks; use `%%time` for one longer cell run. |
| Colab file disappeared | Was it saved outside the temporary session storage? | Save to Google Drive or download the notebook/output before the session ends. |

## Safe recovery sequence

1. Read the full error and identify the cell that failed.
2. Confirm the selected kernel and required package versions.
3. Restart the kernel and run all cells in order.
4. Fix the first failing cell, then repeat the clean run.
5. Save the notebook and any output files you need to keep.
