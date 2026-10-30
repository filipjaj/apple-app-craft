---
name: test-swift-behavior
description: "Add or improve meaningful Swift unit and integration tests, using Swift Testing where supported and preserving the project\u2019s existing UI and performance checks."
---

# Test Swift App Behavior

## Goal

Prove a user-relevant invariant or failure recovery with isolated, repeatable tests.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect the current test framework, runner, target configuration, and failure. State the behavior to prove and choose the narrowest layer that can observe it.
2. Use isolated fixtures per test. Assert observable outcomes, not private implementation steps. Use required prerequisites only when continuing would produce meaningless failures.
3. Parameterize genuinely different input cases so their results are independent. Include boundary and recovery cases that could plausibly fail in the feature.
4. For asynchronous behavior use controlled dependencies and explicit completion conditions rather than arbitrary sleeps. Avoid shared mutable fixtures that depend on serial execution.
5. Use Swift Testing APIs supported by the installed toolchain. Preserve XCTest UI/performance or other existing checks where required; migrate unit tests incrementally and keep assertions within their own framework.
6. For supported build/test work use SwiftProbe first when available, inspect its schema, verify the intended root, and use explicit-root CLI calls if MCP root differs. Discover actual Xcode scheme, configuration/test plan and simulator UUID; set an appropriate timeout and keep the verdict and artifacts. Use native project commands for unsupported checks.

## Runtime boundaries on Mac

Map acceptance criteria to the narrowest sufficient evidence. Pure logic tests, a running-app integration/self-test, external menu/focus checks, and a real system trigger establish different claims. Exercise changed background callbacks or observers in a bounded runtime smoke check when source changes can introduce isolation or lifecycle faults; compilation alone will not expose every callback crash.

For menu bar or single-instance apps, inspect whether a hosted test starts a competing process before choosing the harness. Prefer isolated logic tests for pure code, and a dedicated test identity or supported runtime harness for app behavior. Isolate data, preferences, restoration, and endpoints; never clear production saved state to unstick a test. A debug bridge remains opt-in and does not justify adding production CLI/MCP support. Use `verify-macos-app` when broader Mac verification is needed. [Adaptation provenance](../apple-app-craft/references/bama-source.md).

## Verify the outcome

- Run the relevant test selection and confirm failure is informative.
- Run independently and with the intended suite to catch shared-state dependence.
- Retain runner verdicts and artifact paths; distinguish unit coverage from actual UI/device evidence.

Do not rewrite correct project test infrastructure or call a source-pattern check a behavior test.

## Additional source decisions

Keep XCTest where the project needs UI automation or performance APIs; use Swift Testing for appropriate supported unit tests. Preserve meaningful parameter pairings, isolate parallel-test state and halt only when a failed precondition invalidates later assertions. Use stable automation identifiers without changing spoken labels. Supported App Intents testing can exercise a real integration boundary, but does not prove all Siri or device behavior.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
