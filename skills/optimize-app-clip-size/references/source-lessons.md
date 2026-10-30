# Source lessons

Downloaded complete official timestamped transcripts for the three supplied sessions and reviewed technical passages on 2026-10-06. Full video files were skipped at the user’s request; this is not continuous video viewing or new speech recognition. Current documentation was checked separately.

### Build light and fast App Clips — WWDC21 — 00:03:57.000

Measure uncompressed size for each thinned device variant.

[Evidence at 00:03:57.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=237s). Caption anchor: “device variant”.

### Build light and fast App Clips — WWDC21 — 00:07:03.000

Asset catalogs enable optimization and device-appropriate resource delivery.

[Evidence at 00:07:03.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=423s). Caption anchor: “asset catalogs”.

### Build light and fast App Clips — WWDC21 — 00:08:24.000

Exclude assets and other files the App Clip does not need.

[Evidence at 00:08:24.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=504s). Caption anchor: “target membership”.

### Build light and fast App Clips — WWDC21 — 00:10:18.000

Evaluate linked dependencies against the focused clip task.

[Evidence at 00:10:18.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=618s). Caption anchor: “external dependencies”.

### Build light and fast App Clips — WWDC21 — 00:15:37.000

Test deferred content under varied bandwidth so size savings do not delay completion.

[Evidence at 00:15:37.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=937s). Caption anchor: “network link”.

### What’s new in App Clips — WWDC23 — 00:01:33.000

Size rules depend on invocation context; the session’s numeric limits are historical.

[Evidence at 00:01:33.000](https://www.youtube.com/watch?v=WKSq9m1hvAQ&t=93s). Caption anchor: “physical invocations”.

## Documentation and interpretation

- [choosing the right functionality for your app clip](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip).
- [configuring the launch experience of your app clip](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip).

As checked on 2026-10-06, Apple documents 10 MB for iOS 15 and earlier, 15 MB for iOS 16, and up to 100 MB on iOS 17+ for digital-only clips with reliable connectivity and no older OS support. A generated demo link provides a distinct physical-invocation exception, with no URL parameters. Recheck these conditions for the actual target; a task-oriented clip is not automatically eligible for the demo exception. Network timing and regression comparisons are implementation reasoning.

Local provenance: publisher transcripts and documentation snapshots under `source-additions/app-clips/`; these source assets are excluded from the portable plugin.
