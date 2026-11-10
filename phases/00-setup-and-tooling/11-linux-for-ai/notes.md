# Lesson 11: Linux for AI

**Author:** Andrew.Nd  
**Phase:** 00 — Setup & Tooling

## 1. Introduction

Linux is an operating system widely used in software engineering, cloud computing, servers, and AI development. Understanding the Linux terminal helps AI engineers manage files, permissions, processes, resources, packages, and network connections.

## 2. Filesystem navigation

Linux organizes files and directories in a tree that begins at the root directory `/`.

Useful commands:

- `pwd` — display the current working directory.
- `ls -la` — list files, including hidden files, with details.
- `cd directory` — enter a directory.
- `cd ..` — move to the parent directory.
- `cd ~` — move to the user's home directory.
- `cd -` — return to the previous directory.

Important directories include `/home` for user directories, `/etc` for system configuration, `/tmp` for temporary files, `/usr` for user-space programs and resources, and `/var` for changing system data and logs.

## 3. File permissions and ownership

Linux permissions control who can read, write, or execute a file.

- `r` — read.
- `w` — write.
- `x` — execute.

The three permission groups are owner, group, and others.

Examples:

- `chmod 600 file.txt` — owner can read and write; everyone else has no access.
- `chmod 640 file.txt` — owner can read and write; group can read.
- `chmod 644 file.txt` — owner can read and write; group and others can read.
- `id` — display user and group identity.
- `stat file.txt` — display file metadata.

The `umask` controls which permissions are removed from default permissions when new files and directories are created. My system reports `0002`. This commonly produces `664` for regular files and `775` for directories.

## 4. Process management

A process is a running instance of a program. Each process has a process ID (PID).

Useful commands:

- `ps -u "$USER"` — list processes belonging to the current user.
- `ps -p PID -o pid,ppid,stat,comm` — inspect a particular process.
- `top` — monitor running processes.
- `jobs -l` — list background jobs in the current shell.
- `command &` — start a command in the background.
- `kill -TERM PID` — request that a process terminate.
- `wait PID` — wait for a background process to finish.
- `uptime` — show how long the system has been running and its load averages.

A PID identifies a process. A PPID identifies its parent process. Process state indicates whether it is running, sleeping, stopped, or in another state.

Always identify a process before stopping it. Do not terminate unfamiliar system processes.

## 5. CPU, memory, and disk space

AI workloads can use significant CPU, RAM, GPU memory, and storage.

- `free -h` — display memory and swap usage.
- `nproc` — display the number of available processing units.
- `df -h` — show filesystem disk usage.
- `du -sh directory` — show the total size of a directory.

My system reported two available CPU cores and approximately 3.7 GiB of RAM. The system check showed substantial swap usage, so memory availability should be monitored when running AI workloads.

## 6. Package management

Ubuntu uses APT (Advanced Package Tool) to manage software packages.

- `apt --version` — display the APT version.
- `apt-cache policy package-name` — inspect installed and available package versions.
- `sudo apt update` — refresh package information.
- `sudo apt install package-name` — install a package.

Package installation and system updates may require administrator permissions. On this managed workstation, I should request IT assistance rather than attempt to bypass access restrictions.

## 7. Networking

Networking allows applications and machines to communicate.

Useful commands:

- `ip -brief address` — display network interfaces and addresses.
- `ip route` — display routing information.
- `ss -tuln` — display listening TCP and UDP sockets.
- `getent hosts pypi.org` — perform a hostname lookup.
- `curl -I https://pypi.org` — inspect HTTP response headers.

My system successfully resolved `pypi.org` and received HTTP 200 from its website.

A listening port does not automatically mean that a service is exposed to the public internet. Network access depends on interface binding, routing, and firewall rules.

## 8. Long-running sessions

Long-running training jobs can be interrupted when a terminal closes or a remote connection drops.

Tools such as `tmux` and `screen` help keep terminal sessions available. Neither was installed on my workstation during this lesson. I should request an approved installation if needed.

## 9. Linux and macOS

Linux and macOS are Unix-like operating systems, but they differ in their system architecture and administration tools.

- Ubuntu uses APT for package management.
- macOS commonly uses Homebrew for additional packages.
- Some terminal utilities and command options differ between GNU/Linux and macOS.
- Linux is widely used for cloud servers, containers, and AI deployment environments.
- macOS is also suitable for development, but GPU and deployment workflows may differ.

## 10. Relevance to AI engineering

Linux skills help an AI engineer prepare development environments, install dependencies, manage training processes, monitor resource usage, inspect logs, transfer files, and troubleshoot network or deployment problems.

Understanding these tools is important when moving from local development to cloud machines and production systems.
