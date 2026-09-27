## Outcome and domain owner

<!-- State the actor, observable outcome, and who owns unresolved domain choices. Link the agent-job brief when the work is non-trivial. -->

## Boundary and contract changes

<!-- Name affected bounded contexts, authoritative data/interface owners, and updated contract, design, or ADR paths. State "none" if unchanged. -->

## Acceptance evidence

| Requirement or failure case | Command/review and observed result | Revision or artifact |
| --- | --- | --- |
| <!-- Observable result --> | <!-- Pass, fail, or not run with reason --> | <!-- SHA, path, or link --> |

## Quality and deployment

- Local checks: `./scripts/check-local.sh` — <!-- result or reason not run -->
- Kind browser path: `./scripts/deploy-kind.sh` and `./scripts/test-kind-e2e.sh` — <!-- result or reason not run -->
- SonarQube gate, coverage, duplication, issues, hotspots — <!-- project keys, result, or reason unavailable -->
- OpenDesign review for substantial UI work — <!-- prototype/reviewer evidence or reason not applicable -->
- Jev advisory assessment, if authorized — <!-- model, score distribution, evidence scope, or not run -->

## Limits and handoff

<!-- List remaining risks, assumptions, failing or unavailable checks, and the owner of each next decision. Do not copy the source template's verification results into a generated project. -->
