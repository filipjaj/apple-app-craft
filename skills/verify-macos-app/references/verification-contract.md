# Verification contract

Use existing harnesses before adding one. A new harness is warranted when repeated runtime or visual checks are required and current tooling cannot establish the requested behavior.

## Harness invariants

- Explicit test mode redirects the complete state boundary: data and sidecar files, preferences, restoration, endpoints, external writes, and process identity where required. An environment variable does nothing unless source code actually reads it.
- Seed only the isolated store. Fixtures represent user-creatable states: empty, normal, long content, missing media, selection, error/recovery, and dense data when relevant.
- Enumerate relevant surfaces by stable identity. Await readiness or a bounded completion signal, not an arbitrary sleep.
- Capture at known point/pixel dimensions and scale; record appearance and focus. Retain native keyboard focus behavior. Do not assume inactive windows are invalid: they are a distinct state.
- Exit deterministically, including open sheets and cancellation. Return failure for missing captures, failed checks, or an incomplete run. Keep partial diagnostics after a crash.
- A bridge self-test validates its command path. External menu enabled-state/focus checks and actual global shortcuts require their own observed runtime evidence.

## Evidence record

| Criterion | Method | Result | Evidence | Limitation |
|---|---|---|---|---|
| Example: completing an item survives relaunch | Integration + runtime relaunch | Pending until run | Verdict/log artifact | Snapshot alone cannot prove persistence |

Record the source state (commit plus uncommitted diff when applicable), configuration, fixture, platform/tool versions, and artifact paths sufficient to reproduce the check. Keep logs and private traces out of public deliverables unless inspected and appropriate. Do not widen a small change into an all-surface screenshot campaign; a milestone check can cover the whole primary journey.
