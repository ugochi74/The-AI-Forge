# GPU Setup & Cloud

Course lesson: [GPU Setup & Cloud](https://aiengineeringfromscratch.com/lesson?path=phases/00-setup-and-tooling/03-gpu-setup-and-cloud)

## Goal

Check whether PyTorch can use a local accelerator, compare CPU and GPU matrix
multiplication, and estimate a model's rough fp16 weight size from VRAM.

## My setup

- The local environment has CPU-only PyTorch and no detected NVIDIA GPU.
- Google Colab provided a Tesla T4; PyTorch reported CUDA available.
- On the second benchmark run, CPU took 2.797 s and GPU took 0.088 s, about
  32x faster for this matrix multiplication.
- The T4 reports 15,360 MiB. The fp16 weight-only estimate is about 8 billion
  parameters; practical capacity is lower because other training data uses VRAM.

## Run the local check

From the root of `The-AI-Forge`, activate the course virtual environment and
run the checker:

```bash
source course-repo/.venv/bin/activate
python3 phases/00-setup-and-tooling/03-gpu-setup-and-cloud/code/gpu_check.py
```

No local GPU is required for the early course lessons. When a lesson needs a
GPU, use a Colab GPU runtime or another GPU machine. Colab's free GPU access
may not always be available.

## Key ideas

- GPUs have many cores suited to parallel matrix operations.
- `torch.cuda.synchronize()` waits for asynchronous GPU work to finish, making
  timings meaningful.
- An fp16 parameter uses about two bytes, so `VRAM bytes / 2` is a rough
  weights-only parameter limit, not a practical training guarantee.
