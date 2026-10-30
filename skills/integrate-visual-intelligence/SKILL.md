---
name: integrate-visual-intelligence
description: "Integrate or improve Apple Visual Intelligence entity search and ranked results. Use when the system supplies visual or semantic content to discover app data."
---

# Integrate Visual Intelligence

## Goal

Return relevant app entities quickly from a supported visual-intelligence search request.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify the searchable entity types, visible result value and supported system APIs. Preserve account and content access rules; visual matching does not grant access to private app entities.

2. Implement the appropriate query representation for incoming semantic or visual content using the installed SDK. Resolve results to stable domain identity and avoid duplicating competing query registrations where the framework expects one combined query.

3. Return a small relevant result set ordered by useful similarity or task criteria. Match image sizes to the result layout and avoid downloading full-resolution resources for every candidate.

4. Keep local or server search bounded and cancellable. Validate returned entities and handle no matches, missing content and unavailable service with a useful result rather than fabricated matches.

5. Evaluate varied visual inputs, latency and ranking quality with realistic entities and supported devices. Distinguish successful query invocation from meaningful result relevance and permission-safe access.

## Verify the outcome

- Results are relevant, ranked and permission-safe.
- Entity identity and image sizes fit the presentation.
- No-match and cancellation paths remain useful.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
