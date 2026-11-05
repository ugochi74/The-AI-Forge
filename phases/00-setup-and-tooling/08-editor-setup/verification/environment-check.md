# Editor Setup Verification

| Check | Status |
|---|---|
| VS Code version | Learner reported 1.100.2, x64; see tool-versions.txt |
| Installed extensions | All eight lesson extensions listed in learner CLI output; see ../outputs/installed-extensions.txt and ../outputs/remote-git-extensions.txt |
| Python interpreter selection | Demo ran with /bin/python3; subsequently created .venv, verified ipykernel import, and learner ran notebook with .venv kernel |
| Pylance diagnostics and type hints | Passed: learner saw the integer/string warning and greet(name: str) -> str on hover |
| Formatting on save | Passed: learner confirmed clean spacing after reload and save with Black using python3 |
| Notebook support | Passed: learner selected project .venv kernel and sum([2, 4, 6]) returned 12 |
| Integrated terminal | Passed: Python: Run Python File in Terminal printed Hello, Andrew |
| Remote SSH | Extension and OpenSSH client confirmed. Connection not run: no remote host identified or saved SSH config |
| Lesson quiz | Passed 3/3: D, D, D |

Record actual observations and link output files as checks are performed.
