# Environment Check

Complete this checklist after you run the setup commands.

## Required for the beginner route

- [x] Python 3.11 or newer: Python 3.12.3 was found in the workspace.
- [x] Git: version 2.43.0 was found in the workspace.
- [x] Confirm both versions in a fresh zsh login shell: Python 3.12.3 and Git 2.43.0.

## Project environment

- [x] `uv` runs in a fresh zsh login shell: uv 0.13.6.
- [x] Clone the course repository and create `.venv` there.
- [x] Install and import NumPy, Matplotlib, and Jupyter.
- [x] Install PyTorch and confirm it imports. CPU build 2.15.0; CUDA is unavailable on this machine.
- [x] Confirm Node.js and pnpm work in a fresh zsh login shell.
- [x] Run the course beginner preflight from the course repository root.

## Result

- Date: 2026-10-31
- Course repository path: `course-repo/` inside this workspace.
- Checkout: sparse checkout containing the Dev Environment lesson and the first Math Foundations lesson.
- Virtual environment: `.venv/`, created with Python 3.12.3.
- Packages: NumPy, Matplotlib, Jupyter, and CPU-only PyTorch installed. The package import check printed `Python packages are ready`; PyTorch reported `2.15.0+cpu` and `CUDA available: False`.
- Node toolchain: Node.js v26.13.0 and pnpm 12.16.1 are available in a fresh zsh login shell.
- Preflight result: Passed, 2/2 required beginner checks (Python and Git).
- Next lesson readiness: the preflight's suggested vectors command is present in the checkout.
- Error and fix: `uv`, Rust, and Julia initially were not found in the shell. Their user-level install directories are now loaded in zsh; fresh-shell version checks succeeded. Package downloads required network access.

## Checkpoint Answer

The system layer comes first because it provides the foundation for all development tools. It includes the operating system, hardware, system libraries, terminal and environment settings.

Package managers such as `uv`, `npm` and `Cargo`, as well as runtimes like Python, Node.js, Rust and Julia, depend on this foundation to work correctly.

Setting up the system layer first reduces compatibility and installation
problems and provides a stable base for AI engineering tools.

## Additional Environment Check

Command: `python3 phases/00-setup-and-tooling/01-dev-environment/code/check_environment.py`

Result: Linux; Python 3.12.3. The script completed successfully.
