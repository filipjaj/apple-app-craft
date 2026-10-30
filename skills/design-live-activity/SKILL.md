---
name: design-live-activity
description: "Design or refine a Live Activity across Lock Screen, Dynamic Island, and StandBy presentations. Use for glanceable ongoing-event experiences."
---

# Design a Live Activity

## Goal

Show the current event’s most useful information at a glance on every supported presentation.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Choose an ongoing user-relevant event and identify the single most useful status and essential action. Avoid using an activity as a promotional surface.
2. Design compact, minimal, expanded, and Lock Screen layouts for their geometry. Keep relative placement consistent across expansion; make the minimal presentation convey event-specific status.
3. Use concise text and meaningful numeric transitions for updates. Alert only when attention is needed. Treat stale and ended states explicitly and retire completed activity information appropriately.
4. Express identity through restrained color, typography, and graphics rather than inserting the entire app icon. Check StandBy scale, night appearance, sensor cutouts, and extended backgrounds.
5. If implementation is requested, inspect ActivityKit support and the app’s existing update delivery before coding. Connect controls and deep links to real domain actions; design guidance does not establish push-update infrastructure.

## Verify the outcome

- Use realistic long values and all supported activity presentations.
- Check significant updates, stale data, completion, and the app destination when opened.
- Inspect contrast and layout on target devices or simulations; report which surfaces were available.

Do not shrink the whole in-app screen into the activity or reduce the minimal presentation to a generic logo.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
