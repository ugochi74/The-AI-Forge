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

Created a configuration with two services:

1. ai-dev: Python AI development environment.
2. qdrant: Vector database for storing and searching embeddings.

### Exposed Ports

- 8888: Jupyter Notebook.
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
