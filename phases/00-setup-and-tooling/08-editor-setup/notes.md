# Editor Setup

**Author:** Andrew.Nd

## Status

Complete. Python settings have been merged into the active `.vscode/settings.json`.
Type checking, format-on-save, script execution, and notebook execution passed
by learner confirmation.

## Concepts

Type hints describe expected types. `greet(42)` passes an integer;
`greet("42")` passes a string. Pylance can flag the mismatch before execution.

## Prediction questions and answers

**Question: How can `greet(42)` be changed to pass text?**

**Answer:** Wrap the value in quotation marks: `greet("42")`.

The learner correctly explained that quotation marks make the value a string.

## Commands and observations

Learner ran `code --version` and `code --list-extensions`. VS Code reported
1.100.2 (x64); the extension list contained only `golang.go`. Raw output is
saved in `outputs/editor-check.txt`. A later CLI check confirmed Python, Pylance, Debugpy, Jupyter, Black, and Ruff
are installed; see `outputs/installed-extensions.txt`. The learner also reports
selecting the project interpreter.

## Workspace settings

Basic Pylance checking is enabled. Black is selected as the Python formatter
with formatting on save. Python rulers are set at 88 and 120 characters,
notebook output scrolling is enabled, and terminal scrollback is 10,000 lines.
Existing interpreter settings were preserved. UI verification is still pending.

## Formatting diagnosis

The demo was saved at `code/vscode/editor_demo.py`. Black logs reported that
it was waiting for Python Environments and formatting was requested before
its server started. The configured `.venv/bin/python` is missing. Black now
uses `python3` explicitly with its bundled formatter; editor verification is
still pending. This does not recreate or repair the project virtual environment.

## Formatting checkpoint

After reloading VS Code, the learner confirmed that saving the demo cleaned
its spacing. Format-on-save is verified by the learner. Type diagnostics
and hover information still need checking.

## Type-checking checkpoint

The learner confirmed a Pylance warning for `greet(42)` and signature information
when hovering over `greet`. Formatting changes layout; type checking detects
incompatible argument types. Restore `greet("Andrew")` before running the demo.

## lesson
Formatting cleans the code’s layout; type checking flags incompatible values.

## Demo execution

VS Code ran the corrected demo with `/bin/python3` and printed `Hello, Andrew`.
This verifies integrated Python execution with system Python; it does not
verify a project virtual environment. See `outputs/demo-run.txt`.

## Notebook kernel setup

The system Python kernel could not run notebook cells because `ipykernel` was
missing. Created `.venv` with `python3 -m venv .venv` and installed `ipykernel`
there, without sudo or system Python changes. Select `.venv/bin/python` as
the notebook kernel and rerun the cell. Editor execution is not yet verified.
The earlier missing-venv diagnosis describes the state before this repair.

## Notebook execution checkpoint

VS Code initially kept selecting `/bin/python3`. After switching the notebook
to the project `.venv`, the learner confirmed `sum([2, 4, 6])` returned `12`.
Notebook execution is verified by learner confirmation. Selecting a notebook
kernel is separate from selecting an interpreter for ordinary Python files.

## GitLens and Remote SSH

Learner CLI output confirms `eamodio.gitlens` and
`ms-vscode-remote.remote-ssh` are installed, along with Remote SSH Edit.
GitLens helps inspect repository history; Remote SSH supports working on
a remote host. Extension installation does not verify an SSH connection.
Remote host availability has not yet been confirmed.

## SSH client check

`ssh -V` confirms OpenSSH 9.6p1 is installed. No `~/.ssh/config` exists.
No remote host has been identified, so the optional connection exercise was
not run. A client and extension do not create or provision a remote server.

## Lesson result

Quiz passed **3/3** (D, D, D): Remote SSH, notebook output scrolling, and
basic type checking. Remote connection not run because no remote host was
identified. Lesson complete; next is Lesson 09: Data Management. Earlier
pending-check descriptions document the troubleshooting sequence.
