# Vue frontend guidance

- Follow [repository guidance](../AGENTS.md) and [the frontend README](README.md).
- For substantial UI changes, use [OpenDesign](https://github.com/nexu-io/open-design) and update [DESIGN.md](DESIGN.md) with the reviewed prototype, interaction states, accessibility, and responsive decisions.
- Keep domain decisions and secrets in backend services. Treat API responses as untrusted and show useful loading and failure states.
- Keep `web/vite.config.ts`, the [OpenAPI contract](../docs/contracts/openapi.yaml), and the frontend guide aligned when the request path changes.
- After `npm ci`, run `npm run typecheck`, `npm run test:unit:coverage`, and `npm run build`; run `../scripts/test-kind-e2e.sh` against a ready Kind release for changed user flows. Record browser or accessibility checks only when performed.
