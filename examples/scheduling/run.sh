#!/usr/bin/env bash
# Thin process wrapper; the prompt workflows perform all content work.
set -euo pipefail
umask 077
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PROMPT_FILE="${1:?Usage: run.sh /absolute/path/to/prompt.md}"
shift
CODEX_BIN="${CODEX_BIN:-codex}"
RUN_LOG_ROOT="${RUN_LOG_ROOT:-$ROOT_DIR/examples/.state/scheduled-runs}"
[[ -r "$PROMPT_FILE" ]] || { echo "Cannot read prompt: $PROMPT_FILE" >&2; exit 1; }
mkdir -p "$RUN_LOG_ROOT"
if ! mkdir "$RUN_LOG_ROOT/.lock"; then
  [[ -d "$RUN_LOG_ROOT/.lock" ]] || exit 1
  echo "Another run holds $RUN_LOG_ROOT/.lock; skipping."
  exit 0
fi
trap 'rmdir "$RUN_LOG_ROOT/.lock"' EXIT
RUN_DIR="$(mktemp -d "$RUN_LOG_ROOT/$(date -u +%Y%m%dT%H%M%SZ)-XXXXXX")"
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$RUN_DIR/started-at"
{
  cat "$PROMPT_FILE"
  printf '\nRun directory: %s\n' "$RUN_DIR"
  printf 'If diagnostics are requested, keep MCP observations in %s/mcp-observations.md.\n' "$RUN_DIR"
  printf 'Finish this invocation within 45 minutes; report incomplete stages honestly.\n'
} > "$RUN_DIR/prompt.md"
echo "Run logs: $RUN_DIR"
set +e
"$CODEX_BIN" --search -a never exec \
  --cd "$ROOT_DIR" --model gpt-6.1-sol \
  -c model_reasoning_effort=low \
  --sandbox workspace-write -c sandbox_workspace_write.network_access=true \
  --json --output-last-message "$RUN_DIR/summary.md" \
  "$@" - < "$RUN_DIR/prompt.md" > "$RUN_DIR/events.jsonl" 2> "$RUN_DIR/stderr.log"
STATUS=$?
set -e
printf '%s\n' "$STATUS" > "$RUN_DIR/exit-code"
date -u +%Y-%m-%dT%H:%M:%SZ > "$RUN_DIR/finished-at"
exit "$STATUS"
