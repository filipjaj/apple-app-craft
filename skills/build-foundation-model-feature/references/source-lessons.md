# Source lessons

The full supplied English caption transcripts were reviewed. Notes below paraphrase timestamped evidence; timestamps refer to the matching YouTube and Apple session timelines. API details also draw on official Apple documentation retrieved on 2026-10-05. The videos describe OS 27 APIs; confirm availability against the project’s installed SDK.

## 00:02:45.684 — Xrv8m_EHCbg

Use reported model capacity and token counts rather than assuming every device has the same budget.

[Evidence at 00:02:45.684](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=165s). Caption evidence anchor: “context size”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## 00:03:39.482 — Xrv8m_EHCbg

Image prompts combine task instructions with an attachment; orientation and input choice matter.

[Evidence at 00:03:39.482](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=219s). Caption evidence anchor: “image attachment”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## 00:08:30.075 — Xrv8m_EHCbg

Provider interchangeability does not erase separate authentication, billing, or data policies.

[Evidence at 00:08:30.075](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=510s). Caption evidence anchor: “never store private keys”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## 00:09:41.158 — Xrv8m_EHCbg

Choose precision tools and grounded retrieval only when they serve the feature.

[Evidence at 00:09:41.158](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=581s). Caption evidence anchor: “BarcodeReaderTool”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## Current documentation

- [Analyzing images with multimodal prompting](https://developer.apple.com/documentation/foundationmodels/analyzing-images-with-multimodal-prompting): consult for exact API spelling, configuration, and SDK availability.
- [Expanding generation with tool calling](https://developer.apple.com/documentation/foundationmodels/expanding-generation-with-tool-calling): consult for exact API spelling, configuration, and SDK availability.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: Code-along: Bring on-device AI to your app using the Foundation Models framework | Apple — 00:16:28.000

Check actual model availability and provide useful behavior when the assumed model is unavailable.

[Evidence at 00:16:28.000](https://www.youtube.com/watch?v=XuX66Oljro0&t=988s). Caption anchor: “Don’t worry - later on I’ll show”.

### WWDC26: What’s new in the Foundation Models framework | Apple — 00:08:30.075

Fetch provider credentials securely rather than embedding private keys in the application binary.

[Evidence at 00:08:30.075](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=510s). Caption anchor: “Remember, never store private keys in your”.

### WWDC25: Deep dive into the Foundation Models framework | Apple — 00:12:44.000

Use schema guides to describe the intended meaning of generated fields and still validate the task result.

[Evidence at 00:12:44.000](https://www.youtube.com/watch?v=6Wgg7DIY29E&t=764s). Caption anchor: “We can say our name should be”.

### Code along with the Foundation Models framework | Meet with Apple — 00:33:36.000

Guided generation expresses nested result structure rather than relying on free-form text parsing alone.

[Evidence at 00:33:36.000](https://www.youtube.com/watch?v=S5F196tqRMI&t=2016s). Caption anchor: “This itinerary object should contain an array”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
