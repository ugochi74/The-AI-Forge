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

## Current session

- Date: 2026-11-05
- Lesson: 0/07 — Docker for AI (**in progress**, not yet completed).
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
- Resume here: run `phases/00-setup-and-tooling/07-docker-for-ai/README.md`
  on an approved Docker-enabled host, then review copied files versus bind mounts.
- Reflection: recorded the session's concepts, corrected misconceptions, and
  practical limits in `phases/00-setup-and-tooling/07-docker-for-ai/reflection.md`.
- Remaining: execute and verify the practical exercises, continue teaching,
  and take the lesson quiz. Lesson 0/07 remains
  in progress; prepared artifacts are not completion evidence.

## Review queue
Empty for now; learn adds lessons the quizzes flag.
