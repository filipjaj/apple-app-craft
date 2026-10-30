---
name: synchronize-app-data
description: "Implement, review, or repair Apple app CloudKit/Core Data sync, CKSyncEngine state or cloud-sharing behavior. Use for cross-device convergence; local schema modeling belongs to persistence work."
---

# Synchronize App Data

## Goal

Converge intended local and cloud data while preserving edits, account boundaries and sharing permissions.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Inspect the existing local store, cloud scope, record identity and ownership. Define merge rules and offline behavior before changing the sync mechanism. Retain native Core Data/SwiftData integration when appropriate rather than introducing a second sync engine over the same data.

2. For CKSyncEngine, durably persist the required engine state and local pending edits/deletions in the app’s storage. Register changes and provide batches according to current delegate semantics. Automatic scheduling is the default; explicit manual scheduling is useful for controlled tests, not a guaranteed wall-clock service.

3. Handle conflicts, deletions, partial failure and retryable server errors with deterministic merge rules. Reconcile sent/fetched events without losing edits made while a request was in flight. Use lightweight fetches and bounded materialization where large assets or object graphs are involved.

4. Handle iCloud sign-in, sign-out and account replacement explicitly. The engine can reset its internal pending state on account changes; protect local persistence according to account ownership so one person’s data is not uploaded into another account. Sharing permissions must be enforced by actual cloud/share capabilities.

5. Test two devices, offline edits, concurrent changes, delete/edit conflicts, app termination, account switching and read-only participants. Monitor error rates relative to traffic and platform rather than raw error counts alone. Report convergence evidence and remaining eventual-consistency limits.

## Verify the outcome

- Durable local edits survive interruption and reach the intended account.
- Conflict and deletion rules converge across devices.
- Account changes and sharing restrictions preserve ownership.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
