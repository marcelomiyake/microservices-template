# Rust + Vue microservices PoC template

A Kind-first starter for small proof-of-concept systems. It contains two Rust HTTP services, a Vue 3/TypeScript frontend, a Helm chart for local Kubernetes, and documentation scaffolding adapted from [OpenTube](https://github.com/marcelomiyake/opentube), [Search Autocomplete System](https://github.com/marcelomiyake/search-autocomplete-system), [Notification System](https://github.com/marcelomiyake/notification-system), [URL Shortener](https://github.com/marcelomiyake/url-shortener), and [Web Crawler](https://github.com/marcelomiyake/web-crawler).

The example behavior is intentionally small: the Vue app calls `web-api`, which calls `example-service`. All three run as Kubernetes Deployments in Kind. There is no database, queue, authentication, or production deployment until a generated project has requirements for them. [Documentation index](docs/README.md) · [System design](docs/system-design.md) · [HTTP contract](docs/contracts/openapi.yaml).

## Create a project from this template

On GitHub, select **Use this template → Create a new repository**. GitHub copies the default branch's files into a new repository with unrelated history. Then:

1. Replace the title, purpose, and example behavior in this README and the component READMEs.
2. Rename `example-service`, `web-api`, and `web` if your domain calls for different boundaries. Update the Cargo workspace, package name, paths, environment variables, API contract, and links together.
3. Replace the example flow in [the system design](docs/system-design.md), record real decisions in `docs/adr/`, and document every cross-service interface in `docs/contracts/`.
4. Remove template instructions, unused sample code, and any documentation sections that do not apply. Record actual verification results only after running checks.

This source repository is configured as a GitHub template. To enable the same setting on a fork, a repository admin selects **Settings → Template repository**. GitHub [does not allow Git LFS files in template repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository).

## Repository map

| Path | Role |
| --- | --- |
| `services/example-service/` | Owns the sample message endpoint. |
| `services/web-api/` | Browser-facing API and client of `example-service`. |
| `web/` | Vue app; Vite proxies `/api` to `web-api` during local development. |
| `deploy/helm/microservices-poc/` | Kind chart for three Deployments and ClusterIP Services. |
| `scripts/` | Guarded Kind deploy and undeploy commands. |
| `.sonar/` | Separate SonarQube scopes for the two Rust services and Vue. |
| `docs/` | Architecture, decisions, contracts, operations, verification, and reusable Markdown templates. |

Each component has its own README and scoped `AGENTS.md`. `CLAUDE.md` imports the corresponding guidance.

## Prerequisites

- **Build and deploy:** Docker, Kind, kubectl, Helm 3 or 4, Rust 1.98.1 with Cargo, Node.js 22.12 or newer, and npm. The Rust toolchain includes `rustfmt` and `clippy`. Create or select a local Kind cluster named `kind` with context `kind-kind`.
- **Quality tooling:** `cargo-llvm-cov` for Rust coverage, Playwright Chromium for browser E2E, and a reachable SonarQube server plus `SONAR_TOKEN` to run the SonarQube gate. OpenDesign is a separate design-time app; Jev requires an authorized `TYPESAFE_API_KEY` for its advisory assessment.
- **Use:** the deployed Kind release, a browser, and a loopback port forward. No account, database, or secret is needed.

## Deploy to Kind

The script verifies the active context, builds three local images, loads them into Kind, installs/upgrades the Helm release, and waits for readiness:

```sh
./scripts/deploy-kind.sh
kubectl --context kind-kind -n microservices-poc port-forward service/web 8080:8080 --address 127.0.0.1
```

Open <http://127.0.0.1:8080>. The expected message is “Your Rust and Vue PoC is running.” Each application defaults to two replicas; [resource budgets](docs/kubernetes-resources.md) are local defaults. No public ingress is installed. The scripts default to cluster `kind`, namespace and release `microservices-poc`; override with `KIND_CLUSTER_NAME`, `POC_NAMESPACE`, and `POC_RELEASE` if needed. Use one release per namespace because service DNS names are fixed.

Run the real browser end-to-end check while the release is ready:

```sh
cd web && npx playwright install chromium && cd ..
./scripts/test-kind-e2e.sh
```

Stop the port forward with Ctrl-C. Remove the application with `./scripts/undeploy-kind.sh`. There is no persistent data; the scripts leave the namespace and Kind cluster intact. See [the operations guide](docs/operations.md) and [chart README](deploy/helm/microservices-poc/README.md).

## Optional process-only development

Use three terminals from the repository root:

```sh
cargo run -p example-service
```

```sh
cargo run -p web-api
```

```sh
cd web
npm ci
npm run dev
```

Open the URL printed by Vite (normally <http://127.0.0.1:5173>). You can also inspect `http://127.0.0.1:8081/api/example` and the service health paths `/health` on ports 8081 and 8082.

`web-api` uses `EXAMPLE_SERVICE_URL` (default `http://127.0.0.1:8082`) and `PORT` (default `8081`). `example-service` uses `PORT` (default `8082`). If you change the API port, update `web/vite.config.ts` as well.

## Verify

```sh
./scripts/check-local.sh
```

The local check requires `cargo-llvm-cov` and runs Rust formatting, Clippy and tests, Vue typecheck/build/tests, Helm lint, and the 80% per-component coverage gate. Use `./scripts/check-local.sh --quick` while iterating. [GitHub Actions](.github/workflows/validate.yml) runs the full check and the real Kind browser path on pull requests and pushes to `main`. With a separately configured SonarQube server, `./scripts/sonar-scan.sh` enforces its gate plus overall coverage, duplication, active-issue, and hotspot thresholds; a local server cannot be reached by GitHub-hosted runners. See [testing and quality gates](docs/quality-gates.md) for scopes, setup, and limits. [The starter verification record](docs/verification/quality-harness.md) reports observed results. Record each generated project's executed commands, revision, environment, and results in a new record based on [the verification template](docs/templates/verification-record.template.md). A successful local build or Kind deployment does not demonstrate production capacity or availability.

## Design and agent workflow

Use [OpenDesign](https://github.com/nexu-io/open-design) as design-time tooling for substantial Vue changes. Keep the accepted flow, interaction states, accessibility notes, and review evidence in [web/DESIGN.md](web/DESIGN.md); see [the frontend design workflow](docs/frontend-design.md). This starter screen has no recorded OpenDesign review.

For non-trivial domain work, prepare a [DDD agent brief](docs/agent-workflow.md) with terms, invariants, owners, contracts, risks, and acceptance checks. [Jev quality verification](docs/jev-quality.md) can score a sanitized brief or actual implementation evidence when authorized; the result is advisory. Use [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) for commits.

## Stop and extend

Stop optional local processes with Ctrl-C. Kind is the supported PoC deployment target. When generated projects add stateful dependencies, document their ownership, resource budgets, recovery, and retention before deployment.

Use [the documentation standard](docs/documentation-standard.md) and [the generated-project checklist](docs/using-this-template.md) while replacing the sample. The [templates folder](docs/templates/) contains outlines for new project and component guides, ADRs, contracts, operations, design notes, and verification records.

## License

MIT; see [LICENSE](LICENSE). Keep the notice when redistributing substantial portions of the template.
