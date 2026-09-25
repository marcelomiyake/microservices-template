# Quality harness verification

This record covers template application revision `70edfed` on 2026-09-25, using a local Linux workstation, the existing `kind-kind` context, and namespace `microservices-poc`. It verifies sample behavior only; generated projects must rerun checks with their own requirements.

## Executed checks

| Check | Observed result | Scope |
| --- | --- | --- |
| `cargo fmt --all --check` and `cargo clippy --workspace --all-targets -- -D warnings` | Passed | Rust formatting and static checks. |
| `cargo test --workspace --locked` | Passed: one example-service HTTP contract test and two web-api HTTP integration tests | Web API used a loopback upstream for success and downstream-error translation. |
| `cd web && npm ci && npm run typecheck && npm run test:unit && npm run build` | Passed: three Vue unit/component tests; production build produced `dist/` | Success, retry after error, and malformed API response. |
| `helm lint deploy/helm/microservices-poc` | Passed | Static chart check. |
| `./scripts/coverage.sh` | Passed the 80% line target for each component: example-service **86.7%** (13/15), web-api **89.7%** (35/39), Vue **93.8%** (15/16) | Rust reports cover library behavior; `src/main.rs` startup glue is excluded. Browser E2E is not included in LCOV. |
| `./scripts/deploy-kind.sh` | Passed; `example-service`, `web-api`, and `web` each reached 2/2 ready | Local Kind Helm release. |
| `./scripts/test-kind-e2e.sh` | Passed: one Playwright Chromium test opened the real Vue page and observed the message delivered through the two Rust services | Browser connected to a loopback port forward of the Kind web Service. |
| `./scripts/sonar-scan.sh` and `python3 scripts/check-sonar-gate.py` | Passed all three SonarQube server gates and local coverage, duplication, issue, and hotspot checks | Exact values and access limit are in [the SonarQube record](sonarqube.md). |
| `./scripts/undeploy-kind.sh` | Passed; Helm release removed | The `microservices-poc` namespace and Kind cluster remain. |

The OpenDesign workflow is documented for future substantial frontend changes. The starter page has no completed OpenDesign prototype review. Jev results are recorded separately in [the advisory assessment](jev-readiness.md). These checks do not establish production capacity, security certification, or a formal accessibility audit.
