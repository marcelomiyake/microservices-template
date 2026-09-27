# Frontend design handoff

This starter screen is a simple implemented baseline. No OpenDesign prototype review is recorded for it. Generated PoCs should replace this handoff with their actual design evidence.

## User flow

The browser opens a status page, requests the example message through the web API, and shows either the response or a retry action after failure.

## Visual language

The sample uses a narrow centered layout, system typography, a light neutral background, teal action color, and a single response card. These are starter choices, not a product design system.

## Interaction states

- Loading: connecting message while the request is pending.
- Success: display the response text.
- Error: explain that both Rust services must run, then offer Retry.

## Accessibility and responsive behavior

The response card uses `aria-live="polite"`; the retry control is a native button with a visible focus ring. The layout fits narrow screens through a fluid heading and page width. A formal accessibility audit has not been recorded.

## OpenDesign review

For substantial UI work, use [OpenDesign](https://github.com/nexu-io/open-design) with `web/` as the working directory. Refine the flow and visual states in a rendered prototype, review it, then implement the accepted design in Vue. Record the prototype location, date, decisions, and any unavailable steps in [frontend design workflow](../docs/frontend-design.md) and a verification record. OpenDesign output is design-time material, not a runtime dependency or proof of working API behavior.
