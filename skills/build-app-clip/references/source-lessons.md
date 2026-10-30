# Source lessons

Downloaded complete official timestamped transcripts for the three supplied sessions and reviewed technical passages on 2026-10-06. Full video files were skipped at the user’s request; this is not continuous video viewing or new speech recognition. Current documentation was checked separately.

### What’s new in App Clips — WWDC21 — 00:00:26.000

An App Clip promises a fast experience around a specific task.

[Evidence at 00:00:26.000](https://www.youtube.com/watch?v=tz5Dp4u0ka0&t=26s). Caption anchor: “specific task”.

### Build light and fast App Clips — WWDC21 — 00:22:53.000

Make the relevant feature independently launchable through a deep link.

[Evidence at 00:22:53.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=1373s). Caption anchor: “modular functionality”.

### Build light and fast App Clips — WWDC21 — 00:24:12.000

Share invocation handling between clip and full app instead of maintaining parallel launch logic.

[Evidence at 00:24:12.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=1452s). Caption anchor: “refactoring”.

### Build light and fast App Clips — WWDC21 — 00:26:52.000

Use streamlined notification and location permissions only where the task needs them.

[Evidence at 00:26:52.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=1612s). Caption anchor: “ephemeral notifications”.

### Build light and fast App Clips — WWDC21 — 00:27:45.000

Handle location-confirmation refusal and errors without silently assuming confirmation.

[Evidence at 00:27:45.000](https://www.youtube.com/watch?v=Qt0yX-fUQ2Q&t=1665s). Caption anchor: “opt out”.

## Documentation and interpretation

- [choosing the right functionality for your app clip](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip).
- [sharing data between your app clip and your full app](https://developer.apple.com/documentation/appclip/sharing-data-between-your-app-clip-and-your-full-app).

URL validation, transaction authorization, idempotency and missing-data recovery are implementation reasoning. Current Apple documentation supplies the capability restrictions, single-target rule, full-app parity and directional keychain migration behavior. Do not copy documentation examples without checking that both targets use the same real app-group identifier and supported APIs.

Local provenance: publisher transcripts and documentation snapshots under `source-additions/app-clips/`; these source assets are excluded from the portable plugin.
