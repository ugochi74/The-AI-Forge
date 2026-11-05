# Lesson 7 outputs

Each `run-<UTC timestamp>-<unique suffix>/` directory contains real command
output and a `summary.md` with exit codes. Failed checks are retained as
evidence; they do not indicate lesson completion. No successful Docker output
is fabricated when the daemon cannot be reached.

From the repository root, capture current prerequisites:

```bash
bash phases/00-setup-and-tooling/07-docker-for-ai/code/capture_outputs.sh --check
```

On a Docker-enabled host with Compose, capture the practical CPU exercises:

```bash
bash phases/00-setup-and-tooling/07-docker-for-ai/code/capture_outputs.sh
```

The full run downloads/builds large CUDA/PyTorch images. It captures build logs,
PyTorch versions, Qdrant/API responses, persistence checks, and image sizes.
It stops on failure and preserves earlier results. Successful runs stop the
lesson stack; if a run fails after starting services, stop them from `code/`
with `docker compose down`. Volumes and downloaded images are retained.

`models/` and `datasets/` hold bind-mounted data and are ignored by Git. Their
persistence markers are created only when the container check actually runs.
Jupyter logs are not collected automatically because they can contain access
tokens. Review all output before committing it.
