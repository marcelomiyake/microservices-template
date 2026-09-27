# Frontend design with OpenDesign

The frontend in each generated PoC should have a deliberate design handoff before substantial visual or interaction changes. [OpenDesign](https://github.com/nexu-io/open-design) is the design-time tool used by the reference projects. The template does not bundle or auto-install it.

## Workflow

1. Write the actor, task, states, accessibility needs, and responsive constraints in [`web/DESIGN.md`](../web/DESIGN.md).
2. Open OpenDesign from its official project and select this repository's `web/` directory as the working directory. Follow its current setup instructions for the installed version.
3. Prototype the flow, including loading, success, empty, error, disabled, and recovery states where relevant. Review the rendered prototype at desktop and narrow widths.
4. Record accepted decisions, prototype path/link, date, reviewer, and unresolved questions in `web/DESIGN.md`. If OpenDesign is unavailable, record that limitation and the alternative review performed.
5. Implement the accepted design in Vue. Verify keyboard/focus behavior, accessible names, responsive layout, unit states, and the real Kind browser path. Store genuine app screenshots only after running the UI.

The starter page has not been reviewed in OpenDesign. A prototype does not replace API contracts, tests, accessibility checks, or a working deployment. Keep generated assets and credentials out of source control unless the project intentionally adopts them.
