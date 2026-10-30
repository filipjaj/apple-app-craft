# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

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

## 35. WWDC24: Meet Swift Testing | Apple

Write expressive unit tests with ordinary Swift expressions, isolated fixtures, informative failures, and independently runnable input cases.

[Original session](https://www.youtube.com/watch?v=WFnkNcvLnCI) · Original library transcript: `transcripts/35-WFnkNcvLnCI.md`

- Mark ordinary Swift functions with @Test; tests may be asynchronous, throwing, or isolated to a global actor. [Evidence at 00:02:25.817](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=145s)

- Use #expect to capture failed expressions and their values, and #require when continuing after a failed prerequisite would not make sense. [Evidence at 00:05:37.714](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=337s)

- Use traits for display names, conditions, bugs, tags, execution limits, or serialization, choosing the trait that actually describes the requirement. [Evidence at 00:12:53.365](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=773s)

- Group related tests into suites and use a fresh suite instance per test to avoid unintended sharing of fixture state. [Evidence at 00:07:57.657](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=477s)

- Use tags to associate tests across suites and files and to select feature-oriented groups in test plans. [Evidence at 00:12:44.522](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=764s)

- Replace repeated test bodies or internal input loops with parameterized tests so each argument has separate results and can be rerun independently. [Evidence at 00:16:54.293](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=1014s)

- Migrate XCTest unit tests incrementally in the same target; as described in this session, retain XCTest for UI automation, performance APIs, and Objective-C-only tests. [Evidence at 00:20:39.074](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=1239s)

- Keep each testing system’s assertions inside its own tests instead of mixing XCTest assertions with Swift Testing expectations. [Evidence at 00:21:32.638](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=1292s)

Visual examples: [Expectation failure details](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=349s) — The require expression unwraps an optional and prevents the following expectation from running on failure.; [Independent suite instances](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=489s) — The test suite contains two related tests in a dedicated struct.; [Parameterized test results](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=979s) — Xcode pauses the parameterized test with the failing Scotland Coast argument visible in the debugger.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: Record, replay, and review: UI automation with Xcode | Apple — 00:08:56.000

Use stable automation metadata instead of changing spoken accessibility labels solely to satisfy recordings.

[Evidence at 00:08:56.000](https://www.youtube.com/watch?v=TI-XF0M8Ge0&t=536s). Caption anchor: “This makes it a useful way to”.

### WWDC26: Migrate to Swift Testing | Apple — 00:02:14.000

Retain XCTest for UI automation and performance scenarios while migrating appropriate unit tests to Swift Testing.

[Evidence at 00:02:14.000](https://www.youtube.com/watch?v=565Tf50PUrQ&t=134s). Caption anchor: “use Issue.record instead. With Swift Testing, you'll”.

### WWDC24: Go further with Swift Testing | Apple — 00:12:20.000

Use paired test inputs when only meaningful pairs belong together instead of producing an accidental Cartesian product.

[Evidence at 00:12:20.000](https://www.youtube.com/watch?v=bOvWGHi-BxI&t=740s). Caption anchor: “to match up pairs of inputs that”.

### WWDC24: Meet Swift Testing | Apple — 00:19:27.522

Use a halting requirement only where later checks need that precondition to be valid.

[Evidence at 00:19:27.522](https://www.youtube.com/watch?v=WFnkNcvLnCI&t=1167s). Caption anchor: “by using #require instead of #expect, and”.

### WWDC26: Validate your App Intents adoption with AppIntentsTesting | Apple — 00:09:07.000

Supported App Intents integration tests can invoke the installed app by identifier rather than relying on brittle UI scripts.

[Evidence at 00:09:07.000](https://www.youtube.com/watch?v=Ljdcg9t1mUw&t=547s). Caption anchor: “Your test target never imports any code”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
