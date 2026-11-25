---
name: modernize-legacy-apple-app
description: "Migrate a legacy RxSwift/UIKit Apple app slice by slice behind an existing parity harness, with pinned release baselines and verifiable release candidates."
---

# Modernize a Legacy Apple App

## Workflow

Preserve the existing release branch and establish the exact last-shipped baseline. Find the project's existing parity harness and read its runbook and qualified scenarios before executing. Reuse its validation and capture mechanism. If none exists, characterize one affected journey on the pinned baseline using the project’s current test and capture tools. Treat that evidence as the limit of the parity claim.

1. Pin the shipped commit, build/toolchain, device and OS, fixture identities, and relevant account/service conditions. Use an isolated candidate checkout. Inspect existing baseline evidence before refreshing it. Record blocked or missing scenarios as coverage gaps.
2. Choose a single release-sized slice and set behavior contracts and explicit accepted differences up front. Preserve UIKit entry points, routes, data semantics and analytics. Move SwiftUI behind the existing boundary. Audit Rx subscription ownership, replay, cancellation, ordering and main-thread UI delivery before replacing a reactive chain. Map each behavior explicitly. A shared Rx stream can require explicit fan-out and replay when bridged to an async sequence. Tie subscription disposal to task cancellation and test that superseded flatMapLatest work cannot publish stale state.
3. Run the independently qualified source and UI scenarios on the candidate and compare to the pinned baseline in the same environment. Cover existing data with a supported upgrade path when the slice changes persistence. Verify semantic and behavioral contracts in addition to screenshots. Use SwiftProbe for supported Swift test operations. Diagnose infrastructure failure separately from product failure and rerun only the affected evidence.
4. Bind receipts to the tested candidate SHA and retain the diff, artifacts and blockers. Integrating, rebasing or replacing the candidate invalidates affected evidence. A green subset is a scoped claim. Keep the release candidate and rollback route explicit and run the release workflow only at the requested stage.

## Deliverable

Provide the retained candidate SHA and baseline, evidence receipts by scenario, coverage gaps, and the release or rollback route.

## Sources

The project’s modernization toolkit and [Use SwiftUI with AppKit and UIKit](https://developer.apple.com/videos/play/wwdc2026/272/?time=341) for interoperability. The parity and release workflow is adapted from an existing harness.
