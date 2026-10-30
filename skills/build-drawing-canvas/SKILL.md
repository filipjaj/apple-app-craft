---
name: build-drawing-canvas
description: "Implement or review PencilKit/PaperKit drawing, markup templates, canvas overlays or handwriting recognition. Use for editable drawing content and canvas interaction."
---

# Build Drawing Canvas

## Goal

Preserve editable drawing content and predictable interactions as the canvas zooms, scrolls and reopens.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Choose the requested canvas capabilities and existing supported framework, then check content-version and SDK compatibility. Retain editable source data rather than relying on a flattened screenshot as the only saved representation.

2. Separate fixed template elements, user-editable markup and transient editing overlays. Set allowed interactions according to the task, and anchor controls or collaboration adornments in the correct canvas coordinates so zoom and scrolling stay aligned.

3. Integrate tool selection, undo/redo, document ownership and autosave with the existing app. Persist edits atomically at appropriate boundaries and handle restoration failures without silently erasing a drawing.

4. If recognition is requested, distinguish the best readable result from broader indexable candidates. Keep original strokes and account for language or recognition-model changes; recognized text is not a permanent replacement for the drawing.

5. Test draw/edit/undo, template protection, zoomed overlays, save/reopen and supported content versions, plus accessible alternatives for essential commands. Validate imported stroke approximations visually and preserve the original when conversion loses meaning.

## Verify the outcome

- Reopened drawings retain editable content and undo expectations.
- Templates and overlays behave correctly while zooming.
- Recognition and import do not destroy source strokes.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
