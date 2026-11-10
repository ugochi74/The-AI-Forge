#!/usr/bin/env bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LESSON_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
REPORT="$LESSON_DIR/outputs/process-network-practice.txt"

mkdir -p "$LESSON_DIR/outputs"

{
    echo "======================================"
    echo "PROCESS AND NETWORKING PRACTICE"
    echo "======================================"
    date
    echo

    echo "1. PROCESS INFORMATION"
    echo "--------------------------------------"
    echo "Current shell:"
    ps -p $$ -o pid,ppid,stat,comm
    echo

    echo "2. BACKGROUND PROCESS"
    echo "--------------------------------------"
    sleep 300 &
    PROCESS_ID=$!

    echo "Started a temporary sleep process."
    echo "Its process ID is: $PROCESS_ID"
    echo
    echo "Process details:"
    ps -p "$PROCESS_ID" -o pid,ppid,stat,%cpu,%mem,etime,comm
    echo

    echo "Background jobs:"
    jobs -l
    echo

    echo "Stopping only the temporary process..."
    kill -TERM "$PROCESS_ID"
    wait "$PROCESS_ID" 2>/dev/null
    echo "Temporary process stopped."
    echo

    echo "3. NETWORK INTERFACES"
    echo "--------------------------------------"
    if command -v ip >/dev/null 2>&1; then
        echo "Interface names and link states:"
        ip -brief link | awk '{print $1, $2}'
        echo
        echo "Interface address status (actual addresses redacted):"
        ip -brief address |
            awk '{print $1, $2, (NF > 2 ? "[address values redacted]" : "")}'
        echo
        echo "Routing summary:"
        ip route | awk '
            /^default/ { default_route = 1 }
            { routes++ }
            END {
                print "Default route configured: " (default_route ? "yes" : "no")
                print "Total route entries: " routes
            }'
    else
        echo "The ip command is not available."
    fi
    echo

    echo "4. NETWORK CONNECTIONS"
    echo "--------------------------------------"
    if command -v ss >/dev/null 2>&1; then
        ss -tulnH | awk '
            NF {
                count[$1]++
                total++
            }
            END {
                print "Total network sockets:", total
                for (protocol in count) {
                    print protocol " sockets:", count[protocol]
                }
                print "Local and peer addresses have been redacted."
            }'
    else
        echo "The ss command is not available."
    fi
    echo

    echo "5. DNS LOOKUP"
    echo "--------------------------------------"
    if getent hosts pypi.org >/dev/null 2>&1; then
        echo "DNS lookup for pypi.org: successful"
    else
        echo "DNS lookup for pypi.org: failed"
    fi
    echo

    echo "6. PACKAGE INFORMATION"
    echo "--------------------------------------"
    if command -v apt-cache >/dev/null 2>&1; then
        apt-cache policy python3 | awk '/Installed:|Candidate:/'
    else
        echo "apt-cache is not available."
    fi
    echo

    echo "7. PROCESS MANAGEMENT COMMANDS"
    echo "--------------------------------------"
    echo "ps     - display processes"
    echo "jobs   - display background jobs in this shell"
    echo "kill   - send a signal to a process"
    echo "wait   - wait for a background process to finish"
    echo "nice   - start a process with adjusted scheduling priority"
    echo "top    - monitor running processes"
    echo

    echo "======================================"
    echo "PRACTICE COMPLETED"
    echo "======================================"

} 2>&1 | tee "$REPORT"

echo
echo "Report saved to: outputs/process-network-practice.txt"
