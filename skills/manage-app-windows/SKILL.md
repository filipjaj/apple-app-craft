---
name: manage-app-windows
description: "Build, review, or improve Apple app multiwindow and document-opening behavior, including scene-local state, descriptive window titles, restoration and iPad window-control accommodation. Use when opening another document or window must preserve existing work; not an isolated layout bug."
---

# Manage App Windows

## Goal

Let people open, identify and return to independent work contexts without replacing or losing their existing work.

## Working context

Inspect the actual app framework, deployment targets, SDK, scene setup and project conventions. Resolve framework details with Context7, then query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for decision criteria and timestamped evidence. The session describes iPadOS 26; preserve older supported systems and the user’s product direction.

## Workflow

1. Identify which product objects deserve independent windows and the existing document-opening contract. Inspect multiple-scene support and target capabilities. For document apps, prefer the existing native document architecture; DocumentGroup supports document windows, while WindowGroup suits other scene content. Do not add multiwindow to a flow that does not need it.

2. When supported multitasking opens a different document, use additive window presentation rather than replacing the active document’s context. Define whether opening the same document activates an existing window or offers another view. Use document identity and supported APIs, not a global mutable current-document variable or an assumed openWindow behavior.

3. Separate scene-local selection, navigation, focus and unfinished input from shared domain data. Own model state at the correct scene/document lifetime; coordinate edits to the same underlying object deliberately. Opening or closing one window must not reset another, and closing must follow the existing save/unsaved-change contract.

4. Provide meaningful, distinguishable window titles based on their content, such as document names, with a useful untitled fallback. Update titles after rename and disambiguate identical visible names when needed. Inspect the system’s open-window list; a scene identifier is not automatically a useful user-facing title.

5. Accommodate system window controls in native toolbar layout, especially leading controls and custom headers. Inspect the actual safe area and available APIs rather than hardcoding traffic-light coordinates or permanently reserving a duplicate top strip. Preserve reachability and content legibility during resizing.

6. Implement or specify restoration appropriate to the product. Restore document identity and intentional scene state, handle missing or inaccessible content, and preserve save/reopen behavior. Exercise two documents, duplicate opening, switching focus, renaming, resizing, closing and relaunch; report actual device checks separately from code inspection.

## macOS utility panels

Distinguish document/scene windows from transient utility panels. Before choosing a panel, define whether text input requires activation, what Escape/Return do, when dismissal occurs, where focus returns, and which display/space owns placement. Use current display geometry rather than fixed desktop coordinates. Test repeated invocation, switching apps, resizing, and multiple displays as relevant. For global shortcuts, menu bar lifecycle, or cross-app window manipulation use `integrate-macos-utilities` when available. A preview does not establish activation or focus restoration. [Adaptation provenance](../apple-app-craft/references/bama-source.md).

## Verify the outcome

- Opening another document preserves the first window’s edits and navigation.
- Window titles identify the intended context, including rename and duplicate-name cases.
- Independent windows retain their state; shared data changes propagate intentionally.
- Window controls, restoration and save/close behavior work on supported targets.

Do not make every screen a window, replace one shared document pointer on every open, or infer correct scene isolation from a single-window preview.

## Additional source decisions

Match document launch, templates, undo and restoration to the existing document lifecycle. Auxiliary windows and document windows need different restoration choices. Initial spatial placement and replacement-window APIs are platform-specific; do not use them to discard a person’s existing document context on another platform.

## Deliverable

Leave the requested design, implementation or prioritized review. Explain command/window behavior, compatibility decisions, performed checks and remaining limitations.
