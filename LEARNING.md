# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
To become a competent AI Engineer and build a personal AI chatbot.

## Placement
- Date: 2026-10-30
- Score: self-selected
- Entry point: Phase 0: Setup & Tooling
- Pace: ~40 hours/week

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | 16 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 26 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP — Foundations to Advanced | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 76 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 34 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-10-31 | 0/01 | 3/3 | Passed the Dev Environment quiz; ran and recorded all four language examples; set up `course-repo/.venv` with NumPy, Matplotlib, Jupyter, and CPU PyTorch; verified Node/pnpm, Rust/Cargo, Julia, and the Python packages; beginner preflight passed 2/2. |
| 2026-11-01 | 0/02 | 3/3 | Practiced staging and committing selected files, branches, `.gitignore`, and history inspection. Forked the course repository and pushed `my-progress` (`da22ef4`) to the personal fork. |
| 2026-11-01 | 0/03 | 3/3 | Verified the local environment is CPU-only, configured Colab with a Tesla T4, confirmed PyTorch CUDA access, measured 2.797s CPU vs 0.088s GPU (~32x), and estimated about 8B fp16 weights from T4 memory. |
| 2026-11-02 | 0/04 | 3/3 | Reviewed safe API key storage, Anthropic's `x-api-key` header, and HTTP 429 rate limits; clarified that raw HTTP exposes request details and status/error responses hidden by SDK abstractions. |
| 2026-11-03 | 0/05 | 3/3 | Explained that notebooks are for trying ideas and inspecting results, while reusable chatbot code belongs in `.py` scripts; ran a small average calculation in a notebook cell. |
| 2026-11-04 | 0/06 | 3/3 | Set up and verified the Python environment using `.venv` and pip; installed and checked NumPy, Matplotlib, Jupyter, scikit-learn, and pandas; ran the setup script and passed all required checks. |
| 2026-11-05 | 0/07 | 3/3 | Complete: theory quiz 3/3 (D, C, B); local syntax/path checks passed. Runtime exercises not run because Docker daemon access is denied and Compose is missing; GPU test not run on CPU-only hardware. |
| 2026-11-05 | 0/08 | 3/3 | Configured VS Code; verified Black on save, Pylance warning/signature, script output Hello, Andrew, and notebook result 12 using project .venv/ipykernel. All eight extensions confirmed. Remote connection not run: no remote host identified. |

## Lesson 07 session record

- Date: 2026-11-05
- Lesson: 0/07 — Docker for AI (**complete**).
- Recall: answered both Python environment warm-up questions correctly
  (interpreter path and pip/conda dependency tracking); these were unscored.
- Covered: why a package list alone misses the runtime environment; Docker
  images versus containers; the Dockerfile's base image and environment settings.
- Checkpoint: correctly identified that CUDA acceleration needs a server with
  an NVIDIA GPU after discussing why an image cannot add GPU hardware.
- Checkpoint: correctly explained that another container can reuse an image
  after the first container stops. Initially expected each container to install
  NumPy again; clarified that Dockerfile `RUN` instructions execute at image
  build time and correctly identified this on follow-up.
- Checkpoint: after clarification, correctly identified that the container uses
  its own Python 3.12 even when the host uses Python 3.11. Explained that `CMD`
  starts the chatbot and `COPY` puts its script into the image; discussed
  `WORKDIR /workspace` as the working directory, not an automatic code copy.
- Practical work requested: prepared the four lesson exercises with a Flask API,
  Compose services, optional GPU override, persistent-storage checks, a CUDA
  devel/runtime build argument, and a command runbook. Python/YAML syntax passed.
- Build attempt: Docker client 28.2.2 is present, but daemon access was denied
  even with elevated execution; Docker Compose is missing. No image build,
  container execution, HTTP response, or image-size measurement was verified.
- Output capture: added `code/capture_outputs.sh` and ran its prerequisite check;
  actual Docker/Compose errors and exit codes are saved under
  `outputs/run-20261105T021644Z-6gS5vw/`. Shell syntax passed. The script can
  capture full exercise results when Docker access and Compose are available.
- Checkpoint: correctly predicted that an image's copied script still prints
  `Hello` after a host edit without rebuilding, while a bind-mounted script
  prints `Welcome` on the next run. Correctly explained that files saved through
  the `/models` bind mount remain in the host folder after container removal.
- Checkpoint: understood that a replacement Qdrant container can reuse a named
  volume. Correctly selected the Flask service name `api` for communication
  from `ai-dev`. Needed clarification that published host ports do not change
  container ports; then described these as outside versus internal entrances.
- Checkpoint: HTTP versus HTTPS needed repeated clarification; eventually
  selected `http://` for the Flask example without TLS. Revisit this distinction
  in a later example rather than treating it as mastered.
- Checkpoint: reviewed Compose status/logs and shutdown; understood `down -v`
  removes the project's declared named and attached anonymous volumes, with
  external volumes and bind-mounted host folders excluded.
- Checkpoint: chose the CUDA runtime base for running prebuilt packages.
  Initially confused the image tag with base selection; correctly identified
  `--build-arg CUDA_VARIANT=runtime` as choosing the variant after clarification.
  Correctly predicted reuse of a cached Flask installation when only a later
  copied application file changes.
- Checkpoint: described Compose as a conductor and correctly recalled
  `http://api:5000` for the Flask service after the port/protocol review.
- Quiz: passed all three post-lesson questions, 3/3 (D, C, B): persistent
  storage, NVIDIA Container Toolkit, and service-name networking.
- System limitations: image builds, container network/HTTP checks, persistence,
  and image-size comparison were not run because Docker daemon access is denied
  and Docker Compose is missing. GPU execution was not run on the CPU-only host.
- Available checks rerun: Python/YAML/shell syntax and bind source paths passed;
  actual results saved in the lesson outputs/local-checks.txt.
- Resume here: advance to the next unlogged Phase 0 lesson. The Lesson 7 runbook
  remains available for optional future runtime practice.
- Reflection: recorded the session's concepts, corrected misconceptions, and
  practical limits in `phases/00-setup-and-tooling/07-docker-for-ai/reflection.md`.
- Lesson 0/07 is complete for the learning plan.
  No successful container execution or image-size measurement is claimed.

## Current session

- Lesson: 0/08 — Editor Setup (**complete**).
- Quiz: 3/3; answers D, D, D.
- Verified: eight recommended extensions, Black on save, Pylance diagnostics
  and hover signatures, script execution, and notebook execution.
- Troubleshooting: Black waited for environment discovery; configured its
  python3 interpreter. Created .venv and installed ipykernel for notebooks.
- Optional Remote SSH connection not run: no remote host identified.
- Next lesson: 0/09 — Data Management.

## Review queue
Empty for now; learn adds lessons the quizzes flag.
