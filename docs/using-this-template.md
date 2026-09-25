# Use this template for a PoC

The starter provides a working Kind path and documentation structure. GitHub generates a new repository from the default branch without carrying this repository's commit history. This source repository is marked **Template repository**; an admin can set the same option on a fork by following [GitHub's instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository).

## First pass

1. State the actual problem, audience, success criteria, and local/demo limits in the root README.
2. Decide the first bounded context and who owns each request, event, and piece of state. Keep one Rust service if the problem does not yet require more; remove the sample second service if it adds no value, then update the Helm chart.
3. Rename or replace sample packages and directories. Search for `example-service`, `web-api`, `/example`, `microservices-poc-web`, and this repository's name before finalizing.
4. Update Cargo members, npm metadata, Dockerfiles, Helm image and Service names, Nginx/Vite proxies, environment variables, HTTP contract, component READMEs, and scoped agent guidance together.
5. Replace the sample system design with the implemented architecture. Use ADRs for meaningful decisions, including data stores, queues, and deployment; do not turn the template's choices into unexplained universal rules.
6. Keep Kind deployment runnable. Document requests and limits for every chart container, including dependencies and init containers. Add a database model only when the project owns a schema, and document PVC retention before adding state.
7. Run checks and deploy to Kind, then create a verification record with the revision, environment, exact commands, outcomes, and gaps. Add real UI screenshots only after running the app.
8. Use OpenDesign for substantial Vue design and maintain `web/DESIGN.md` with the reviewed prototype and interaction states. Run Vue unit/component tests and a real Kind Playwright flow.
9. Rename the three SonarQube project keys, generate current per-component coverage, and run the server quality and duplication gate. Configure tokens outside the repository. Record any unavailable analysis as incomplete.
10. Use a DDD agent brief for domain changes and, when authorized, Jev for advisory quality verification. Keep score evidence tied to the generated project's revision; do not copy this template's results as the new project's results.
11. Use Conventional Commits for history. Remove unused templates or sections if they make the project harder to navigate, and keep the documentation index in sync.
12. Verify the copied [GitHub Actions workflow](../.github/workflows/validate.yml) on the new repository. Require its local-checks and Kind E2E jobs for branch protection once they pass. Configure a network-reachable SonarQube server separately if its gate must run in CI.

## Interface discipline

For every new service boundary, record the owner, producer, known consumers, authoritative schema or OpenAPI source, validation, errors, timeout, retry, and compatibility behavior. Keep browser credentials out of Vue code. Do not infer durability, idempotency, or production capacity from the sample.

## Publishing and repository settings

The checked-in starter contains no Git LFS objects. Before marking a repository as a GitHub template, ensure any future assets also avoid Git LFS. Publishing or changing the GitHub template setting requires repository admin access. GitHub copies files and structure; repository-specific secrets and deployment settings need separate setup.
