# Dev Environment

Course lesson: [Dev Environment](https://aiengineeringfromscratch.com/lesson?path=phases/00-setup-and-tooling/01-dev-environment)

## Goal

Prepare a Python environment for the course. Keep its packages separate from
other projects. Check that the required tools work before you begin later
lessons.

## Setup Status

Completed in `course-repo/`: created `.venv` with Python 3.12.3; installed
NumPy, Matplotlib, Jupyter, and CPU-only PyTorch; confirmed Node.js and pnpm;
and passed the official beginner preflight (Python and Git, 2/2). See
[`verification/environment-check.md`](verification/environment-check.md) for
the recorded results.

## The four layers

| Layer | Examples | Purpose |
|---|---|---|
| System | Operating system, shell, Git, GPU drivers | Runs the tools |
| Package managers | `uv`, `pnpm`, `cargo`, `juliaup` | Installs project dependencies |
| Language runtimes | Python, Node.js, Rust, Julia | Runs code in each language |
| AI libraries | NumPy, PyTorch, JAX, Transformers | Provides reusable AI operations |

Install and check the layers from the system upward. Each layer depends on the
layers below it.

## What you need to start

The beginner route requires Python 3.11 or newer and Git. The course verifier
checks these two tools first. It reports other tools as optional or needed in
later lessons.

This workspace previously reported Python 3.12.3, Git 2.43.0, and Node.js
26.13.0. Your terminal found `uv 0.13.6` after you added `~/.local/bin` to
the current `PATH`. Check the versions again in your own terminal before you
rely on them.

You do not need a GPU to start. This machine has the CPU-only PyTorch build in
`course-repo/.venv`; CUDA is unavailable. Rust and Julia are installed, though
their GPU or performance features are not needed for the beginner route.

## Inspect your current setup

Run the Python script from the root of The-AI-Forge:

```bash
python3 phases/00-setup-and-tooling/01-dev-environment/code/check_environment.py
```

It reports the operating system and Python version. Record the output in
`outputs/environment-check.txt`. Record individual versions in
`verification/tool-versions.txt`. Extend the script as you learn to check
other tools.

Run each available example in `code/` with its language runtime. Save actual
terminal output in [outputs/environment-check.txt](outputs/environment-check.txt).
Mark a program as not run when its runtime is unavailable.

## Set up the course environment

Run these commands from the cloned course repository root. That folder must
contain the course `README.md` and `phases/` directory. Do not run them from
this personal notes repository.

Check the required tools:

```bash
python3 --version
git --version
uv --version
```

Create an isolated Python environment and install packages used by early
lessons:

```bash
uv python install 3.12
uv venv
source .venv/bin/activate
uv pip install numpy matplotlib jupyter
```

The `.venv` folder holds packages for this project. Activation makes its
Python available to commands in the current terminal.

Check that the packages import:

```bash
python3 -c "import numpy, matplotlib, jupyter; print('Python packages are ready')"
```

Run the course preflight from the course repository root:

```bash
python3 phases/00-setup-and-tooling/01-dev-environment/code/verify.py --route beginner
```

The preflight checks Python and Git for this route. It prints the next course
command when both checks pass. Add `--show-later` to inspect optional tools.

## Keep `uv` available in zsh

Your current `export PATH="$HOME/.local/bin:$PATH"` command only affects the
open terminal. Add this line once to `~/.zshrc` to use `uv` in new terminals:

```zsh
export PATH="$HOME/.local/bin:$PATH"
```

Then reload the file and check `uv`:

```zsh
source ~/.zshrc
uv --version
```

Rustup and Juliaup also add their executable directories to your shell path.
Open a new terminal after installation, or reload `~/.zshrc`, then run
`rustc --version`, `cargo --version`, and `julia --version`.

## Troubleshooting

If zsh reports `command not found: uv`, check whether `~/.local/bin` is on
`PATH`. If `source .venv/bin/activate` fails, `uv venv` did not create the
environment in the current directory. Change to the course repository root
and run `uv venv` there.

## Checkpoint

Explain why the system layer comes before package managers and runtimes.
Record your command output in [environment verification](verification/environment-check.md).
