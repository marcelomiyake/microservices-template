# Kind Helm chart

This chart deploys `example-service`, `web-api`, and `web` to a dedicated namespace in a local Kind cluster. Each application has two replicas, a ClusterIP Service, HTTP liveness/readiness probes, CPU/memory requests and limits, and a non-root container. It includes no database, queue, public Ingress, NodePort, or LoadBalancer.

Use [the deployment script](../../../scripts/deploy-kind.sh) from the repository root to build images, load them into Kind, and install or upgrade this chart. The script requires the active context to match `kind-${KIND_CLUSTER_NAME:-kind}`. It uses namespace and release `microservices-poc` unless `POC_NAMESPACE` and `POC_RELEASE` are set. The resource defaults are in [values.yaml](values.yaml) and summarized in [the resource budget](../../../docs/kubernetes-resources.md).

Service names are fixed within the namespace because Nginx proxies to `web-api` and the API calls `example-service`. Use one release per namespace. Update the chart and Nginx together when renaming services.

After deploy:

```sh
kubectl --context kind-kind -n microservices-poc port-forward service/web 8080:8080 --address 127.0.0.1
```

Open <http://127.0.0.1:8080>. Stop the port forward with Ctrl-C, then use [the undeploy script](../../../scripts/undeploy-kind.sh) to remove the release. This chart has no PVC or other persistent data. The scripts do not delete the namespace or cluster.
