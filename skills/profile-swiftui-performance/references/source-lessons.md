# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 8. SwiftUI essentials | Meet with Apple

This session explains SwiftUI's mental model through views as descriptions, values, and rendered pixels. It connects view composition, dependency tracking, and state lifetime to writing understandable, efficient UI code.

[Original session](https://www.youtube.com/watch?v=yqsyBJ1jbz0) · Original library transcript: `transcripts/08-yqsyBJ1jbz0.md`

- Distinguish the view's code description, its particular value, and the pixels produced from it. View structs are lightweight, transient inputs to rendering. [Evidence at 00:00:55.920](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=55s)

- Start with built-in views to inherit contextual behavior such as system colors, platform typography, and Dynamic Type support. [Evidence at 00:04:53.360](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=293s)

- Treat modifiers as wrappers around preceding views. Reordering padding and background changes the result, so modifier order must match your intent. [Evidence at 00:08:25.120](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=505s)

- Compose repeated UI into custom views, then parameterize them with the data they display. This keeps the layout reusable and reduces duplicated code. [Evidence at 00:14:59.920](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=899s)

- SwiftUI tracks the properties read while evaluating a view. Changes invalidate dependent work, so avoid making a large view depend on data that only a small part needs. [Evidence at 00:20:00.960](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=1200s)

- Break complex views into focused components to keep updates efficient and the code easier to reason about. [Evidence at 00:20:15.040](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=1215s)

- Use State for values that must survive updates during a view's lifetime. Understand that persistent state storage and transient view instances have different lifetimes. [Evidence at 00:25:03.200](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=1503s)

Visual examples: [Padding and background order](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=508s) — The code, nested modifier wrappers, and rendered label show padding outside the orange background.; [View dependency tracking](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=1100s) — The SearchRow diagram links its output to photoName and tripName dependencies.; [Persistent state storage](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=1430s) — The stage diagram separates transient view values from persistent state storage.

## 22. WWDC21: Demystify SwiftUI | Apple

Understand how SwiftUI connects ephemeral view values to persistent state and selectively updates a dependency graph.

[Original session](https://www.youtube.com/watch?v=XwdVz0Ef1vU) · Original library transcript: `transcripts/22-XwdVz0Ef1vU.md`

- Distinguish explicit identity supplied by data or IDs from structural identity determined by a view’s type and position. [Evidence at 00:04:21.194](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=261s)

- Preserve one view’s identity when representing different states of the same element, so transitions and state remain continuous. [Evidence at 00:11:30.089](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=690s)

- Prefer ViewBuilder and generic structure over unnecessary AnyView wrappers, which erase information useful to SwiftUI and the compiler. [Evidence at 00:12:42.295](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=762s)

- State storage follows the lifetime of a view’s identity; switching between separately identified branches replaces that storage. [Evidence at 00:22:47.766](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=1367s)

- Choose stable, unique identifiers for dynamic data; computed random IDs and collection offsets can cause incorrect transitions and state loss. [Evidence at 00:34:18.957](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=2058s)

- Treat view inputs as dependencies: a changed input invalidates dependent views, and value comparison can avoid unnecessary downstream work. [Evidence at 00:30:36.468](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=1836s)

- Move a conditional into a modifier such as opacity when the condition represents one view in different states, using an inert value when appropriate. [Evidence at 00:38:26.104](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=2306s)

Visual examples: [AnyView and ViewBuilder](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=765s) — The code contrasts type erasure through AnyView with concrete conditional view types.; [Identity and state lifetime](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=1370s) — The branch code and storage diagram show how view identity controls state lifetime.; [The dependency graph](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=1848s) — The graph connects view nodes to the state values that drive their updates.

## 27. WWDC25: Optimize SwiftUI performance with Instruments | Apple

A measurement-driven walkthrough of formatter caching, granular observation, and the Cause & Effect Graph in Instruments 26.

[Original session](https://www.youtube.com/watch?v=3b1ecu-Jobk) · Original library transcript: `transcripts/27-3b1ecu-Jobk.md`

- Start with the SwiftUI instrument’s Update Groups and long-update lanes to determine whether SwiftUI work is responsible for a responsiveness problem. [Evidence at 00:03:00.643](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=180s)

- Inspect a long body update’s time range in Time Profiler to identify the expensive functions contributing to it. [Evidence at 00:07:10.508](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=430s)

- Move repeated formatting out of view bodies, reuse expensive formatter objects, and cache derived strings when their underlying inputs change. [Evidence at 00:11:50.172](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=710s)

- Consider both individual update cost and total update count: many fast view updates can collectively miss a frame deadline. [Evidence at 00:15:58.182](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=958s)

- Use the Cause & Effect Graph to find what invalidated a declarative view; an imperative call-stack backtrace may not reveal that cause. [Evidence at 00:24:45.311](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=1485s)

- Make observable dependencies granular, such as a favorite status per item, instead of having every row read a shared collection. [Evidence at 00:29:47.902](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=1787s)

- Avoid putting rapidly changing geometry or timer values in the environment, where checks across many dependent views can accumulate. [Evidence at 00:33:59.250](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=2039s)

- Record another trace after a change and verify the expected updates disappeared before treating the performance fix as complete. [Evidence at 00:14:48.120](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=888s)

Visual examples: [Inspecting a slow view body](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=442s) — Instruments shows the slow update interval alongside the Time Profiler call tree.; [Cause & Effect Graph](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=1481s) — The diagram traces a state-change signal through view-body evaluation and rendering.; [Granular observation](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=1799s) — Only the first card depends on the changed favorite value, so the other cards stay unchanged.

## 36. WWDC25: Code-along: Elevate an app with Swift concurrency | Apple

A hands-on progression from main-actor code to measured concurrency improvements, with compiler-guided fixes for unsafe shared mutable state.

[Original session](https://www.youtube.com/watch?v=UoFK7uY9MnY) · Original library transcript: `transcripts/36-UoFK7uY9MnY.md`

- Use asynchronous framework APIs and a view-lifecycle task for photo loading so waiting does not block UI interaction. [Evidence at 00:06:49.420](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=409s)

- Profile expensive computation before introducing parallelism, and distinguish responsiveness from the time it takes to produce results. [Evidence at 00:21:50.047](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=1310s)

- Under the demonstrated main-actor-default configuration, make the processor nonisolated and its entry point @concurrent async to move expensive work into the background. [Evidence at 00:14:51.980](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=891s)

- Use async let for a known set of independent operations, such as sticker extraction and dominant-color computation. [Evidence at 00:16:36.074](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=996s)

- Remove unnecessary mutable sharing by giving each color-extraction task its own extractor instance. [Evidence at 00:20:17.251](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=1217s)

- Capture a Sendable value snapshot for a SwiftUI effect closure instead of accessing main-actor state from background-evaluated code. [Evidence at 00:24:12.431](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=1452s)

- Use a task group for a dynamic number of photo-processing jobs, then collect completed results while keeping model updates in their proper isolation context. [Evidence at 00:28:33.523](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=1713s)

- Account for completion order explicitly: task-group results may arrive in a different order from the input selection. [Evidence at 00:28:22.259](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=1702s)

Visual examples: [Moving processing off the main actor](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=906s) — The processing function now carries concurrent and async annotations to move expensive work off the main actor.; [Parallel extraction with async let](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=1008s) — The diagram places sticker extraction and color extraction on separate concurrent work paths.; [Collecting task-group results](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=1709s) — Child tasks finish independently and feed their results back into the result collection.


## Meet with Apple performance workshop — 2026-10-06

Reviewed the complete supplied caption transcript; no frames or media viewed. Extend the existing measured-responsiveness workflow with selective state dependencies, closure capture diagnosis and hot-path isolation.

### 01:18:33.200

Shared observable state plus narrow display inputs can break broad binding dependencies; migrating every state value is unnecessary.

[Evidence at 01:18:33.200](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=4713s). Caption anchor: “observable macro”.

### 01:21:00.560

Derive the row/card display input outside it so unchanged children can avoid updates.

[Evidence at 01:21:00.560](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=4860s). Caption anchor: “is flipped property”.

### 01:32:03.520

A stored view-builder closure can change by capturing an updated parent even when its resulting content is unchanged.

[Evidence at 01:32:03.520](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=5523s). Caption anchor: “implicitly capturing self”.

### 01:36:36.800

When immediate construction fits the contract, evaluate builders in the initializer and store their resulting views.

[Evidence at 01:36:36.800](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=5796s). Caption anchor: “store the result instead of the closure”.

### 01:40:20.670

Skipped body evaluations still have comparison costs; they are different from creation and executed updates.

[Evidence at 01:40:20.670](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=6020s). Caption anchor: “skipped update”.

### 01:45:34.400

Keep frequently changing geometry in narrowly observed state so the parent can write it without reading it.

[Evidence at 01:45:34.400](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=6334s). Caption anchor: “only writes it”.

### 01:48:28.640

When local State is appropriate, isolate the hot update to its smallest affected view.

[Evidence at 01:48:28.640](https://www.youtube.com/watch?v=yXAQTIKR8fk&t=6508s). Caption anchor: “isolating that state to a smaller view”.

The case study’s update counts and zero-hitch result are examples, not targets for another app. Inspect the actual SDK and trace; do not rewrite all state as Observation or remove legitimate callbacks.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Dive into lazy stacks and scrolling with SwiftUI | Apple — 00:08:08.000

Use focused scroll geometry observations for a real presentation change rather than unrestricted per-frame view work.

[Evidence at 00:08:08.000](https://www.youtube.com/watch?v=4FNbTRr5MtQ&t=488s). Caption anchor: “But the button shouldn't always be visible.”.

### WWDC22: Visualize and optimize Swift concurrency | Apple — 00:04:45.000

Use concurrency traces to investigate UI work that is delayed or fails to complete.

[Evidence at 00:04:45.000](https://www.youtube.com/watch?v=bq4DVvVJ7H8&t=285s). Caption anchor: “or will never finish. We should strive”.

### WWDC26: Profile, fix, and verify: Improve app responsiveness with Instruments | Apple — 00:08:29.000

Sampling can miss a short isolated call; interpret traces against call frequency and reproduction evidence.

[Evidence at 00:08:29.000](https://www.youtube.com/watch?v=uFExeZgEvI0&t=509s). Caption anchor: “Because it started and finished entirely between”.

### WWDC25: Optimize CPU performance with Instruments | Apple — 00:10:02.000

For supported CPU optimization, choose the profiler whose sampling weights actual CPU resource use appropriately.

[Evidence at 00:10:02.000](https://www.youtube.com/watch?v=li0TMRDzyU8&t=602s). Caption anchor: “To avoid this problem, we can switch”.

### WWDC25: Optimize SwiftUI performance with Instruments | Apple — 00:13:02.359

Reuse stable expensive formatters and caches with correct invalidation instead of rebuilding them in every view body.

[Evidence at 00:13:02.359](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=782s). Caption anchor: “Because the format will never change, I”.

### WWDC23: Demystify SwiftUI performance | Apple — 00:08:23.000

Debug-only SwiftUI investigation helpers must not be shipped or treated as supported production APIs.

[Evidence at 00:08:23.000](https://www.youtube.com/watch?v=eytrguSSYN8&t=503s). Caption anchor: “In this case, that means, it is”.

### WWDC22: Link fast: Improve build and launch times | Apple — 00:03:41.000

Understand which static-library objects are linked before attributing build or launch cost to the whole dependency.

[Evidence at 00:03:41.000](https://www.youtube.com/watch?v=yLXGtXNYhdg&t=221s). Caption anchor: “even if only a few of those”.

### WWDC22: Improve app size and runtime performance | Apple — 00:03:33.000

Size-oriented linker options involve runtime tradeoffs and require current toolchain verification and measurement.

[Evidence at 00:03:33.000](https://www.youtube.com/watch?v=bQUIpicLq6o&t=213s). Caption anchor: “even if you use an older OS”.

### WWDC23: Analyze hangs with Instruments | Apple — 00:20:20.000

Lazy containers can reduce eager construction, but verify the actual measured cause before substituting them.

[Evidence at 00:20:20.000](https://www.youtube.com/watch?v=lWVuP3Vts_0&t=1220s). Caption anchor: “even though we only need the first”.

### WWDC21: Understand and eliminate hangs from your app | Apple — 00:10:59.000

Reserve main-thread work for what UI updates actually require to avoid blocking responsiveness.

[Evidence at 00:10:59.000](https://www.youtube.com/watch?v=DYrACtIXe9g&t=659s). Caption anchor: “To ensure performance, it's important the main”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
