# Kind resource budgets

These are chart-configured local PoC defaults from [values.yaml](../deploy/helm/microservices-poc/values.yaml), not measured use or production sizing. Each Deployment defaults to two replicas. Review budgets after measuring the generated project's workload.

| Workload/container | CPU request | Memory request | CPU limit | Memory limit |
| --- | ---: | ---: | ---: | ---: |
| `example-service` | 25m | 32Mi | 250m | 128Mi |
| `web-api` | 25m | 32Mi | 250m | 128Mi |
| `web` | 25m | 32Mi | 250m | 128Mi |

The chart sets both requests and limits on every current container. New sidecars, init containers, databases, and queues need their own budgets and documentation. See [operations](operations.md) for the deployment lifecycle.
