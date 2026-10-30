# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 9. WWDC26: Create UI prototypes using agents in Xcode | Apple

Coding agents and Xcode previews can shorten the feedback loop for UI prototyping. The session demonstrates exploring divergent designs, testing realistic content, and tuning interaction details while keeping creative judgment with the designer.

[Original session](https://www.youtube.com/watch?v=QleOvMW9vTU) · Original library transcript: `transcripts/09-QleOvMW9vTU.md`

- Specify features and stylistic intent before asking for a generated UI. Vague prompts can anchor the project to arbitrary layouts and unwanted features. [Evidence at 00:04:01.860](https://www.youtube.com/watch?v=QleOvMW9vTU&t=241s)

- Ask for multiple distinctly named previews. Compare alternatives, identify promising elements, and remix them through further iterations. [Evidence at 00:06:39.940](https://www.youtube.com/watch?v=QleOvMW9vTU&t=399s)

- Populate prototypes with believable content so the design can be evaluated in realistic use, including long text and large collections. [Evidence at 00:08:58.040](https://www.youtube.com/watch?v=QleOvMW9vTU&t=538s)

- Explicitly explore empty states and other edge cases. Keep sample models reusable and editable so later prototypes can share them. [Evidence at 00:08:27.180](https://www.youtube.com/watch?v=QleOvMW9vTU&t=507s)

- Get feedback from people using the prototype. Generated sample content is useful preparation, but real use reveals how the experience works for its audience. [Evidence at 00:11:07.820](https://www.youtube.com/watch?v=QleOvMW9vTU&t=667s)

- Build a tuning panel when repeatedly editing animation constants becomes cumbersome. Expose the parameters that affect the feel of the interaction. [Evidence at 00:14:04.700](https://www.youtube.com/watch?v=QleOvMW9vTU&t=844s)

- Break complex animations into named phases and tune delays or springs in isolation. A side-by-side panel keeps the controls and the result visible together. [Evidence at 00:14:34.120](https://www.youtube.com/watch?v=QleOvMW9vTU&t=874s)

- Keep ownership of product and design decisions. Use agents to explore and implement possibilities while you assess which experience serves people best. [Evidence at 00:02:33.740](https://www.youtube.com/watch?v=QleOvMW9vTU&t=153s)

Visual examples: [Comparing preview alternatives](https://www.youtube.com/watch?v=QleOvMW9vTU&t=411s) — The collage shows substantially different card and progress-layout directions for the same prototype.; [Prototyping edge cases](https://www.youtube.com/watch?v=QleOvMW9vTU&t=595s) — The Xcode preview presents one generated edge-case variant alongside its reusable model code.; [Tuning animation phases](https://www.youtube.com/watch?v=QleOvMW9vTU&t=834s) — The tuning panel exposes animation controls on the running phone prototype.

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

## 37. SwiftUI in motion | Meet with Apple

Choose motion tools that preserve context, explain changes, and guide attention, starting with effects supplied by standard controls.

[Original session](https://www.youtube.com/watch?v=koVinhvGLQo) · Original library transcript: `transcripts/37-koVinhvGLQo.md`

- Start with built-in navigation, sheet, scroll, and symbol behavior, then refine those effects to fit the application. [Evidence at 00:02:22.640](https://www.youtube.com/watch?v=koVinhvGLQo&t=142s)

- Connect a zoom transition’s source and destination with a namespace and matching identifier; target a meaningful shared thumbnail when appropriate. [Evidence at 00:04:40.479](https://www.youtube.com/watch?v=koVinhvGLQo&t=280s)

- Combine scroll target behavior and target layout for snapping, and use scroll-transition phase values for effects responding to position. [Evidence at 00:09:24.959](https://www.youtube.com/watch?v=koVinhvGLQo&t=564s)

- Choose symbol effects by purpose: indefinite effects represent ongoing activity, discrete effects acknowledge events, and content transitions animate replacement. [Evidence at 00:12:22.790](https://www.youtube.com/watch?v=koVinhvGLQo&t=742s)

- Use withAnimation when selected mutation sources should animate, or a value-driven animation modifier when the view should animate whenever that value changes. [Evidence at 00:18:29.120](https://www.youtube.com/watch?v=koVinhvGLQo&t=1109s)

- Scope animation overrides to subviews when spring overshoot suits a bar but causes distracting transitions in its numeric label. [Evidence at 00:19:46.960](https://www.youtube.com/watch?v=koVinhvGLQo&t=1186s)

- Use named springs for the intended feel, then reach for a custom spring only when additional timing and bounce control are necessary. [Evidence at 00:22:36.960](https://www.youtube.com/watch?v=koVinhvGLQo&t=1356s)

- Build phase animators from explicit phase values and per-phase timing; use a custom Transition for insertion or removal effects. [Evidence at 00:26:03.919](https://www.youtube.com/watch?v=koVinhvGLQo&t=1563s)

Visual examples: [Matching zoom-transition sources](https://www.youtube.com/watch?v=koVinhvGLQo&t=292s) — The stage screen pairs transition-source code with the corresponding photo grid.; [Scoping animation overrides](https://www.youtube.com/watch?v=koVinhvGLQo&t=1198s) — Separate highlighted animation modifiers control the text and progress bar independently.; [Defining animation phases](https://www.youtube.com/watch?v=koVinhvGLQo&t=1559s) — PhaseAnimator assigns a different animation to each drop, squish, expand, and rise phase.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### SwiftUI in motion | Meet with Apple — 00:15:30.000

Tie the visible change to intentional animation; verify API spelling because speech-derived captions can misrecognize withAnimation.

[Evidence at 00:15:30.000](https://www.youtube.com/watch?v=koVinhvGLQo&t=930s). Caption anchor: “this instead. Do that with the width”.

### WWDC24: Create custom visual effects with SwiftUI | Apple — 00:09:19.000

Use transitions to communicate the addition or removal of meaningful content.

[Evidence at 00:09:19.000](https://www.youtube.com/watch?v=alhFwkbsxrs&t=559s). Caption anchor: “and transitions are a useful way to”.

### WWDC24: Enhance your UI animations and transitions | Apple — 00:03:34.000

Capture a stable model identifier for transition sources instead of a view that may be reused.

[Evidence at 00:03:34.000](https://www.youtube.com/watch?v=UDaNFV1Ll3E&t=214s). Caption anchor: “and it should capture a stable identifier.”.

### WWDC23: Explore SwiftUI animation | Apple — 00:06:46.000

Animate a coherent vector of values that satisfies the framework's interpolation contract.

[Evidence at 00:06:46.000](https://www.youtube.com/watch?v=IuSuHJs5-KE&t=406s). Caption anchor: “The only requirement is that the view”.

### WWDC23: Animate with springs | Apple — 00:18:03.000

Treat spring presets as context-dependent starting points and tune duration or bounce deliberately.

[Evidence at 00:18:03.000](https://www.youtube.com/watch?v=HaZ2jw9rx9M&t=1083s). Caption anchor: “But an important part of using a”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
