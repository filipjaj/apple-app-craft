---
name: create-layered-app-icon
description: "Prepare or review layered Apple app-icon artwork and an Icon Composer handoff. Use for icon design, appearance variants, or project integration."
---

# Create a Layered App Icon

## Goal

Deliver an identifiable icon that survives small sizes, platform masks, and appearance changes.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect the existing identity and target platforms. Choose a clear central silhouette and use the relevant current Apple grid and template.
2. Separate background and foreground artwork by intended depth and material control. Simplify shapes and remove baked-in lighting that competes with system treatment.
3. Prepare scalable vector layers where possible, outline exported text, and use transparent raster layers where vector export is unsuitable. Leave final system masks out of layer artwork.
4. When Icon Composer is available, tune groups and material properties, then check light, dark, clear, and tinted variants. Adjust optical positioning for circular canvases.
5. Integrate the saved icon document using the project’s supported tooling. If the tool is unavailable, deliver source layers and explicit handoff instructions; do not claim to have produced or validated a native icon document.

## Verify the outcome

- Inspect small size, contrasting backgrounds, and moving-light previews when available.
- Verify silhouette and essential identity in monochrome/tinted appearances.
- Check actual target-device output after integration; a flattened preview is only a design artifact.

Do not fabricate a .icon file by renaming a raster image or bake a system mask into every layer.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
