# Lesson 07: Docker for AI

Implementation and exercises for the upstream [Docker for AI lesson](https://aiengineeringfromscratch.com/lesson?path=00-setup-and-tooling/07-docker-for-ai).
**Status: complete. Quiz: 3/3. Local checks passed.**
Runtime exercises were not run because Docker daemon access is denied and
Docker Compose is missing; GPU execution was not run on the CPU-only host.

## Prerequisites

Run on a machine where Docker Engine is running and your account is authorized
to use it. Install the Docker Compose plugin through your approved installation
process. Check these before downloading the multi-gigabyte CUDA/PyTorch images:

```bash
docker version
docker compose version
docker run --rm hello-world
```

The default stack runs without GPU access, matching this learner's CPU-only
setup. GPU use additionally needs NVIDIA hardware, a compatible host driver,
and NVIDIA Container Toolkit. A CUDA image does not supply hardware or a host
driver. Installation guidance: [Docker Engine](https://docs.docker.com/engine/install/),
[Compose plugin](https://docs.docker.com/compose/install/linux/), and
[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

## 1. Build and verify PyTorch

From the repository root:

```bash
cd phases/00-setup-and-tooling/07-docker-for-ai/code
mkdir -p ../outputs/models ../outputs/datasets
docker compose config --quiet
docker compose build ai-dev
docker run --rm ai-forge-lesson07:devel python -c 'import torch; print(torch.__version__); print("CUDA available:", torch.cuda.is_available())'
```

Check that PyTorch starts with `2.6.0`. CUDA availability should be false on a
CPU-only host; this is not a failed CPU exercise. `RUN` installs packages during
the image build; `CMD` supplies the default startup command. Compose overrides
the image's `CMD` to launch Jupyter or the Flask API.

## 2. Start Jupyter, Qdrant, and Flask

Continue in `code/`:

```bash
docker compose up -d
docker compose ps
docker compose logs ai-dev
docker compose exec -T ai-dev curl --fail --retry 20 --retry-connrefused --retry-delay 2 http://qdrant:6333/collections
docker compose exec -T ai-dev curl --fail --retry 20 --retry-connrefused --retry-delay 2 http://api:5000/health
docker compose exec -T ai-dev python /workspace/phases/00-setup-and-tooling/07-docker-for-ai/code/verify_stack.py
```

The retries allow the services time to start. Verify JSON replies with status
`ok`. The Python check also verifies PyTorch and creates tiny persistence markers.
Qdrant and the API are reached by Compose service names inside the network.
Use the Jupyter token URL from the logs at `http://localhost:8888`.

## 3. Flask exercise and port mapping

Flask is added to the Dockerfile; `app.py` is the exercise server. The `api`
service maps host port 5000 to container port 5000. Check from the host:

```bash
curl --fail http://localhost:5000/
curl --fail http://localhost:5000/health
```

The health route should return `{"status":"ok"}`. This is a development API,
not a chatbot or production server. Binding Flask to `0.0.0.0` inside the
container lets Docker forward requests to it. Published host ports are bound
to loopback. To run the same exercise with the lesson's explicit `-p` syntax,
first stop the Compose API to free port 5000:

```bash
docker compose stop api
docker run --rm -p 127.0.0.1:5000:5000 --mount "type=bind,src=$(pwd)/app.py,dst=/app/app.py,readonly" ai-forge-lesson07:devel python /app/app.py
```

Check the URL in another terminal, then press Ctrl-C to stop that container.

## 4. Verify persistent storage

The repository is mounted at `/workspace`. Lesson-local model and dataset
directories are mounted at `/models` and `/data`; generated contents are ignored
by Git. Qdrant uses a named volume. Check persistence across removal/recreation:

```bash
docker compose down
docker compose up -d
docker compose exec -T ai-dev curl --fail --retry 20 --retry-connrefused --retry-delay 2 http://qdrant:6333/collections
docker compose exec -T ai-dev curl --fail --retry 20 --retry-connrefused --retry-delay 2 http://api:5000/health
docker compose exec -T ai-dev python /workspace/phases/00-setup-and-tooling/07-docker-for-ai/code/verify_stack.py
cat ../outputs/models/lesson07-persistence.txt ../outputs/datasets/lesson07-persistence.txt
```

The check should report existing markers survived. Stopping a container alone
does not erase its writable layer; removing it does. Bind-mounted files and named
volumes survive container removal. `docker compose down` preserves named volumes.

## 5. Compare development and runtime images

The `CUDA_VARIANT` build argument switches the same Dockerfile between the
lesson's CUDA development and runtime bases:

```bash
docker build --build-arg CUDA_VARIANT=runtime -t ai-forge-lesson07:runtime .
docker run --rm ai-forge-lesson07:runtime python -c 'import torch; print(torch.__version__)'
docker image ls ai-forge-lesson07
docker image inspect ai-forge-lesson07:devel ai-forge-lesson07:runtime --format '{{.RepoTags}} {{.Size}} bytes' > ../outputs/image-sizes.txt
```

Record both measured sizes and their difference. The runtime base omits CUDA
development tools such as `nvcc`; this Dockerfile still installs general build
tools. Do not claim a measured size reduction before running both builds.

## Optional GPU verification

On an authorized NVIDIA host with the toolkit configured:

```bash
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
docker compose -f docker-compose.yml -f compose.gpu.yml up -d
docker compose exec -T ai-dev python -c 'import torch; print(torch.cuda.is_available()); assert torch.cuda.is_available()'
```

## Finish and record evidence

To save command results automatically in timestamped output folders, run from
the repository root:

```bash
bash phases/00-setup-and-tooling/07-docker-for-ai/code/capture_outputs.sh --check
# Once Docker access and Compose are available, run all practical CPU checks:
bash phases/00-setup-and-tooling/07-docker-for-ai/code/capture_outputs.sh
```

See [outputs/README.md](outputs/README.md) for captured files and failure handling.

```bash
docker compose logs --no-color > ../outputs/compose.log
docker compose down
```

Review logs for Jupyter tokens before committing them. Record actual results in
`verification/environment-check.md` and update the reflection with runtime
results if you revisit the practical exercises. The theory quiz is passed
(3/3), and the lesson is complete. Record any future runtime results separately
from exercises not run due to Docker daemon access and missing Compose in
`LEARNING.md` and the root README. No image builds, runtime results, or quiz scores are inferred from
the existence of these files.
