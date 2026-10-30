---
name: build-storekit-purchases
description: "Build, review, or repair Apple in-app purchases and subscriptions with StoreKit, including transaction verification and lifecycle testing. Use for entitlement behavior and purchase UI, not acquisition copy alone."
---

# Build StoreKit Purchases

## Goal

Grant and maintain the correct paid access across purchase, renewal, cancellation and recovery.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify the product types, storefronts, supported systems and existing entitlement authority. Load actual product metadata and show price, duration and terms consistently. Check current program and API availability before using newer billing plans, group subscriptions or retention messaging.

2. Handle verified success, unverified results, pending approval, cancellation and errors distinctly. Grant access only under the app’s verified entitlement contract. Deliver content durably and idempotently before finishing a transaction; a button tap or local Boolean is not proof of ownership.

3. Observe transaction updates for the appropriate service lifetime and reconcile unfinished transactions and current entitlements at launch. Handle expiration, revocation, refunds and account changes, including other valid entitlements such as shared access. Make server reconciliation and notification handling idempotent when the product uses a backend.

4. Provide understandable restoration and purchase recovery, following current StoreKit guidance for explicit user-initiated synchronization. Avoid retry loops that create repeated purchases. Present offers only when eligible and preserve a clear cancellation path; fallback retention messaging must still be truthful.

5. Test with StoreKit configuration, sandbox and appropriate beta distribution, recording their different scope and accelerated subscription behavior. Cover interrupted delivery, pending completion, refunds, renewal failure, grace periods and reinstall. Do not claim production billing is verified by local tests or publish commerce configuration without authorization.

## Verify the outcome

- Verified transactions grant access exactly once.
- Later lifecycle events update access correctly.
- Failure and pending states remain recoverable and understandable.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
