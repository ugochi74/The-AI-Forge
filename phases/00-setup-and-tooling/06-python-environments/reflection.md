# Lesson 06 Reflection: Python Environments

**Author:** Andrew.Nd

## What I Learned

I learned why Python projects need isolated environments and how virtual environments help prevent dependency conflicts.

I also learned about venv, uv, conda, package installation and dependency management.

## Practical Experience

I ran the official environment setup script.

The script detected that uv was unavailable and automatically used Python venv and pip instead.

It reused my existing `.venv`, installed the missing packages and successfully completed its verification checks.

## Challenges

The main issue was that uv was not available in my terminal.

This did not stop the setup because the script provided a pip fallback.

## What I Will Apply

I will create and use separate virtual environments for my Python projects, install dependencies inside the correct environment and avoid committing virtual environment folders to Git.

## Outstanding Items

PyTorch has not been installed because it is optional for this lesson. I will install it when a project requires it.