#!/usr/bin/env bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LESSON_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
REPORT="$LESSON_DIR/outputs/linux-system-check.txt"

mkdir -p "$LESSON_DIR/outputs"

{
    echo "======================================"
    echo "LINUX FOR AI - SYSTEM CHECK"
    echo "======================================"
    echo "Date: $(date)"
    echo

    echo "1. OPERATING SYSTEM"
    echo "--------------------------------------"
    cat /etc/os-release
    echo
    uname -srm
    echo

    echo "2. USER AND PERMISSIONS"
    echo "--------------------------------------"
    echo "User ID: $(id -u)"
    echo "Primary group ID: $(id -g)"
    echo "Current umask:"
    umask
    echo "Permissions practice file:"
    stat -c '%A %a' "$LESSON_DIR/outputs/permissions-practice.txt" 2>&1
    echo

    echo "3. RUNNING PROCESSES"
    echo "--------------------------------------"
    ps -u "$(id -un)" -o pid,ppid,stat,%cpu,%mem,etime,comm --sort=-%cpu | head -n 15
    echo
    echo "Current system uptime:"
    uptime
    echo

    echo "4. MEMORY AND CPU"
    echo "--------------------------------------"
    free -h
    echo "Available CPU cores:"
    nproc
    echo

    echo "5. DISK SPACE"
    echo "--------------------------------------"
    df -h "$HOME"
    echo "Lesson folder size:"
    du -sh "$LESSON_DIR" | awk '{print $1 " (lesson directory)"}'
    echo

    echo "6. PACKAGE MANAGEMENT"
    echo "--------------------------------------"
    if command -v apt >/dev/null 2>&1; then
        apt --version
    else
        echo "apt is not available"
    fi

    if command -v apt-cache >/dev/null 2>&1; then
        apt-cache policy curl | awk '/Installed:|Candidate:/'
    fi
    echo

    echo "7. NETWORK CONNECTIVITY"
    echo "--------------------------------------"
    if getent hosts pypi.org >/dev/null 2>&1; then
        echo "DNS lookup for pypi.org: successful"
    else
        echo "DNS lookup for pypi.org: failed"
    fi

    if command -v curl >/dev/null 2>&1; then
        curl -sS -o /dev/null \
            -w 'HTTPS response status: %{http_code}\n' \
            --max-time 10 https://pypi.org ||
            echo "HTTPS request failed"
    else
        echo "curl is not available"
    fi
    echo

    echo "8. LONG-RUNNING SESSION AND GPU TOOLS"
    echo "--------------------------------------"
    for tool in tmux screen nvidia-smi; do
        if command -v "$tool" >/dev/null 2>&1; then
            echo "$tool: available"
        else
            echo "$tool: not available"
        fi
    done
    echo

    echo "9. OTHER USEFUL SYSTEM TOOLS"
    echo "--------------------------------------"
    for tool in git python3 pip3 rsync ssh scp; do
        if command -v "$tool" >/dev/null 2>&1; then
            echo "$tool: available"
        else
            echo "$tool: not available"
        fi
    done

    echo
    echo "======================================"
    echo "SYSTEM CHECK COMPLETED"
    echo "======================================"

} 2>&1 | tee "$REPORT"

echo
echo "Report saved to: outputs/linux-system-check.txt"
