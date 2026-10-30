---
name: extract-document-content
description: "Implement or review document recognition with Apple Vision, including tables, text, machine-readable codes and recognized fields. Use for extracting content, not building a text editor."
---

# Extract Document Content

## Goal

Turn a document image into useful structured information while preserving uncertainty and source context.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify the source document types and fields the user actually needs. Choose the current Vision recognition API supported by the app, and preserve a usable original document for review and correction.

2. Prepare image orientation, page ordering and sufficient resolution before recognition. Keep processing off UI-blocking paths and bound memory/work for multi-page inputs, with cancellation and progress appropriate to the task.

3. Use available structural observations for paragraphs, lists, tables, codes and detected fields rather than flattening everything into one string prematurely. Convert normalized coordinates correctly when highlighting source regions.

4. Treat recognition output as fallible. Validate important values and relationships, expose uncertainty or allow correction, and avoid automatically executing an embedded URL or treating recognized payment data as authorized.

5. Test rotated pages, low-quality images, multiple columns, tables and missing text with representative documents. Compare extracted values and reading order to the source and preserve user edits when reprocessing.

## Verify the outcome

- Extracted structure matches the document’s useful layout.
- Orientation and highlights map to the correct source regions.
- Uncertain or incorrect results are reviewable and correctable.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
