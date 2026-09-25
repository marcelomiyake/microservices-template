# Documentation standard

This standard adapts the documentation roles used in the five reference PoCs. Keep claims about implementation and verification tied to source and actual runs.

## Document ownership

| Document | Purpose |
| --- | --- |
| Root README | Human overview, prerequisites, quickstart, use, checks, deployment and stop/undeploy instructions where applicable. |
| Component README | Component owner, responsibility, consumers, authoritative contracts, build/run/test steps. |
| AGENTS.md | Short, scoped instructions for coding agents; link to human and architecture docs. |
| CLAUDE.md | `@AGENTS.md` compatibility import beside each AGENTS file. |
| System design | Problem, goals, boundaries, lifecycle, contracts, consistency, security, operations, alternatives, and open questions. |
| ADR | One consequential architectural choice, its options, consequences, evidence, and review trigger. |
| Contract | Owner, producer, known consumers, authoritative schema, behavior, and compatibility. |
| Operations guide | Exact build, run/deploy, use, stop/undeploy, recovery, and data-retention procedure. |
| Verification record | Revision, environment, executed commands, observed outcomes, and limits. |
| Frontend design handoff | OpenDesign prototype, accepted interaction states, accessibility, responsive choices, and actual review evidence. |

## Rules

- `docs/README.md` indexes every maintained Markdown document. Link related documents back to the source of truth.
- Keep runnable commands and config values current. Distinguish build prerequisites from runtime/use prerequisites.
- Describe implemented behavior as implemented; label proposals and assumptions. Do not copy old project measurements, screenshots, AI model attributions, or quality scores into a generated project.
- Give each API, event, data schema, and cross-component dependency an owner and list known producers and consumers. Mark unknown consumers `Unknown` until inspected.
- Update code, OpenAPI/schema, System Design, component READMEs, and operations together when an interface or workflow changes.
- An ADR records a decision with its date and owner. For a retrospective record, mark original decision date and approval unknown when the evidence does not establish them. Supersede past decisions with a new ADR instead of rewriting history.
- Record test commands and actual results with a revision and environment. An unrun check is a gap, not a pass.
- Keep unit/component, dependency integration, and real Kind browser end-to-end tests distinct. State whether an E2E test used a mocked API. Import per-component coverage only from executed tests and document any excluded startup/bootstrap code.
- For SonarQube, keep separate project scopes and verify the analyzed revision, server gate, overall coverage, duplication, issues, and security hotspots. A scanner upload or empty gate is not a pass.
- Use OpenDesign for substantial frontend design when available; record the reviewed prototype and any unavailable step. Design output is not proof of functional behavior.
- Use DDD for domain language, invariants, contexts, ownership, and contracts. Jev may score a sanitized brief or implementation evidence but cannot decide policy or certify tests. Record the model and probability distribution if called.
- Follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages.
- Add screenshots only from a real running UI and label local/demo provenance. Add a data model when an owned schema exists. For Kind, document each container's CPU and memory requests and limits alongside the chart values; include new sidecars, init containers, and dependencies.
- For Kind deployment, state the intended context, namespace, access path, and undeploy command. For stateful systems, distinguish application removal from data deletion. Do not describe destructive cleanup as routine undeploy.
- Keep agent guidance actionable and concise. Nested `AGENTS.md` files add local instructions; do not duplicate the README.
