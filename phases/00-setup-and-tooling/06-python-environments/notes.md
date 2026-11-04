# Lesson 06: Python Environments

**Author:** Andrew.Nd  
**Course:** AI Engineering from Scratch  
**Phase:** 00 - Setup and Tooling  
**Lesson:** 06 - Python Environments

## 1. What Are Python Environments?

A Python environment is an isolated space where a project keeps its own Python packages and dependencies.

Different projects may require different versions of the same package. Virtual environments help prevent dependency conflicts between projects.

## 2. Environment Management Tools

- **venv:** Python's built-in tool for creating virtual environments.
- **uv:** A fast Python package and project manager.
- **conda:** An environment and package manager commonly used in data science and machine learning.

## 3. Dependency Management

- `pyproject.toml` describes project information and dependencies.
- Lockfiles record resolved dependency versions.
- Virtual environments keep project packages separate from global Python packages.

## 4. Useful Commands

Activate an environment:

```bash
source .venv/bin/activate
```

Install a package:

```bash
python -m pip install package-name
```

Check installed packages:

```bash
python -m pip list
```

Check the Python executable:

```bash
which python
```

## 5. Good Practices

- Use a separate virtual environment for each project.
- Activate the correct environment before running code.
- Avoid installing project dependencies globally.
- Do not commit `.venv` to Git.
- Keep track of project dependencies.
- Avoid mixing pip and conda unnecessarily.

## 6. Practical Setup

The official environment setup script reused my existing `.venv`.

Since `uv` was unavailable, the script successfully used Python `venv` and pip.

The missing Jupyter and scikit-learn packages were installed successfully.

## Key Takeaway

Virtual environments make Python projects easier to manage by isolating dependencies and reducing package conflicts.