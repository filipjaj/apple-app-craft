# Source lessons

Reviewed the complete publisher English transcript of Elevate the design of your iPad app, relevant current official documentation passages, and one representative menu frame on 2026-10-06. This was not continuous full-video viewing.

### 00:05:49.780

System window controls affect toolbar placement.

[Evidence at 00:05:49.780](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=349s). Caption anchor: “leading edge”.

### 00:06:25.620

Integrate controls with the toolbar rather than retaining a compatibility-only top strip.

[Evidence at 00:06:25.620](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=385s). Caption anchor: “wrap your toolbar”.

### 00:07:23.832

Replacing the one existing document context is discouraged for multitasking document apps.

[Evidence at 00:07:23.832](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=443s). Caption anchor: “no longer recommended”.

### 00:07:34.541

Open documents additively when multitasking is supported.

[Evidence at 00:07:34.541](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=454s). Caption anchor: “their own window”.

### 00:08:09.482

Useful window titles let people find the correct open context.

[Evidence at 00:08:09.482](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=489s). Caption anchor: “descriptive names”.

## Documentation and interpretation

- [windows](https://developer.apple.com/design/human-interface-guidelines/windows).
- [multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking).
- [documents](https://developer.apple.com/documentation/swiftui/documentgroup).
- [windowgroup](https://developer.apple.com/documentation/swiftui/windowgroup).

The session motivates additive document windows and descriptive titles. Scene isolation, same-document reuse, save boundaries and restoration failure checks are implementation reasoning. DocumentGroup and WindowGroup are alternatives chosen for the actual architecture; do not migrate a working document stack merely to use one API.

Local provenance: `source-additions/transcripts/QYUFSEcwx4U.md` and official documentation snapshots under `source-additions/documents/`. Source media is excluded from the portable skills.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC24: Work with windows in SwiftUI | Apple — 00:08:07.000

Initial spatial window placement is platform-specific and should not prevent the person from moving the window.

[Evidence at 00:08:07.000](https://www.youtube.com/watch?v=6t7LhRkBobk&t=487s). Caption anchor: “so that this placement is only applied”.

### WWDC24: Tailor macOS windows with SwiftUI | Apple — 00:05:41.000

Choose restoration behavior by window purpose rather than restoring every auxiliary window.

[Evidence at 00:05:41.000](https://www.youtube.com/watch?v=zosCe4q1xPI&t=341s). Caption anchor: “But the About window should not. So”.

### WWDC24: Evolve your document launch experience | Apple — 00:06:35.000

Templates can provide intentional starting document content without replacing existing document contexts.

[Evidence at 00:06:35.000](https://www.youtube.com/watch?v=VEAHUaqY5bE&t=395s). Caption anchor: “liven up the view, and make it”.

### WWDC23: Build better document-based apps | Apple — 00:07:27.000

Use the document's real undo manager and native save lifecycle for consistent editing behavior.

[Evidence at 00:07:27.000](https://www.youtube.com/watch?v=TqoU3bL-7i8&t=447s). Caption anchor: “'UIDocumentViewController' will make a best effort to”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
