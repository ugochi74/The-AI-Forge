# Lesson 11 Verification

**Author:** Andrew.Nd  
**Platform:** Ubuntu 24.04.2 LTS  
**Date:** 2026-11-10

## Completed checks

| Area | Evidence | Result |
|---|---|---|
| Linux identity | `uname -a`, `/etc/os-release` | Passed |
| Filesystem navigation | `pwd`, `ls`, `cd` | Passed |
| File permissions | `stat`, `chmod` | Passed |
| User and groups | `id` | Passed |
| Default permissions | `umask` | Passed |
| Process listing | `ps -u "$USER"` | Passed |
| Background process | `sleep 300 &`, `ps`, `jobs`, `kill`, `wait` | Passed |
| CPU and memory | `nproc`, `free -h` | Passed |
| Disk space | `df -h`, `du -sh` | Passed |
| Package information | `apt --version`, `apt-cache policy` | Passed |
| Network interfaces | `ip -brief address`, `ip route` | Passed |
| Listening sockets | `ss -tuln` | Passed |
| DNS lookup | `getent hosts pypi.org` | Passed |
| HTTP connectivity | `curl -I https://pypi.org` | Passed; HTTP 200 |

## Environment limitations

- `tmux` and `screen` were not available.
- `nvidia-smi` was not available; GPU availability remains unconfirmed.
- The Docker interface existed but was down. Docker daemon access remains subject to the previously documented workplace restriction.
- Package installation was not attempted because administrator access is restricted.
- The system reported approximately 3.7 GiB RAM, with substantial swap usage at the time of the check.

## Evidence files

- `outputs/linux-system-check.txt`
- `outputs/process-network-practice.txt`
- `outputs/permissions-practice.txt`

## Verification conclusion

The Linux navigation, permissions, process, resource, package-information, and networking checks completed successfully. The unavailable tools and administrator restrictions are documented rather than treated as successful installations or tests.
