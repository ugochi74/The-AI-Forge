# The-AI-Forge

Building and documenting my AI engineering learning journey, with the goal of becoming a competent AI engineer and building a personal AI chatbot.

## Learning path

- [Study plan](LEARNING.md)
- [Phase 00: Setup & Tooling](phases/00-setup-and-tooling/README.md)

## Progress

**Phase 00: Setup & Tooling is complete.** Next: Phase 1 — Math Foundations.

Lessons 01–12 have recorded **3/3 lesson quiz scores**; Lesson 13 has **2/2**.

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
| [10 · Terminal & Shell](phases/00-setup-and-tooling/10-terminal-and-shell/docs/en.md) | Complete | Practiced command pipelines, text filtering, output redirection, system monitoring, rsync synchronization, and persistent Zsh aliases. Quiz: 3/3. |
| [11 · Linux for AI](phases/00-setup-and-tooling/11-linux-for-ai/) | Complete | Quiz 3/3; completed filesystem navigation, permissions, ownership, process management, resource monitoring, APT, and networking exercises. Quiz recorded. |
| [12 · Debugging & Profiling](phases/00-setup-and-tooling/12-debugging-and-profiling/) | Complete | Quiz 3/3; CPU practical checks passed; GPU skipped. |
| [13 · Python for AI Engineering](phases/00-setup-and-tooling/13-python-for-ai-engineering/) | Complete | Quiz 2/2; Python/TypeScript demos, 31 tests and five exercises passed. |

## Repository layout

- `phases/`: lesson work organized by phase and numbered lesson.
- Lesson folders contain `code/`, `outputs/`, `verification/`, notes, and reflections as applicable.
- `AI-Engineering-skills-map/`: AI engineering skills articles.
- `LEARNING.md`: study plan, quiz scores, and completed lesson history.

## Current progress: Phase 0 complete

[Lesson 12 — Debugging & Profiling](phases/00-setup-and-tooling/12-debugging-and-profiling/README.md): quiz **3/3**. CPU debugging, training, NaN injection, profiling, scripted debugger inspection, and TensorBoard checks passed. GPU work was skipped on this CPU-only environment.

[Lesson 13 — Python for AI Engineering](phases/00-setup-and-tooling/13-python-for-ai-engineering/README.md): quiz **2/2**. Python and TypeScript demos, all 31 supplied tests, and all five Python exercises passed. Outputs, reflections, dependency versions and runbooks are saved in both lesson workspaces.

The agent executed the practical checks; learner checkpoints, quiz answers and reflection were recorded separately. Independent debugger practice remains available in the runbook.

**Next lesson:** Phase 1, Lesson 01 — Linear Algebra Intuition. Use `learn` to start, or `check-understanding 0` for an optional Phase 0 review.

## Previous focus: Terminal & Shell

Completed the practical work for **Terminal & Shell** on 2026-11-09.

Practiced command pipelines and text filtering with `grep`, `wc`, and `awk`; output redirection; system resource monitoring; rsync synchronization; and persistent Zsh aliases.

Used a sample training log to extract four loss values, captured error and command output, recorded training history, and synchronized local directories using rsync.

SSH, SCP, and rsync clients are available. Personal SSH key generation is not permitted by workplace policy, and `tmux` and `screen` are not installed.

The [Lesson 10 documentation](phases/00-setup-and-tooling/10-terminal-and-shell/docs/en.md), [command notes](phases/00-setup-and-tooling/10-terminal-and-shell/notes.md), reflection, and practice outputs record the work. Lesson commits were pushed to `main`, including the corrected rsync practice commit `580f7ea`.

The practical work is complete; the quiz score has not yet been recorded.

## Previous focus: Data Management

Completed **Data Management** on 2026-11-06.

Loaded and cached MRPC, compared CSV and Parquet sizes, reloaded Parquet, and verified a repeatable 70/15/15 split. Streamed C4 briefly without downloading its full corpus.

The local utility, prompt, and command results are in the [Lesson 09 workspace](phases/00-setup-and-tooling/09-data-management/README.md).

## Earlier focus: Docker for AI

Completed the Docker for AI theory quiz with **3/3**.

Reviewed Python environments, container images, Dockerfiles, `RUN`, `WORKDIR`, `CMD`, and `COPY`. Practiced reasoning about copied files versus bind mounts, named volumes, service-name networking, host/container ports, HTTP versus HTTPS, Compose lifecycle commands, CUDA base variants, and build caching.

The [Lesson 7 exercise runbook](phases/00-setup-and-tooling/07-docker-for-ai/README.md) covers all four practical exercises, with an optional GPU configuration.

Python and YAML syntax checks passed. Actual container builds and runtime exercises were blocked because Docker daemon access was denied and Docker Compose was missing. Container image-size measurements were therefore not run.

The [Lesson 7 outputs](phases/00-setup-and-tooling/07-docker-for-ai/outputs/README.md) include captured prerequisite errors and a script for recording future build and exercise results automatically.

The [Docker session reflection](phases/00-setup-and-tooling/07-docker-for-ai/reflection.md) records the concepts reviewed, misconceptions clarified, and hands-on work still needed for optional future practice.




# Phase 01: Math Foundations

**Goal:** Understand the mathematical foundations behind AI and machine learning through practical exercises and code.

## Lesson Progress

| No. | Lesson | Status |
|---|---|---|
| 01 | [Linear Algebra Intuition](phases/01-math-foundations/01-linear-algebra-intuition/) | Complete |
| 02 | [Vectors, Matrices & Operations](phases/01-math-foundations/02-vectors-matrices-operations/) | In progress |
| 03 | Matrix Transformations & Eigenvalues | Not started |
| 04 | Calculus for ML: Derivatives & Gradients | Not started |
| 05 | Chain Rule & Automatic Differentiation | Not started |
| 06 | Probability & Distributions | Not started |
| 07 | Bayes' Theorem & Statistical Thinking | Not started |
| 08 | Optimization: Gradient Descent Family | Not started |
| 09 | Information Theory: Entropy, KL Divergence | Not started |
| 10 | Dimensionality Reduction: PCA, t-SNE, UMAP | Not started |
| 11 | Singular Value Decomposition | Not started |
| 12 | Tensor Operations | Not started |
| 13 | Numerical Stability | Not started |
| 14 | Norms & Distances | Not started |
| 15 | Statistics for ML | Not started |
| 16 | Sampling Methods | Not started |
| 17 | Linear Systems | Not started |
| 18 | Convex Optimization | Not started |
| 19 | Complex Numbers for AI | Not started |
| 20 | The Fourier Transform | Not started |
| 21 | Graph Theory for ML | Not started |
| 22 | Stochastic Processes | Not started |

## Standard Lesson Structure

Each lesson will contain:

- `notes.md` — explanations and important concepts.
- `code/` — practical implementations.
- `outputs/` — actual program outputs and exercise results.
- `verification/` — test results and evidence.
- `reflection.md` — personal learning reflections.

## Learning Rules

1. Understand the concept before implementing it.
2. Write and run the practical examples.
3. Record actual outputs.
4. Complete the lesson exercises and quiz.
5. Update `LEARNING.md` after completing each lesson.

**Current focus:** Lesson 02 — Vectors, Matrices & Operations (Lesson 01 Complete).
