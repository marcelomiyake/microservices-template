#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mode="${1:---full}"
if [[ "$mode" != "--full" && "$mode" != "--quick" || $# -gt 1 ]]; then
  echo 'Usage: ./scripts/check-local.sh [--full|--quick]' >&2
  exit 2
fi

for tool in cargo npm helm; do
  command -v "$tool" >/dev/null || { echo "Missing required command: $tool" >&2; exit 2; }
done

cd "$root_dir"
cargo fmt --all --check
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo test --workspace --locked
(
  cd web
  npm ci
  npm run typecheck
  if [[ "$mode" == "--quick" ]]; then
    npm run test:unit
  fi
  npm run build
)
helm lint deploy/helm/microservices-poc

if [[ "$mode" == "--full" ]]; then
  "$root_dir/scripts/coverage.sh"
fi

echo "Local checks passed ($mode). Kind E2E and SonarQube require their separate environments."
