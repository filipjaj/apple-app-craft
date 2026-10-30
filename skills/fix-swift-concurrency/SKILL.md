---
name: fix-swift-concurrency
description: "Diagnose and repair Swift actor isolation, Sendable errors, cancellation, and asynchronous work ordering; support incremental Swift language-mode migration."
---

# Fix Swift Concurrency

## Goal

Keep asynchronous work responsive and consistent without introducing unsafe sharing.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect compiler version, language mode, strict-concurrency settings, default actor isolation, and the relevant API annotations. Read the diagnostic as a boundary in runtime behavior.
2. Trace ownership and execution before adding annotations. Async suspension does not automatically move expensive CPU work off the main actor; profile the work and improve its algorithm before parallelizing.
3. Keep ordered operations together. Use structured concurrency for independent work and a task group for a variable workload, preserving identifiers or input order explicitly when completion order differs.
4. Keep UI updates in their isolation domain. Pass Sendable snapshots to background-capable SwiftUI closures or give independent operations their own mutable helper. Recheck assumptions after await because actor work may interleave.
5. Define cancellation and stale-result handling. Tie work to the appropriate lifetime and preserve consistency on cancellation. If migrating language mode, work target by target and separate broad refactoring from diagnostic fixes.
6. Use unsafe isolation/sendability escape hatches only with an explicit, verified runtime invariant; prefer expressing actual ownership or isolation. Do not blanket-suppress warnings or treat main-thread coincidence as actor proof.

## Verify the outcome

- Build affected targets under the actual isolation and language settings.
- Exercise cancellation, overlapping requests, navigation away, and out-of-order completion.
- Confirm expensive work no longer blocks the UI and shared state remains consistent.

Do not add detached tasks, unchecked Sendable, or assumeIsolated solely to silence the compiler.

## Additional source decisions

Preserve a documented cancellation contract, including whether partial results are possible and which short regions must finish or roll back. Set visible loading state before suspension. Read the actual Swift version, default actor isolation and execution settings: async alone does not offload CPU work, and older nonisolated execution descriptions are not universal current rules. Avoid blocking cooperative workers or claiming unsafe Sendable conformance as a fix.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
