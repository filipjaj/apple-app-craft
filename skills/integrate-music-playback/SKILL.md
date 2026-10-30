---
name: integrate-music-playback
description: "Build or repair Apple Music integration using MusicKit, including authorization, subscription checks and player ownership. Use for music playback behavior, not a generic audio-engine profile."
---

# Integrate Music Playback

## Goal

Play the intended music through a coherent queue while respecting authorization and subscription capability.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify the requested catalog/library use, existing playback and supported systems. Check MusicKit authorization at a contextual moment and handle denied or restricted access without treating it as a playback error.

2. Inspect subscription capabilities separately from permission. Offer subscription UI only when appropriate eligibility is present, and preserve available non-subscriber behavior rather than assuming authorization enables all catalog playback.

3. Choose system versus application player by the intended queue ownership and interaction with the Music app. Inspect current queue access semantics; do not assume a system player exposes the same readable/editable queue as an application player.

4. Keep selection, queue changes, playback state and UI in sync across asynchronous operations. Resolve stable music identity and handle unavailable items, region changes, interruption and cancellation.

5. Test authorization/subscription changes, empty selections, queue replacement, pause/resume and external playback control on supported devices. Report actual playback evidence separately from successful catalog lookup or UI previews.

## Verify the outcome

- Permission and subscription capability are handled separately.
- Queue ownership matches the product’s playback expectations.
- Missing tracks and interrupted playback recover predictably.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
