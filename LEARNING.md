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
| 1 | Math Foundations | In progress | 23 |
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
| 2026-11-13 | 1/01 | Complete | Built intuitive vector foundations, dot products, and cosine similarity. Implemented pure Python zero-dependency vector operations and neural network linear layer forward pass (y = Wx + b); all test assertions verified. |
| 2026-11-13 | 1/02 | In progress | Started vectors and matrices operations. Practised vector addition, scalar multiplication (including a negative scalar), matrix dimensions, and identifying a matrix element. Currently learning matrix addition; no lesson quiz score recorded yet. |
| 2026-11-18 | 1/01 | In progress | Reviewed vector normalization and cosine similarity, including examples with similarity values 1, 0, and -1. Practised matrix-vector multiplication by hand with a 2×2 matrix and different input vectors. |\n| 2026-11-19 | 1/01 | In progress | Implemented matrix-vector multiplication in Python using nested loops. Verified valid multiplication returns `[13, 23]`; tested incompatible dimensions and an empty matrix, both raising the expected `ValueError`. Practised matrix dimensions: columns determine input-vector length and rows determine output-vector length. |\n| 2026-11-20 | 1/01 | In progress | Implemented ReLU and vector ReLU, combined a linear layer with ReLU, and built a two-layer feed-forward network using reusable functions. Ran `two_layer_network.py` and verified output `[13, 4]`. Learned that forward propagation produces predictions and a loss function measures prediction error. Loss-function implementation is the next step; no quiz score recorded. |

## Lesson 07 session record

- Date: 2026-11-05
- Lesson: 0/07 — Docker for AI (**complete**).
- Recall: answered both Python environment warm-up questions correctly (interpreter path and pip/conda dependency tracking); these were unscored.
- Covered: why a package list alone misses the runtime environment; Docker images versus containers; the Dockerfile's base image and environment settings.
- Checkpoint: correctly identified that CUDA acceleration needs a server with an NVIDIA GPU after discussing why an image cannot add GPU hardware.
- Checkpoint: correctly explained that another container can reuse an image after the first container stops. Initially expected each container to install NumPy again; clarified that Dockerfile `RUN` instructions execute at image build time and correctly identified this on follow-up.
- Checkpoint: after clarification, correctly identified that the container uses its own Python 3.12 even when the host uses Python 3.11. Explained that `CMD` starts the chatbot and `COPY` puts its script into the image; discussed `WORKDIR /workspace` as the working directory, not an automatic code copy.
- Practical work requested: prepared the four lesson exercises with a Flask API, Compose services, optional GPU override, persistent-storage checks, a CUDA devel/runtime build argument, and a command runbook. Python/YAML syntax passed.
- Build attempt: Docker client 28.2.2 is present, but daemon access was denied even with elevated execution; Docker Compose is missing. No image build, container execution, HTTP response, or image-size measurement was verified.
- Output capture: added `code/capture_outputs.sh` and ran its prerequisite check; actual Docker/Compose errors and exit codes are saved under `outputs/run-20261105T021644Z-6gS5vw/`. Shell syntax passed. The script can capture full exercise results when Docker access and Compose are available.
- Checkpoint: correctly predicted that an image's copied script still prints `Hello` after a host edit without rebuilding, while a bind-mounted script prints `Welcome` on the next run. Correctly explained that files saved through the `/models` bind mount remain in the host folder after container removal.
- Checkpoint: understood that a replacement Qdrant container can reuse a named volume. Correctly selected the Flask service name `api` for communication from `ai-dev`. Needed clarification that published host ports do not change container ports; then described these as outside versus internal entrances.
- Checkpoint: HTTP versus HTTPS needed repeated clarification; eventually selected `http://` for the Flask example without TLS. Revisit this distinction in a later example rather than treating it as mastered.
- Checkpoint: reviewed Compose status/logs and shutdown; understood `down -v` removes the project's declared named and attached anonymous volumes, with external volumes and bind-mounted host folders excluded.
- Checkpoint: chose the CUDA runtime base for running prebuilt packages. Initially confused the image tag with base selection; correctly identified `--build-arg CUDA_VARIANT=runtime` as choosing the variant after clarification. Correctly predicted reuse of a cached Flask installation when only a later copied application file changes.
- Checkpoint: described Compose as a conductor and correctly recalled `http://api:5000` for the Flask service after the port/protocol review.
- Quiz: passed all three post-lesson questions, 3/3 (D, C, B): persistent storage, NVIDIA Container Toolkit, and service-name networking.
- System limitations: image builds, container network/HTTP checks, persistence, and image-size comparison were not run because Docker daemon access is denied and Docker Compose is missing. GPU execution was not run on the CPU-only host.
- Available checks rerun: Python/YAML/shell syntax and bind source paths passed; actual results saved in the lesson outputs/local-checks.txt.
- Reflection: recorded the session's concepts, corrected misconceptions, and practical limits in `phases/00-setup-and-tooling/07-docker-for-ai/reflection.md`.
- Lesson 0/07 is complete for the learning plan. No successful container execution or image-size measurement is claimed.

## Current session

- Phase 0 — Setup & Tooling: **complete**.
- Phase 1 — Math Foundations: **in progress**.
- Lesson 01 — Linear Algebra Intuition: **in progress**.
- Recent implementation: vector operations, normalization, dot product, cosine similarity, matrix-vector multiplication, a neural-network linear layer, ReLU activation, and a two-layer feed-forward network.
- Latest verified run: `two_layer_network.py` produced `[13, 4]` for the supplied weights, biases, and input.
- Concept checkpoint: forward propagation passes input through the network to produce predictions; a loss function measures the difference between predictions and target values.
- Next topic: implement Mean Squared Error (MSE) in pure Python. The loss function has been introduced conceptually but has **not** yet been implemented.
- No quiz score has been recorded for this session.

## Review queue

- Continue practising matrix addition and matrix multiplication in Lesson 1/02.
- Add or review beginner-friendly Python examples and tests for the matrix operations.
- Keep quiz scores and practical verification evidence separate; only record checks that were actually run.

## Phase 01 – Math Foundations

### Lesson 01: Linear Algebra Intuition — 17 November 2026

**Progress made today**
- Implemented vector normalization in Python and verified that `[3, 4]` becomes `[0.6, 0.8]`.
- Implemented the dot product using a loop and verified that `[3, 2] · [4, 5] = 22`.
- Implemented cosine similarity using the dot product and vector magnitudes.
- Learned that a zero dot product indicates perpendicular vectors, while cosine similarity measures the alignment of vector directions.
- Connected cosine similarity to AI embeddings and comparing numerical representations.

**Python concepts practised**
- Functions, parameters, return values, lists, loops, conditionals, and raising `ValueError`.
- Calling one function from another and testing implementations with sample inputs.

**Next topics**
- Matrix-vector multiplication.
- Neural network linear layer: `y = Wx + b`.

### Lesson 01: Linear Algebra Intuition — 18 November 2026

**What I learned today**
- Reviewed vector magnitude and normalization, including why a normalized vector has a magnitude of 1.
- Practised cosine similarity calculations and interpreted the key values: 1 for vectors pointing in the same direction, 0 for perpendicular vectors, and -1 for vectors pointing in opposite directions.
- Calculated a cosine similarity of 0 using the vectors `[3, 4]` and `[-4, 3]`.
- Learned matrix-vector multiplication using the matrix `[[2, 3], [4, 5]]` and input vectors such as `[2, 3]`, `[3, 2]`, and `[1, 1]`.
- Understood that each matrix row is multiplied by the same input vector, producing one output value per row.
- Learned that the output vector contains as many values as the matrix has rows.
- Started a Python implementation using nested loops, a running total, and a result list. The implementation still needs to be run and tested.

**Example**
```python
matrix = [
    [2, 3],
    [4, 5]
]

vector = [2, 3]

# Expected output: [13, 23]
```

**Python concepts practised**
- Importing functions from other modules.
- Using `if __name__ == "__main__":` to keep test code from running during imports.
- Working with nested lists, nested loops, indexes, and appending results to a list.

**Next steps**
- Run and verify the matrix-vector multiplication implementation.
- Add validation for incompatible matrix and vector dimensions.
- Connect matrix-vector multiplication to a neural network linear layer: `y = Wx + b`.


### Lesson 01: Linear Algebra Intuition — 19 November 2026

**What I learned and implemented today**
- Completed a Python implementation of matrix-vector multiplication using nested loops.
- Used a running total to multiply each matrix row by the corresponding input-vector values, then appended one result for each row.
- Confirmed that the matrix `[[2, 3], [4, 5]]` multiplied by `[2, 3]` produces `[13, 23]`.
- Learned that the number of matrix columns must match the number of input-vector values.
- Added dimension validation with `ValueError` when a row length does not match the vector length.
- Added empty-matrix validation with `if not matrix` and `ValueError`.
- Tested valid multiplication, incompatible dimensions, and an empty matrix. The valid case returned `[13, 23]`; the two invalid cases raised the expected errors.
- Reinforced the dimension rule: matrix columns determine the input-vector length, while matrix rows determine the output-vector length.

**Python concepts practised**
- Nested `for` loops, `range()`, list indexing, accumulating values with `+=`, and `list.append()`.
- Input validation using `if` and raising `ValueError`.
- Checking for an empty list with `if not matrix`.

**Next step**
- Connect matrix-vector multiplication to a neural network linear layer: `y = Wx + b`.


### Lesson 01: Linear Algebra Intuition — 20 November 2026

**What I learned and implemented today**
- Implemented the ReLU activation function: `relu(value)` returns the value when it is positive and returns zero when it is negative.
- Implemented `relu_vector(vector)` to apply ReLU to every value in a list.
- Connected the linear layer `y = Wx + b` to ReLU with `linear_layer_with_relu()`.
- Built `two_layer_network()`, passing the first layer's activated output into the second layer.
- Ran `two_layer_network.py` successfully and verified the output `[13, 4]`.
- Learned that this sequence of passing data through network layers is called **forward propagation**.
- Distinguished forward propagation from loss: forward propagation produces predictions, while a loss function measures prediction error against target values.
- Introduced Mean Squared Error (MSE), but have not implemented it yet.

**Next step**
- Implement a small pure Python MSE function and test it with simple prediction and target lists.
- Continue one concept and one small implementation at a time.
