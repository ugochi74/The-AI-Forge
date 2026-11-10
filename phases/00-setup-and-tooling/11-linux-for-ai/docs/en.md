# Linux for AI — Command Reference

**Author:** Andrew.Nd

| Task | Command | Purpose |
|---|---|---|
| Current directory | `pwd` | Show the working directory |
| List files | `ls -la` | Include hidden files and details |
| Change directory | `cd directory` | Enter a directory |
| Home directory | `cd ~` | Navigate to the user's home |
| File permissions | `stat file.txt` | Inspect permissions and ownership |
| Change permissions | `chmod 640 file.txt` | Set file permissions |
| User identity | `id` | Show UID and groups |
| Default permissions | `umask` | Show permission mask |
| List processes | `ps -u "$USER"` | Show the user's processes |
| Monitor processes | `top` | View system activity |
| Background job | `command &` | Run a command in the background |
| Stop a process | `kill -TERM PID` | Request process termination |
| Memory | `free -h` | Show RAM and swap |
| CPU count | `nproc` | Show available processing units |
| Disk space | `df -h` | Show filesystem usage |
| Directory size | `du -sh directory` | Show directory size |
| Package version | `apt-cache policy package` | Inspect package versions |
| Network interfaces | `ip -brief address` | Show interface addresses |
| Routing | `ip route` | Show network routes |
| Listening sockets | `ss -tuln` | Show listening ports |
| DNS lookup | `getent hosts pypi.org` | Resolve a hostname |
| HTTP headers | `curl -I https://pypi.org` | Check an HTTP response |

## Permission numbers

| Number | Permission |
|---|---|
| 7 | Read, write, execute |
| 6 | Read, write |
| 5 | Read, execute |
| 4 | Read only |
| 0 | No permission |

The three digits in a mode represent owner, group, and others. For example, `640` means owner read/write, group read, and others no access.

## Package management

Ubuntu uses APT. Commands that install packages or change system package information may require administrator access. Follow workplace IT policy.

## Long-running sessions

`tmux` and `screen` are commonly used to keep terminal sessions alive. Check whether they are installed before relying on them.

## macOS note

macOS has similar terminal concepts, but it does not use Ubuntu's APT package manager by default. Homebrew is commonly used to install developer tools. Some command options differ between macOS and Linux.
