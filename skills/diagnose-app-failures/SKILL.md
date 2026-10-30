---
name: diagnose-app-failures
description: "Investigate Apple app crashes, test failures, misleading debugger output or missing diagnostic context using Xcode reports, LLDB and structured logging. Use for diagnosis before a fix."
---

# Diagnose App Failures

## Goal

Find an app failure’s cause from reproducible behavior and relevant diagnostic evidence.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Capture the failing journey, expected behavior, exact build and environment. Preserve the original result bundle, crash log, reproduction and relevant symbols. Distinguish a test infrastructure failure, debugger display problem and product defect before editing code.

2. Use test report activities, screenshots and failure location to reconstruct what occurred. Check device/configuration differences and isolate the first causal failure rather than treating every downstream assertion as a separate defect.

3. Use targeted breakpoints, conditions and stack inspection to test a hypothesis. Account for optimization, missing modules and symbol paths before interpreting debugger output as corrupt data. Debugger expressions may execute code; prefer observation when execution would disturb evidence.

4. Add meaningful structured log categories and levels for the operation under investigation. Keep secrets and personal content private, and use correlation identifiers that do not expose account data. Remove noisy print debugging or scope it appropriately after the cause is understood.

5. Produce the smallest supported fix when requested, with a reproduction or meaningful regression check. Rerun under the original conditions and report actual results, artifacts and unresolved cases. Coverage or a successful debugger attachment alone does not prove the defect is fixed.

## Verify the outcome

- A supported causal explanation matches the observed failure.
- Diagnostics preserve useful context without exposing secrets.
- The original reproduction is resolved or its remaining blocker is explicit.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
