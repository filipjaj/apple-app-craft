---
name: integrate-drag-drop
description: "Implement or improve SwiftUI drag-and-drop, reordering and transferable content. Use for drag semantics and destination validation, including accessible alternatives."
---

# Integrate Drag and Drop

## Goal

Move or copy the intended app content to a valid destination without corrupting its source or identity.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Define supported sources, destinations and copy/move/reorder semantics, including cross-app behavior. Use stable model identity and supported transfer representations instead of encoding the current view as domain data.

2. Validate destination capability and payload before committing a drop. Handle asynchronous loading, permission-scoped resources and cancellation; do not delete the source or show a completed move before accepted content is durably owned.

3. Keep model ordering and visual feedback in sync through the existing data owner. Preserve selection and avoid using recycled view identity to identify a dragged item.

4. Provide a discoverable equivalent action when dragging is the only way to accomplish an essential task, and test the actual interaction with accessibility technologies. Avoid hover-only drop controls.

5. Test valid/invalid drops, repeated items, interrupted loads and the relevant touch/pointer/cross-app paths. Verify final source/destination content and ordering rather than just the drag preview.

## Verify the outcome

- Copy and move preserve the promised source/destination semantics.
- Invalid or interrupted drops leave data consistent.
- Essential actions have accessible equivalents.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
