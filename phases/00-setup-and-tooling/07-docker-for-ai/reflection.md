# Docker for AI — Session Reflection

Date: 2026-11-05

Status: In progress; practical execution and lesson quiz pending.

This reflection summarizes the learning discussion and verified work so far.

## What became clearer

- A Python package list alone does not capture the full runtime environment.
- An image is a reusable template; stopping a container does not require
  rebuilding the image before creating another container.
- `RUN` executes during image building. Packages installed there are already
  available when containers start.
- A container uses its own installed Python. Host Python 3.11 and container
  Python 3.12 do not conflict merely because their versions differ.
- `WORKDIR` sets the working directory, `COPY` adds files to the image, and
  `CMD` specifies the default startup command, such as starting a chatbot.
- CUDA software cannot create GPU hardware; GPU acceleration needs a compatible
  NVIDIA GPU, driver, and container access.

## What needed more explanation

Initially, it was unclear whether containers reinstall packages at startup and
whether different host/container Python versions cause a conflict. Small
examples using `python --version` helped separate building from running.

Copied files versus bind-mounted files, persistence, and Compose still need
hands-on practice before claiming confidence with them.

## Practical work and limits

With agent assistance, prepared a Dockerfile, Jupyter/Qdrant/Flask Compose stack,
optional GPU settings, service and storage checks, and an output-capture script.
Python, YAML, and shell syntax checks passed.

The image build could not reach the Docker daemon, and Docker Compose is not
installed in this session. Captured output records these failures. No successful
container run, API response, persistence result, or image-size comparison has
been verified yet.

## Next steps

Run the exercise guide on an approved Docker-enabled host, inspect actual
outputs, practise changing code through a bind mount, and take the lesson quiz.
For the personal chatbot, the goal is to package its software environment and
keep model/data files available across container replacement.
