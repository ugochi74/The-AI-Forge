# Runbook

Run setup commands from the repository root. Python 3.12 was used for the saved reports.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install torch==2.15.0+cpu --index-url https://download.pytorch.org/whl/cpu
.venv/bin/python -m pip install -r phases/00-setup-and-tooling/13-python-for-ai-engineering/verification/requirements.txt
.venv/bin/python -m pip check
npm ci --prefix phases/00-setup-and-tooling/13-python-for-ai-engineering
.venv/bin/python phases/00-setup-and-tooling/12-debugging-and-profiling/verification/run_checks.py
.venv/bin/python phases/00-setup-and-tooling/12-debugging-and-profiling/verification/check_tensorboard.py
```

The runner checks both lessons and saves commands, output and exit codes. The TypeScript runner and TensorBoard need local sockets; restricted hosts may need execution permission. Inspect each output report for actual results. GPU checks are skipped on CPU-only hardware.

## Interactive debugger practice

```sh
.venv/bin/python phases/00-setup-and-tooling/12-debugging-and-profiling/code/training_practice.py --debug
```

At `(Pdb)`, try `p x.shape`, `p x.device`, `p model[0].weight.grad.shape`, and `c`. Saved debugger verification used scripted agent input; repeat this command for personal practice.

## TensorBoard

```sh
.venv/bin/python -m tensorboard.main --logdir phases/00-setup-and-tooling/12-debugging-and-profiling/runs --host 127.0.0.1 --port 6006
```

Open http://127.0.0.1:6006 on the host running the server. Event files are ignored in Git; the training script regenerates them. JSON loss history and verification reports are committed artifacts only when you commit them. No GPU execution is claimed.
