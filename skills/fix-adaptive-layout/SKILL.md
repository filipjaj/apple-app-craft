---
name: fix-adaptive-layout
description: "Repair SwiftUI clipping, truncation, alignment, or unstable measurement; implement layouts that adapt to content, window size, and Dynamic Type."
---

# Fix Adaptive SwiftUI Layout

## Goal

Keep essential content and actions usable as space and text size change.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Reproduce the layout problem using the actual content, container width, text size, and locale. Inspect modifier order and the size proposal/report/placement chain.
2. Identify which child wants space and which modifier constrains it. Use intrinsic sizing, baseline alignment, appropriate layout priority, fit/fill image behavior, and overlays whose decoration should not dictate size.
3. Prefer adaptive built-in containers and alternative arrangements over device-specific dimensions. Use ViewThatFits when there are meaningful arrangements in preference order.
4. Choose eager Grid for coordinated cell measurement and lazy collections for deferred creation when those tradeoffs fit the content. Reach for custom Layout only when standard composition cannot express the needed relationship.
5. For a custom layout, handle unspecified proposals, nonzero bounds origins, child spacing, and stable identity. Avoid feeding repeated geometry measurements back into parent sizing; cache only demonstrated repeated work.

## Verify the outcome

- Inspect narrow and wide windows, long localized strings, and accessibility text sizes.
- Essential text and controls remain reachable without overlap or unwanted clipping.
- Change arrangement while checking that selection, focus, and row state survive.

Do not solve overflow by shrinking all text, disabling Dynamic Type, or hard-coding one device’s dimensions.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
