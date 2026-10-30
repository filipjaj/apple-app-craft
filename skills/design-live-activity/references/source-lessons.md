# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 2. WWDC23: Design dynamic Live Activities  | Apple

Live Activities help people follow ongoing events without repeatedly opening an app. The session shows how to adapt the same activity to the Lock Screen, StandBy, and Dynamic Island while keeping it useful at a glance.

[Original session](https://www.youtube.com/watch?v=m6WMwSj_EbA) · Original library transcript: `transcripts/02-m6WMwSj_EbA.md`

- Prioritize the information someone needs at a glance. Build a layout specific to the activity, with buttons only for essential controls. [Evidence at 00:02:00.821](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=120s)

- Carry your app's identity into the activity through color, type, and graphics. Integrate a logo into the layout instead of inserting the entire app icon. [Evidence at 00:03:18.432](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=198s)

- Keep the Lock Screen presentation compact and change its height as relevant information appears or disappears. [Evidence at 00:04:05.612](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=245s)

- Use transitions to explain updates: numeric transitions for changing numbers and replacement or position transitions for changing content. Alert only when an update needs attention. [Evidence at 00:04:47.721](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=287s)

- Check StandBy at its larger display scale. Use sufficiently sharp assets, avoid artwork that breaks when the background extends, and verify contrast in night mode. [Evidence at 00:06:18.378](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=378s)

- Fit content to the Dynamic Island's rounded geometry. Maintain concentric margins, avoid wasted space, and wrap expanded content closely around the sensor region. [Evidence at 00:09:56.396](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=596s)

- Give compact, expanded, and minimal presentations meaningful information. Preserve relative placement between compact and expanded layouts, and avoid reducing the minimal view to a logo. [Evidence at 00:14:01.608](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=841s)

- Remove an ended activity after a short delay so stale information does not accumulate on the Lock Screen. [Evidence at 00:05:49.249](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=349s)

Visual examples: [StandBy presentation](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=381s) — The tide graph demonstrates how a Live Activity uses the larger horizontal StandBy canvas.; [Dynamic Island geometry](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=599s) — The inset outline follows the sensor cutout and the rounded outer boundary.; [Compact, expanded, and minimal](https://www.youtube.com/watch?v=m6WMwSj_EbA&t=844s) — The minimal delivery icon carries activity-specific meaning inside the small circular presentation.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Live Activities essentials | Apple — 00:08:26.000

Define when ongoing activity content becomes stale and show that state meaningfully.

[Evidence at 00:08:26.000](https://www.youtube.com/watch?v=Wco2do-tfI4&t=506s). Caption anchor: “A staleDate lets you specify when this”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
