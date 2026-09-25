#!/usr/bin/env bash
set -euo pipefail

cluster_name="${KIND_CLUSTER_NAME:-kind}"
context="kind-${cluster_name}"
namespace="${POC_NAMESPACE:-microservices-poc}"
release="${POC_RELEASE:-microservices-poc}"

if [[ "$(kubectl config current-context)" != "$context" ]]; then
  echo "Current kubectl context must be $context" >&2
  exit 1
fi

helm --kube-context "$context" -n "$namespace" uninstall "$release"
echo "Removed the application release. Namespace $namespace remains."
