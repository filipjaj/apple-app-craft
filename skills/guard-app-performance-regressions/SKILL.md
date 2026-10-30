---
name: guard-app-performance-regressions
description: "Add or improve repeatable Apple app performance checks around a critical user journey, with scoped UI measurements, representative devices, baseline comparisons and trace-based regression triage. Use for performance regression testing and build-system changes; not ordinary functional test coverage."
---

# Guard App Performance Regressions

## Goal

Catch meaningful slowdowns in a critical user journey and produce enough evidence to diagnose them before release.

## Working context

Inspect the actual deployment targets, SDK, project conventions, and available profiling tools. Resolve framework/API details with Context7 and query the relevant concept; use current official Apple documentation when coverage is insufficient. Read [source lessons](references/source-lessons.md) for timestamped reasoning. Preserve the requested scope and supported systems. Capture evidence before changing code; report unavailable device/tool checks clearly.

## Workflow

1. Choose the user journey and define start/end boundaries that reflect useful readiness, such as launch-to-usable or tap-to-effect-ready. Select metrics and acceptance thresholds appropriate to the app. Tail latency may matter; do not copy Snap’s P90 choice or estimate a population percentile from a handful of runs.

2. Use the existing test runner and measurement pipeline. Add low-overhead named intervals/counters or OSSignposter when needed to connect the app operation with Instruments. Preserve interval identity across overlapping work and end/failure paths. Prefer native measurement facilities over introducing a new tracing service merely because the case study has one.

3. Separate scenario preparation from the measured operation for each iteration. Reset data/state, establish readiness, then trigger and wait for the actual completion condition. Keep login, tab loading and fixture setup outside the interval unless they are part of the measured user journey. Match signpost and profiler intervals to the operation; use XCTest metrics and measurement options supported by the SDK.

4. Compare baseline and candidate under matched release/profile builds, device/OS classes, datasets and thermal conditions. Separate cold/warm paths and collect enough repeats to characterize variance. Group results by device/configuration, retain raw samples and failed iterations, and do not hide a regression by pooling unlike devices or silently dropping outliers.

5. For a repeated meaningful slowdown, capture an Instruments trace over the same measured operation. Distinguish on-CPU work from waiting, I/O or lock contention before proposing a fix. Compare call trees and thread state; for toolchain/build changes inspect effective optimization flags, generated code and linked artifacts even when source and visible settings look unchanged.

6. Complete the scoped test or repair and integrate it with existing CI only as authorized. Record the baseline, thresholds, statistical uncertainty, artifact paths and actual verdict. Verify functional completion as well as timing. Use real iOS/device measurements for performance claims; simulator or headless success has a narrower meaning.

## Verify the outcome

- The measured interval excludes unrelated setup and ends at actual user-visible readiness.
- Keep per-configuration samples, baseline provenance, variance and reproducible trace artifacts.
- Investigate repeatable build/toolchain regressions even when application source is unchanged.
- Report unavailable device runs and distinguish authored tests from executed measurements.

Do not make noisy single-run results a release gate, assert P90 from insufficient samples, or recreate Snap’s bespoke infrastructure without a project need.

## Additional source decisions

For supported MetricKit or equivalent telemetry, establish subscriptions at the required lifetime and retain their owner. Compare the same meaningful operation and environment over time. Real-device hangs and extension/system scheduling need separate evidence from a simulator microbenchmark; gate newer metrics APIs against the actual deployment target.

## Deliverable

Leave the scoped implementation or actionable review. Report changed behavior, baseline and candidate evidence, actual checks and limitations; distinguish a measurement plan from executed results.
