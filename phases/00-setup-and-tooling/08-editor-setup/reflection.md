# Editor Setup — Session Reflection

Status: Complete; quiz passed **3/3**.

## What I learned

Quotation marks make `"42"` a string. Type hints describe expected types,
while a formatter cleans code layout. Black needed a working interpreter
before format-on-save could run.

## What needs more practice

Notebook kernel selection was the main troubleshooting point. Future remote
connection practice needs an available remote host.

## Prediction questions and answers

**Question: How can `greet(42)` pass text instead of a number?**

**Answer:** Use quotation marks: `greet("42")`. The learner answered correctly.

## Practical results

Confirmed Python tool installations through the learner's CLI output.
Black initially waited for environment discovery; configured it to use
`python3` and its bundled formatter. After reloading VS Code and saving, the
learner confirmed that the spacing became clean. Format-on-save passed;
Pylance diagnostics and hover signatures also passed by learner confirmation;
VS Code also ran the demo using `/bin/python3` and printed `Hello, Andrew`.
Notebook execution also passed: after selecting the project `.venv` kernel,
`sum([2, 4, 6])` returned `12`. Initially, selecting system Python caused an
`ipykernel` error. Kernel selection determines which environment runs the cells.
The quiz is now passed, 3/3. Remote connection was not run because no remote
host was identified.

## Remote development

Verified GitLens and Remote SSH installation through CLI output and confirmed
the OpenSSH client version. Learned that Remote SSH edits files and runs
commands on another computer. No remote host has been identified, so no SSH
connection was attempted. This is separate from installing the SSH tools.

## Final result

Passed all three post-lesson questions (D, D, D): Remote SSH enables remote
editing; output scrolling contains long notebook logs; basic type checking
flags incompatible argument types. Lesson complete.
