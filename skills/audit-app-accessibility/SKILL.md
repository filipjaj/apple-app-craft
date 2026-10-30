---
name: audit-app-accessibility
description: "Audit or fix accessibility in Apple app flows and custom controls, including VoiceOver semantics, larger text, gesture alternatives, and system appearance preferences."
---

# Audit App Accessibility

## Goal

Let people complete the same essential tasks with different abilities and input methods.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Select a concrete task and identify the visual, auditory, motor, and cognitive assumptions it makes. Inspect actual controls and rendered output when available.
2. Preserve built-in control semantics through styling where practical. For custom controls expose purpose, current value, actions, and feedback; use adjustable actions for one-dimensional values and distinct actions for multiple axes.
3. Group related content when it improves navigation, while retaining separately actionable elements that people need. Hide decorative images and use specific labels only when defaults are misleading.
4. Provide alternatives to hover, drag/drop, and precise gestures. Expose finite destinations or gesture outcomes as actions. Direct touch should be deliberate and should not remove equivalent accessible operations.
5. Test the main task with VoiceOver and relevant alternate input, plus large text and appearance preferences. Avoid flooding announcements with intermediate values. Record inclusion gaps and implement the highest-impact corrections within scope.

## Verify the outcome

- Task completion is possible without relying only on color, hearing, or precise touch.
- Check focus order, names, values, available actions, and announcements after changes.
- Separate inspected semantics from actual VoiceOver, Switch Control, and device verification.

Source modifiers and screenshots cannot prove that assistive-technology navigation works.

## Additional source decisions

Evaluate complete critical tasks with the relevant assistive technology, including hover-only controls, custom gestures, drag/drop and long-form reading. Use meaningful custom actions when a single adjustable direction cannot represent the task. Automated audit exceptions need a specific rationale; previews and an audit pass alone do not establish Accessibility Nutrition Label claims.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
