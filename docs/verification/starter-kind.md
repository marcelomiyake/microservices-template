# Starter Kind verification

This record covers the template's sample code and chart before its first commit. It does not verify future generated projects or production capacity.

## Environment

| Field | Value |
| --- | --- |
| Revision/worktree | `40d28d1` base commit with uncommitted template additions |
| Date/time | 2026-09-25 18:55 UTC |
| Local tools | Cargo 1.98.1, Node.js 24.21.0, Docker 29.8.1, Kind 0.33.0, Helm 4.3.0, kubectl 1.37.1 |
| Cluster/context | Existing local `kind` cluster, `kind-kind`, namespace `microservices-poc` |

## Commands and observed results

| Command or action | Observed result | Limit |
| --- | --- | --- |
| `cargo fmt --all` and `cargo clippy --workspace --all-targets -- -D warnings` | Passed | Formatting command applied formatting before the check. |
| `cargo test --workspace` | Passed; `web-api` had two tests for success and downstream failure, while `example-service` had no unit tests | The end-to-end Kind path was checked separately. |
| `cd web && npm ci && npm run typecheck && npm run build` | Passed; Vite produced `dist/` | No browser automation was run. |
| `helm lint deploy/helm/microservices-poc` | Passed with icon recommendation only | Static chart check. |
| `helm template ...` and `kubectl apply --dry-run=client --validate=false -f ...` | Rendered three Deployments and three Services | Client dry run did not validate against the API server. |
| `./scripts/deploy-kind.sh` | Final rollout passed; all three Deployments reached 2/2 ready | The initial frontend image failed due to Nginx temp-directory permissions; the Dockerfile was corrected and redeployed successfully. |
| `kubectl ... port-forward service/web 8080:8080 --address 127.0.0.1` plus `curl` to `/`, `/healthz`, and `/api/example` | HTML loaded; health returned `ok`; API returned `{"message":"Your Rust and Vue PoC is running."}` | This checks the HTTP path, not browser rendering or load capacity. |
| `./scripts/undeploy-kind.sh` | Passed; Helm release removed | Namespace remains, as documented. |

## Follow-up

Generated projects must replace the sample path and add focused tests for their real behavior. Run browser accessibility and workload checks when those requirements are defined. Record measured resource use before treating chart values as sizing evidence.
