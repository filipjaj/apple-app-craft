---
name: improve-ux-copy
description: "Write or improve Apple app labels, onboarding, empty states, errors, and confirmations. Use when wording affects task understanding, recovery, or product personality."
---

# Improve App UX Copy

## Goal

Make each message help the person decide or complete the next useful action.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Collect the actual strings and their UI context, audience, and triggered state. Establish the product’s purpose and a few stable voice attributes.
2. Keep voice consistent while adapting tone to the moment. Make onboarding explain a concrete benefit; let warmth support success without obscuring information.
3. Name actions by their outcomes. Distinguish empty content from no results, temporary loading, and failure. State what happened and offer a real recovery path.
4. Use direct factual language for consequential choices. Explain what will be lost or changed; avoid jokes, blame, jargon, and unsupported promises.
5. Update strings in the project’s localization system when implementation is requested. Keep placeholders, pluralization, and accessible labels consistent with their roles. Provide before/after examples for review-only work.

## Verify the outcome

- Read strings aloud and verify labels predict the actual action.
- Check constrained layouts and long translated text without hiding essential meaning.
- Ensure every recovery action exists and every factual claim is supported.

Do not promise a retry, undo, privacy guarantee, or success condition that the product does not implement.

## Additional source decisions

Keep consistent voice and terminology while adapting tone to the situation. Remove decorative interjections and politeness that add no meaning, but retain detail that people need for decisions, recovery or privacy. Check labels in their actual context and avoid mechanically replacing personality with shorter text.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
