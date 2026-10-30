---
name: adopt-liquid-glass
description: "Adopt or review Apple Liquid Glass in SwiftUI navigation and controls. Use for a requested design-system update or custom glass interaction, with target-SDK availability checks."
---

# Adopt Liquid Glass

## Goal

Create a clear floating control layer that remains legible over app content.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect target SDKs, deployment versions, and existing native controls. Build and review automatic system changes before adding custom material treatments.
2. Separate content from navigation and action surfaces. Remove conflicting custom sheet and toolbar backgrounds when native treatments already supply hierarchy.
3. Group related toolbar actions and reserve meaningful tint for priority, selection, or status. Keep persistent accessories separate from screen-specific actions. If adopting tab-bar minimization and a bottom accessory, adapt its content to the actual placement and verify both expanded and collapsed states; do not shrink controls or lose essential playback/status information to make them fit.
4. Use regular material for ordinary controls; consider clear treatment over rich media only when the foreground remains legible. Avoid glass-on-glass stacking and redundant scroll-edge treatments.
5. When custom glass is justified, verify current effect/container APIs and compose nearby controls with shared sampling and appropriate identity for transitions. Match nested shape geometry to comfortable padding. Provide compatible behavior for supported older targets.

## Verify the outcome

- Inspect scrolling over varied content and media in light and dark appearance.
- Check Reduce Transparency, Increase Contrast, and Reduce Motion.
- Verify standard and custom controls remain readable and hit targets remain usable.

Do not apply glass to every content card or approximate an unavailable API with arbitrary blur and shadows.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
