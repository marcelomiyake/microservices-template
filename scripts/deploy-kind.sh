#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cluster_name="${KIND_CLUSTER_NAME:-kind}"
context="kind-${cluster_name}"
namespace="${POC_NAMESPACE:-microservices-poc}"
release="${POC_RELEASE:-microservices-poc}"
tag="local-$(date +%s)-$$"

for command in docker kind kubectl helm; do
  command -v "$command" >/dev/null || { echo "Missing required command: $command" >&2; exit 1; }
done

if [[ "$(kubectl config current-context)" != "$context" ]]; then
  echo "Current kubectl context must be $context" >&2
  exit 1
fi
kind get clusters | grep -Fxq "$cluster_name" || { echo "Kind cluster $cluster_name not found" >&2; exit 1; }

cd "$root_dir"
docker build -f services/example-service/Dockerfile -t "example-service:$tag" .
docker build -f services/web-api/Dockerfile -t "web-api:$tag" .
docker build -f web/Dockerfile -t "microservices-poc-web:$tag" .
kind load docker-image "example-service:$tag" "web-api:$tag" "microservices-poc-web:$tag" --name "$cluster_name"

helm upgrade --install "$release" ./deploy/helm/microservices-poc \
  --kube-context "$context" --namespace "$namespace" --create-namespace \
  --set "exampleService.image.tag=$tag" \
  --set "webApi.image.tag=$tag" \
  --set "web.image.tag=$tag" \
  --wait --timeout 5m

kubectl --context "$context" -n "$namespace" get deployments
echo "Open with: kubectl --context $context -n $namespace port-forward service/web 8080:8080 --address 127.0.0.1"
