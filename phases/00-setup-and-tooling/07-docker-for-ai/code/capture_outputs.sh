#!/usr/bin/env bash
# Capture real command output; run with --check for prerequisites only.
set -euo pipefail

case "${1:-}" in
    ""|--check) ;;
    *) echo "Usage: bash capture_outputs.sh [--check]" >&2; exit 2 ;;
esac

CODE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$CODE_DIR"
mkdir -p ../outputs
RUN_DIR="$(mktemp -d "../outputs/run-$(date -u +%Y%m%dT%H%M%SZ)-XXXXXX")"
SUMMARY="$RUN_DIR/summary.md"
printf '# Lesson 7 execution results\n\nUTC: %s\n\n' "$(date -u +%FT%TZ)" > "$SUMMARY"
printf '| Output | Exit code |\n|---|---|\n' >> "$SUMMARY"
echo "Saving evidence to $RUN_DIR"

capture() {
    local name="$1"
    shift
    local result=0
    printf '\nRunning: '
    printf '%q ' "$@"
    printf '\n'
    {
        printf 'Command: '
        printf '%q ' "$@"
        printf '\n\n'
    } > "$RUN_DIR/$name"
    "$@" 2>&1 | tee -a "$RUN_DIR/$name" || result=$?
    printf '| [%s](%s) | %s |\n' "$name" "$name" "$result" >> "$SUMMARY"
    return "$result"
}

finish() {
    local result=$?
    if [ "$result" -ne 0 ]; then
        printf '\n**Incomplete:** execution stopped after a failed check. Later exercises were not verified.\n' >> "$SUMMARY"
    fi
    echo "Evidence: $SUMMARY"
}
trap finish EXIT

prerequisites=0
capture environment-check.txt docker version || prerequisites=1
capture compose-version.txt docker compose version || prerequisites=1
if [ "$prerequisites" -ne 0 ]; then
    printf '\nDocker daemon access and Docker Compose are required. No builds or containers were started.\n' >> "$SUMMARY"
    exit 1
fi
if [ "${1:-}" = --check ]; then
    printf '\nPrerequisites passed; exercise execution was not requested.\n' >> "$SUMMARY"
    exit 0
fi

mkdir -p ../outputs/models ../outputs/datasets
capture compose-config.txt docker compose config --quiet
capture hello-world.txt docker run --rm hello-world
capture build-devel.txt docker compose build ai-dev
capture pytorch.txt docker run --rm ai-forge-lesson07:devel python -c \
    'import torch; print(torch.__version__); print("CUDA available:", torch.cuda.is_available()); assert torch.__version__.startswith("2.6.0")'
capture stack-start.txt docker compose up -d
capture services.txt docker compose ps

wait_for_services() {
    local suffix="$1"
    capture "qdrant-$suffix.txt" docker compose exec -T ai-dev curl \
        --fail --retry 20 --retry-connrefused --retry-delay 2 http://qdrant:6333/collections
    capture "api-$suffix.txt" docker compose exec -T ai-dev curl \
        --fail --retry 20 --retry-connrefused --retry-delay 2 http://api:5000/health
}

wait_for_services initial
capture stack-verification.txt docker compose exec -T ai-dev python \
    /workspace/phases/00-setup-and-tooling/07-docker-for-ai/code/verify_stack.py
capture flask-home.txt curl --fail --max-time 15 http://localhost:5000/
capture flask-health.txt curl --fail --max-time 15 http://localhost:5000/health
capture stack-stop.txt docker compose down
capture stack-recreate.txt docker compose up -d
wait_for_services recreated
capture persistence.txt docker compose exec -T ai-dev python \
    /workspace/phases/00-setup-and-tooling/07-docker-for-ai/code/verify_stack.py
capture build-runtime.txt docker build --build-arg CUDA_VARIANT=runtime -t ai-forge-lesson07:runtime .
capture pytorch-runtime.txt docker run --rm ai-forge-lesson07:runtime python -c \
    'import torch; print(torch.__version__); assert torch.__version__.startswith("2.6.0")'
capture image-sizes.txt docker image inspect ai-forge-lesson07:devel ai-forge-lesson07:runtime \
    --format '{{.RepoTags}} {{.Size}} bytes'
capture cleanup.txt docker compose down
printf '\nCPU exercise commands passed. GPU checks and the learner quiz are separate.\n' >> "$SUMMARY"
