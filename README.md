# The-AI-Forge

Building and documenting my AI engineering learning journey, with the goal of becoming a competent AI engineer and building a personal AI chatbot.

## Learning path

- [Study plan](LEARNING.md)
- [Phase 00: Setup & Tooling](phases/00-setup-and-tooling/README.md)

## Progress

Currently working through **Phase 00: Setup & Tooling**. Lessons 01–09 have recorded **3/3 lesson quiz scores**. Lesson 10 is complete; its quiz score has not been recorded.

| Lesson | Status | Work recorded |
|--------|--------|---------------|
| [01 · Dev Environment](phases/00-setup-and-tooling/01-dev-environment/) | Complete | Ran Python, TypeScript, Rust, and Julia examples; verified development tools. |
| [02 · Git & Collaboration](phases/00-setup-and-tooling/02-git-and-collaboration/) | Complete | Practiced staging, commits, branches, history, and pushing progress to a personal fork. |
| [03 · GPU Setup & Cloud](phases/00-setup-and-tooling/03-gpu-setup-and-cloud/) | Complete | Verified the local CPU environment and tested PyTorch CUDA on a Colab Tesla T4. |
| [04 · APIs & Keys](phases/00-setup-and-tooling/04-apis-and-keys/) | Complete | Reviewed API key storage, authentication headers, and rate-limit responses. |
| [05 · Jupyter Notebooks](phases/00-setup-and-tooling/05-jupyter-notebooks/) | Complete | Practiced notebook calculations and when to move reusable code into Python scripts. |
| [06 · Python Environments](phases/00-setup-and-tooling/06-python-environments/) | Complete | Created and verified a virtual environment with NumPy, Matplotlib, Jupyter, scikit-learn, and pandas. |
| [07 · Docker for AI](phases/00-setup-and-tooling/07-docker-for-ai/) | Complete | Quiz 3/3; local syntax/path checks passed. Runtime exercises not run: Docker daemon access denied and Compose missing. GPU status not verified because `nvidia-smi` was unavailable. |
| [08 · Editor Setup](phases/00-setup-and-tooling/08-editor-setup/) | Complete | Quiz 3/3; eight extensions installed, formatting/type checks, script execution, and notebook execution verified. Remote connection not run: no host identified. |
| [09 · Data Management](phases/00-setup-and-tooling/09-data-management/) | Complete | Quiz 3/3; streamed IMDB and C4, cached and inspected MRPC, compared CSV/Parquet, verified seeded splits, and ignored downloaded artifacts. |
| [10 · Terminal & Shell](phases/00-setup-and-tooling/10-terminal-and-shell/docs/en.md) | Complete | Practiced command pipelines, text filtering, output redirection, system monitoring, rsync synchronization, and persistent Zsh aliases. Recorded command outputs and workplace tool constraints. |

## Repository layout

- `phases/`: lesson work organized by phase and numbered lesson.
- Lesson folders contain `code/`, `outputs/`, `verification/`, notes, and reflections as applicable.
- `AI-Engineering-skills-map/`: AI engineering skills articles.
- `LEARNING.md`: study plan, quiz scores, and completed lesson history.

## Current focus

Completed **Terminal & Shell** on 2026-11-09. Practiced command pipelines and text filtering with `grep`, `wc`, and `awk`; output redirection; system resource monitoring; rsync synchronization; and persistent Zsh aliases.

Used a sample training log to extract four loss values, captured error and command output, recorded training history, and synchronized local directories using rsync.

SSH, SCP, and rsync clients are available. Personal SSH key generation is not permitted by workplace policy, and `tmux` and `screen` are not installed.

The [Lesson 10 documentation](phases/00-setup-and-tooling/10-terminal-and-shell/docs/en.md), [command notes](phases/00-setup-and-tooling/10-terminal-and-shell/notes.md), reflection, and practice outputs record the work. Lesson commits were pushed to `main`, including the corrected rsync practice commit `580f7ea`.

**Next lesson: Linux for AI (Phase 00, Lesson 11).**

## Previous focus: Data Management

Completed **Data Management** on 2026-11-06. Loaded and cached MRPC, compared CSV and Parquet sizes, reloaded Parquet, and verified a repeatable 70/15/15 split. Streamed C4 briefly without downloading its full corpus. The local utility, prompt, and command results are in the [Lesson 09 workspace](phases/00-setup-and-tooling/09-data-management/README.md).

## Earlier focus: Docker for AI

As of **2026-11-05**, resumed Docker for AI and answered both Python environment recall questions correctly (unscored). Discussed why a Python package list alone does not capture the runtime environment and why CUDA requires compatible GPU hardware.

Confirmed that containers can reuse an existing image and that Dockerfile `RUN` instructions install packages at build time. Reviewed the container's separate Python installation, `WORKDIR`, `CMD`, and copying code with `COPY`. Correctly predicted the difference between copied and bind-mounted code, and that files saved through a bind mount survive container removal. Reviewed named volume reuse, service-name networking, host/container ports, and HTTP versus HTTPS; correctly recalled `http://api:5000` on a later check. Also reviewed Compose lifecycle commands, CUDA base variants versus image tags, and build caching. Correctly predicted reuse of an unchanged package installation step.

The [Lesson 7 exercise runbook](phases/00-setup-and-tooling/07-docker-for-ai/README.md) covers all four practical exercises, with an optional GPU configuration. Python and YAML syntax checks passed; the actual build was blocked by Docker daemon permissions, and Docker Compose is missing. Container exercises and image-size measurements were not run because Docker daemon access is denied and Compose is missing. The theory quiz is passed: **3/3**. The exact resume point is saved in [the study plan](LEARNING.md#current-session).

The [Lesson 7 outputs](phases/00-setup-and-tooling/07-docker-for-ai/outputs/README.md) include captured prerequisite errors and a script for recording future build and exercise results automatically.

The [Docker session reflection](phases/00-setup-and-tooling/07-docker-for-ai/reflection.md) records the concepts reviewed, misconceptions clarified, and hands-on work still needed for optional future practice. Lesson 7 is complete; the theory quiz is passed.

## Latest lesson

Completed [Terminal & Shell](phases/00-setup-and-tooling/10-terminal-and-shell/docs/en.md). Practiced shell pipelines, text filtering, redirection, system monitoring, rsync, and aliases. The quiz score has not been recorded. Next: **Linux for AI**.
