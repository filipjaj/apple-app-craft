# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Integrate on-device AI models into your app using Core AI | Apple — 00:15:28.000

Download a large model when the person chooses to use the feature rather than for everyone automatically.

[Evidence at 00:15:28.000](https://www.youtube.com/watch?v=gl5lD2gEhb0&t=928s). Caption anchor: “even people who'll never touch this feature.”.

### WWDC26: Meet Core AI | Apple — 00:16:13.000

Prepare or specialize the model before interactive inference to avoid delaying the feature's first useful result.

[Evidence at 00:16:13.000](https://www.youtube.com/watch?v=XJFfCVW1UZ0&t=973s). Caption anchor: “It is recommended you avoid having model”.

### WWDC26: Dive into Core AI model authoring and optimization | Apple — 00:24:56.000

Change model function boundaries deliberately when the measured constraints justify a different authoring design.

[Evidence at 00:24:56.000](https://www.youtube.com/watch?v=MdlyLT_y3i0&t=1496s). Caption anchor: “Instead of converting the model as-is, I”.

### Current documentation checked

- [Official managing model specialization and caching documentation](https://developer.apple.com/documentation/coreai/managing-model-specialization-and-caching).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
