#!/usr/bin/env bash
# Public/offline lane: no private backend checkout, API credentials or network.
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
echo "Public offline checks passed."
