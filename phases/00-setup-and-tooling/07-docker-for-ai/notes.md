# Docker for AI

**Author:** Andrew.Nd

## Summary

Docker allows developers to package applications and their dependencies
into containers. It helps maintain consistent development environments
and makes applications easier to deploy.

Docker Compose allows multiple containers to work together.

## Core Concepts

- **Docker Image:** A template used to create containers.
- **Docker Container:** A running instance of an image.
- **Dockerfile:** Instructions for building a Docker image.
- **Docker Volume:** Stores data persistently.
- **Docker Compose:** Manages multiple containers using a YAML file.
- **GPU Support:** Allows containers to access compatible host GPUs.

## Lesson Implementation

### Dockerfile

Created a Dockerfile containing Python, PyTorch, CUDA and AI libraries.

### Docker Compose

Created a configuration with three services:

1. ai-dev: Python AI development environment.
2. qdrant: Vector database for storing and searching embeddings.
3. api: Flask greeting and health endpoints.

### Exposed Ports

- 8888: Jupyter Notebook.
- 5000: Flask development API.
- 6333: Qdrant HTTP API.
- 6334: Qdrant gRPC API.

## Verification Status

Dockerfile and Docker Compose configuration files were created.

Container build and execution are pending workplace IT approval
for Docker permissions and installation of Docker Compose.

## Exercise preparation — 2026-11-05

- Added Flask and a small development API with `/` and `/health` routes.
- Added the API service to Compose alongside Jupyter and Qdrant.
- Parameterized the CUDA base with `CUDA_VARIANT` for the devel/runtime comparison.
- Added an optional GPU override; the default stack does not request a GPU.
- Added service/PyTorch checks and persistent marker checks for mounted storage.
- Added [a complete exercise runbook](README.md), including build commands,
  port mapping, persistence, image sizes, and cleanup.
- Python and YAML syntax checks passed. A real image build was attempted but
  failed on Docker daemon permissions. Compose remains unavailable.
- See [verification evidence](verification/environment-check.md). These are
  prepared exercise artifacts; runtime exercises and the quiz remain unfinished.

## Copied code and persistent storage

- `COPY` saves code in the image during building. Later host edits require a
  rebuild to update that copy.
- A bind mount makes a host file or folder available directly inside a container.
  Host code edits are visible there without rebuilding; the app may need a restart.
- Files saved through the `/models` and `/data` bind mounts remain in their host
  folders after container removal.
- Qdrant's `qdrant_data` is a named volume managed by Docker. A replacement
  container can attach the same volume and reuse its saved data.

## Service networking and ports

For a hypothetical mapping `127.0.0.1:9000:5000`:

| Caller | Flask address |
|---|---|
| Host browser | `http://localhost:9000` |
| `ai-dev` on the Compose network | `http://api:5000` |

The host port is the outside entrance; the container port is the internal door
where the application listens. Inside `ai-dev`, `localhost` refers to `ai-dev`
itself. Use `http://` for this Flask example: HTTPS requires TLS configuration.
The actual Compose file currently publishes host port 5000, not 9000.

## Compose lifecycle commands

```bash
docker compose up -d       # Start the stack in the background
docker compose ps          # Inspect service status
docker compose logs api    # Inspect Flask output and errors
docker compose logs -f api # Follow new Flask log messages
docker compose down        # Remove containers/network; retain named volumes
```

Adding `-v` to `down` removes named volumes declared by this project and anonymous
volumes attached to its containers. External volumes and bind-mounted host
folders are not removed. For this stack, `down -v` deletes Qdrant's saved volume.
These commands were discussed; successful execution is still pending.
