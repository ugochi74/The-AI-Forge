# Reflection

## Learner response

> I will use tools like tracemalloc and cProfile to catch memory leaks in long chat sessions and pinpoint slow bottlenecks in my retrieval

## Observed understanding

Correctly predicted reproducible seeded splits, batch sizes 4/4/2, standardized value 2, and generator memory savings. Quiz correctly covered mutable defaults and training-only preprocessing statistics.

Quiz: **2/2**, completed 2026-11-11.

## Practical evidence

The agent ran the lesson exercises and saved reports in outputs/. The learner answered conceptual checkpoints and the quiz. The saved pdb session used scripted agent input; independent learner debugger practice is available in the runbook. No hands-on learner execution or GPU execution is inferred from agent runs.

## Application notes

tracemalloc tracks Python allocations, not all native tensor or GPU memory. cProfile measures function time. Streaming records and processing batches can reduce retained Python data during ingestion; use profiling to verify the effect on a real chatbot.
