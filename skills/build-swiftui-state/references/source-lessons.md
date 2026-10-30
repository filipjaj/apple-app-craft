# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 6. WWDC24: SwiftUI essentials | Apple

SwiftUI views are declarative descriptions that compose into larger interfaces and update as their data changes. The framework combines adaptive components with lower-level customization and interoperability, allowing incremental adoption.

[Original session](https://www.youtube.com/watch?v=HyQgpxX__-A) · Original library transcript: `transcripts/06-HyQgpxX__-A.md`

- Describe the UI you want using value-type views. Use imperative actions to change state, then let SwiftUI update the interface. [Evidence at 00:04:50.212](https://www.youtube.com/watch?v=HyQgpxX__-A&t=290s)

- Compose small reusable views and modifiers. Modifier order defines the resulting hierarchy, and splitting views does not inherently hurt performance. [Evidence at 00:05:17.048](https://www.youtube.com/watch?v=HyQgpxX__-A&t=317s)

- Choose a clear source of truth. Use State for view-owned storage and Binding when a child must read and edit state owned elsewhere. [Evidence at 00:10:49.045](https://www.youtube.com/watch?v=HyQgpxX__-A&t=649s)

- Make animation part of a state change and choose transitions appropriate to the content, such as a numeric transition for a changing score. [Evidence at 00:12:06.405](https://www.youtube.com/watch?v=HyQgpxX__-A&t=726s)

- Use semantic built-in components to gain platform-appropriate behavior, accessibility, and localization. Use previews to inspect different environments quickly. [Evidence at 00:13:19.874](https://www.youtube.com/watch?v=HyQgpxX__-A&t=799s)

- Share views and concepts across platforms, then adapt for each platform's input and layout conventions. A Watch crown or Mac windowing model may require specific treatment. [Evidence at 00:18:58.648](https://www.youtube.com/watch?v=HyQgpxX__-A&t=1138s)

- Adopt SwiftUI incrementally using representable views and hosting controllers to bridge UIKit or AppKit. Combine it with other SDK frameworks as the app needs them. [Evidence at 00:22:00.211](https://www.youtube.com/watch?v=HyQgpxX__-A&t=1320s)

Visual examples: [Modifier order and composition](https://www.youtube.com/watch?v=HyQgpxX__-A&t=409s) — The stacked image variants and modifier arrows show clipping, shadow, and overlay composition.; [State and bindings](https://www.youtube.com/watch?v=HyQgpxX__-A&t=661s) — The @State rating property, button mutations, and numeric label are visible together.; [Adapting across platforms](https://www.youtube.com/watch?v=HyQgpxX__-A&t=1150s) — The platform collage compares different control and navigation treatments rather than repeating one fixed layout.

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

## 23. Flow data through SwiftUI | Meet with Apple

Uses a travel wishlist to explain who owns data, how views observe it, and which storage choices preserve it across launches.

[Original session](https://www.youtube.com/watch?v=Qxv4Tf4-AdU) · Original library transcript: `transcripts/23-Qxv4Tf4-AdU.md`

- Use @State for UI-owned state whose storage follows the view’s identity rather than the short-lived view struct. [Evidence at 00:08:01.039](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=481s)

- Pass a binding when a child view or control must both read and update state owned elsewhere. [Evidence at 00:10:04.800](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=604s)

- Make reference-based models observable so views update when the model properties they actually read change. [Evidence at 00:15:53.600](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=953s)

- Own a shared data source near the app root and inject it into the environment when passing it through many intermediary views becomes cumbersome. [Evidence at 00:19:18.240](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=1158s)

- Store small preferences with @AppStorage so choices such as sort order survive navigation and app launches. [Evidence at 00:22:23.360](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=1343s)

- Use SwiftData @Model for persistent model objects, refining relationships and delete rules to match the domain. [Evidence at 00:26:15.039](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=1575s)

- Replace manual data-source lookups with appropriately sorted or filtered @Query results, and configure a model container at the app level. [Evidence at 00:27:56.640](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=1676s)

Visual examples: [State storage and identity](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=477s) — The storage table ties a persistent state value to a stable view identity.; [Observable property dependencies](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=949s) — The computed photoURL property illustrates dependencies on observable model properties.; [SwiftData relationships](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=1587s) — The model code highlights cascade deletion and inverse relationships.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### SwiftUI essentials | Meet with Apple — 00:08:01.680

Modifier order changes the view being wrapped; inspect that order when behavior is surprising.

[Evidence at 00:08:01.680](https://www.youtube.com/watch?v=yqsyBJ1jbz0&t=481s). Caption anchor: “in the view hierarchy. One final note”.

### WWDC24: Demystify SwiftUI containers | Apple — 00:03:12.000

Design a container's composition contract explicitly rather than limiting it accidentally to one data collection.

[Evidence at 00:03:12.000](https://www.youtube.com/watch?v=LWbgpheCqgo&t=192s). Caption anchor: “only allowing cards to be constructed from”.

### WWDC24: SwiftUI essentials | Apple — 00:04:43.318

SwiftUI views describe current UI state and are not persistent imperative view objects.

[Evidence at 00:04:43.318](https://www.youtube.com/watch?v=HyQgpxX__-A&t=283s). Caption anchor: “of what the current state of the”.

### Flow data through SwiftUI | Meet with Apple — 00:05:35.120

Drive presentation and enabled state from the same intentional state owner.

[Evidence at 00:05:35.120](https://www.youtube.com/watch?v=Qxv4Tf4-AdU&t=335s). Caption anchor: “tapping the button should always make the”.

### WWDC26: Use SwiftUI with AppKit and UIKit | Apple — 00:02:43.000

A mixed native/SwiftUI control should reflect one coherent value across all dependent components.

[Evidence at 00:02:43.000](https://www.youtube.com/watch?v=EANNnEFUOQ0&t=163s). Caption anchor: “or color well, but is displayed inline”.

### WWDC23: Discover Observation in SwiftUI | Apple — 00:03:56.000

Observation tracks properties actually read by the view and can reduce unrelated body updates.

[Evidence at 00:03:56.000](https://www.youtube.com/watch?v=W6FF70H_GwI&t=236s). Caption anchor: “Tracking things like that let your UI”.

### WWDC24: What’s new in SwiftUI | Apple — 00:13:53.000

Use supported environment and focused-value declarations without changing the intended ownership or scope.

[Evidence at 00:13:53.000](https://www.youtube.com/watch?v=CNMRV0F0w74&t=833s). Caption anchor: “Instead of having to write out a”.

### WWDC21: Demystify SwiftUI | Apple — 00:09:21.694

Structural identity determines which conditional view state persists across updates.

[Evidence at 00:09:21.694](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=561s). Caption anchor: “while the second view only shows when”.

### WWDC20: Data Essentials in SwiftUI | Apple — 00:05:34.000

State lifetime survives transient view values when owned at the appropriate identity boundary.

[Evidence at 00:05:34.000](https://www.youtube.com/watch?v=V2yKZHrXRYA&t=334s). Caption anchor: “Why is that important? Well, remember that”.

### WWDC25: What’s new in Swift | Apple — 00:13:42.000

Keep related synchronous state updates coherent so observers do not consume intermediate inconsistent values.

[Evidence at 00:13:42.000](https://www.youtube.com/watch?v=Pvf8OLnAUGI&t=822s). Caption anchor: “to other properties between these two points”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
