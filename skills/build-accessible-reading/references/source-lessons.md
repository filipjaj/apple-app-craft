# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Elevate your app’s text experience with TextKit | Apple — 00:06:25.000

Use viewport layout information to render visible text while preserving the complete logical document.

[Evidence at 00:06:25.000](https://www.youtube.com/watch?v=8t64PukyOIQ&t=385s). Caption anchor: “only rendering text that the user can”.

### WWDC26: Enhance the accessibility of your reading app | Apple — 00:09:40.000

Paginated read-all should continue through the content rather than stopping at the visible page.

[Evidence at 00:09:40.000](https://www.youtube.com/watch?v=5FjB-0nP-Ws&t=580s). Caption anchor: “With paginated content, the best experience for”.

### Current documentation checked

- [Official display text with a custom layout documentation](https://developer.apple.com/de/documentation/uikit/display-text-with-a-custom-layout).
- [Official nstextlayoutmanager documentation](https://developer.apple.com/de/documentation/uikit/nstextlayoutmanager).
- [Official nsaccessibilityprotocol documentation](https://developer.apple.com/de/documentation/appkit/nsaccessibilityprotocol).
- [Official nstextviewportlayoutcontroller documentation](https://developer.apple.com/de/documentation/uikit/nstextviewportlayoutcontroller).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
