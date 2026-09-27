#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cluster_name="${KIND_CLUSTER_NAME:-kind}"
context="kind-${cluster_name}"
namespace="${POC_NAMESPACE:-microservices-poc}"
port="${E2E_PORT:-18080}"

for tool in kubectl curl npm; do
  command -v "$tool" >/dev/null || { echo "Missing required command: $tool" >&2; exit 2; }
done
if [[ "$(kubectl config current-context)" != "$context" ]]; then
  echo "Current kubectl context must be $context" >&2
  exit 2
fi

mkdir -p "$root_dir/target"
kubectl --context "$context" -n "$namespace" rollout status deployment/web --timeout=90s
kubectl --context "$context" -n "$namespace" port-forward service/web "$port":8080 --address 127.0.0.1 > "$root_dir/target/kind-e2e-port-forward.log" 2>&1 &
forward_pid=$!
cleanup() { kill "$forward_pid" 2>/dev/null || true; wait "$forward_pid" 2>/dev/null || true; }
trap cleanup EXIT

ready=false
for _ in {1..30}; do
  if ! kill -0 "$forward_pid" 2>/dev/null; then
    echo "Frontend port-forward stopped; see target/kind-e2e-port-forward.log" >&2
    exit 1
  fi
  if curl --fail --silent "http://127.0.0.1:$port/healthz" >/dev/null; then
    ready=true
    break
  fi
  sleep 1
done
if [[ "$ready" != true ]]; then
  echo "Frontend port-forward did not become ready; see target/kind-e2e-port-forward.log" >&2
  exit 1
fi

cd "$root_dir/web"
E2E_BASE_URL="http://127.0.0.1:$port" npm run test:e2e
