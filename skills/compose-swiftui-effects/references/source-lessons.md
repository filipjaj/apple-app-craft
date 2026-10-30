# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 17. WWDC26: Compose advanced graphics effects with SwiftUI | Apple

Advanced SwiftUI effects can be built by composing familiar graphics, data, and layout stages. The example combines an animated shader background with playback-synchronized transcript scrolling and a precisely attached timestamp.

[Original session](https://www.youtube.com/watch?v=HTDU2HKqM8c) · Original library transcript: `transcripts/17-HTDU2HKqM8c.md`

- Break a visual design into layers and identify the data and transformation each needs. Build and connect small stages instead of treating the whole effect as one opaque problem. [Evidence at 00:16:20.588](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=980s)

- Choose the shader effect for the job: colorEffect transforms colors, distortionEffect changes sample positions, and layerEffect can sample across the view's layer. [Evidence at 00:05:27.951](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=327s)

- Use noise textures for organic per-pixel variation. Repeated, offset noise sampling produces domain warping and richer flowing patterns. [Evidence at 00:10:52.750](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=652s)

- Pass changing time into stateless shaders to animate them. TimelineView provides scheduled updates that can drive those parameters. [Evidence at 00:11:21.200](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=681s)

- Drive text emphasis and scroll position from playback state so the current transcript line stays legible and centered. [Evidence at 00:12:39.550](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=759s)

- Use overlays for attached information that should not change the main layout, such as a timestamp beside the current line. [Evidence at 00:13:10.083](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=790s)

- Use alignment guides to express relationships between view edges without manually calculating offsets. Compose these layout tools with graphics and timing to build a reusable effect. [Evidence at 00:15:15.419](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=915s)

Visual examples: [Choosing a shader effect](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=367s) — The input/output grid illustrates a shader mapping sample position and color to a new output.; [Noise and domain warping](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=655s) — The domain-warping Metal function appears beside the colorful output, making the noise-sampling offsets tangible.; [Alignment guides and graphics](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=918s) — The diagram aligns the timestamp subview’s top edge to its container’s bottom edge, beside the alignmentGuide code.

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

## 38. WWDC22: Compose custom layouts with SwiftUI | Apple

Participate directly in SwiftUI’s layout engine to measure and place children while supporting natural spacing, larger text, and animated layout changes.

[Original session](https://www.youtube.com/watch?v=ao0s5rMCIgc) · Original library transcript: `transcripts/38-ao0s5rMCIgc.md`

- Use Grid when measuring every cell allows coordinated sizing in both dimensions; use lazy grids when deferred creation of scrollable content is the priority. [Evidence at 00:04:14.454](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=254s)

- Control column alignment and spanning deliberately, including gridColumnAlignment and gridCellColumns for cells that need different behavior. [Evidence at 00:07:23.744](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=443s)

- Implement sizeThatFits to report a custom container’s size and placeSubviews to position children through the supplied subview proxies. [Evidence at 00:11:02.496](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=662s)

- Measure ideal sizes with an unspecified proposal, and respect subviews’ spacing preferences for platform-appropriate layout. [Evidence at 00:14:01.909](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=841s)

- Place children relative to the supplied bounds rather than assuming a zero origin; introduce layout caching only when profiling justifies it. [Evidence at 00:12:42.629](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=762s)

- Use the Layout protocol for child-driven sizing instead of feeding GeometryReader measurements back upward in a potentially unstable layout loop. [Evidence at 00:19:41.582](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1181s)

- Offer horizontal and vertical alternatives through ViewThatFits when larger text makes the preferred layout too wide. [Evidence at 00:21:16.109](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1276s)

- Pass per-child metadata with LayoutValueKey, and use AnyLayout to change arrangement while preserving child identity and enabling smooth transitions. [Evidence at 00:25:09.510](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1509s)

Visual examples: [Custom layout methods](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=674s) — The sizeThatFits signature and container diagram show where a custom layout receives its size proposal.; [Adapting to larger text](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1279s) — The large-text preview switches the buttons to a vertical alternative through ViewThatFits.; [Switching layouts with preserved identity](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1521s) — AnyLayout switches between horizontal and radial layouts while retaining the same child views.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Compose advanced graphics effects with SwiftUI | Apple — 00:06:03.227

Distinguish color transformation from position distortion when composing the effect pipeline.

[Evidence at 00:06:03.227](https://www.youtube.com/watch?v=HTDU2HKqM8c&t=363s). Caption anchor: “This is useful for simple effects like”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
