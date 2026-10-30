---
name: integrate-app-intents
description: "Expose Apple app entities and actions to system experiences such as Siri and Spotlight using App Intents. Use for entity lookup, indexing, direct opening, and conversational app actions."
---

# Integrate App Intents

## Goal

Make system-invoked actions resolve the same entities and obey the same domain rules as the app.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inventory useful entities and actions in the existing data layer, their stable identifiers, required parameters, and effects. Verify current SDK capabilities and supported schema domains.
2. Define entity lookup and dependencies against the real store. Use persistent identity for independently addressable entities and transient representations for contextual values without separate lookup.
3. Keep the search index synchronized on create, edit, and deletion. A declaration of indexed capability is insufficient without the actual indexing path.
4. Route opening and onscreen context through the app’s existing navigation. Implement mutations by resolving parameters and invoking domain operations rather than duplicating business rules.
5. For update actions distinguish omitted parameters from explicitly cleared values. Use supported schemas when they match the domain, and keep result views lightweight. Preserve authentication and confirmation behavior required by the action.

## Verify the outcome

- Exercise lookup, create, edit, open, and delete through the available system entry points.
- Test missing/deleted entities, omitted versus cleared values, and index updates.
- Verify the app and intent see the same results and errors; do not claim Siri support from compilation alone.

Do not invent schema domains, maintain a second app database, or treat intent invocation as permission to bypass domain rules.

## Additional source decisions

Keep entity identity stable across devices and process boundaries. Distinguish resolving existing content from importing content to create a new entity. Summaries must represent required inputs, and mutations must execute in the process with the relevant authority and storage access. New schemas or testing APIs require supported SDKs; system integration is only added when the requested app task needs it.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.

For the compact result or confirmation experience itself, read [design-interactive-snippets](../design-interactive-snippets/SKILL.md) when that task is in scope.
