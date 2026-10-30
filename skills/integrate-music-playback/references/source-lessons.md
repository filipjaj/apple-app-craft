# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Integrate MusicKit into your app | Apple — 00:11:20.000

Choose player ownership deliberately because system and application queues expose different capabilities.

[Evidence at 00:11:20.000](https://www.youtube.com/watch?v=2rwWEy2USw8&t=680s). Caption anchor: “With SystemMusicPlayer, you may only set the”.

### Current documentation checked

- [Official request%28%29 documentation](https://developer.apple.com/documentation/musickit/musicauthorization/request%28%29).
- [Official currentstatus documentation](https://developer.apple.com/documentation/musickit/musicauthorization/currentstatus).
- [Official canbecomesubscriber documentation](https://developer.apple.com/documentation/musickit/musicsubscription/canbecomesubscriber).
- [Official canplaycatalogcontent documentation](https://developer.apple.com/documentation/musickit/musicsubscription/canplaycatalogcontent).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
