---
name: optimize-app-clip-size
description: "Measure and reduce an App Clip’s uncompressed distribution size and time to useful content. Use when an App Clip exceeds its applicable size limit, downloads too slowly, or includes unnecessary assets and dependencies; not a general SwiftUI rendering investigation."
---

# Optimize App Clip Size

## Goal

Deliver the promised App Clip task quickly within the size budget required by its supported systems and invocation methods.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. Resolve App Clips with Context7 and query the concept being implemented; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for dated evidence and current-rule distinctions. Preserve the user’s product direction and existing working behavior.

## Workflow

1. Confirm the minimum supported iOS version, task-oriented versus demo use, expected connectivity, and digital or physical invocation methods. Resolve the current official size rules before setting a budget. The 2021 and 2023 sessions describe historical limits; do not hardcode their 10 MB or 50 MB limits as universal current rules. Keep margin below the applicable ceiling rather than filling it by default.

2. Create a Release archive of the corresponding full app and export the App Clip using the installed Xcode’s supported distribution and thinning workflow. Inspect the App Thinning Size Report and the uncompressed size of every relevant device variant. Measure the clip product, not the full IPA’s compressed size or a Debug build. Record the baseline and inspect exported bundle contents for the largest contributors.

3. Limit target membership and Copy Bundle Resources to the promised clip task. Separate shared from full-app-only asset catalogs, source files, localizations and frameworks. Remove accidental documentation archives, unused media and unrelated features while preserving accessibility assets, needed translations and essential task behavior. Rebuild after each meaningful dependency boundary change.

4. Use asset catalogs and device thinning where supported. Match raster dimensions and format to actual display use, compare compressed output in the app, and preserve transparency and sharp edges where necessary. Consider vector resources, SF Symbols and one reusable base image instead of multiple baked variations. Choose supported formats by measured size and visible quality; no codec or image format is always smallest.

5. Inspect dependencies and archive optimization settings. Prefer existing supported system capabilities when they meet the task and avoid bundling a large library for a tiny operation. Keep the app’s valid Release settings and verify changes empirically. The old export instruction to rebuild from bitcode is historical; do not add obsolete bitcode settings or blindly change compiler flags.

6. If assets still dominate, decide which must be bundled to make the first interaction useful and which can arrive later. Use placeholders, caching and progressive loading appropriate to the clip’s lifetime. Background Assets availability and suitability differ between demos and in-the-moment clips; verify current guidance before using it, and do not assume ordinary background URLSession transfers are available. Test loading failures and constrained connectivity so moving bytes off the binary does not merely move the wait onto the user.

7. Repeat the same archive/export measurement and compare every device variant against the chosen budget. Measure cold launch and time to usable task under representative network conditions, separately from warm launches. Recheck visual quality, accessibility and completion in both targets. Report before/after sizes, measurement conditions and launch evidence; a simulator launch does not prove download speed or App Store acceptance.

## Verify the outcome

- All relevant uncompressed device variants fit the verified budget with margin.
- The export contains only resources and dependencies needed by the task.
- Visual quality, localization and accessibility survive the reductions.
- Deferred assets do not block essential work or leave the task unusable on a slow connection.

Do not equate a small compressed IPA with a compliant clip, remove task-critical content to hit a number, or treat the platform ceiling as the performance goal.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, compatibility decisions, performed checks and remaining limits. Use the project’s required build/test tools (including SwiftProbe when configured); source review alone does not prove device or distribution behavior.
