---
name: design-app-interface
description: "Design or redesign Apple app screens with deliberate content hierarchy, typography, spacing, color roles, and complete UI states. Use after the product journey is known; for critique of existing designs use review-app-design."
---

# Design an App Interface

## Goal

Turn a defined user task into a coherent, implementable screen design.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect the task, existing journey, real content, brand constraints, and target devices. Preserve an established product direction. Identify the information needed for the next decision and the action that completes it.
2. Create the content hierarchy before styling: primary information, supporting context, primary action, and secondary actions. Choose lists for scan-oriented structured content and collections for visual items when that fits the task.
3. Compose a first screen using familiar navigation and controls. Specify semantic text roles, color roles, alignment relationships, and spacing tied to grouping. Do not impose a universal numeric spacing scale on an existing design system.
4. Apply identity through content, imagery, purposeful type, and restrained emphasis. Keep functional surfaces distinct from content, and keep text legible over media.
5. Design the screen’s populated, empty, loading, error, selected, and disabled states where applicable. Include a useful recovery path and long-content examples; avoid a polished happy path with missing behavior.
6. Produce the requested artifact: a concrete annotated design when planning, rendered alternatives when exploration is requested, or implemented screens when building. Compare alternatives by task clarity and effort, then refine the chosen direction.

## Shared parts and reference fidelity

Reuse established semantic tokens and component styles. For repeated custom UI, name raw palette/scale values separately from semantic roles and let components consume the roles. Add only tokens the screens actually need. A component gallery is useful when repeated custom controls have hover, pressed, focused, selected, disabled, or error states that need review; do not build a gallery for a single standard control.

When adapting a reference, measure important pane widths, row pitch, alignment, text roles, and state differences using `capture-reference-app` when available. State the chosen fidelity goal and capture conditions. Preserve control semantics, focus, and accessibility when translating to native UI. Apply the project's spacing system; do not impose a universal grid, hide a valid focus ring, or treat a pixel-diff percentage as a usability verdict. [Adaptation provenance](../apple-app-craft/references/bama-source.md).

## Verify the outcome

- Check whether each screen makes location, available actions, and next steps apparent.
- Inspect actual content at narrow/wide widths, larger text, and light/dark appearance.
- Verify hierarchy survives missing media and long labels; distinguish rendered evidence from a proposed design.

Do not start from decoration, reuse one generic card layout for every content type, or silently invent extra screens.

## Deliverable

Leave the requested design artifact, evidence-based critique, interaction specification, or implemented change. Explain the important decisions, checks performed, and remaining uncertainty.
