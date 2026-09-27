# Kind operations

This runbook covers the checked-in local Kind deployment. It has no persistent-data lifecycle.

## Build and deploy prerequisites

- Docker, Kind, kubectl, Helm 3 or 4, and a local Kind cluster. The defaults expect cluster `kind` and active context `kind-kind`.
- Network access on a fresh checkout to fetch Cargo, npm, and base-image dependencies.
- Free local capacity for six application pods (two replicas each), plus Kind system pods.

## Use prerequisites

A ready Helm release, loopback port 8080, and a browser. No credentials or external services are required.

## Build and deploy

From the repository root:

```sh
kubectl config current-context
./scripts/deploy-kind.sh
kubectl --context kind-kind -n microservices-poc get deployments,pods,services
```

The script rejects an unexpected active context, builds three images, loads them into the selected Kind cluster, installs/upgrades the Helm release, and waits for readiness. It defaults to cluster `kind`, namespace `microservices-poc`, and release `microservices-poc`; override with `KIND_CLUSTER_NAME`, `POC_NAMESPACE`, and `POC_RELEASE`. Use one release per namespace because Service DNS names are fixed in the Nginx and API configs. The [chart values](../deploy/helm/microservices-poc/values.yaml) configure replicas and image settings.

## Resource budgets

See [Kubernetes resource budgets](kubernetes-resources.md) for every current container's CPU/memory request and limit. These are local defaults, not measured sizing.

## Use and verify

```sh
kubectl --context kind-kind -n microservices-poc port-forward service/web 8080:8080 --address 127.0.0.1
```

Open <http://127.0.0.1:8080>. The page should show the sample message. `GET /api/example` through the same port should return JSON. `web` serves `/healthz`; the Rust services serve `/health`. The API health endpoint checks its own process, not downstream availability. Record actual observed results in [verification](verification/README.md).

## Undeploy and data retention

Stop port-forward with Ctrl-C, then run:

```sh
./scripts/undeploy-kind.sh
```

The script removes the Helm release but leaves the namespace and Kind cluster. The starter has no database, PVC, or queue data. A generated project that adds persistent state must document its retention and deletion commands separately.

## Recovery and limits

If rollout fails, inspect `kubectl --context kind-kind -n microservices-poc get pods`, then describe the affected pod and its events. Check the active context and cluster name before rerunning the script. If the page loads but the sample call fails, inspect `web-api` and `example-service` pods and their Service endpoints. A Kind run does not prove production capacity or availability.
