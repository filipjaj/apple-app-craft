---
name: protect-app-data-privacy
description: "Review or improve Apple app data access, privacy manifests, SDK data practices and consent-dependent flows. Use for implementation privacy work; not drafting legal advice."
---

# Protect App Data Privacy

## Goal

Collect and use only the data needed for the user’s chosen task, with accurate disclosure and enforceable choices.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Map the requested feature’s data sources, destinations, retention and third-party SDK behavior. Decide what is actually necessary. Prefer selective system pickers or limited/write-only access when they meet the task rather than requesting a whole personal-data library.

2. Request permissions in a contextual moment with a meaningful purpose string. Support denial, limited access, revocation and changes while the app is running. An entitlement or privacy manifest does not substitute for user permission or correct runtime handling.

3. Inspect required-reason API usage and actual SDK behavior, then declare only approved reasons that match the implementation. Check current Apple requirements and generated privacy reports; SDK signatures establish provenance, not permission to collect unrelated data.

4. Enforce opt-in and opt-out in the data flow itself, including queued work, derived data and server processing when relevant. Reduce unnecessary identifiers and logging, and separate diagnostics from personal content. Do not invent fingerprinting or mark a manifest compliant based solely on its presence.

5. Test the task with each relevant permission state and consent changes during pending work. Compare disclosures and manifests with observed behavior. Report verified implementation findings and any external policy or server action still required; preserve the user’s authorized scope.

## Verify the outcome

- The task uses the least data access that satisfies it.
- Permission changes and opt-out affect real data flows.
- Manifests and disclosures match actual app and SDK behavior.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
