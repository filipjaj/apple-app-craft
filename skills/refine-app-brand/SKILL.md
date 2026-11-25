---
name: refine-app-brand
description: "Improve an Apple app\u2019s visual identity and design system through SwiftUI tokens, imagery, typography, color, symbols, and interaction while keeping familiar native controls."
---

# Refine Native App Branding

## Goal

Make the app recognizably its own without making common tasks harder.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect the product’s purpose, audience, current brand assets, and representative screens. Identify the few characteristics that should carry across the experience.
2. Express identity primarily through content imagery, hierarchy, writing, and responsive motion. Preserve familiar navigation and action meanings.
3. Use semantic color roles for adaptable UI and reserve brand tint for meaningful emphasis. Design dark appearance intentionally and inspect actual content backgrounds.
4. Use system text styles or scale custom type with Dynamic Type. Make icons consistent and recognizable at small sizes; pair ambiguous imagery with labels.
5. Invest custom-component effort in a distinctive product interaction with a clear benefit. Refine that interaction without replacing standard controls throughout the app.

## Build an app-owned design system

Inventory repeated decisions in code and representative screens. Extend existing tokens into a small SwiftUI vocabulary for semantic color, type roles and spacing. Components consume roles. Check text on accent fills separately from accent text. Scale custom type with `Font.custom(_:size:relativeTo:)` and use `@ScaledMetric` where geometry follows text size. Support Increased Contrast and Reduce Motion when the design depends on color or animation. Migrate one real journey before expanding the vocabulary.

When the user points to Mobbin or another reference, use available reference tools or supplied screens to study hierarchy, density, action placement and pacing. Apply those observations to the app’s own palette, copy, type and assets. Keep reference screenshots in research. Use original mascot or illustration art when it supports a specific moment, such as onboarding or an empty state. Preserve accessible alternatives for meaningful images.

Review the rendered journey for repetitive card shells, decorative badges, empty gradients, mixed icon styles and filler copy. Retain elements that serve the task or express the app’s identity. Record token roles and state behavior in the project’s existing design notes. [Adaptation provenance](../apple-app-craft/references/bama-source.md).

Apple’s session supplies the component, content and typography principles. The token and reference workflow applies those principles to this collection. [Communicate your brand identity on iOS](https://developer.apple.com/videos/play/wwdc2026/251/).

## Verify the outcome

- Inspect key screens in light/dark appearance and large text.
- Check that people can identify primary actions without knowing the brand.
- Verify custom symbols retain platform action meaning and motion remains responsive.

Do not use repeated logos, blanket tinting, or custom typography at fixed sizes as a substitute for hierarchy.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
