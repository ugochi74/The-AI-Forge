# Terminal and Shell

## Overview

This lesson introduced practical terminal and shell commands for managing files, processing command output, monitoring system resources, and automating repeated tasks.

## Key Concepts

### 1. Command Pipelines

Pipes (`|`) pass the output of one command into another command.

Examples:
- `cat fake_train.log | grep "ERROR"` finds error messages.
- `grep "loss:" fake_train.log | wc -l` counts training-loss entries.
- `grep "loss:" fake_train.log | awk '{print $NF}'` extracts loss values.

### 2. Output Redirection

Redirection saves command output and error messages to files.

- `>` writes output and replaces existing content.
- `>>` appends output to a file.
- `2>` redirects error messages.
- `2>&1` combines standard output and error output.

### 3. System Resource Monitoring

| Command | Purpose |
|---|---|
| `free -h` | Displays memory and swap usage. |
| `nproc` | Displays the number of available processing units. |
| `top` | Shows running processes and system activity. |
| `df -h` | Displays disk space usage. |

### 4. File Synchronization with rsync

The `rsync` command synchronizes files and directories.

- `rsync -av --dry-run source/ backup/` previews changes without copying files.
- `rsync -av source/ backup/` performs the synchronization.

The practice confirmed that updated files are copied and unchanged files do not need to be transferred again.

### 5. Shell Aliases

An alias provides a shorter name for a frequently used command.

The alias `ll='ls -lah'` was added to `~/.zshrc` and loaded using `source ~/.zshrc`.

## Remote Access and Terminal Tools

SSH, SCP, and rsync command-line clients are available. Remote authentication was not configured because workplace policy does not permit personal SSH key generation.

The `tmux` and `screen` commands were unavailable and require workplace IT support for installation.

## Practical Outputs

The lesson produced command logs, extracted training-loss values, captured errors, run-history records, and local rsync source and backup files in the `outputs/` directory.

## Summary

This lesson developed practical shell skills for filtering command output, redirecting results, monitoring system resources, synchronizing files, and creating command shortcuts. These skills are useful for managing development environments and working with AI engineering projects from the terminal.
