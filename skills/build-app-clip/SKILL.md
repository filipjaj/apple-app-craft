---
name: build-app-clip
description: "Build, review, or improve a focused App Clip in an existing iOS app, including shared entry routing, capability restrictions, task completion and transition to the full app. Use for App Clip product and target architecture; use the specialized size or invocation workflow for those isolated problems."
---

# Build App Clip

## Goal

Let someone complete one contextual task immediately and continue in the full app without losing the task or its data.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. Resolve App Clips with Context7 and query the concept being implemented; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for dated evidence and current-rule distinctions. Preserve the user’s product direction and existing working behavior.

## Workflow

1. Choose the exact in-the-moment task or useful app demo, its invocation context, and what constitutes completion. Enter directly at the relevant content or transaction rather than replaying full-app onboarding. Keep the same functionality available in the corresponding full app; multiple experiences belong to one App Clip target, not a separate target for every venue.

2. Inspect the existing app’s architecture, targets, signing and supported iOS versions. Add or refine the App Clip target using the actual Xcode workflow. Share domain operations and required views while limiting target membership and dependencies. Refactor only the entry module that needs independent launch; a restaurant checkout example does not justify rewriting the entire app.

3. Use a common, typed invocation decoder and domain entry operation for the clip and full app. Read the browsing-web user activity’s webpage URL using the existing framework lifecycle, including resumed invocations. Validate permitted routes, parameter types, identifiers and available content. Treat links as untrusted input: a table or order ID is context, not authorization or a trusted price. Handle a missing URL, expired content and repeated invocation without crashing or repeating a purchase.

4. Review the current App Clip framework and entitlement restrictions before adopting full-app services. Successful compilation does not prove that a framework works in a clip. Check runtime availability for required operations, particularly App Intents, background activity, private/shared CloudKit storage and access to personal data. Use only capabilities needed for the chosen task and provide a useful fallback when unavailable.

5. Keep authentication and payment proportional to the task. Allow guest use when the product permits it; consider supported system authentication and payment flows where appropriate. When location confirmation is useful for physical invocation, distinguish confirmation from continuous location access and handle refusal or failure. Use ephemeral notifications only for a task that benefits from them, with current authorization semantics; do not request permissions merely because a clip can.

6. Preserve task results and continuity deliberately. Store ordinary continuation data in an agreed app-group container or shared defaults, and sensitive credentials in the keychain with supported parent/clip entitlements. Keychain sharing is directional: the clip cannot read the full app’s old secrets; full-app access to clip items starts at iOS 15.4. Revalidate authorization and account identity, distinguish duplicate items, and make migration idempotent. Never treat a stored user identifier as proof of authentication or put bearer secrets in defaults or invocation URLs.

7. Offer the full app at a useful moment without making installation a prerequisite to the promised clip task. The full app replaces the clip and receives later invocations, so exercise its equivalent entry path and recovery when clip data is missing or purged. Check launch, completion, denied permissions, interrupted work, upgrade and reinstallation with the project’s build/test tools, and separate code inspection from actual device checks.

## Verify the outcome

- A valid invocation reaches the intended task without unnecessary onboarding.
- The clip uses supported capabilities and handles absent URLs, refusal and unavailable content.
- Both targets run the same domain rules and resist unauthorized or repeated transactions.
- Upgrade preserves available task data and the full app handles subsequent invocations.

Do not copy the entire app into the clip, require installation to finish its advertised task, or assume local clip data and credentials are permanent.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, compatibility decisions, performed checks and remaining limits. Use the project’s required build/test tools (including SwiftProbe when configured); source review alone does not prove device or distribution behavior.
