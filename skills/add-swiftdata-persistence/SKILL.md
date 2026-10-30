---
name: add-swiftdata-persistence
description: "Implement or repair SwiftData persistence, relationships, scoped queries, and error handling in an Apple app. Use to replace in-memory storage or fix unreliable saved state."
---

# Add SwiftData Persistence

## Goal

Preserve domain data across launches with predictable relationships and efficient reads.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Identify data that must survive relaunch, its identifiers, relationships, deletion semantics, and any existing stores. Inspect deployment requirements before choosing model features.
2. Map persistent types to the domain and serializable representation. Make relationship ownership and delete behavior deliberate; use inheritance only for genuinely stable shared structure supported by the SDK.
3. Connect the container and context at a stable scope. Replace duplicated in-memory repositories only after callers and needed invariants have been identified.
4. Fetch the collection needed by the view with predicates, sorting, and limits rather than loading every object and filtering later. Keep heavy media separate from lightweight list representation.
5. Handle creation and save failures with useful recovery. Preserve derived state such as timestamps and completion status. For existing user stores, identify schema changes and verify migration before changing production configuration.

## Verify the outcome

- Create, edit, delete, and relaunch using an isolated test store.
- Verify relationship delete behavior, filtering, ordering, empty results, and save-failure handling.
- Use an existing-store fixture for migration work; do not clear the user’s real store to make tests pass.

Do not silently replace existing user data, suppress save errors, or claim cloud synchronization from local persistence tests.

## Additional source decisions

Use queryable model types where they express the domain rather than treating Codable as a blanket schema escape hatch. Choose inheritance from real shallow/deep query needs. Resolve existing duplicates before imposing uniqueness, preserve history position for incremental processing, and test data from supported older schema versions before changing a live store. Custom stores and new schema APIs require actual SDK support and a specific need.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
