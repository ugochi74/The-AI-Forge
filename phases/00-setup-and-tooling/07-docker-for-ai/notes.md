# Docker for AI

**Author:** Andrew.Nd

## Summary

Docker allows developers to package applications and their dependencies
into containers. It helps maintain consistent development environments
and makes applications easier to deploy.

Docker Compose allows multiple containers to work together.

An image is the saved template used to create containers. Stopping a container leaves that image available.

The host port is the outside entrance, and the container port is the internal door where Flask listens.

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


## Final lesson status

Complete. Theory quiz: **3/3**.
Local Python/YAML/shell syntax and bind-source path checks passed. Docker
runtime exercises were not run because daemon access is denied and Compose
is missing. Host Flask execution was not run because Flask is not installed.
GPU execution was not run because this host is CPU-only. See
[verification results](verification/environment-check.md) and
[local check output](outputs/local-checks.txt). Earlier pending items are
retained as optional future practice.
