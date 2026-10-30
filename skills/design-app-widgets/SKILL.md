---
name: design-app-widgets
description: "Design, implement, or review WidgetKit widgets, including timelines, relevant content and interactive actions. Use for glanceable system widgets; use design-live-activity for a single ongoing event."
---

# Design App Widgets

## Goal

Surface one timely piece of app value and its most useful action without requiring the app to open.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Choose what someone needs to know or do at a glance, and the widget families and platforms the app actually supports. Design a widget for that value instead of shrinking a full app screen. Use realistic data, system margins and readable hierarchy.

2. Build snapshots, placeholders and timelines with useful current and predictable future entries. Choose the reload policy from how data changes; a reload request is a scheduling hint, not an exact timer. Cache appropriate data and define stale, unavailable and signed-out presentations.

3. Route deep links to the correct app object. For supported interactive buttons or toggles, invoke the same domain operation through a suitable App Intent and update authoritative data before refreshing views. Handle denied access and failure without displaying a false success.

4. Reload only affected timelines when data changes. Verify current reload budgets and push capabilities; opportunistic updates do not replace urgent notifications or Live Activities. Respect extension execution limits and avoid polling to simulate a continuously running app.

5. Check all requested sizes, tinted/clear/full-color appearances, localization, Dynamic Type and accessibility, plus remote-widget environments where relevant. Verify timeline transitions and action outcomes on devices, distinguishing previews from actual update delivery.

## Verify the outcome

- Useful content remains available when a refresh is delayed.
- Actions and deep links affect the intended object.
- Supported families and appearances preserve essential information.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
