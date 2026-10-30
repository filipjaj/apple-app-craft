---
name: improve-app-search
description: "Design or repair Apple app search scope, placement, suggestions, filters, and result states. Use when finding content is confusing or a searchable feature needs implementation."
---

# Improve App Search

## Goal

Let people understand what they search and efficiently reach useful results.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Identify the searched domain, frequency of use, and whether entry is for discovery or immediate query input. Choose placement that communicates the scope on each target platform.
2. Preserve familiar field elements and editing behavior. Keep scoped search near its content; use a dedicated discovery surface only when its content serves the task.
3. Distinguish idle suggestions, loading, matches, no matches, and failure. Keep the current query visible. Offer useful recents and an accessible way to clear history when history is stored.
4. Begin broad and reveal meaningful refinement controls. Use explicit filters before hidden token-only workflows. Make active query and filters understandable and reversible.
5. Connect search to the actual data layer with scoped fetching where supported. For async results, cancel or reject obsolete requests so late responses cannot replace a newer query. Preserve current content where that improves continuity.

## Verify the outcome

- Exercise fast query changes, clearing, typos, filters, no matches, and failed requests.
- Verify result scope is consistent with where search appears.
- Check keyboard focus, large text, and accessibility labels for suggestions and filters.

Do not treat an empty query, no matches, and a network failure as the same state.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
