# Jupyter Notebooks

Course lesson: [Jupyter Notebooks](https://aiengineeringfromscratch.com/lesson?path=phases/00-setup-and-tooling/05-jupyter-notebooks)

## Goal

Use a notebook to explore data and test ideas, then move reusable code into a
Python script. Keep experiments reproducible by running every cell in order
from a clean kernel.

## Core ideas

- A notebook (`.ipynb`) combines code cells, Markdown cells, and saved outputs.
- The kernel is the Python process behind the notebook. It runs cells and keeps
  variables in memory between runs.
- Cells run in the order you execute them, not necessarily top to bottom. A
  variable can remain in the kernel after its defining cell is edited or
  deleted; use **Restart and Run All** before sharing.
- `%timeit` repeats one line and reports an average. `%%time` runs one cell
  once and reports elapsed time.
- Use notebooks to explore, prototype, visualize, and explain. Move reusable
  utilities, training pipelines, and production code into `.py` files.
- Large arrays and models remain in kernel memory. Delete unneeded variables or
  restart the kernel when memory use grows.

## Build evidence

- `code/jupyter_basics.ipynb` compares Python and NumPy timings, loads the
  sample CSV, displays a DataFrame, plots accuracy, and demonstrates shared
  kernel state.
- `code/notebook_tips.py` contains reusable examples that can run as a script
  or be imported into a notebook.
- `outputs/prompt-notebook-helper.md` is a quick diagnostic guide for common
  notebook problems.

## Run

From the repository root, start Jupyter with its data, configuration, and
runtime files inside the project environment. This workspace does not allow
writing those files to the usual user directory:

```bash
JUPYTER_DATA_DIR="$PWD/.venv/share/jupyter" \
JUPYTER_CONFIG_DIR="$PWD/.venv/etc/jupyter" \
JUPYTER_RUNTIME_DIR="$PWD/.venv/runtime" \
IPYTHONDIR="$PWD/.venv/etc/ipython" \
.venv/bin/jupyter lab
```

The direct dependencies are listed in `requirements-notebooks.txt`.

Open `phases/00-setup-and-tooling/05-jupyter-notebooks/code/jupyter_basics.ipynb`
and use **Kernel → Restart and Run All**. The notebook reads its fixture from
`outputs/model_metrics.csv`.

## Notes from the lesson

The average example used during the lesson was `numbers = [3, 6, 9]`, giving
`Average: 6.0`. In a notebook, that result appears under the cell; in a script,
the `print` call writes it to the terminal.
