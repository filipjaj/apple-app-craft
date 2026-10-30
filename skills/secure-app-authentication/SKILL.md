---
name: secure-app-authentication
description: "Implement, review, or improve passkeys and Apple AuthenticationServices account flows, including credential upgrades and recovery. Use for account authentication; App Attest verifies app integrity separately."
---

# Secure App Authentication

## Goal

Let the intended account sign in and recover access while maintaining server-verified identity.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Inspect the relying-party domain, server authentication design, account identifiers and supported systems. Preserve existing account linking and recovery rules. Configure the appropriate app/site association and request only profile fields genuinely needed for account creation.

2. Use a server-provided fresh challenge for registration or assertion and verify returned credentials on the server with current WebAuthn/relying-party rules. The client’s success callback is not an authenticated session. Bind the result to the intended account and challenge, and protect against replay and identity substitution.

3. Handle cancellation, unavailable credentials and cross-device sign-in without forcing biometrics or claiming that passkeys require one specific device method. Create passkeys for new accounts and offer supported upgrades for existing authenticated accounts without silently linking another person’s account.

4. Treat password retirement and other-factor removal as deliberate account lifecycle decisions with a working recovery path. Update credential-manager signals and metadata when supported. Recovery and credential-management URLs must handle unauthenticated arrival and return to the requested destination after sign-in.

5. Test new and existing accounts, multiple credentials, cancellation, reinstall, cross-device use and lost-access recovery. Verify server rejection of invalid or replayed results and safe session storage. Do not roll out account migration or remove production factors without authorization.

## Verify the outcome

- Server verification establishes the intended identity.
- Cancellation and unavailable credentials have useful recovery.
- Upgrade and recovery preserve account ownership.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
