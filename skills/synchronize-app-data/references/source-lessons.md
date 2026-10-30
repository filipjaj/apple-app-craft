# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC24: Use CloudKit Console to monitor and optimize database activity | Apple — 00:05:33.000

Compare cloud error rates against traffic and platform rather than drawing conclusions from raw counts alone.

[Evidence at 00:05:33.000](https://www.youtube.com/watch?v=EImMro_8TLQ&t=333s). Caption anchor: “so I expect there to always be”.

### WWDC22: Optimize your use of Core Data and CloudKit | Apple — 00:14:48.000

Use object identifiers and bounded materialization to avoid loading whole attachment graphs unnecessarily.

[Evidence at 00:14:48.000](https://www.youtube.com/watch?v=C1a1ULZlzMI&t=888s). Caption anchor: “Instead of verifying by fetching posts, I”.

### WWDC23: Sync to iCloud with CKSyncEngine | Apple — 00:09:20.000

Use automatic sync scheduling normally and manual control for specific coordinated tests or justified cases.

[Evidence at 00:09:20.000](https://www.youtube.com/watch?v=BUFaXlNYokA&t=560s). Caption anchor: “Manually syncing can also be useful when”.

### WWDC21: Build apps that share data through CloudKit and Core Data  | Apple — 00:14:40.000

Read-only cloud sharing must prevent participant mutation at the actual sharing boundary.

[Evidence at 00:14:40.000](https://www.youtube.com/watch?v=1BDDD1UY2fk&t=880s). Caption anchor: “but this time, I want the share”.

### Current documentation checked

- [Official accountchange%28_%3A%29 documentation](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange%28_%3A%29).
- [Official addpendingrecordzonechanges%3A documentation](https://developer.apple.com/documentation/cloudkit/cksyncenginestate/addpendingrecordzonechanges%3A).
- [Official remove%28pendingrecordzonechanges%3A%29 documentation](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class/remove%28pendingrecordzonechanges%3A%29).
- [Official accountchange documentation](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
