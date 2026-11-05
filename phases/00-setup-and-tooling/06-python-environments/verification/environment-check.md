# Python Environment Verification

**Author:** Andrew.Nd  
**Course:** AI Engineering from Scratch  
**Phase:** 00 - Setup and Tooling  
**Lesson:** 06 - Python Environments

## 1. Environment Details

- Python version: 3.12.3
- Virtual environment: `.venv`
- Python executable: `/home/recoding/The-AI-Forge/.venv/bin/python`
- Package manager used: pip 26.3
- uv: Not installed; pip fallback used successfully.

## 2. Installed Packages

| Package | Version | Status |
|---|---|---|
| NumPy | 2.5.4 | Installed |
| Matplotlib | 3.11.2 | Installed |
| Jupyter | 1.1.1 | Installed |
| Scikit-learn | 1.9.1 | Installed |
| Pandas | 3.1.0 | Installed |

Jupyter Core version: 5.9.1.

## 3. Verification Results

- Existing virtual environment successfully reused.
- Required core packages installed.
- Package version checks passed.
- NumPy matrix multiplication test passed.
- Setup script reported: All checks passed.

## 4. Optional Dependencies

- PyTorch: Not installed.
- uv: Not available in the terminal.

## 5. Final Result

The Python environment setup completed successfully using Python venv and pip. All required core package checks passed.

## Follow-up exercise verification

- Core environment rechecked: setup script reported all checks passed; see
  `../outputs/environment-recheck.txt`. This is newer than the versions above.
- Isolation verified: main `.venv` has NumPy 2.5.4; the separate
  `code/isolation-demo/.venv` has NumPy 1.26.4. See
  `../outputs/environment-isolation.txt`. Installing the older version in the
  second environment did not change the main version.
- Outside-environment install attempt was blocked by Ubuntu's PEP 668
  `externally-managed-environment` protection. No system package was changed;
  the output records the reason in `../outputs/system-install-check.txt`.

## Dependency project import check

Learner output confirms PyTorch 2.15.0+cpu and Anthropic 2.5.0 import in
`code/dependency-demo/.venv`. CPU tensor calculation returned `[2, 4, 6]`;
CUDA availability was false, as expected on this host. PyTorch warned that
NumPy was absent. Added NumPy to the project dependencies and reinstalled the
editable project; NumPy integration was then verified below.
See `../outputs/dependency-project-check.txt` for the initial import results.

## NumPy integration recheck

After reinstalling the editable project, learner output confirms NumPy 2.5.4,
PyTorch 2.15.0+cpu, and Anthropic 2.5.0. Tensor-to-NumPy conversion returned
`[2 4 6]` without the previous missing-NumPy warning. The learner also reported
`No broken requirements found` from pip check. See
`../outputs/dependency-numpy-check.txt`.

## Lockfile generation

Generated `code/dependency-demo/requirements.lock` successfully with pip-tools
under Python 3.12. It pins 26 packages, including NumPy 2.5.4, PyTorch
2.15.0+cpu, Anthropic 2.5.0, and setuptools 84.2.1. The CPU index is included
and `constraints-cpu.txt` preserves the CPU build. Generation output is in
`outputs/lockfile-generation.txt`.

## Fresh-environment lockfile verification

Installed `requirements.lock` in `code/dependency-demo/lock-check/.venv`.
Imports show NumPy 2.5.4, PyTorch 2.15.0+cpu, and Anthropic 2.5.0; tensor
conversion returned `[2 4 6]`. `pip check` returned no broken requirements.
Actual results: `../outputs/lockfile-reproduction.txt`. This verifies
reproduction for the tested Linux/Python 3.12 CPU environment. Lesson 06
practical checks are complete for this host; system-wide installation is
restricted by PEP 668 as recorded above.
