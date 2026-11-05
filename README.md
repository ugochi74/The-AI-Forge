# The-AI-Forge

Building and documenting my AI engineering learning journey, with the goal of
becoming a competent AI engineer and building a personal AI chatbot.

## Learning path

- [Study plan](LEARNING.md)
- [Phase 00: Setup & Tooling](phases/00-setup-and-tooling/README.md)

## Progress

Currently studying **Phase 00: Setup & Tooling**. Lessons 01–08 are complete. Each has a
**3/3 lesson quiz**.

| Lesson | Status | Work recorded |
|--------|--------|---------------|
| [01 · Dev Environment](phases/00-setup-and-tooling/01-dev-environment/) | Complete | Ran Python, TypeScript, Rust, and Julia examples; verified development tools. |
| [02 · Git & Collaboration](phases/00-setup-and-tooling/02-git-and-collaboration/) | Complete | Practiced staging, commits, branches, history, and pushing progress to a personal fork. |
| [03 · GPU Setup & Cloud](phases/00-setup-and-tooling/03-gpu-setup-and-cloud/) | Complete | Verified the local CPU environment and tested PyTorch CUDA on a Colab Tesla T4. |
| [04 · APIs & Keys](phases/00-setup-and-tooling/04-apis-and-keys/) | Complete | Reviewed API key storage, authentication headers, and rate-limit responses. |
| [05 · Jupyter Notebooks](phases/00-setup-and-tooling/05-jupyter-notebooks/) | Complete | Practiced notebook calculations and when to move reusable code into Python scripts. |
| [06 · Python Environments](phases/00-setup-and-tooling/06-python-environments/) | Complete | Created and verified a virtual environment with NumPy, Matplotlib, Jupyter, scikit-learn, and pandas. |
| [07 · Docker for AI](phases/00-setup-and-tooling/07-docker-for-ai/) | Complete | Quiz 3/3; local syntax/path checks passed. Runtime exercises not run: Docker daemon access denied and Compose missing. GPU test not run: CPU-only host. |
| [08 · Editor Setup](phases/00-setup-and-tooling/08-editor-setup/) | Complete | Quiz 3/3; eight extensions installed, formatting/type checks, script execution, and notebook execution verified. Remote connection not run: no host identified. |

## Repository layout

- `phases/`: lesson work organized by phase and numbered lesson.
- Lesson folders contain `code/`, `outputs/`, `verification/`, notes, and
  reflections as applicable.
- `AI-Engineering-skills-map/`: AI engineering skills articles.
- `LEARNING.md`: study plan, quiz scores, and completed lesson history.

## Current focus

As of **2026-11-05**, resumed Docker for AI and answered both Python environment
recall questions correctly (unscored). Discussed why a Python package list alone
does not capture the runtime environment and why CUDA requires compatible GPU
hardware.

Confirmed that containers can reuse an existing image and that Dockerfile
`RUN` instructions install packages at build time. Reviewed the container's
separate Python installation, `WORKDIR`, `CMD`, and copying code with `COPY`.
Correctly predicted the difference between copied and bind-mounted code, and
that files saved through a bind mount survive container removal. Reviewed named
volume reuse, service-name networking, host/container ports, and HTTP versus
HTTPS; correctly recalled `http://api:5000` on a later check. Also reviewed
Compose lifecycle commands, CUDA base variants versus image tags, and build
caching. Correctly predicted reuse of an unchanged package installation step.
The [Lesson 7 exercise runbook](phases/00-setup-and-tooling/07-docker-for-ai/README.md)
now covers all four practical exercises, with an optional GPU configuration.
Python and YAML syntax checks passed; the actual build was blocked by Docker
daemon permissions, and Docker Compose is missing. Container exercises and image-size
measurements were not run because Docker daemon access is denied and Compose
is missing. The theory quiz is passed: **3/3**. The exact resume point is saved
in [the study plan](LEARNING.md#current-session).

The [Lesson 7 outputs](phases/00-setup-and-tooling/07-docker-for-ai/outputs/README.md)
include captured prerequisite errors and a script for recording future build
and exercise results automatically.

The [Docker session reflection](phases/00-setup-and-tooling/07-docker-for-ai/reflection.md)
records the concepts reviewed, misconceptions clarified, and hands-on work still
needed for optional future practice. Lesson 7 is complete; the theory quiz is passed.

## Latest lesson

Completed [Editor Setup](phases/00-setup-and-tooling/08-editor-setup/README.md)
with a **3/3** quiz. Verified formatting on save, type warnings and hover
signatures, Python script execution, and Jupyter execution with the project
`.venv`. Next: **Data Management**.
