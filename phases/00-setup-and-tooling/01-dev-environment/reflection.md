# Reflection

## Why does the system layer come before runtimes and AI libraries?

The system layer provides the operating system, shell, hardware support, and
system libraries that runtimes and package managers depend on. Setting it up
first gives the higher layers a stable foundation.

## Which setup step failed, and how did you fix it?

The shell initially could not find `uv` because `~/.local/bin` was not on
`PATH`. Adding that directory to the shell configuration fixed it. Rust and
Julia also needed their installer-managed directories loaded into zsh; they
now work in a login shell.

## Which command confirms that your project packages are ready?

After creating and activating the course repository's virtual environment and
installing the packages, this import check confirms NumPy, Matplotlib, and
Jupyter are available:

```bash
python3 -c "import numpy, matplotlib, jupyter; print('Python packages are ready')"
```

It printed `Python packages are ready`. PyTorch also imports successfully as
version `2.15.0+cpu`; CUDA is unavailable, and a GPU is not needed for the
beginner route.

## What setup task remains before the next lesson?

The setup work is complete: the course repository has a `.venv`, the lesson
packages and pnpm are installed, and the beginner preflight passed. The next
step is to open the next lesson and follow its first exercise.
