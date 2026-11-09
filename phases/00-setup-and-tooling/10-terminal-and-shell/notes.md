# Terminal and Shell — Practical Notes

**Author:** Andrew.Nd

## 1. Working with Command Output

- `cat filename` — displays file contents.
- `grep "text" filename` — searches for matching text.
- `wc -l` — counts lines.
- `awk '{print $NF}'` — prints the last field on each line.
- `|` — sends one command's output to another command.

Example: `grep "loss:" fake_train.log | awk '{print $NF}'`

## 2. Redirecting Output

| Operator | Use |
|---|---|
| `>` | Write output and replace existing content. |
| `>>` | Append output to a file. |
| `2>` | Save error output. |
| `2>&1` | Redirect error output to the same destination as standard output. |

**Important:** Use `>` carefully because it can overwrite existing file contents.

## 3. Monitoring System Resources

- `free -h` — check memory and swap usage.
- `nproc` — check available processing units.
- `top` — monitor running processes and resource usage.
- `df -h` — check disk space.

Press `q` to exit `top`.

## 4. Synchronizing Files

- `rsync -av --dry-run source/ backup/` — preview synchronization.
- `rsync -av source/ backup/` — perform synchronization.

The trailing slash in `source/` means to synchronize the contents of the source directory.

## 5. Shell Aliases

An alias creates a shortcut for a command.

Example: `alias ll='ls -lah'`

To make an alias persistent in Zsh, add it to `~/.zshrc` and reload the configuration using `source ~/.zshrc`.

## 6. Remote Access Tools

- SSH — connects to remote systems.
- SCP — copies files between systems.
- rsync — synchronizes files and directories.

Remote SSH authentication was not configured because of workplace restrictions on personal SSH key generation.

## 7. Environment Limitations

- `tmux` was not installed.
- `screen` was not installed.
- Docker access requires workplace IT support.

## Key Lessons

1. Pipes make it possible to combine simple commands into useful workflows.
2. Redirection helps save command results and error messages.
3. Resource-monitoring commands help inspect system performance.
4. rsync supports efficient file synchronization.
5. Shell aliases reduce repetitive typing.
6. Workplace security policies must be respected when configuring remote access.
