---
name: verify-macos-app
description: "Verify a changed macOS app with build/test results, deterministic window captures, and exercised interactions tied to acceptance criteria. Use for a Mac release check or runtime/UI validation; a small source-only fix needs only proportionate checks."
---

# Verify a macOS App

Establish which user-visible claims the current app build actually satisfies. For verification-only requests, report failures without changing product code unless fixes were authorized.

## Map the project first

Inspect the actual package/project, scheme, test plan, build configuration, process model, supported macOS versions, and existing harness. Read the `swiftprobe` skill when installed and inspect available tool schemas for build/test calls; use an explicit project/worktree root. SwiftProbe is an optional external tool, not bundled here. When unavailable or lacking a needed capability, use project-native checks and report the substitution. Do not assume Bama's `build.sh`, launch flags, environment variables, or snapshot helpers exist.

## Verification loop

1. Map each acceptance criterion to a build result, meaningful unit/integration test, rendered capture, exercised interaction, or named manual check. Reuse still-current evidence for the same source and configuration. Read [the verification contract](references/verification-contract.md) when creating a capture harness or report.
2. Run the narrow build and tests appropriate to the change. Keep actual verdicts, test counts, source revision/state, configuration, and artifact paths. A zero-test run is a failure; a clean build alone establishes compilation.
3. When runtime fixtures are needed, isolate persistent data, preferences, window restoration, process identity, endpoints, and external side effects. Confirm isolation before seeding. Do not delete production stores, preferences, or saved application state to make a check pass. A single-instance utility may require a separate test identity or a supported harness; stop that check if safe isolation is unavailable.
4. For UI changes, render or capture affected pages and relevant sheets, panels, menus, and Settings in supported appearances. Hold fixture data, clock-dependent values, scale, window size, and focus conditions stable. Use the available supported capture tool; no global appearance changes are needed. Include active/inactive states when relevant.
5. Open the images and inspect clipping, blank content, hierarchy, alignment, contrast, long text, and state coverage. Compare with the chosen acceptance criteria/reference. Record capture limitations, including missing material rendering; do not remove valid focus rings to make an image look calmer. Diff metrics help localize changes but cannot prove behavior or accessibility.
6. Exercise changed actions: keyboard/focus, menus, cancellation/Undo, persistence after relaunch, and permissions or cross-app triggers where relevant. Start a changed observer/timer/background callback to expose runtime isolation failures, with a bounded completion condition. Internal command tests do not establish that external menu routing or a real global shortcut works.
7. Fix within the authorized scope and rerun affected checks. If the same result repeats without new evidence, change the diagnostic approach; after three unsuccessful repair rounds for one problem, record the blocker and continue independent checks. Stop when scoped acceptance passes or report precisely which checks remain unavailable.

## Report

Give each criterion a status: pass, fail, unavailable, or blocked, with evidence and any manual follow-up. Summarize what the captures show and separate compilation, tests, rendered output, interaction, accessibility, and measured performance. Never mark an unperformed check as passed. Committing, installing over a user's app, or launching a new milestone is not a verification requirement.

Workflow attribution: [Bama source and license](references/bama-source.md).
