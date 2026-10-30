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

## 12. WWDC26: Xcode, agents, and you | Apple

Xcode agents can support exploration, planning, implementation, visual refinement, and coordinated project-wide changes. The session demonstrates using project context and validation tools while maintaining human direction throughout the workflow.

[Original session](https://www.youtube.com/watch?v=wXY-bSAhKtE) · Original library transcript: `transcripts/12-wXY-bSAhKtE.md`

- Explore the codebase before making changes. Capture architecture and data-model findings in project documents that can evolve with the code. [Evidence at 00:04:42.304](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=282s)

- Use documentation-search tools to ground unfamiliar APIs in current reference material rather than relying only on the agent's existing knowledge. [Evidence at 00:06:26.654](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=386s)

- Plan the feature and resolve requirements before implementation. Keep the discussion active through queued messages and clarifying questions. [Evidence at 00:08:55.739](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=535s)

- Review changes as they appear, then validate with builds, rendered previews, and tests. Let failures guide specific corrections. [Evidence at 00:23:04.677](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=1384s)

- Prototype visual alternatives with realistic data. Images and sketches communicate design intent, while inline annotations locate focused code changes. [Evidence at 00:17:26.401](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=1046s)

- Keep creative decisions under human control: choose the chart or layout, assess the preview, and direct the finishing adjustments. [Evidence at 00:17:59.861](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=1079s)

- Use orchestration for broad, divisible tasks such as localization and accessibility. Review the combined result, including translated strings and actual VoiceOver navigation. [Evidence at 00:21:34.555](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=1294s)

Visual examples: [Reviewing and validating changes](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=910s) — The Xcode agent conversation shows an investigation of chart options that the developer can review.; [Visual prototype iteration](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=1049s) — The Xcode conversation and highlighted code changes show visual iteration with the agent while a person reviews the implementation.; [Localization and accessibility review](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=1290s) — The app is running on an iPad for interaction and accessibility review; the still frame shows the actual UI under test.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC22: Build your first app in Swift Playgrounds | Apple — 00:03:46.000

Choose a data collection that represents intentional uniqueness and ordering rather than accidental duplicated UI data.

[Evidence at 00:03:46.000](https://www.youtube.com/watch?v=-K9Czth-AOw&t=226s). Caption anchor: “In order to avoid duplicating our teas,”.

### WWDC26: Create UI prototypes using agents in Xcode | Apple — 00:14:04.700

A tunable prototype can make motion exploration concrete while preserving the designer's judgment.

[Evidence at 00:14:04.700](https://www.youtube.com/watch?v=QleOvMW9vTU&t=844s). Caption anchor: “Instead of building the UI directly, enlist”.

### WWDC26: Xcode, agents, and you | Apple — 00:14:49.386

Compare working chart prototypes in the intended screen rather than choosing from text descriptions alone.

[Evidence at 00:14:49.386](https://www.youtube.com/watch?v=wXY-bSAhKtE&t=889s). Caption anchor: “I'm asking what options would work best”.

### Meet agentic coding in Xcode | Apple Developer — 00:02:47.000

Treat an agent-generated app change as a reviewable first draft and verify its integrated behavior.

[Evidence at 00:02:47.000](https://www.youtube.com/watch?v=oV6mC8Rt1kY&t=167s). Caption anchor: “What would have taken me hours is”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
