# Source lessons

Reviewed the complete English caption transcript of Optimize your app’s speed and efficiency on 2026-10-06, with current official documentation and Context7 discovery. These are transcript-derived lessons; no full video or frames were downloaded/viewed. The source is a multi-part workshop, with OS 26-era examples. Check the project’s installed SDK and model provider.

### 01:51:45.110

Choose metrics connected to the app’s critical user journey; Snap uses tail latency for its own goals.

[Evidence at 01:51:45.110](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=6705s). Caption anchor: “90th percentile”.

### 01:53:36.870

Feature-specific measurements should be straightforward to define.

[Evidence at 01:53:36.870](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=6816s). Caption anchor: “intervals and counters”.

### 01:56:48.400

Differentiate computation from waiting before choosing an optimization.

[Evidence at 01:56:48.400](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=7008s). Caption anchor: “blocked waiting”.

### 01:57:15.160

Correlate named intervals with deeper Instruments data.

[Evidence at 01:57:15.160](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=7035s). Caption anchor: “OS signpost”.

### 01:58:02.080

Prepare the scenario separately from the performance-sensitive operation.

[Evidence at 01:58:02.080](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=7082s). Caption anchor: “setup and measurement blocks”.

### 01:58:51.790

Repeated samples across devices support meaningful regression analysis.

[Evidence at 01:58:51.790](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=7131s). Caption anchor: “statistical analysis”.

### 01:59:33.640

Build changes can create regressions even without changed feature logic.

[Evidence at 01:59:33.640](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=7173s). Caption anchor: “build system migration”.

### 02:01:20.560

Compare generated behavior when traces expose a toolchain/build regression.

[Evidence at 02:01:20.560](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=7280s). Caption anchor: “SIMD versions”.

## Current documentation and interpretation

- [performance measure](https://developer.apple.com/documentation/xctest/xctestcase/measure(metrics:options:block:)).
- [signposter](https://developer.apple.com/documentation/os/ossignposter).

Snap’s cross-platform protobuf pipeline and dashboards are a case study, not prerequisites. Adapt the measurement boundaries and trace correlation to the project’s existing stack. The workshop’s SIMD example demonstrates a confirmed code-generation difference; it does not imply that every build migration needs manual assembly review. Threshold selection, baseline provenance, sufficient sampling and grouping by device are measurement reasoning.

Local source provenance: `source-additions/transcripts/yXAQTIKR8fk.md`; current documentation snapshots in `source-additions/documents/`. Source assets are excluded from the portable plugin.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Meet the new MetricKit | Apple — 00:05:08.000

Subscribe to supported metric streams early and keep their owner alive to avoid missing later reports.

[Evidence at 00:05:08.000](https://www.youtube.com/watch?v=WygVIj420KE&t=308s). Caption anchor: “This setup should be done at app”.

### WWDC22: Track down hangs with Xcode and on-device detection | Apple — 00:08:56.000

Investigate hangs under real on-device conditions, including when the debugger is disconnected.

[Evidence at 00:08:56.000](https://www.youtube.com/watch?v=BAUc15xKw0I&t=536s). Caption anchor: “including in places where I don't always”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
