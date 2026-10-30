---
name: compose-swiftui-effects
description: "Implement a requested SwiftUI graphics effect by composing layout, shader inputs, timing, and content state. Use for custom visual effects rather than routine UI styling."
---

# Compose SwiftUI Graphics Effects

## Goal

Build an understandable graphics pipeline with controlled cost and readable content.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Break the supplied effect into layers and state which data and transformation each needs. Use ordinary composition where it can express the effect before introducing shaders.
2. Choose color, distortion, or layer sampling based on the required transformation. Verify supported shader signatures and deployment availability before implementation.
3. Keep shader computation stateless and provide explicit varying inputs such as time. Make sampling bounds and clipping deliberate; avoid unintended per-frame work outside the rendering stage.
4. Drive semantic emphasis and scrolling from the actual content state. Use overlays for attached decoration and alignment relationships rather than unexplained offsets.
5. Keep background-capable geometry/effect closures independent of mutable isolated state. Pause decorative schedules when no longer useful and provide reduced-motion or compatible fallback behavior.

## Verify the outcome

- Check layout, clipping, text legibility, and graphics output at varied sizes.
- Inspect rendering cost and responsiveness on a relevant device.
- Exercise pause/resume, state changes, and accessibility preferences.

Do not hide a shader behind a monolithic view or treat visual fidelity as proof of acceptable runtime cost.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
