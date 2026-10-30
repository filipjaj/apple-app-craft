---
name: profile-swiftui-performance
description: "Diagnose and improve measured SwiftUI responsiveness using Instruments or equivalent project profiling. Use for scrolling hitches, slow updates, and excessive invalidation."
---

# Profile SwiftUI Performance

## Goal

Reduce the measured work that causes the user-visible responsiveness problem.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Define a reproducible interaction, representative dataset, device, and build configuration. Capture a baseline trace or clearly state if measurement tooling is unavailable.
2. Use SwiftUI update lanes to establish whether SwiftUI work coincides with the symptom. Correlate long updates with Time Profiler; consider both update duration and cumulative update count.
3. Find expensive computation and repeated formatting in view evaluation. Reuse expensive helpers or cache derived results only with clear invalidation inputs.
4. Trace why views were invalidated using the cause/effect graph when supported. Inspect changed properties, executed updates, creation events and skipped updates separately, including their downstream work. Derive narrow display values outside children that otherwise read broad bindings. Use Observation where shared ownership and deployment support justify it; local State and useful bindings remain appropriate.
5. Inspect stored escaping view-builder closures when their captures repeatedly change with a parent. When the builder needs only immediate construction, evaluate it in the initializer and store the resulting view rather than the closure. Preserve genuinely deferred builders and event actions; verify their lifetimes and current captured values. Avoid an equality shortcut that ignores meaningful behavior changes.
6. Keep hot scroll/timer/geometry writes away from broad parent reads and frequent scalar environment writes. A stable observable reference can carry data directly or through the environment, with only affected views reading its changing property. Alternatively isolate local State in a small view. Skipped body updates still incur comparisons; use the trace to establish their cost.
7. Make the smallest change supported by the trace. Record the same interaction again under comparable conditions; verify the expected work disappeared and behavior stayed correct.

## Verify the outcome

- Compare before/after traces with identical interaction, data, and configuration.
- Report measured quantities and artifact paths; separate hypotheses from measured gains.
- Check scrolling, selection, and updates for visual or correctness regressions.

Do not assert that extracting views, adding caches, or choosing lazy containers improved performance without a measurement.

## Additional source decisions

Interpret sampling against the reproduced journey: brief work may be missed, CPU resource weighting differs from elapsed-time profiling, and main-thread waiting differs from execution cost. Reuse expensive stable formatters with correct invalidation. Lazy containers and compiler/linker flags are measured choices, not universal repairs; debug-only inspection APIs must be removed from shipping code.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
