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
| 0 | Setup & Tooling | Done | 16 |
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
| 2026-11-06 | 0/09 | 3/3 | Loaded and cached MRPC, compared CSV/Parquet, verified repeatable 70/15/15 splits, and streamed C4 without downloading the full corpus. Most useful chatbot practice: keep downloaded artifacts out of Git and use DVC/cloud pointers when sharing versions. |
| 2026-11-09 | 0/10 | 3/3 | Practised shell pipelines and text filtering (`grep`, `wc`, `awk`), output redirection, system monitoring, rsync synchronization, and persistent Zsh aliases. Saved lesson documentation, reflection, and practice outputs; committed and pushed the work on `main`. Quiz completed 2026-11-10: C, D, A; correctly identified tmux session reattachment, combined stdout/stderr redirection, and SSH local port forwarding. |
| 2026-11-10 | 0/11 | 3/3 | Practised Linux filesystem navigation, permissions, ownership, process management, CPU and memory monitoring, disk usage, APT package information, and networking. Saved system-check and process-network practice reports. Documented workstation limits including unavailable tmux, screen, and nvidia-smi tools. Passed the quiz on execute permissions, directory disk usage, and macOS/Linux sed differences (C, C, D). |
| 2026-11-11 | 0/12 | 3/3 | Quiz answers B, C, D: data leakage, data-loading bottlenecks, and NaN debugging. Correctly matched tensor input shape, recognized overfitting, and chose tracemalloc for growing Python allocations. CPU practical checks passed, including training, NaN injection, scripted pdb, line/memory profiling and TensorBoard HTTP 200. GPU checks skipped. Learner reflection saved; hands-on learner debugger use is not claimed. |
| 2026-11-11 | 0/13 | 2/2 | Quiz answers D, A: shared mutable defaults and fitting standardization on training data only. Correctly predicted seeded splits, batch sizes, standardized value, and generator memory behavior. Python/TypeScript demos, 31 supplied tests, and all five Python exercises ran; learner reflection saved: use tracemalloc for long-chat memory growth and cProfile for retrieval bottlenecks. |

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

- Lesson: 0/09 — Data Management (**complete**).
- Quiz: 3/3; answers C, C, A.
- Verified MRPC caching, five examples, CSV/Parquet size comparison and
  round-trip, reproducible 70/15/15 splits, C4 streaming, model cache reuse,
  and lesson-local ignore rules. Practical output is saved under the Lesson 09
  `outputs/` folder.
- Reflection: keep downloaded files out of Git; use DVC or cloud storage
  pointers when a production chatbot needs shared data versions.
- Next lesson: 0/10 — Terminal & Shell.

**## Current session**

- Lesson: 0/10 — Terminal & Shell (**complete**).
- Covered: command pipelines, text filtering, output redirection, system resource monitoring, rsync synchronization, and shell aliases.
- Practical work: analyzed a sample training log, extracted four loss values, captured errors and command output, recorded training history, and synchronized local directories using rsync.
- Environment notes: SSH, SCP, and rsync clients are available. Personal SSH key generation is not permitted by workplace policy. `tmux` and `screen` were not installed.
- Git: lesson documentation, notes, reflection, and practice outputs were committed and pushed on `main`. Corrected rsync commit: `580f7ea`.
- Quiz: 3/3, completed 2026-11-10; answers C, D, A. Correctly identified tmux session reattachment, combined stdout/stderr redirection, and SSH local port forwarding.
- Next lesson: 0/11 — Linux for AI.


## Current session

Phase 0 — Setup & Tooling: **complete**. Lessons 01–13 have recorded quiz results.

- Lesson 0/12 — Debugging & Profiling: **complete**, quiz **3/3** (B, C, D), 2026-11-11.
- Lesson 0/13 — Python for AI Engineering: **complete**, quiz **2/2** (D, A), 2026-11-11.
- Learner checkpoints: matched tensor input dimensions, recognized overfitting, selected tracemalloc for memory growth, predicted repeatable splits, batch sizes, standardization arithmetic and generator memory behavior.
- NaN detection needed guided examples earlier; revisit it in a future warm-up.
- Agent-executed practical work: full CPU debugging toolkit; 300-step training with TensorBoard; deliberate NaN failure; cProfile, line_profiler, memory_profiler and tracemalloc; scripted pdb inspection; TensorBoard HTTP 200; Python and TypeScript toolkit demos; 31 course tests; all five Python exercises including NumPy comparisons.
- GPU memory exercise explicitly skipped: no CUDA/MPS GPU. Scripted pdb verification is not hands-on learner debugger evidence.
- Environment: project `.venv`; CPU PyTorch, NumPy, TensorBoard and profilers installed. Pinned setuptools 80.9.0 fixes TensorBoard's pkg_resources dependency. TypeScript uses local tsx and package-lock.json. Final pip check passed.
- Learner reflection: "I will use tools like tracemalloc and cProfile to catch memory leaks in long chat sessions and pinpoint slow bottlenecks in my retrieval"
- Source manifests, runbooks, dependency versions, reflection, and actual output reports are saved in the Lesson 12 and 13 folders.
- Next lesson: **1/01 — Linear Algebra Intuition**. Phase 1 has not started.
- Optional phase review: `check-understanding 0`.


## Review queue
Empty for now; learn adds lessons the quizzes flag.
