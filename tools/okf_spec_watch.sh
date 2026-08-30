#!/usr/bin/env bash
# OKF spec watch: diff upstream okf/SPEC.md against the vendored copy.
# See docs/okf-conformance.md, "Watching the spec".
#
# Usage: tools/okf_spec_watch.sh docs/upstream/okf-SPEC-v0.2-<sha>.md
# Exit 0 when the spec is unchanged, 1 when it moved (open an adoption
# issue titled "OKF spec change detected: review for adoption").
set -euo pipefail
VENDORED="${1:?usage: $0 <vendored-spec-path>}"
UPSTREAM_URL="https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/SPEC.md"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT
curl -sfL "$UPSTREAM_URL" -o "$TMP"
if diff -u "$VENDORED" "$TMP"; then
  echo "spec unchanged"
else
  echo "SPEC CHANGED: open an adoption issue"
  exit 1
fi
