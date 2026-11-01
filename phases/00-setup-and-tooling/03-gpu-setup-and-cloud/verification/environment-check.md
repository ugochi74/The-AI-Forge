# GPU Setup & Cloud Verification

## Local machine

- [x] Check local NVIDIA access: `nvidia-smi` is not available in this environment.
- [x] Run `gpu_check.py`: local PyTorch is 2.15.0+cpu; CUDA and MPS are unavailable to it.
- [x] Confirm CPU-only local setup is usable for early lessons.

## Google Colab

- [x] Select a GPU runtime and confirm `nvidia-smi` reports a Tesla T4.
- [x] Confirm `torch.cuda.is_available()` is `True` in Colab.
- [x] Run the CPU and GPU matrix benchmark twice.
- [x] Estimate the T4's fp16 weights-only capacity from its VRAM.

## Results

- Colab GPU: Tesla T4, 15,360 MiB.
- PyTorch: 2.11.0+cu130; CUDA available: True.
- Second benchmark: CPU 2.797 s; GPU 0.088 s; about 32x speedup.
- fp16 estimate: approximately 8.05 billion parameters for weights alone;
  actual training capacity is lower.
