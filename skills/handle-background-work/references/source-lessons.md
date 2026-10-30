# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC22: Efficiency awaits: Background tasks in SwiftUI | Apple — 00:05:24.000

Use a supported background transfer when the job warrants it, and separate transfer completion from refresh runtime.

[Evidence at 00:05:24.000](https://www.youtube.com/watch?v=JDw4Cs1Hbpo&t=324s). Caption anchor: “In this case, we should make sure”.

### Current documentation checked

- [Official using background tasks documentation](https://developer.apple.com/de/documentation/watchkit/using-background-tasks).
- [Official using background tasks to update your app documentation](https://developer.apple.com/de/documentation/uikit/using-background-tasks-to-update-your-app).
- [Official building an app to notify users of covid 19 exposure documentation](https://developer.apple.com/de/documentation/exposurenotification/building-an-app-to-notify-users-of-covid-19-exposure).
- [Official bgtaskscheduler documentation](https://developer.apple.com/de/documentation/backgroundtasks/bgtaskscheduler).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
