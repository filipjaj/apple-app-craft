# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Unwrap PaperKit | Apple — 00:05:32.000

Anchor editing adornments in canvas coordinates so they follow zoom and scrolling.

[Evidence at 00:05:32.000](https://www.youtube.com/watch?v=M-nlZjvyGB0&t=332s). Caption anchor: “I want them to exist on top”.

### WWDC26: Read between the strokes with PencilKit | Apple — 00:06:05.000

Persisted handwriting-search content may need refreshing when recognition models change; preserve the source strokes.

[Evidence at 00:06:05.000](https://www.youtube.com/watch?v=UCDcC5mZKkg&t=365s). Caption anchor: “Where recognized text gives you one best”.

### Current documentation checked

- [Official pkstroke swift.struct documentation](https://developer.apple.com/de/documentation/pencilkit/pkstroke-swift.struct).
- [Official pkcanvasview documentation](https://developer.apple.com/de/documentation/pencilkit/pkcanvasview).
- [Official controlling stroke rendering for animation and editing documentation](https://developer.apple.com/de/documentation/pencilkit/controlling-stroke-rendering-for-animation-and-editing).
- [Official importing external drawing data into pencilkit documentation](https://developer.apple.com/de/documentation/pencilkit/importing-external-drawing-data-into-pencilkit).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
