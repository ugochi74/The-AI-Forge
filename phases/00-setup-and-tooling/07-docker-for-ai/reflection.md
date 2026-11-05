# Docker for AI — Session Reflection

Date: 2026-11-05

Status: Complete; theory quiz passed 3/3.

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




### Check: what would adding -v do to that saved volume? docker compose down -v


Named volumes declared by that Compose project and anonymous volumes attached to its containers. It doesn’t remove every volume on the machine, external volumes, or bind-mounted host folders.

For our stack, it would delete qdrant_data, including Qdrant’s saved data. Your host models/ and datasets/ folders would remain.

## Prediction questions and answers

Discussion checkpoints with corrected answers; these are not additional scored quiz questions or verified Docker runs.

**Question 1: Why might copying only a Python package list be insufficient?**

**Answer:** It does not capture the Python interpreter and system libraries needed by the application.

**Question 2: Does a CUDA image give a CPU-only laptop GPU acceleration?**

**Answer:** No. GPU acceleration requires physical compatible NVIDIA hardware, its host driver, and container access.

**Question 3: Must an image be rebuilt after stopping a container before starting another?**

**Answer:** No. Another container can reuse the existing image.

**Question 4: Must each container download NumPy if it was installed in the image?**

**Answer:** No. The installed package is already available in the image.

**Question 5: When does RUN python -m pip install numpy execute?**

**Answer:** During image building, not each time a container starts.

**Question 6: What does CMD ["python", "--version"] do?**

**Answer:** At startup, it prints the container's Python version and exits.

**Question 7: The host has Python 3.11 and the container has Python 3.12. Which runs inside the container?**

**Answer:** Python 3.12. The different installed versions do not inherently conflict.

**Question 8: Does CMD ["python", "chatbot.py"] install Python or start the chatbot?**

**Answer:** It starts the chatbot with the Python already installed in the image.

**Question 9: Which instruction adds chatbot.py to the image: WORKDIR, COPY, or CMD?**

**Answer:** COPY adds the file; WORKDIR sets the working directory and CMD defines the default startup command.

**Question 10: After changing a host file previously copied into the image, is restarting enough?**

**Answer:** No. Rebuild the image to update that copied file.

**Question 11: An image contains a script printing Hello, but the host script now prints Welcome. What does the unchanged image run?**

**Answer:** The earlier script, which prints Hello.

**Question 12: What does the edited script print when the host file is bind-mounted and run again?**

**Answer:** Welcome, because the mount exposes the current host file.

**Question 13: Does a file saved through the /models bind mount disappear when the container is removed?**

**Answer:** No. The saved file remains in its host folder.

**Question 14: Can a replacement Qdrant container reuse data from the same named volume?**

**Answer:** Yes, if that volume and its contents have been retained.

**Question 15: From ai-dev, which address reaches the Flask service?**

**Answer:** http://api:5000. Use the service name and its container port.

**Question 16: With 127.0.0.1:8000:5000, which URL does the laptop use?**

**Answer:** http://localhost:8000. The host port is 8000 and the container port is 5000.

**Question 17: With 127.0.0.1:9000:5000, which URL does the laptop use?**

**Answer:** http://localhost:9000.

**Question 18: After publishing host port 9000, does ai-dev connect to api:9000 or api:5000?**

**Answer:** api:5000. Publishing a different host port does not change Flask's internal listening port.

**Question 19: Does this Flask example use HTTP or HTTPS?**

**Answer:** HTTP: http://api:5000. HTTPS needs TLS configuration, which this example does not have.

**Question 20: How do host and container ports differ?**

**Answer:** The host port is the outside entrance; the container port is the internal door where the application listens.

**Question 21: Which command displays Flask service errors?**

**Answer:** docker compose logs api. Add -f to follow new log messages.

**Question 22: Which command removes the stack containers while retaining Qdrant data?**

**Answer:** docker compose down, without -v.

**Question 23: What does docker compose down -v remove?**

**Answer:** Named volumes declared by this project and anonymous volumes attached to its containers. External volumes and bind-mounted host folders are not removed.

**Question 24: Which CUDA base would you try for prebuilt packages without compiling CUDA code?**

**Answer:** runtime. The devel variant additionally provides CUDA development tools such as the compiler.

**Question 25: Does the :runtime tag select the base, or does --build-arg CUDA_VARIANT=runtime?**

**Answer:** The build argument selects the base in this Dockerfile. The tag only labels the resulting image; a runtime-based image could be tagged experiment.

**Question 26: If only app.py changes after an earlier Flask installation step, must Flask normally be reinstalled?**

**Answer:** No. Docker can reuse the earlier installation step from cache when its inputs are unchanged.

**Question 27: What does Compose manage compared with manually starting each container?**

**Answer:** It coordinates service commands, startup, networking, ports, and storage from a YAML file—like a conductor.


## Completion record and system limitations

Lesson 7 is complete. Python, YAML, and shell syntax and bind-source path
checks passed; see [local-checks.txt](outputs/local-checks.txt). Docker daemon
access is denied, Docker Compose is missing, and host Flask is not installed.
Container builds, service/HTTP checks, persistence, and image-size comparisons
were not run because Docker daemon access is denied and Compose is missing.
GPU execution was not run because this host is CPU-only. The theory quiz is passed, **3/3**. Earlier pending-work descriptions
remain as suggestions for future practice, not requirements blocking progression.
