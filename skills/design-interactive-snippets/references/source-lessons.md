# Source lessons

Reviewed the complete publisher English transcript for WWDC25: Design interactive snippets, plus the official implementation article on 2026-10-06. One representative confirmation frame was inspected; the full video was not watched continuously. Design guidance from a session is not a guarantee of current API availability.

## 00:01:40.257

Use readable type and deliberate spacing for glanceable task information.

[Evidence at 00:01:40.257](https://www.youtube.com/watch?v=AP2kex2cGJI&t=100s). Caption anchor: “type size”.

## 00:02:24.853

Keep the routine task concise and link to deeper app content; preserve larger-text usability.

[Evidence at 00:02:24.853](https://www.youtube.com/watch?v=AP2kex2cGJI&t=144s). Caption anchor: “340 points”.

## 00:03:41.744

Reflect the actual app state and provide feedback after follow-up actions.

[Evidence at 00:03:41.744](https://www.youtube.com/watch?v=AP2kex2cGJI&t=221s). Caption anchor: “updated data”.

## 00:04:51.322

Separate displaying outcomes from requesting commitment; customization buttons alone do not place the order.

[Evidence at 00:04:51.322](https://www.youtube.com/watch?v=AP2kex2cGJI&t=291s). Caption anchor: “results and confirmations”.

## 00:06:10.098

Support people who are listening without looking at the screen.

[Evidence at 00:06:10.098](https://www.youtube.com/watch?v=AP2kex2cGJI&t=370s). Caption anchor: “Dialog is what Siri speaks”.

## 00:06:28.954

The visual snippet must explain the task without relying on spoken dialog.

[Evidence at 00:06:28.954](https://www.youtube.com/watch?v=AP2kex2cGJI&t=388s). Caption anchor: “understandable on its own”.

## Implementation and lifecycle

[Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets) supplies the implementation mechanics: return SnippetIntent alongside existing typed values; use intent-backed controls; repeatedly render from shared app state without side effects; request confirmation before continuing the final operation. It also notes that some Siri AI paths omit dialog or snippet presentation, and that reload can present a snippet while dismissing another. Verify exact signatures and availability in the installed SDK.

The lifecycle, compatibility, and reload guidance comes from this companion article rather than the design video. The safeguards against duplicate writes and accidental replacement are implementation reasoning based on those documented mechanics.

Local provenance: `source-additions/transcripts/AP2kex2cGJI.md` and `source-additions/documents/displaying-static-and-interactive-snippets.md`. The runtime skill does not depend on local video files.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: Design interactive snippets | Apple — 00:01:19.445

Make compact system interactions concise enough to understand in the current moment.

[Evidence at 00:01:19.445](https://www.youtube.com/watch?v=AP2kex2cGJI&t=79s). Caption anchor: “Then, we’ll learn how to make concise”.

### WWDC26: Explore advanced App Intents features for Siri and Apple Intelligence | Apple — 00:03:01.000

A spoken response must explain the outcome independently of visual supporting content.

[Evidence at 00:03:01.000](https://www.youtube.com/watch?v=vyfRyVCVsiY&t=181s). Caption anchor: “I'll also change the IntentResult by passing”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
