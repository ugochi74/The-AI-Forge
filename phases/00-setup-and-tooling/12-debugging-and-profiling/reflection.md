# Reflection

## Learner response

> I will use tools like tracemalloc and cProfile to catch memory leaks in long chat sessions and pinpoint slow bottlenecks in my retrieval

## Observed understanding

Distinguished profiling from debugging; recognized a matching (12, 8) input, the overfitting pattern, and tracemalloc as a Python allocation tool. NaN detection initially needed guided examples. Correctly predicted the conditional breakpoint pause.

Quiz: **3/3**, completed 2026-11-11.

## Practical evidence

The agent ran the lesson exercises and saved reports in outputs/. The learner answered conceptual checkpoints and the quiz. The saved pdb session used scripted agent input; independent learner debugger practice is available in the runbook. No hands-on learner execution or GPU execution is inferred from agent runs.

## Application notes

tracemalloc tracks Python allocations, not all native tensor or GPU memory. cProfile measures function time. Streaming records and processing batches can reduce retained Python data during ingestion; use profiling to verify the effect on a real chatbot.
