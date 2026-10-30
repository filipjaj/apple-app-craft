---
name: verify-app-attestation
description: "Implement or review Apple App Attest client/server flows, assertions and replay protection. Use for app integrity and abuse signals, not user authentication or a general privacy audit."
---

# Verify App Attestation

## Goal

Use server-validated app integrity signals to reduce abuse without blocking legitimate users indiscriminately.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Define the specific protected server operation and current abuse threat. Check device support and existing authentication. App integrity is a risk signal and does not establish the user’s identity or replace authorization.

2. Generate and associate the app’s attestation key with server-issued challenges using supported APIs. Validate attestation on the server against Apple’s current verification procedure, expected app/environment identity and challenge. Store the resulting key association securely.

3. Bind assertions to the exact request and a fresh challenge. Verify signatures and anti-replay counters on the server, with concurrency and duplicate-request handling that preserves the required monotonic contract. Do not trust a client-supplied success flag.

4. Handle unavailable service, unsupported devices and invalid keys using documented recovery and a bounded, server-informed retry strategy. Keep attestation setup out of critical user journeys when feasible, and distinguish a temporary failure from evidence of abuse.

5. Test valid, invalid, replayed and mismatched assertions plus reinstall/key lifecycle and outage behavior. Roll out enforcement using an explicit risk policy and measured legitimate-user impact; do not blanket-deny everyone who lacks an attestation signal.

## Verify the outcome

- Server verification binds the signal to the expected app and request.
- Replay and wrong-environment assertions fail.
- Outages and unsupported devices follow an explicit risk policy.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
