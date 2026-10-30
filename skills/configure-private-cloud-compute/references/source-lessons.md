# Source lessons

The full supplied English caption transcripts were reviewed. Notes below paraphrase timestamped evidence; timestamps refer to the matching YouTube and Apple session timelines. API details also draw on official Apple documentation retrieved on 2026-10-05. The videos describe OS 27 APIs; confirm availability against the project’s installed SDK.

## 00:03:50.815 — 8a6pWfkYPuA

Check model availability and provide a graceful alternative.

[Evidence at 00:03:50.815](https://www.youtube.com/watch?v=8a6pWfkYPuA&t=230s). Caption evidence anchor: “availability API”. Local source provenance: `source-additions/transcripts/8a6pWfkYPuA.txt`.

## 00:04:15.517 — 8a6pWfkYPuA

Model choice changes connectivity requirements and daily limits.

[Evidence at 00:04:15.517](https://www.youtube.com/watch?v=8a6pWfkYPuA&t=255s). Caption evidence anchor: “requires an internet connection”. Local source provenance: `source-additions/transcripts/8a6pWfkYPuA.txt`.

## 00:05:49.287 — 8a6pWfkYPuA

Reasoning consumes the context budget and affects latency.

[Evidence at 00:05:49.287](https://www.youtube.com/watch?v=8a6pWfkYPuA&t=349s). Caption evidence anchor: “reasoning is extra text”. Local source provenance: `source-additions/transcripts/8a6pWfkYPuA.txt`.

## 00:08:27.560 — 8a6pWfkYPuA

Quota status belongs in persistent task UI with useful recovery.

[Evidence at 00:08:27.560](https://www.youtube.com/watch?v=8a6pWfkYPuA&t=507s). Caption evidence anchor: “integrate this with your existing UI”. Local source provenance: `source-additions/transcripts/8a6pWfkYPuA.txt`.

## 00:09:06.091 — 8a6pWfkYPuA

Simulate approaching and exhausted quotas during verification.

[Evidence at 00:09:06.091](https://www.youtube.com/watch?v=8a6pWfkYPuA&t=546s). Caption evidence anchor: “debug option”. Local source provenance: `source-additions/transcripts/8a6pWfkYPuA.txt`.

## Current documentation

- [Adding server-side intelligence with Private Cloud Compute](https://developer.apple.com/documentation/foundationmodels/adding-server-side-intelligence-with-private-cloud-compute): consult for exact API spelling, configuration, and SDK availability.

The supplied PCC article lists a managed entitlement, model availability checks, persistent quotaUsage status and optional limitIncreaseSuggestion, quotaLimitReached error handling, and Xcode quota simulation. It distinguishes daily quota exhaustion from rate limiting. The article’s on-device fallback requires a task that still fits the destination model; this skill adds explicit budgeting and duplicate-effect checks as implementation reasoning.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Build with the new Apple Foundation Model on Private Cloud Compute | Apple — 00:08:27.560

Present persistent usage-limit state within the feature instead of a dismissible alert that loses context.

[Evidence at 00:08:27.560](https://www.youtube.com/watch?v=8a6pWfkYPuA&t=507s). Caption anchor: “You should integrate this with your existing”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
