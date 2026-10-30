---
name: design-native-controls
description: "Choose and specify controls, feedback, gestures, and presentation behavior for an Apple app interaction. Use when an interaction model is undecided or a custom control needs a complete behavior contract."
---

# Design Native Control Interactions

## Goal

Make an interaction understandable, predictable, and usable through equivalent input methods.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Describe the person’s intent and domain state: choose one item, toggle a condition, adjust a value, trigger an action, or navigate. Identify value bounds, selection cardinality, commitment timing, and cancellation.
2. Choose a native control whose behavior matches those semantics. Style it before replacing it. Justify custom interaction with a concrete product benefit rather than appearance alone.
3. Specify resting, focused, pressed, selected, disabled, loading, success, and failure states where relevant. Decide when changes commit and whether users can undo or cancel. Immediate feedback must not imply success before work completes.
4. Place persistent and contextual controls at the scope of their effects. Distinguish navigation from mutation; keep related actions grouped and primary actions identifiable without tinting everything.
5. For gesture-rich or custom controls, define purpose, value, actions, feedback, and a non-gesture path to each essential operation. Use independent actions for independent axes. Consider keyboard, pointer, VoiceOver, and alternate input according to the targets.
6. On iPadOS 26 and later, check pointer tracking and individual hover targets in control clusters. Prefer supported system hover behavior; remove assumptions about the older magnetic pointer without shrinking touch targets. Verify custom effects by touch and pointer, and ensure hover is not the sole indicator of essential state.
7. Produce an interaction specification or implement it within the request. Describe observable transitions and boundary behavior so rendering and accessibility implementation share one contract.

## Verify the outcome

- Exercise bounds, repeated activation, cancellation, disabled state, and delayed/failing work.
- Verify labels and visual feedback accurately predict the outcome and current value.
- Check each essential operation with relevant alternate input; record untested device behavior.

Do not use a gesture-only shortcut as the only path to an essential action or add confirmation to every reversible change.

## Deliverable

Leave the requested design artifact, evidence-based critique, interaction specification, or implemented change. Explain the important decisions, checks performed, and remaining uncertainty.
