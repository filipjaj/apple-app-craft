# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Build real-time apps and services with gRPC and Swift | Apple — 00:08:07.000

Share reusable clients at the appropriate lifetime and release connections according to real background requirements.

[Evidence at 00:08:07.000](https://www.youtube.com/watch?v=CCFxlFF9XRI&t=487s). Caption anchor: “Instead, my app should create a client”.

### WWDC21: Use async/await with URLSession | Apple — 00:02:06.000

Keep asynchronous completion and UI isolation consistent instead of relying on accidental callback queues.

[Evidence at 00:02:06.000](https://www.youtube.com/watch?v=Owcx2Upk6p8&t=126s). Caption anchor: “to avoid any threading issues such as”.

### WWDC23: Meet Swift OpenAPI Generator | Apple — 00:03:21.000

Typed HTTP clients still need status, content-type and response contract validation.

[Evidence at 00:03:21.000](https://www.youtube.com/watch?v=US5Blei-5Kg&t=201s). Caption anchor: “Then we must validate the responses of”.

### WWDC21: Reduce network delays for your app | Apple — 00:11:21.000

Handshake early data must be idempotent and replay-safe, particularly for operations with side effects.

[Evidence at 00:11:21.000](https://www.youtube.com/watch?v=51jOPr4jsP0&t=681s). Caption anchor: “Let me explain what it means and”.

### WWDC23: Build robust and resumable file transfers | Apple — 00:07:15.000

Resumable downloads need server byte-range support, resource identity and a surviving temporary file.

[Evidence at 00:07:15.000](https://www.youtube.com/watch?v=pBBKkppW9kw&t=435s). Caption anchor: “Next, the server must support byte-range requests”.

### WWDC25: Use structured concurrency with Network framework | Apple — 00:03:24.000

Choose secure transport and network constraints according to the requested operation.

[Evidence at 00:03:24.000](https://www.youtube.com/watch?v=9mJ-mqiyhVU&t=204s). Caption anchor: “but don’t worry, it will all make”.

### Current documentation checked

- [Official pausing and resuming downloads documentation](https://developer.apple.com/de/documentation/foundation/pausing-and-resuming-downloads).
- [Official urlsession documentation](https://developer.apple.com/de/documentation/foundation/urlsession).
- [Official downloading files from websites documentation](https://developer.apple.com/de/documentation/foundation/downloading-files-from-websites).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
