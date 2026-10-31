# Git & Collaboration

Course lesson: [Git & Collaboration](https://aiengineeringfromscratch.com/lesson?path=phases/00-setup-and-tooling/02-git-and-collaboration)

## Goal

Use Git to track changes, save project snapshots, work safely on branches, and
back up work to a remote repository you own.

## Core workflow

```text
working directory --git add--> staging area --git commit--> local repository
local repository --git push--> remote repository
```

## Commands to practice

```bash
git status
git add <file>
git commit -m "Describe the change"
git push -u origin my-progress
git checkout -b experiment/example
git log --oneline
```

Fork the course repository before pushing. In this workspace, `course-repo/`
currently has the course maintainers' repository as `origin`; do not push to
that remote. Use your own fork as the push destination.

## Lesson exercises

1. Fork the course repository, make a `my-progress` branch, add a practice
   file, commit it, and push the branch to your fork.
2. Add model checkpoint patterns to `.gitignore` and confirm Git ignores them.
3. Inspect recent history with `git log --oneline` and `git show --stat`.

Record command results in `outputs/environment-check.txt` and progress in
`verification/environment-check.md`.
