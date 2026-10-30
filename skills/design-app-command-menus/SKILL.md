---
name: design-app-command-menus
description: "Design, implement, or review an iPad or Mac app\u2019s menu bar, command organization, keyboard shortcuts and focused-window routing. Use for discoverable persistent commands and predictable enabled states; not general context menus or an ordinary button style."
---

# Design App Command Menus

## Goal

Make app commands easy to find, predictable in position and correctly targeted to the person’s active work.

## Working context

Inspect the actual app framework, deployment targets, SDK, scene setup and project conventions. Resolve framework details with Context7, then query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for decision criteria and timestamped evidence. The session describes iPadOS 26; preserve older supported systems and the user’s product direction.

## Workflow

1. Inventory existing app commands, their scope and availability. Preserve system menu conventions and standard command behavior. Decide which actions belong in existing menus and which warrant an app-specific menu; retain the same underlying domain operations as toolbar and touch actions.

2. Order app-specific actions by task importance and usage frequency, group related operations, and use submenus for secondary actions when the menu becomes too long. Keep standard system ordering. Use concise action labels and familiar symbols consistent with the app; iPad rows need touch space, so inspect the actual menu rather than assuming a Mac-sized list.

3. Populate View with actual navigation destinations and a sidebar visibility command when these apply. Provide shortcuts for frequent actions while preserving standard system shortcuts and avoiding collisions with text editing. Menu and toolbar activation should produce equivalent selection and outcomes.

4. Keep temporarily unavailable commands and menus in stable positions, disabling them instead of hiding them as selection or focus changes. Contextual labels such as Show/Hide Sidebar can reflect state without rebuilding the menu hierarchy. Do not manufacture menus for capabilities the app does not support.

5. For implementation, use supported scene commands and system command groups, extending them before replacing their default behavior. Route commands through the active scene or focused content using the appropriate focused values/bindings or framework equivalent. Scene focus and text/selection focus differ; use the scope the action actually requires. Disable commands when no valid target exists and revalidate at execution.

6. Exercise the menu by touch, pointer and keyboard, including text-editing focus, selection changes, two windows, inactive or closed targets, and long/localized labels. Verify commands act on the intended document once and reflect undo/save/async state correctly. Report which interactions were observed and which remain specifications.

## Prove routing through the real entry point

Keep an action/command map when commands span menus, shortcuts, toolbars, or requested automation surfaces: name, shortcut, target scope, availability, and underlying domain operation. Share that operation while validating the current target at execution; do not add a URL scheme or intent for every command by default.

An internal invocation proves the domain handler, not that a SwiftUI menu is enabled or that the shortcut reaches the intended focused window. Inspect and exercise the actual menu externally when available, including no selection, text-editing focus, and two documents. After deletion/completion, check selection continuity and Undo in the UI. Label unavailable external checks explicitly. [Adaptation provenance](../apple-app-craft/references/bama-source.md).

## Verify the outcome

- Temporarily unavailable items remain in predictable positions with accurate enabled states.
- Shortcuts preserve system expectations and do not send actions to the wrong focused window.
- View destinations and sidebar toggles stay consistent with in-app navigation.
- Touch, pointer and keyboard invoke the same domain action with usable labels and grouping.

Do not alphabetize task commands by default, hide temporarily inactive items, or point every window’s commands at one global selection.

## Deliverable

Leave the requested design, implementation or prioritized review. Explain command/window behavior, compatibility decisions, performed checks and remaining limitations.
