# DDD for agent work

Use domain-driven design to make a PoC's language and ownership explicit before changing behavior. A folder, pod, service, or agent task is not automatically a bounded context. Establish boundaries from coherent use cases, rules, data ownership, consistency needs, and terminology.

## Before implementation

Copy [the agent-job brief](templates/agent-job.template.md) for non-trivial work. Name the actor and outcome, the command/use case, business invariants, state transitions, authoritative data owner, known producers and consumers, failure behavior, scope, and observable acceptance checks. Separate repository facts from assumptions and proposed decisions, citing paths and the revision inspected.

Keep unknown policy choices with their product/domain owner. Use aggregates and value objects when they protect a named invariant. Keep simpler flows simple; do not add CQRS, event sourcing, or an extra service because a pattern exists in a reference project.

## During and after implementation

Keep terms consistent within each context and update API/event contracts, System Design, component guides, and tests with the code. For a cross-context change, identify the owner on both sides, data authority, dependency order, timeout/retry behavior, and expected failure result. After implementation, compare actual tests and Kind evidence to the brief's acceptance criteria. Record gaps rather than inferring success.

Use this loop for each agent task:

1. Read root and affected component `AGENTS.md` files, then cite the current revision and relevant contract, design, code, and test paths in the job brief.
2. Turn each accepted requirement and failure case into an observable check before editing. Keep unknown domain policy with its named owner.
3. Change the smallest owned slice. Update tests and documentation beside the authoritative code and contract.
4. Run `./scripts/check-local.sh --quick` while iterating and `./scripts/check-local.sh` before handoff. For changed browser flows, deploy to Kind and run `./scripts/test-kind-e2e.sh`. Run the SonarQube gate when the configured server is reachable.
5. Report actual results using [the pull request evidence format](../.github/pull_request_template.md). State skipped checks, risks, and decision owners. A CI result applies to its own revision; rerun after relevant code changes.

For an authorized advisory assessment of the brief, follow [Jev quality verification](jev-quality.md). Jev scores the quality of the supplied brief; it does not decide domain policy or certify the code.
