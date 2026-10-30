---
name: refine-app-brand
description: "Improve an Apple app\u2019s visual identity through content, typography, color, symbols, and interaction while keeping familiar native controls."
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

## Keep identity maintainable

When identity spans repeated custom surfaces, consolidate the actual repeated values into semantic roles for text, accent, on-accent content, surfaces, selection, and motion. Preserve existing tokens and native adaptability. Components consume role names rather than raw palette entries; inspect accent text separately from text on accent fills across supported appearances and contrast settings.

Document the few rules that explain token use in the project's existing design notes. Add a state gallery only when it helps verify reused custom parts. Introduce an accent picker, custom chrome, or new theme setting only when the product calls for it. For a named reference, use its measurable relationships while keeping the user's own identity and usable native controls. [Adaptation provenance](../apple-app-craft/references/bama-source.md).

## Verify the outcome

- Inspect key screens in light/dark appearance and large text.
- Check that people can identify primary actions without knowing the brand.
- Verify custom symbols retain platform action meaning and motion remains responsive.

Do not use repeated logos, blanket tinting, or custom typography at fixed sizes as a substitute for hierarchy.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
