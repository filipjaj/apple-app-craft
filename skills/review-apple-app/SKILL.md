---
name: review-apple-app
description: "Review an Apple app or feature across its user journey, SwiftUI implementation, and native interaction quality. Use for an explicitly requested broad review; report evidence and prioritized fixes."
---

# Review an Apple App

## Goal

Find the most consequential obstacles to a reliable, understandable app experience.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Identify review scope, supported devices, current code or diff, and intended user task. Inspect available builds, screenshots, tests, and source. State evidence limitations without inventing runtime observations.
2. Trace the primary task end to end. Check orientation, action hierarchy, navigation continuity, empty/loading/error states, recovery, and content legibility.
3. Follow data ownership and stable identity through the relevant views. Inspect async boundaries, persistence errors, and expensive work only where the implementation or symptom makes them relevant.
4. Check accessible semantics, scalable layout, and familiar control behavior. Use actual rendered or assistive-technology evidence when available; source inspection alone cannot establish usability.
5. Report findings by user impact with a precise location, trigger, observed or inferred failure, and smallest useful correction. Distinguish defects from design alternatives. If fixes were requested, implement and verify the agreed scope.

## Verify the outcome

- Every finding has inspectable evidence and a concrete consequence.
- Prioritize blockers and state/data failures before cosmetic preferences.
- List checks performed and untested behaviors; report no findings when evidence supports that result.

Do not claim profiling, VoiceOver, or device checks were performed when only code or screenshots were available.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
