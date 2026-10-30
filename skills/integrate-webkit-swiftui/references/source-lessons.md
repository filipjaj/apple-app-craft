# Source lessons

Reviewed the complete publisher English transcript of WWDC25: Meet WebKit for SwiftUI, current Apple WebKit SwiftUI/page/scheme/navigation documentation, and one representative custom resource-loading frame on 2026-10-06. This was not continuous full-video viewing. Confirm API and platform availability against the installed SDK.

## 00:03:42.419

Use WebPage when loading control and observable page state are needed.

[Evidence at 00:03:42.419](https://www.youtube.com/watch?v=KUvb7pm1b3U&t=222s). Caption anchor: “create a WebPage”.

## 00:04:57.060

Base URLs determine how HTML resolves its related resources.

[Evidence at 00:04:57.060](https://www.youtube.com/watch?v=KUvb7pm1b3U&t=297s). Caption anchor: “relative URLs”.

## 00:07:47.931

A custom scheme replies with response metadata followed by resource data.

[Evidence at 00:07:47.931](https://www.youtube.com/watch?v=KUvb7pm1b3U&t=467s). Caption anchor: “URLSchemeTaskResult”.

## 00:08:20.997

Resource loading must honor task cancellation.

[Evidence at 00:08:20.997](https://www.youtube.com/watch?v=KUvb7pm1b3U&t=500s). Caption anchor: “cancelled”.

## 00:10:36.299

Navigation does not always reach finish; observe and handle failure paths.

[Evidence at 00:10:36.299](https://www.youtube.com/watch?v=KUvb7pm1b3U&t=636s). Caption anchor: “always guaranteed”.

## 00:13:21.764

Make embedded versus external navigation an explicit policy.

[Evidence at 00:13:21.764](https://www.youtube.com/watch?v=KUvb7pm1b3U&t=801s). Caption anchor: “navigation policies”.

## 00:18:33.809

Pass values through JavaScript arguments and validate returned Swift types.

[Evidence at 00:18:33.809](https://www.youtube.com/watch?v=KUvb7pm1b3U&t=1113s). Caption anchor: “dictionary of arguments”.

## 00:19:29.298

Coordinate scrolling and selection through meaningful geometry changes.

[Evidence at 00:19:29.298](https://www.youtube.com/watch?v=KUvb7pm1b3U&t=1169s). Caption anchor: “onScrollGeometryChange”.

## Current documentation and implementation reasoning

- [WebKit for SwiftUI](https://developer.apple.com/documentation/webkit/webkit-for-swiftui): WebView for display, WebPage for observable control and interaction, and native customization APIs.
- [WebPage](https://developer.apple.com/documentation/webkit/webpage): MainActor isolation, platform availability, load-returned event sequences, navigations, configuration/data-store choices, and JavaScript calls. Current docs list navigations; the supplied session demonstrates currentNavigationEvent. Verify the exact mechanism supported by the project, including Observation availability.
- [URLSchemeHandler](https://developer.apple.com/documentation/webkit/urlschemehandler): custom resource delivery through async sequences and cancellation when WebKit no longer needs a resource.
- [NavigationDeciding](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding): policies for actions, responses and authentication challenges.

The session’s custom lakes scheme, sample domain, and safe-area treatment illustrate one app. They are not defaults for every embedded web experience. URL scope validation, JavaScript boundary checks, late-result rejection, and scroll feedback-loop prevention are implementation reasoning built on the demonstrated lifecycle and data flow.

Local provenance: `source-additions/transcripts/KUvb7pm1b3U.md` and documentation snapshots under `source-additions/documents/`. Large media files are excluded from the portable skill package.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: What’s new in WebKit for Safari 27 | Apple — 00:06:41.000

Check actual browser support before depending on newly evolving layout or transition behavior.

[Evidence at 00:06:41.000](https://www.youtube.com/watch?v=7Hg1fCrm4yM&t=401s). Caption anchor: “We're still the only browser with support,”.

### WWDC25: What’s new in Safari and WebKit | Apple — 00:20:07.000

A custom web menu needs intentional opening, closing and placement relative to its triggering control.

[Evidence at 00:20:07.000](https://www.youtube.com/watch?v=r6LyKY07lsM&t=1207s). Caption anchor: “But, of course, I don’t want my”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
