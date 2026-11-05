# GPU and Compose execution attempt

| Check | Exit code |
|---|---|
| [host-gpu.txt](host-gpu.txt) | 127 |
| [compose-start.txt](compose-start.txt) | 125 |
| [gpu-container.txt](gpu-container.txt) | 126 |

No GPU or Compose runtime verification succeeded. Host nvidia-smi is unavailable; Docker Compose is missing; the GPU container cannot access the Docker daemon.
