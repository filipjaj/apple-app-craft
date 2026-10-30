---
name: handle-background-work
description: "Implement or repair Apple app background refresh or processing with BackgroundTasks and supported transfer APIs. Use for scheduler lifecycle and expiration, not ordinary foreground async work."
---

# Handle Background Work

## Goal

Finish useful deferred work when the system grants time and preserve a recoverable state when it does not.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify why the work belongs in the background, its required capability and supported platform APIs. Match refresh, processing or background transfer to the actual job rather than assuming a foreground Task continues after suspension.

2. Register the appropriate task identifiers and schedule requests using current project configuration. Treat earliest-start dates and system grants as opportunities, not exact alarms. Avoid polling or a promised completion time the OS cannot guarantee.

3. Own cancellation and expiration handling deliberately, checkpoint durable progress and mark task completion accurately. Finish or roll back partial mutations safely and reschedule only useful remaining work.

4. For supported background transfers, coordinate session callbacks and app refresh completion without keeping unnecessary process work alive. Check that the actual app/extension type supports the capability, particularly App Clips.

5. Test expiration, duplicate scheduling, app termination, offline work and resumed completion with real supported tooling. Report debug-triggered execution separately from naturally scheduled device behavior.

## Verify the outcome

- Expiration leaves durable and recoverable task state.
- Scheduling does not promise exact delivery.
- Completed and interrupted work are reported accurately.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
