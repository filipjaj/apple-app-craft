---
name: build-accessible-reading
description: "Build or improve TextKit-based or custom long-form reading experiences, including reading order, pagination and text accessibility. Use for document reading UI; OCR extraction has a separate goal."
---

# Build Accessible Reading

## Goal

Let people read, navigate and select long-form content through their preferred supported reading mode.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Inspect the content model, text system, paging and editing/selection needs. Prefer standard accessible text components when they satisfy the design and check TextKit version/SDK support before adding custom rendering.

2. Keep logical document order separate from visible layout fragments and viewport work. Render only appropriate visible content while retaining a complete readable model. Preserve selection and reading position when layout, font size or page boundaries change.

3. Expose semantic text, labels, ranges and navigation landmarks appropriate to the actual framework. Multiple paragraph views or custom text elements must form a coherent reading experience rather than repeating or skipping content.

4. For paginated reading, support meaningful read-all progression and page navigation with the chosen assistive technology. Provide equivalents for custom gestures and avoid making pointer hover the only way to discover text actions.

5. Test VoiceOver/read-all, selection, pagination, Dynamic Type and relevant language directions using representative long content. Distinguish visual screenshots from actual assistive reading; verify no missing, duplicated or out-of-order text.

## Verify the outcome

- Logical reading order survives pagination and viewport rendering.
- Reading position and selection survive layout changes.
- Assistive reading can complete the same essential task.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
