# Source lessons

The full supplied English caption transcripts were reviewed. Notes below paraphrase timestamped evidence; timestamps refer to the matching YouTube and Apple session timelines. API details also draw on official Apple documentation retrieved on 2026-10-05. The videos describe OS 27 APIs; confirm availability against the project’s installed SDK.

## 00:06:20.936 — 8a6pWfkYPuA

Model and reasoning choices should follow measured feature quality.

[Evidence at 00:06:20.936](https://www.youtube.com/watch?v=8a6pWfkYPuA&t=380s). Caption evidence anchor: “based on data”. Local source provenance: `source-additions/transcripts/8a6pWfkYPuA.txt`.

## 00:16:06.810 — Xrv8m_EHCbg

Repeated evaluation is necessary because responses vary.

[Evidence at 00:16:06.810](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=966s). Caption evidence anchor: “inherently non-deterministic”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## 00:16:24.122 — Xrv8m_EHCbg

Evaluate prompt changes for quality and regressions.

[Evidence at 00:16:24.122](https://www.youtube.com/watch?v=Xrv8m_EHCbg&t=984s). Caption evidence anchor: “quantify accuracy”. Local source provenance: `source-additions/transcripts/Xrv8m_EHCbg.txt`.

## Current documentation

- [Evaluations](https://developer.apple.com/documentation/evaluations): consult for exact API spelling, configuration, and SDK availability.
- [Designing effective evaluations](https://developer.apple.com/documentation/evaluations/designing-effective-evaluations): consult for exact API spelling, configuration, and SDK availability.

The companion evaluation article supports representative challenge datasets, computable versus model-judge criteria, inspecting raw outputs, versioned comparisons, and holdout checks against overfitting. The overview video establishes the need for evaluation; it is not a full Evaluations API tutorial.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Improve your prompts by hill-climbing with Evaluations | Apple — 00:24:29.000

Change one meaningful variable at a time so evaluation results can explain the source of an improvement.

[Evidence at 00:24:29.000](https://www.youtube.com/watch?v=sNDkT9mYDTQ&t=1469s). Caption anchor: “Hill-climbing works best when you focus on”.

### WWDC26: Meet the Evaluations framework | Apple — 00:11:30.000

Evaluation samples should represent varied lengths and content types from the intended task.

[Evidence at 00:11:30.000](https://www.youtube.com/watch?v=sexp6TEkoWU&t=690s). Caption anchor: “so our reviews should be different lengths.”.

### WWDC26: Create robust evaluations for agentic apps | Apple — 00:17:55.000

Evaluate forbidden tool calls as failures, not just whether the final output sounds useful.

[Evidence at 00:17:55.000](https://www.youtube.com/watch?v=YPJd4AV8Om0&t=1075s). Caption anchor: “Sometimes what an agent shouldn't do is”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
