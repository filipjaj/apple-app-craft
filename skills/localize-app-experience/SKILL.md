---
name: localize-app-experience
description: "Prepare, translate, or review Apple app localization using String Catalogs and locale-aware presentation. Use for language and internationalization work, including translation-assisted workflows."
---

# Localize App Experience

## Goal

Make the same app task understandable and usable in each requested language and locale.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify requested languages, source language, app modules and existing localization conventions. Inspect String Catalog extraction, dynamic keys and server-provided content. Translate the requested scope without changing the product’s vocabulary or silently expanding language coverage.

2. Provide translators with task context, screen location and ambiguous meanings. Separate stable voice from situational tone. Keep context files scoped to translation work; generated comments and model translations are drafts that need review against the app.

3. Localize complete messages with placeholders and appropriate plural variations rather than concatenating translated fragments. Use locale-aware dates, numbers and measurements. Preserve intentional names and nontranslatable content, and validate placeholder types and counts.

4. Allow horizontal and vertical expansion, right-to-left presentation and supported text sizes. Keep semantic ordering and directionally appropriate symbols; do not mirror every image or force English-specific widths. Coordinate the language requested from servers and define fallback behavior.

5. Exercise critical flows in the requested locales with realistic long strings, plural counts and translated accessibility labels. Confirm manual and dynamically sourced keys remain available after extraction. Use native-speaker or qualified feedback where available and disclose unreviewed machine translation.

## Verify the outcome

- Messages retain meaning and correct substitutions.
- Layouts work for long text and right-to-left languages.
- Locale changes affect content and formatting consistently.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
