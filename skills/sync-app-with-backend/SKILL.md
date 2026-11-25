---
name: sync-app-with-backend
description: "Implement or repair offline-capable Apple app sync with the app's own backend, including local edits, server versions, conflict policy and account isolation."
---

# Sync an Apple App With Its Backend

## Workflow

Describe the authority per field and whether the feature is a read-only cache or editable replica. Keep the existing persistence layer when it can perform an atomic local update and outbox write. A SwiftData custom DataStore is a storage integration, not a sync protocol. Use existing backend endpoints and revisions if they can meet the invariants. If a writable API lacks conditional revisions or deduplication, define the supported contract before promising conflict-safe offline writes.

- Give each mutable entity a stable identity. Record pending mutations durably with idempotency keys and base revisions. Make the backend deduplicate retries and return an authoritative acknowledgement. Use client-generated IDs or an explicit server-ID mapping to handle create followed by offline edit or delete. Preserve parent-child dependencies and coalesce only operations whose semantics permit it. Version queued payloads across app upgrades. Apply acknowledgements without overwriting edits queued after the mutation. Atomically persist remote changes with the corresponding cursor.
- Choose explicit behavior for sequential and concurrent edits, deletes, tombstone expiry, and version gaps. Use server order or revisions where ordering is authoritative. Client clocks cannot safely resolve conflicts by themselves. Define when to full-resync while preserving pending local changes. Prevent remote merges from being emitted as fresh local edits.
- Keep cursors, queues and local views partitioned by account and environment. Cancel or fence in-flight writes on account switch. On expired authentication, pause the affected account queue and resume after refresh or sign-in. Retry transient errors without starving other records. Surface conflicts and permanent failures where user action helps. Use networking or background-work skills for transport and scheduling details.
- Verify offline edits on two installs, retry after a lost response, process death before and after acknowledgement, paginated pull, delete versus edit, and account switch during sync. Report convergence and surviving edits, including cases the backend cannot safely decide.

## Deliverable

Report the conflict policy and evidence that edits and deletes converge after offline use, retries, process death, and account changes.

## Sources

[Create a custom data store with SwiftData](https://developer.apple.com/videos/play/wwdc2024/10138/?time=290) for the storage boundary and [Track model changes with SwiftData history](https://developer.apple.com/videos/play/wwdc2024/10075/?time=318) for local history tokens. Read the app/backend contracts for actual sync semantics. Use synchronize-app-data for CloudKit and CKSyncEngine.
