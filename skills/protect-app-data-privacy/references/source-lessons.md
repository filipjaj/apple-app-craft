# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: Integrate privacy into your development process | Apple — 00:10:26.000

Selective system pickers can satisfy a task without requesting access to a whole photo library.

[Evidence at 00:10:26.000](https://www.youtube.com/watch?v=uYBzcVClCe0&t=626s). Caption anchor: “but I probably don’t need access to”.

### WWDC23: What’s new in privacy | Apple — 00:19:48.000

File-access prompts should occur at an expected task moment with a meaningful explanation.

[Evidence at 00:19:48.000](https://www.youtube.com/watch?v=D_juI4Zq3ok&t=1188s). Caption anchor: “You should only attempt to read other”.

### WWDC24: What’s new in privacy | Apple — 00:18:42.000

Request access contextually and provide a descriptive purpose instead of surprising people.

[Evidence at 00:18:42.000](https://www.youtube.com/watch?v=3S71FgEzqb0&t=1122s). Caption anchor: “Ensure that your app and its processes”.

### WWDC23: Get started with privacy manifests | Apple — 00:09:09.000

Required-reason APIs may only be used for approved purposes matching the app's actual behavior.

[Evidence at 00:09:09.000](https://www.youtube.com/watch?v=OQMF4LDqscc&t=549s). Caption anchor: “the Required reason APIs only for the”.

### Current documentation checked

- [Official tn3183 adding required reason api entries to your privacy manifest documentation](https://developer.apple.com/de/documentation/technotes/tn3183-adding-required-reason-api-entries-to-your-privacy-manifest).
- [Official tn3184 adding data collection details to your privacy manifest documentation](https://developer.apple.com/de/documentation/technotes/tn3184-adding-data-collection-details-to-your-privacy-manifest).
- [Official tn3182 adding privacy tracking keys to your privacy manifest documentation](https://developer.apple.com/de/documentation/technotes/tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
