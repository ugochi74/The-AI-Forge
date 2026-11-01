# Reflection

## What makes a GPU useful for neural-network workloads?

A GPU has many smaller cores that can perform similar calculations in
parallel, which suits the matrix operations used by neural networks.

## Why synchronize during a GPU benchmark?

GPU work is asynchronous. Synchronizing waits for the queued calculation to
finish before the timer stops, so the measured time is meaningful.

## What does VRAM limit?

VRAM limits how much model data and training state can fit on the GPU. At
roughly two bytes per fp16 parameter, the T4's 15,360 MiB gives about an
8-billion-parameter weights-only estimate. Real training needs additional
memory for activations and other state.

## What did the benchmark show?

On the second run, the Colab T4 completed the matrix multiplication in 0.088 s
versus 2.797 s on the CPU, about 32x faster in this run.
