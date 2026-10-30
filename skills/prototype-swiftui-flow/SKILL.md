---
name: prototype-swiftui-flow
description: "Build or iterate a SwiftUI interaction prototype using realistic fixtures and rendered previews. Use to compare design alternatives or evaluate a flow before production integration."
---

# Prototype a SwiftUI Flow

## Goal

Produce a runnable prototype that answers a specific design question.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Name the design question and inspect the host app’s existing conventions, supported platforms, and preview setup. Keep the prototype’s scope explicit.
2. Build reusable sample models with believable short and long text, missing media, empty collections, and dense content. Keep mock services distinct from production dependencies.
3. When exploration is requested, create distinctly named alternatives that differ in hierarchy or interaction, rather than only color. When the user has selected a direction, implement that direction directly.
4. Compose standard SwiftUI components with data inputs and state-driven actions. Implement enough navigation, edits, loading, and recovery to evaluate the task.
5. Render the relevant previews or run the prototype. Use attached design artifacts to compare actual output. Refine the selected direction; add a tuning panel only when repeated interaction adjustments warrant one.

## Repeatable visual evidence

Reuse fixture-driven previews or an existing snapshot harness before introducing launch flags. Hold representative data, window size, scale, appearance, and focus conditions stable. Give relevant panels, sheets, menus, and error states their own capture identity when they answer the design question. Record the actual capture scale rather than assuming Retina is always 2x.

Keep prototype state isolated from live stores, preferences, and external effects. Do not disable keyboard focus to improve a screenshot. Inspect differences against the selected design question; pixel metrics cannot establish working behavior. For repeated Mac runtime checks use `verify-macos-app` when available. [Adaptation provenance](../apple-app-craft/references/bama-source.md).

## Verify the outcome

- Primary actions visibly change state and the flow can be completed.
- Inspect long text, empty and populated fixtures, narrow widths, and accessibility text sizes.
- Report which views were rendered and which interactions were exercised; label simulated behavior.

A screenshot of a preview does not demonstrate working navigation, persistence, or device behavior.

## Additional source decisions

Use realistic content and compare alternatives in the intended screen. A scoped tuning panel can make motion or layout decisions concrete; keep it isolated from production behavior. Treat agent-generated output as a draft requiring integrated review and the relevant app checks.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
