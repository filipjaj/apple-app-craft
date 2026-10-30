# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 13. WWDC26: What’s new in Swift | Apple

The session surveys Swift language, library, tooling, and interoperability updates, then examines advanced performance features. Its recurring theme is making code more expressive while preserving safety across platforms and constrained environments.

[Original session](https://www.youtube.com/watch?v=ssppiors2Ak) · Original library transcript: `transcripts/13-ssppiors2Ak.md`

- Use targeted compiler diagnostics to manage specific warnings within a declaration. Avoid silencing unrelated warnings throughout a project. [Evidence at 00:03:02.920](https://www.youtube.com/watch?v=ssppiors2Ak&t=182s)

- Use explicit module selection to resolve genuine naming conflicts, while still designing APIs with clear names. [Evidence at 00:04:47.493](https://www.youtube.com/watch?v=ssppiors2Ak&t=287s)

- Treat cancellation deliberately. Shield only short operations that must finish or roll back to preserve a consistent state. [Evidence at 00:06:47.427](https://www.youtube.com/watch?v=ssppiors2Ak&t=407s)

- Use testing features to report non-blocking issues, cancel unsuitable parameter cases, and investigate flaky tests through repetition. Account for XCTest and Swift Testing interoperability during migration. [Evidence at 00:08:34.905](https://www.youtube.com/watch?v=ssppiors2Ak&t=514s)

- Use supported language bridges to adopt Swift within existing C, C++, Java, and JavaScript systems, sharing code where platform needs allow it. [Evidence at 00:12:22.700](https://www.youtube.com/watch?v=ssppiors2Ak&t=742s)

- Evaluate WebAssembly and Embedded Swift with binary size and platform constraints in mind. Code reuse across environments still requires attention to available language features. [Evidence at 00:19:23.766](https://www.youtube.com/watch?v=ssppiors2Ak&t=1163s)

- Apply explicit inlining or specialization only when performance-sensitive code warrants it. These optimizations can increase code size without improving speed. [Evidence at 00:20:52.427](https://www.youtube.com/watch?v=ssppiors2Ak&t=1252s)

- Use ownership and borrowing features to avoid unnecessary copying while retaining compiler-checked exclusivity and lifetime guarantees. [Evidence at 00:24:35.881](https://www.youtube.com/watch?v=ssppiors2Ak&t=1475s)

- Prefer safe storage-access tools over unsafe pointers where suitable. Borrowing iteration, borrow/mutate accessors, and reference types offer ways to work with existing storage efficiently. [Evidence at 00:28:43.044](https://www.youtube.com/watch?v=ssppiors2Ak&t=1723s)

Visual examples: [Cancellation and consistency](https://www.youtube.com/watch?v=ssppiors2Ak&t=410s) — The cancellation shield encloses sending the emergency packet while the radio checks cancellation.; [Inlining and specialization](https://www.youtube.com/watch?v=ssppiors2Ak&t=1264s) — The histogram example highlights the specific region where inlining is controlled.; [Ownership and borrowing](https://www.youtube.com/watch?v=ssppiors2Ak&t=1487s) — The diagram connects a borrowing component to the existing value tree and shows the protected access boundary.

## 21. WWDC25: Embracing Swift concurrency | Apple

A practical model for growing a single-threaded Swift app into a concurrent app while preserving isolation and safe ownership.

[Original session](https://www.youtube.com/watch?v=u2rYp8AMuSg) · Original library transcript: `transcripts/21-u2rYp8AMuSg.md`

- Start with straightforward main-actor code and introduce concurrency only when the application needs it. [Evidence at 00:01:12.737](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=72s)

- Use async/await for operations that can suspend; suspension lets other work progress without automatically moving your code off the main actor. [Evidence at 00:06:27.562](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=387s)

- Keep operations that require a specific order in one task, rather than creating independent tasks for each step. [Evidence at 00:09:13.584](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=553s)

- Profile expensive work and improve the algorithm before adding concurrency. [Evidence at 00:10:17.528](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=617s)

- Use @concurrent for expensive computation that should run in the background; keep UI and cache decisions in their appropriate isolation context. [Evidence at 00:11:16.728](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=676s)

- Choose Sendable value types or isolated actors for concurrent sharing; finish modifying a non-Sendable object before safely transferring it to another task. [Evidence at 00:23:13.378](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=1393s)

- Configure the project’s Approachable Concurrency and default isolation settings deliberately; the session’s main-actor defaults depend on build settings. [Evidence at 00:26:53.559](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=1613s)

Visual examples: [Suspension and interleaving](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=399s) — The dotted gap between fetching and decoding illustrates suspension at await.; [Background computation](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=679s) — The code separates a MainActor UI function from concurrent image decoding.; [Safe transfer of mutable objects](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=1277s) — The compiler flags a data race when mutable image state is changed after sending it to the main actor.

## 26. WWDC25: Explore concurrency in SwiftUI | Apple

Read actor isolation and Sendable requirements as descriptions of runtime behavior, then separate time-sensitive view updates from asynchronous model work.

[Original session](https://www.youtube.com/watch?v=Ttxz8bVvX3s) · Original library transcript: `transcripts/26-Ttxz8bVvX3s.md`

- Understand that View conformance supplies main-actor isolation to view members and supports interoperability with UIKit and AppKit. [Evidence at 00:03:17.894](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=197s)

- Read SwiftUI’s concurrency annotations as descriptions of runtime semantics, including places where custom code may run on a background thread. [Evidence at 00:06:58.495](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=418s)

- Keep Shape, Layout, visual-effect, and geometry calculations independent of mutable actor-isolated state when their APIs permit background evaluation. [Evidence at 00:11:31.435](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=691s)

- Capture a Sendable value snapshot when a background-capable closure needs a Boolean or similar input, instead of reading an isolated property through self. [Evidence at 00:16:07.777](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=967s)

- Update loading indicators and time-sensitive animations synchronously before starting asynchronous work. [Evidence at 00:17:51.877](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=1071s)

- Remember that an await may suspend past a display deadline, causing a gesture-linked animation to feel delayed. [Evidence at 00:21:11.246](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=1271s)

- Bridge asynchronous model work and synchronous view logic with state; this also makes non-UI concurrency easier to test independently. [Evidence at 00:24:15.563](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=1455s)

Visual examples: [Background-capable SwiftUI APIs](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=703s) — The API declarations mark geometry callbacks as Sendable and nonisolated.; [Capturing a Sendable snapshot](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=979s) — The diagram shows a copied Boolean captured for a background closure rather than reading isolated state.; [Suspension and frame deadlines](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=1274s) — The timeline places awaited work across a frame deadline, explaining a delayed animation update.

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

## 40. WWDC24: Migrate your app to Swift 6 | Apple

Use compiler diagnostics to make isolation and ownership explicit, preserving runtime guarantees while replacing temporary interoperability assumptions where possible.

[Original session](https://www.youtube.com/watch?v=75-c6jSE8kU) · Original library transcript: `transcripts/40-75-c6jSE8kU.md`

- Distinguish installing a Swift 6 compiler from enabling Swift 6 language mode; the compiler preserves source compatibility until stricter checking is requested. [Evidence at 00:06:33.433](https://www.youtube.com/watch?v=75-c6jSE8kU&t=393s)

- Migrate one target at a time: enable complete concurrency checking in Swift 5 mode, resolve warnings, then enable Swift 6 to preserve the guarantees. [Evidence at 00:07:28.235](https://www.youtube.com/watch?v=75-c6jSE8kU&t=448s)

- Separate substantial architecture refactoring from the migration so each set of changes remains manageable. [Evidence at 00:08:26.435](https://www.youtube.com/watch?v=75-c6jSE8kU&t=506s)

- Eliminate mutable global state when possible, or isolate it to an actor; use nonisolated(unsafe) only with a separately justified safety mechanism. [Evidence at 00:15:09.000](https://www.youtube.com/watch?v=75-c6jSE8kU&t=909s)

- Correct protocol isolation when you control a callback API; otherwise use an actor hop for arbitrary callbacks or a checked isolation assumption only for a known runtime guarantee. [Evidence at 00:24:17.859](https://www.youtube.com/watch?v=75-c6jSE8kU&t=1457s)

- Remove temporary @preconcurrency conformance annotations when the upstream protocol gains the appropriate actor isolation. [Evidence at 00:27:05.708](https://www.youtube.com/watch?v=75-c6jSE8kU&t=1625s)

- Make public value types explicitly Sendable when that is a guarantee you intend to offer clients; one root fix can remove many dependent diagnostics. [Evidence at 00:33:02.584](https://www.youtube.com/watch?v=75-c6jSE8kU&t=1982s)

- For legacy callbacks with dynamic threading rules, establish and verify those rules at construction time rather than assuming all delegates run on the main actor. [Evidence at 00:39:00.181](https://www.youtube.com/watch?v=75-c6jSE8kU&t=2340s)

Visual examples: [Incremental migration settings](https://www.youtube.com/watch?v=75-c6jSE8kU&t=752s) — The target build settings show Strict Concurrency Checking set to Complete.; [Checking legacy callback isolation](https://www.youtube.com/watch?v=75-c6jSE8kU&t=1460s) — MainActor.assumeIsolated checks the isolation assumption inside a legacy delegate callback.; [Public Sendable types](https://www.youtube.com/watch?v=75-c6jSE8kU&t=2019s) — Adding Sendable to the public Drink struct exposes a warning about a non-Sendable stored property.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: Explore concurrency in SwiftUI | Apple — 00:17:34.129

Update visible loading state synchronously before starting long asynchronous work.

[Evidence at 00:17:34.129](https://www.youtube.com/watch?v=Ttxz8bVvX3s&t=1054s). Caption anchor: “It’s extra important if your app has”.

### WWDC21: Explore structured concurrency in Swift | Apple — 00:12:24.000

If cancellation can return partial results, make that contract explicit to callers.

[Evidence at 00:12:24.000](https://www.youtube.com/watch?v=nyuq9qc-2H8&t=744s). Caption anchor: “a dictionary with only some of the”.

### WWDC26: What’s new in Swift | Apple — 00:06:43.461

Keep supported cancellation-shielded regions short and limited to finishing or rolling back started work.

[Evidence at 00:06:43.461](https://www.youtube.com/watch?v=ssppiors2Ak&t=403s). Caption anchor: “Inside of the shield, task cancellation checks”.

### WWDC25: Embracing Swift concurrency | Apple — 00:03:51.636

Use actor isolation to protect UI-owned state; inspect actual language and isolation settings.

[Evidence at 00:03:51.636](https://www.youtube.com/watch?v=u2rYp8AMuSg&t=231s). Caption anchor: “because there is only one main thread”.

### WWDC25: Code-along: Elevate an app with Swift concurrency | Apple — 00:18:03.557

Isolate mutable image-processing state that is unsafe to access concurrently.

[Evidence at 00:18:03.557](https://www.youtube.com/watch?v=UoFK7uY9MnY&t=1083s). Caption anchor: “The only property the PhotoProcessor stores is”.

### WWDC21: Swift concurrency: Behind the scenes | Apple — 00:11:46.000

Cooperative execution has a bounded thread model; do not block its workers waiting for async progress.

[Evidence at 00:11:46.000](https://www.youtube.com/watch?v=f-re0WpYzZo&t=706s). Caption anchor: “instead of performing a full thread context”.

### WWDC23: Beyond the basics of structured concurrency | Apple — 00:05:19.000

Cancellation is cooperative and needs checks or appropriate handlers at useful boundaries.

[Evidence at 00:05:19.000](https://www.youtube.com/watch?v=Ce0GsaRCMew&t=319s). Caption anchor: “asynchronous or synchronous, that should react to”.

### WWDC22: Eliminate data races using Swift Concurrency | Apple — 00:07:35.000

Reference-type Sendable claims require genuine safety, not merely adding a conformance to mutable storage.

[Evidence at 00:07:35.000](https://www.youtube.com/watch?v=xFvZ1CwEFnI&t=455s). Caption anchor: “Classes are reference types, so they can”.

### WWDC24: Migrate your app to Swift 6 | Apple — 00:15:04.547

Unsafe isolation escape hatches are a last resort; prefer compiler-checked sharing.

[Evidence at 00:15:04.547](https://www.youtube.com/watch?v=75-c6jSE8kU&t=904s). Caption anchor: “this puts the burden on you to”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
