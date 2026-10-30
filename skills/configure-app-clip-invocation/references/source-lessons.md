# Source lessons

Downloaded complete official timestamped transcripts for the three supplied sessions and reviewed technical passages on 2026-10-06. Full video files were skipped at the user’s request; this is not continuous video viewing or new speech recognition. Current documentation was checked separately.

### What’s new in App Clips — WWDC23 — 00:03:20.000

Generated default links remove custom server setup for supported default-link invocations.

[Evidence at 00:03:20.000](https://www.youtube.com/watch?v=WKSq9m1hvAQ&t=200s). Caption anchor: “iOS 16.4”.

### What’s new in App Clips — WWDC23 — 00:03:54.000

Retrieve invocation context from the user activity, then parse URL components.

[Evidence at 00:03:54.000](https://www.youtube.com/watch?v=WKSq9m1hvAQ&t=234s). Caption anchor: “webpage URL”.

### What’s new in App Clips — WWDC23 — 00:04:43.000

Link Presentation supports an App Clip preview within another app.

[Evidence at 00:04:43.000](https://www.youtube.com/watch?v=WKSq9m1hvAQ&t=283s). Caption anchor: “rich preview”.

### What’s new in App Clips — WWDC21 — 00:04:03.000

Associated websites can opt into a full-sized card with supported metadata.

[Evidence at 00:04:03.000](https://www.youtube.com/watch?v=tz5Dp4u0ka0&t=243s). Caption anchor: “app-clip-display”.

### What’s new in App Clips — WWDC21 — 00:06:18.000

Local experiences do not prove Maps, location suggestions or Spotlight discovery.

[Evidence at 00:06:18.000](https://www.youtube.com/watch?v=tz5Dp4u0ka0&t=378s). Caption anchor: “registered experiences”.

### What’s new in App Clips — WWDC21 — 00:09:49.000

Choose scan-only placement when NFC contact is impractical.

[Evidence at 00:09:49.000](https://www.youtube.com/watch?v=tz5Dp4u0ka0&t=589s). Caption anchor: “out of reach”.

### What’s new in App Clips — WWDC21 — 00:11:46.000

Physical placement and unobstructed visibility matter for scanning.

[Evidence at 00:11:46.000](https://www.youtube.com/watch?v=tz5Dp4u0ka0&t=706s). Caption anchor: “good visibility”.

### Build light and fast App Clips — WWDC21 — 00:18:44.000

Different hostnames and redirect destinations require deliberate association.

[Evidence at 00:18:44.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=1124s). Caption anchor: “domain validation”.

### Build light and fast App Clips — WWDC21 — 00:20:56.000

Validate the physical code’s encoded host instead of relying on website redirects.

[Evidence at 00:20:56.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=1256s). Caption anchor: “exact domain”.

### Build light and fast App Clips — WWDC21 — 00:25:36.000

Scheme-provided invocation URLs test the routing code, not every discovery surface.

[Evidence at 00:25:36.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=1536s). Caption anchor: “_XCAppClipURL”.

## Documentation and interpretation

- [configuring the launch experience of your app clip](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip).
- [associating your app clip with your website](https://developer.apple.com/documentation/appclip/associating-your-app-clip-with-your-website).
- [testing the launch experience of your app clip](https://developer.apple.com/documentation/appclip/testing-the-launch-experience-of-your-app-clip).
- [launching another app s app clip from your app](https://developer.apple.com/documentation/appclip/launching-another-app-s-app-clip-from-your-app).

The 2021 sessions are historical evidence for domain debugging, code placement and local testing. Current Apple documentation takes precedence for supported invocation/link combinations: generated default links can support QR/NFC, demo links have no parameters, and App Clip Codes have their own link requirements. Printed-code verification, untrusted URL handling and explicit test-layer separation are implementation reasoning. Do not copy inconsistent illustrative URL syntax from an article; use the generated URL and installed SDK.

Local provenance: publisher transcripts and documentation snapshots under `source-additions/app-clips/`; these source assets are excluded from the portable plugin.
