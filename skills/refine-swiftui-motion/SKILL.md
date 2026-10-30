---
name: refine-swiftui-motion
description: "Improve SwiftUI transitions and state-driven animation for clarity, responsiveness, and reduced-motion support. Use for awkward timing, broken continuity, or intentional interaction polish."
---

# Refine SwiftUI Motion

## Goal

Use motion to explain a state change without delaying the task.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Identify the trigger, old and new state, and the relationship motion should communicate. Prefer existing system motion when it already expresses that relationship.
2. Choose an animation attached to the state change or scoped to a specific value as appropriate. Separate insertion/removal transitions from numeric content changes and continuous interpolation.
3. Preserve source and destination identity for continuity. Scope spring behavior so overshoot does not make text or precision feedback unreadable.
4. For multi-stage interaction define named phases and tune their sequencing separately. Add temporary tuning controls only when repeated parameter changes make them useful.
5. Update immediate gesture feedback and loading state synchronously before work that can suspend. Provide a reduced-motion behavior that preserves meaning and task completion.

## Verify the outcome

- Exercise interrupted and repeated interaction, reversal, and fast state changes.
- Check timing and identity on the actual flow, not only an isolated animation preview.
- Verify Reduce Motion and that motion does not delay input or obscure the result.

Do not animate every state change globally or use arbitrary delays to coordinate asynchronous work.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
