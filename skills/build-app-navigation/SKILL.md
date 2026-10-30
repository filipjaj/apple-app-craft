---
name: build-app-navigation
description: "Design or implement Apple app tabs, navigation paths, split views, deep links, and state restoration. Use for confusing routes, lost navigation, or new multi-screen flows."
---

# Build Predictable App Navigation

## Goal

Keep people oriented and preserve their place through exploration and focused tasks.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Map stable content areas, hierarchical destinations, and focused tasks. Use tabs for top-level destinations, pushes for deeper exploration, and presentations for self-contained tasks. Keep creation or mutation actions with their relevant content or toolbar rather than making them tabs; use explicit destination labels and familiar symbols so people can predict where each tab leads.
2. Model navigation using values and stable identifiers. Choose a typed path when the route domain is homogeneous; introduce heterogeneous paths only when useful.
3. Register destinations where the navigation container can discover them, outside lazy row creation. Keep separate histories where tabs or scenes need independent places.
4. Adapt split-view selection and detail history to collapsed widths. Resolve deep-link IDs through the current data layer; handle missing or deleted targets with an understandable fallback.
5. Restore identifiers rather than frozen model objects. Scope restoration per scene when appropriate. Make cancel, save, and back behavior explicit; ask before discarding changed input, while untouched forms can dismiss directly.

## Verify the outcome

- Push, back, switch tabs, and reopen a presentation without unexplained jumps or lost edits.
- Open valid and stale deep links, including a cold launch.
- Check split-view collapse/expansion and restoration with deleted objects.

Do not automatically transport people to a different tab or use a modal for every destination.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
