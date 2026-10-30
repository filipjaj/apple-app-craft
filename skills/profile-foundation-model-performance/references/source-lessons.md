# Source lessons

Reviewed the complete English caption transcript of Optimize your app’s speed and efficiency on 2026-10-06, with current official documentation and Context7 discovery. These are transcript-derived lessons; no full video or frames were downloaded/viewed. The source is a multi-part workshop, with OS 26-era examples. Check the project’s installed SDK and model provider.

### 00:33:00.280

Instructions, tools, prompts and output all affect latency and context capacity.

[Evidence at 00:33:00.280](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=1980s). Caption anchor: “finite context window”.

### 00:34:05.679

Request only necessary output to reduce generation work.

[Evidence at 00:34:05.679](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=2045s). Caption anchor: “response length directly affects speed”.

### 00:35:16.520

Showing partial results changes perceived waiting independently of completion time.

[Evidence at 00:35:16.520](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=2116s). Caption anchor: “even if the total generation time is the same”.

### 00:35:40.920

Stable prefixes allow reuse of previous model work.

[Evidence at 00:35:40.920](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=2140s). Caption anchor: “prefix, stays the same”.

### 00:42:33.110

Use comparable device conditions when interpreting model traces.

[Evidence at 00:42:33.110](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=2553s). Caption anchor: “nominal thermal state”.

### 00:43:09.280

Separate loading from inference when diagnosing latency.

[Evidence at 00:43:09.280](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=2589s). Caption anchor: “asset loading”.

### 00:45:14.000

Schema omission is conditional on sufficient previous task guidance.

[Evidence at 00:45:14.000](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=2714s). Caption anchor: “include schema in prompt”.

### 00:46:21.200

Move eligible preparation ahead of the user-triggered request.

[Evidence at 00:46:21.200](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=2781s). Caption anchor: “pre-warming”.

### 00:48:22.120

Simpler generated structures can reduce output overhead.

[Evidence at 00:48:22.120](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=2902s). Caption anchor: “flattening your type hierarchy”.

## Current documentation and interpretation

- [fm runtime](https://developer.apple.com/documentation/foundationmodels/analyzing-the-runtime-performance-of-your-foundation-models-app).
- [fm kv cache](https://developer.apple.com/documentation/foundationmodels/optimizing-key-value-caching-in-language-model-sessions).
- [fm prewarm](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/prewarm(promptprefix:)).

Current prewarm documentation requires at least one second of lead time and makes no immediate-loading guarantee. Current cache documentation describes provider-dependent cache behavior and accuracy risks from history editing. The workshop’s quiz timings are illustrative, not an acceptance target. Session ownership, stale-result rejection, persisted-schema compatibility and cancellation checks are implementation reasoning. Its introductory claim of no token budgets refers to usage billing; finite context capacity still applies, and current PCC/provider availability differs from this OS 26 on-device talk.

Local source provenance: `source-additions/transcripts/yXAQTIKR8fk.md`; current documentation snapshots in `source-additions/documents/`. Source assets are excluded from the portable plugin.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Debug and profile agentic app experiences with Instruments | Apple — 00:08:38.000

Inspect the active instructions and tools in the inference trace when an agent fails to reach the intended task.

[Evidence at 00:08:38.000](https://www.youtube.com/watch?v=ML67J6l8NLs&t=518s). Caption anchor: “the timeline already told us the instruction”.

### WWDC25: Meet the Foundation Models framework | Apple — 00:21:26.000

Measure the source of model latency before changing verbosity or prewarming strategy.

[Evidence at 00:21:26.000](https://www.youtube.com/watch?v=mJMvFyBvZEk&t=1286s). Caption anchor: “it is important to understand all the”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
