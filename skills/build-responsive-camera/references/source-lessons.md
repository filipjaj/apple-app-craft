# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Build a responsive camera app that launches quickly | Apple — 00:03:58.000

Defer unrelated work until the camera preview has become usable.

[Evidence at 00:03:58.000](https://www.youtube.com/watch?v=nXUsStRc7Tc&t=238s). Caption anchor: “this work should wait until after preview”.

### WWDC24: Build a great Lock Screen camera capture experience | Apple — 00:07:31.000

A Lock Screen capture extension must handle the actual inherited photo-library permission level.

[Evidence at 00:07:31.000](https://www.youtube.com/watch?v=l1beJxAYli0&t=451s). Caption anchor: “such as write only access and limited”.

### WWDC26: Support the Center Stage front camera in your iOS app | Apple — 00:11:01.000

Choose orientation compensation by capture type and measured quality/performance rather than applying it universally.

[Evidence at 00:11:01.000](https://www.youtube.com/watch?v=zRdN66ieSuc&t=661s). Caption anchor: “It is never applied to Bayer RAW”.

### WWDC25: Enhancing your camera experience with capture controls | Apple — 00:16:15.000

Capture controls belong to real capture features; do not start the camera merely to adopt a control.

[Evidence at 00:16:15.000](https://www.youtube.com/watch?v=ieX4Sbfpz0s&t=975s). Caption anchor: “so it should affect the appearance or”.

### Current documentation checked

- [Official displaying video from connected devices documentation](https://developer.apple.com/de/documentation/visionos/displaying-video-from-connected-devices).
- [Official enhancing live video by leveraging truedepth camera data documentation](https://developer.apple.com/de/documentation/avfoundation/enhancing-live-video-by-leveraging-truedepth-camera-data).
- [Official accessing the camera while multitasking on ipad documentation](https://developer.apple.com/de/documentation/avkit/accessing-the-camera-while-multitasking-on-ipad).
- [Official avcam building a camera app documentation](https://developer.apple.com/de/documentation/avfoundation/avcam-building-a-camera-app).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
