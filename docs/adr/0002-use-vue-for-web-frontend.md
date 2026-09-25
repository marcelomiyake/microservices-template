# ADR-0002: Use Vue for the web frontend

- **Status:** Implemented for template baseline
- **Recorded:** 2026-09-25
- **Decision owner:** Template maintainer

## Context

The requested PoC template needs a browser UI. The reference projects use Vue with TypeScript, and the starter only needs a small interactive page.

## Options

| Option | Benefit | Cost |
| --- | --- | --- |
| Vue 3 with TypeScript and Vite | Aligns with the reference projects; simple single-page starter | Node toolchain and separate build |
| Server-rendered HTML | Fewer build tools | Does not meet the requested Vue baseline |

## Decision

Use Vue 3, TypeScript, and Vite without a UI or state-management framework. The browser calls only the web API, keeping service details out of UI code.

## Consequences and evidence

The [Vue app](../../web/src/App.vue) and [Vite config](../../web/vite.config.ts) implement this choice. Revisit if a generated project's routing, accessibility, or deployment needs call for different tooling.
