#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if ! command -v cargo-llvm-cov >/dev/null 2>&1; then
  echo 'Install cargo-llvm-cov before running coverage.' >&2
  exit 2
fi

cd "$root_dir"
mkdir -p target/coverage
cargo llvm-cov -p example-service --all-targets --locked \
  --ignore-filename-regex '/src/main\.rs$' --lcov \
  --output-path target/coverage/example-service.lcov
cargo llvm-cov -p web-api --all-targets --locked \
  --ignore-filename-regex '/src/main\.rs$' --lcov \
  --output-path target/coverage/web-api.lcov
python3 scripts/normalize-rust-lcov.py
(
  cd web
  npm ci
  npm run test:unit:coverage
)
python3 scripts/check-coverage.py
