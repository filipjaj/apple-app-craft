# Source lessons

The full supplied English caption transcripts were reviewed. Notes below paraphrase timestamped evidence; timestamps refer to the matching YouTube and Apple session timelines. API details also draw on official Apple documentation retrieved on 2026-10-05. The videos describe OS 27 APIs; confirm availability against the project’s installed SDK.

## 00:12:27.157 — Xrv8m_EHCbg

Profiles make task-specific context and orchestration explicit.

[Evidence at 00:12:27.157](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=747s). Caption evidence anchor: “dynamic profiles”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## 00:13:23.435 — Xrv8m_EHCbg

Use app-owned state to choose task instructions and tools.

[Evidence at 00:13:23.435](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=803s). Caption evidence anchor: “mode variable”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## 00:14:15.348 — Xrv8m_EHCbg

Choose a model for each task mode rather than using cloud reasoning universally.

[Evidence at 00:14:15.348](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=855s). Caption evidence anchor: “SystemLanguageModel”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## 00:15:02.320 — Xrv8m_EHCbg

A dynamic profile resolves to one active profile at a time.

[Evidence at 00:15:02.320](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=902s). Caption evidence anchor: “single active Profile”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## 00:15:48.283 — Xrv8m_EHCbg

Preserved history requires deliberate privacy and context choices across models.

[Evidence at 00:15:48.283](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=948s). Caption evidence anchor: “privacy boundaries”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## Current documentation

- [Composing dynamic sessions with instructions and profiles](https://developer.apple.com/documentation/foundationmodels/composing-dynamic-sessions-with-instructions-and-profiles): consult for exact API spelling, configuration, and SDK availability.

The companion profile article specifies that dynamic instructions evaluate before requests, exactly one profile is active, value modifiers have precedence while lifecycle callbacks accumulate, and historyTransform changes the request’s view without mutating global history. Transition validation and cancellation checks are implementation reasoning built on these mechanics.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Build agentic app experiences with the Foundation Models framework | Apple — 00:11:41.000

Give mutable session properties deliberate initial values and pass task context to the active profile.

[Evidence at 00:11:41.000](https://www.youtube.com/watch?v=nxW29TKIL0w&t=701s). Caption anchor: “All session properties are mutable and must”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
