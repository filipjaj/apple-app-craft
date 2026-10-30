---
name: optimize-app-rendering-power
description: "Measure and reduce battery cost from unnecessary Apple app rendering, especially Liquid Glass resampling, hidden animations, and scroll edge effects. Use for rendering-related energy problems; use profile-swiftui-performance for responsiveness bottlenecks."
---

# Optimize App Rendering Power

## Goal

Reduce measured rendering power while preserving visible updates, legibility, and essential background work.

## Working context

Inspect the actual deployment targets, SDK, project conventions, and available profiling tools. Resolve framework/API details with Context7 and query the relevant concept; use current official Apple documentation when coverage is insufficient. Read [source lessons](references/source-lessons.md) for timestamped reasoning. Preserve the requested scope and supported systems. Capture evidence before changing code; report unavailable device/tool checks clearly.

## Workflow

1. Define a reproducible screen state and interaction on a representative physical device in a release/profile build. Record the baseline with Power Profiler when supported; note device, OS, duration, thermal state, brightness, and relevant network activity. Whole-device power estimates need comparable conditions and attribution, not a promise about battery life.

2. Use Flash Updated Regions or equivalent rendering diagnostics to locate unexpectedly continuous work. Inspect covered content, idle states, sheets, custom effects, and animations beneath translucent surfaces. A region flashing is a clue about rendering; measure its energy impact separately.

3. Group nearby Liquid Glass elements of similar size in GlassEffectContainer when justified. Avoid combining a large sheet with small controls or distant controls across an animated region: the larger sampled area can add work. Retain native controls and meaningful visual grouping.

4. Pause or omit animations whose motion is not perceptible beneath a covering surface, and restore them when visible. Preserve domain updates and useful visible changes, such as a live count; do not stop a workout or data capture to hide its spinner. Verify sheet dismissal and rapid presentation changes.

5. For scroll views whose background is actually opaque, static, and solid, inspect scrollContentBackground(.visible) or the supported UIKit background treatment. Dynamic foreground content does not exclude this case; a dynamic or translucent background does. Preserve the intended appearance and scroll-edge legibility.

6. Record the same scenario after the smallest supported change. Compare matched steady-state intervals and repeat when noise obscures the result. Keep the traces and measured values, and inspect light/dark appearance, accessibility settings, and restored animations.

## Verify the outcome

- Compare device power under matched conditions; do not infer energy savings solely from fewer flashes or updates.
- Verify visible data remains live while imperceptible animation stops, and motion resumes when appropriate.
- Keep Liquid Glass grouping, scroll-edge legibility, and accessibility behavior usable.

Do not promise the workshop’s battery figures for another app or apply an opaque-background optimization to a background that is not opaque.

## Deliverable

Leave the scoped implementation or actionable review. Report changed behavior, baseline and candidate evidence, actual checks and limitations; distinguish a measurement plan from executed results.
