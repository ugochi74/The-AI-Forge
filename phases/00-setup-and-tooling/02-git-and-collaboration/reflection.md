# Reflection

## What is the difference between the working directory, staging area, and local repository?

The working directory holds my current edits. `git add` selects changes for
the staging area. `git commit` saves the staged changes as a snapshot in the
local repository.

## Why should you create a branch before experimenting?

A branch keeps experimental commits separate from `main`. Commits move the
branch I am working on while `main` stays where it was.

## Why must you fork the course repository before pushing your work?

The course maintainers own the original repository and learners do not have
permission to push to it. A personal fork gives me a remote where I can push
my branch.

## Which file patterns should keep model checkpoints out of Git?

`*.pt`, `*.pth`, and `*.safetensors`, because model checkpoint files can be
very large.

## Which Git command helped you understand the project history?

`git log --oneline` shows a compact commit list. `git show --stat <commit>`
shows which files a specific commit changed.
