# Git & Collaboration Verification

Complete this checklist as you work through the lesson.

## Git setup

- [x] Git is installed: version 2.43.0.
- [x] Git author name and email are configured.
- [x] Fork the course repository to your GitHub account before pushing.

## Exercises

- [x] Create a local `my-progress` branch in `The-AI-Forge`.
- [x] Add and commit a practice file locally (`f609fcf`).
- [x] Create `my-progress` in the course fork, commit a practice file, and push the branch.
- [x] Add `.pt`, `.pth`, and `.safetensors` patterns to the repository-root `.gitignore` and verify them with `git check-ignore -v`.
- [x] Inspect recent commits with `git log --oneline`.
- [x] Inspect a commit with `git show --stat`.

## Results

- Course repository path: `course-repo/` inside this workspace.
- Fork URL: `https://github.com/ugochi74/ai-engineering-from-scratch`
- Branch pushed: `my-progress`; it tracks `origin/my-progress`.
- Practice file commit: `da22ef4` (`Add Git collaboration practice file`).
- `.gitignore` check: `git check-ignore -v` matched `*.pt`, `*.pth`, and `*.safetensors`.
- History command: `git log --oneline` and `git show --stat f609fcf`.
- Error and fix: the initial clone used the maintainers' repository as `origin`. Renamed that remote to `upstream` and set the personal fork as `origin` before pushing.

## Local practice completed

- Personal repository branch: `my-progress`.
- Local commits: `f609fcf` (practice file) and `cdbf198` (checkpoint `.gitignore`).
- Course fork branch: pushed successfully; `my-progress` tracks `origin/my-progress`.
