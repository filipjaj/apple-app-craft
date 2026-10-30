# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 25. WWDC22: The SwiftUI cookbook for navigation | Apple

Navigation becomes model state: links add values, destinations map those values to views, and split-view selection adapts across device sizes.

[Original session](https://www.youtube.com/watch?v=6Rp71CvKIKs) · Original library transcript: `transcripts/25-6Rp71CvKIKs.md`

- Bind a NavigationStack to a path of values to support programmatic pushes, deep links, and popping back to the root. [Evidence at 00:02:06.693](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=126s)

- Separate a NavigationLink’s value from its destination view with navigationDestination; use a typed array for one value type or NavigationPath for heterogeneous values. [Evidence at 00:09:23.830](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=563s)

- Combine NavigationSplitView with list selection for multicolumn navigation that automatically adapts to narrow presentations. [Evidence at 00:13:14.127](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=794s)

- Compose a NavigationStack inside a split-view column when the detail area needs its own push/pop history. [Evidence at 00:14:51.190](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=891s)

- Register destinations outside lazy containers so the stack can find them regardless of which rows or tiles have loaded. [Evidence at 00:16:28.087](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=988s)

- Restore navigation using stable model identifiers rather than serializing entire model values, and handle identifiers whose objects have been deleted. [Evidence at 00:21:28.354](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=1288s)

- Encapsulate navigation state in a Codable model and persist it per scene with SceneStorage, restoring and saving from a view-lifecycle task. [Evidence at 00:18:15.661](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=1095s)

Visual examples: [A data-driven navigation path](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=138s) — NavigationStack binds its path while links carry values instead of separate active flags.; [Split-view selection](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=797s) — The selected category and recipe appear together on iPad while iPhone pushes through the hierarchy.; [Restoring navigation by identifier](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=1291s) — Decoding recipe identifiers reconstructs the navigation path using the shared data model.

## 31. WWDC22: Explore navigation design for iOS | Apple

Organize content around clear top-level purposes, then choose transitions that match either deeper exploration or a focused task.

[Original session](https://www.youtube.com/watch?v=Kd02qR_LyA0) · Original library transcript: `transcripts/31-Kd02qR_LyA0.md`

- Give each tab a meaningful top-level content area and distribute functionality so one catchall tab does not obscure the hierarchy. [Evidence at 00:03:31.311](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=211s)

- Avoid duplicating unrelated actions into a Home tab merely to promote discoverability; do not automatically transport people to another tab. [Evidence at 00:10:42.242](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=642s)

- Preserve access and state across tabs during hierarchical exploration, and use clear labels to explain what each tab contains. [Evidence at 00:11:05.732](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=665s)

- Use pushes for deeper levels of content and workflows that require frequent movement between views; match disclosure indicators to this behavior. [Evidence at 00:14:40.480](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=880s)

- Use titles and meaningful back labels to orient people, and respect reversed progression for right-to-left languages. [Evidence at 00:17:15.835](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=1035s)

- Use a modal for a focused, self-contained task or immersive content, with clear preferred and cancel actions. [Evidence at 00:13:41.421](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=821s)

- Warn before discarding entered data, but dismiss an untouched form directly; reserve an X close control for content with minimal interaction. [Evidence at 00:22:14.200](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=1334s)

- Limit stacked modals while allowing an appropriate nested task when it preserves consistency and focus. [Evidence at 00:23:15.995](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=1395s)

Visual examples: [Balancing top-level tabs](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=486s) — The revised tab bar gives Places, Itineraries, and Profile separate top-level destinations.; [Hierarchical push navigation](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=892s) — The navigation tree shows movement from a parent screen into deeper content.; [Discarding input and dismissing modals](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=1337s) — The discard-changes sheet protects entered form data and offers a return to editing.

## 33. WWDC25: Design foundations from idea to interface | Apple

A practical design critique shows how familiar components and deliberate content organization turn an attractive screen into a usable app.

[Original session](https://www.youtube.com/watch?v=dGcqqA3Sl-o) · Original library transcript: `transcripts/33-dGcqqA3Sl-o.md`

- Evaluate whether each screen explains where the person is, what they can do, and where they can go next. [Evidence at 00:02:20.993](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=140s)

- Inventory features and workflows, understand real usage context, then remove nonessential features and group related ones before styling. [Evidence at 00:04:05.829](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=245s)

- Use tabs for navigation and put screen-specific actions in a toolbar; choose explicit labels and familiar symbols. [Evidence at 00:06:01.932](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=361s)

- Use progressive disclosure to reveal detail when relevant while keeping expanded views connected to their originating screen. [Evidence at 00:09:01.466](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=541s)

- Match layouts to content: lists support scanning structured information, while collections suit visual items with restrained text. [Evidence at 00:10:22.586](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=622s)

- Reduce choice overload by grouping content according to time, progress, or meaningful relationships. [Evidence at 00:12:07.193](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=727s)

- Build hierarchy with system text styles, support Dynamic Type, and protect text legibility over imagery. [Evidence at 00:15:20.037](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=920s)

- Use semantic system colors for adaptable interface roles and add a cohesive brand palette where it preserves legibility and appearance settings. [Evidence at 00:17:06.896](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=1026s)

Visual examples: [Tabs versus screen actions](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=373s) — The tab bar separates Records, Swaps, and Saves as top-level destinations.; [Progressive disclosure](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=564s) — The labeled disclosure control leads from a compact record group to its detailed contents.; [Type hierarchy and legibility](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=916s) — Caption, title, and subtitle labels establish a readable type hierarchy over artwork.

## 2026-10-06 focused refinement

Tabs should predictably lead to sections. Place an Add action with the content it creates instead of making it a destination. [Evidence at 00:06:01.932](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=361s). This clarifies an existing mapped source rather than adding a duplicate session.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### Design with SwiftUI | Meet with Apple — 00:03:59.000

A small set of stable native tabs makes major destinations predictable.

[Evidence at 00:03:59.000](https://www.youtube.com/watch?v=Y5dXhLPfJng&t=239s). Caption anchor: “So one thing I always recommend is”.

### WWDC23: Inspectors in SwiftUI: Discover the details | Apple — 00:08:44.000

Place an inspector within the appropriate navigation hierarchy, including a split view's detail column.

[Evidence at 00:08:44.000](https://www.youtube.com/watch?v=l0ksmCylJRc&t=524s). Caption anchor: “The only axis to worry about is”.

### WWDC23: Beyond scroll views | Apple — 00:05:14.000

Define the intended scroll targets before relying on view-aligned scrolling behavior.

[Evidence at 00:05:14.000](https://www.youtube.com/watch?v=PbyyEQLpX_Y&t=314s). Caption anchor: “Instead of aligning to the containing size”.

### WWDC22: The SwiftUI cookbook for navigation | Apple — 00:05:00.634

Value-driven navigation separates destination identity from the transient link view.

[Evidence at 00:05:00.634](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=300s). Caption anchor: “Previously, NavigationLinks always included a title and”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
