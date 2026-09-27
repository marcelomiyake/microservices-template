# Vue frontend

This Vue 3/TypeScript app demonstrates the browser request path. It calls `GET /api/example` through the Vite development proxy and displays loading, success, and error states. It has no backend credentials or persistent state.

## Contract and owner

- Owner: `web`.
- API owner: `services/web-api`; see [OpenAPI contract](../docs/contracts/openapi.yaml).
- Parent architecture: [system design](../docs/system-design.md).

## Build, run, and verify

Start both Rust services first. From this directory:

```sh
npm ci
npm run dev
npm run typecheck
npm run test:unit:coverage
npm run build
```

Open the URL printed by Vite. Stop the server with Ctrl-C. The built `dist/` is ignored by Git. In Kind, the Helm chart runs this app with Nginx on port 8080, proxies same-origin `/api` to the `web-api` ClusterIP Service, and exposes it through loopback port forwarding. The Vite proxy applies only to optional process-only development.

After deploying to Kind and installing Playwright Chromium (`npx playwright install chromium`), run `../scripts/test-kind-e2e.sh` from this directory or the repository root. The test uses the real Vue → Nginx → web API → example service path. Keep design decisions and OpenDesign prototype review in [DESIGN.md](DESIGN.md); see [frontend design workflow](../docs/frontend-design.md). No OpenDesign review of the starter page is recorded.

[Project README](../README.md) · [Agent guidance](AGENTS.md) · [Documentation index](../docs/README.md)
