# Documentation index

This index separates the Kind-deployed example from reusable documentation outlines. Replace example-specific records after generating a project; copy a file from `templates/` when adding a new document.

## Project and component guides

- [Root README](../README.md) — purpose, quickstart, checks, and template use.
- [Example service](../services/example-service/README.md) · [Web API](../services/web-api/README.md) · [Vue frontend](../web/README.md) — ownership and local workflows.
- [Template adoption guide](using-this-template.md) — generated-project checklist.
- [Frontend design handoff](../web/DESIGN.md) · [OpenDesign workflow](frontend-design.md) — design states and prototype review.

## Agent guidance

- [Root AGENTS.md](../AGENTS.md) · [Root CLAUDE.md](../CLAUDE.md).
- [DDD agent workflow](agent-workflow.md) · [Jev quality verification](jev-quality.md) — job briefs and advisory scoring.
- [Pull request evidence format](../.github/pull_request_template.md) · [CI workflow](../.github/workflows/validate.yml) — reviewable handoffs and automatic local/Kind checks.
- [Example service guidance](../services/example-service/AGENTS.md) · [Claude import](../services/example-service/CLAUDE.md).
- [Web API guidance](../services/web-api/AGENTS.md) · [Claude import](../services/web-api/CLAUDE.md).
- [Frontend guidance](../web/AGENTS.md) · [Claude import](../web/CLAUDE.md).

## Architecture and contracts

- [System design](system-design.md) — implemented example boundary and replacement points.
- [Contract catalog](contracts/README.md) · [OpenAPI source](contracts/openapi.yaml) — HTTP owners and consumers.
- [ADR index](adr/README.md) · [Rust decision](adr/0001-use-rust-for-backend-services.md) · [Vue decision](adr/0002-use-vue-for-web-frontend.md) — template baseline decisions.

## Operations and verification

- [Kind chart guide](../deploy/helm/microservices-poc/README.md) · [Local operations](operations.md) — deploy, access, undeploy, and failure behavior.
- [Kubernetes resource budgets](kubernetes-resources.md) — chart-configured requests and limits.
- [Verification index](verification/README.md) — how to record executed checks.
- [Starter Kind verification](verification/starter-kind.md) — observed build, chart, and request-path results for this template revision.
- [Quality harness verification](verification/quality-harness.md) — current unit, integration, browser E2E, coverage, and Kind results.
- [Testing and quality gates](quality-gates.md) — unit/integration/E2E commands, coverage, and SonarQube checks.
- [SonarQube verification](verification/sonarqube.md) · [Jev verification](verification/jev-readiness.md) — current external-tool evidence or gaps.

## Standards and reusable templates

- [Documentation standard](documentation-standard.md).
- [Root README](templates/root-readme.template.md), [component README](templates/component-readme.template.md), [agent guidance](templates/agents.template.md), [system design](templates/system-design.template.md).
- [ADR](templates/adr.template.md), [API contract](templates/api-contract.template.md), [database model](templates/database-model.template.md), [operations](templates/operations-guide.template.md).
- [Verification record](templates/verification-record.template.md), [design notes](templates/design-notes.template.md), [design report](templates/design-report.template.md), [general document](templates/general-document.template.md).
- [DDD agent job](templates/agent-job.template.md) · [Jev implementation evidence](templates/jev-evidence.template.md).
