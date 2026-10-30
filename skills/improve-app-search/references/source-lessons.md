# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 14. WWDC26: Design intuitive search experiences | Apple

Search placement communicates both how to access it and what it searches. The session combines platform-specific placement guidance with suggestions, filtering, and graceful empty states to reduce the effort of finding content.

[Original session](https://www.youtube.com/watch?v=lx45sKEnZkU) · Original library transcript: `transcripts/14-lx45sKEnZkU.md`

- Choose search placement based on the app's navigation and search scope. On iPhone, consider reachable toolbar or tab placements for frequent searches. [Evidence at 00:03:55.665](https://www.youtube.com/watch?v=lx45sKEnZkU&t=235s)

- Use a search landing tab when discovery content is useful; use a prominent search tab when people usually want to start typing immediately. [Evidence at 00:06:13.967](https://www.youtube.com/watch?v=lx45sKEnZkU&t=373s)

- Place scoped search near the content it searches. On iPad and Mac, use toolbar, sidebar, or dedicated-section placement to clarify which results will change. [Evidence at 00:07:40.314](https://www.youtube.com/watch?v=lx45sKEnZkU&t=460s)

- Preserve familiar search-field elements and behavior even when applying custom branding. [Evidence at 00:02:36.048](https://www.youtube.com/watch?v=lx45sKEnZkU&t=156s)

- Offer useful recent searches and relevant predictive suggestions. Let people clear their history, visually separate typed text from predictions, and keep results prominent. [Evidence at 00:12:11.032](https://www.youtube.com/watch?v=lx45sKEnZkU&t=731s)

- Start broad and let people refine results with contextual filters or scope controls. Tokens can complement visible filters but are less discoverable. [Evidence at 00:14:31.905](https://www.youtube.com/watch?v=lx45sKEnZkU&t=871s)

- Provide a clear no-results state and show the current query so people can recognize typos or revise their search. [Evidence at 00:15:12.375](https://www.youtube.com/watch?v=lx45sKEnZkU&t=912s)

Visual examples: [Search landing experiences](https://www.youtube.com/watch?v=lx45sKEnZkU&t=391s) — Apple TV fills its search landing page with browsable genres before a query is entered.; [Search placement and scope](https://www.youtube.com/watch?v=lx45sKEnZkU&t=520s) — Mail places search in a multi-column interface where the surrounding content defines its scope.; [Filters and search tokens](https://www.youtube.com/watch?v=lx45sKEnZkU&t=840s) — A sender token narrows the message results while preserving the search field and keyboard.

## 16. WWDC26: Code-along: Add persistence with SwiftData | Apple

The session converts an in-memory SwiftUI app into one backed by SwiftData. It connects model and relationship design to efficient fetching, UI integration, runtime error handling, and observed updates.

[Original session](https://www.youtube.com/watch?v=TrxEHvZvQVw) · Original library transcript: `transcripts/16-TrxEHvZvQVw.md`

- Identify the state that must survive relaunches, then represent it with persistent model types and a schema. [Evidence at 00:03:08.539](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=188s)

- Revisit model representation during persistence work. Stored properties must be serializable, and an enum used for a fixed UI demo may need a class for persistent instances. [Evidence at 00:06:53.720](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=413s)

- Declare relationships directly and choose deletion behavior deliberately. Use inheritance when distinct model kinds genuinely share a stable common structure. [Evidence at 00:10:41.367](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=641s)

- Separate lightweight thumbnails from full-resolution images. Load large assets only where needed and use appropriate persistent references. [Evidence at 00:11:02.035](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=662s)

- Connect a model container and context to the UI, then replace hand-maintained storage and filtering layers with model queries and relationships. [Evidence at 00:12:57.618](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=777s)

- Fetch only the data a view needs using predicates, sorting, and limits. Loading everything and filtering afterward trades unnecessary I/O for avoidable memory work. [Evidence at 00:15:36.493](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=936s)

- Construct queries from view inputs for scoped collections and search. Handle empty results and capture persistence errors with useful recovery feedback. [Evidence at 00:17:31.449](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=1051s)

- Restore derived-state updates explicitly after refactoring models. Observation can update timestamps or completion status so queries and lists stay current. [Evidence at 00:21:08.273](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=1268s)

Visual examples: [Persistent model representation](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=416s) — The Goal enum diagram enumerates fixed demo goals, illustrating why persistence changes the representation.; [Relationships and inheritance](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=644s) — The Trip model declares a cascade delete relationship and its inverse in the activities property.; [Predicates, sorting, and limits](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=939s) — The crossed-out filtering example and RAM/I/O bars illustrate the cost of loading everything before filtering.

## 41. WWDC25: Build a SwiftUI app with the new design | Apple

Audit automatic changes first, then use targeted APIs to extend content, organize controls, and compose custom glass effects consistently.

[Original session](https://www.youtube.com/watch?v=3MugGCtm26A) · Original library transcript: `transcripts/41-3MugGCtm26A.md`

- Build with the Xcode 26 SDKs and audit the automatic updates to standard navigation, controls, and presentations before adding customization. [Evidence at 00:02:56.987](https://www.youtube.com/watch?v=3MugGCtm26A&t=176s)

- Use backgroundExtensionEffect to extend artwork behind a floating sidebar while keeping the source image’s content visible. [Evidence at 00:04:14.515](https://www.youtube.com/watch?v=3MugGCtm26A&t=254s)

- Configure tab-bar minimization and bottom accessories together, adapting accessory content to its placement when the bar collapses. [Evidence at 00:05:54.558](https://www.youtube.com/watch?v=3MugGCtm26A&t=354s)

- Remove custom backgrounds that conflict with the new sheet material and automatic toolbar scroll-edge effects. [Evidence at 00:10:51.740](https://www.youtube.com/watch?v=3MugGCtm26A&t=651s)

- Group related toolbar actions with ToolbarSpacer and reserve tint for meaningful emphasis instead of decorative coloring. [Evidence at 00:10:24.101](https://www.youtube.com/watch?v=3MugGCtm26A&t=624s)

- Apply search at the scope it serves, choosing a toolbar search experience or a dedicated search tab that adapts across platforms. [Evidence at 00:12:13.819](https://www.youtube.com/watch?v=3MugGCtm26A&t=733s)

- Adopt standard controls’ new capabilities, including slider ticks, neutral values, and container-concentric shapes. [Evidence at 00:16:27.957](https://www.youtube.com/watch?v=3MugGCtm26A&t=987s)

- Apply glassEffect to custom controls and group nearby glass in a GlassEffectContainer so sampling and blending remain consistent; use namespace-linked IDs for morphing transitions. [Evidence at 00:20:29.666](https://www.youtube.com/watch?v=3MugGCtm26A&t=1229s)

Visual examples: [Background extension](https://www.youtube.com/watch?v=3MugGCtm26A&t=250s) — The backgroundExtensionEffect modifier extends the image behind the sidebar.; [Meaningful toolbar groups](https://www.youtube.com/watch?v=3MugGCtm26A&t=620s) — The Mail interface demonstrates related toolbar actions and a distinct primary action.; [Composing custom glass](https://www.youtube.com/watch?v=3MugGCtm26A&t=1232s) — GlassEffectContainer combines the sampling region of neighboring glass controls.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Design intuitive search experiences | Apple — 00:06:54.971

Choose global versus destination-scoped search according to the content people expect to find.

[Evidence at 00:06:54.971](https://www.youtube.com/watch?v=lx45sKEnZkU&t=414s). Caption anchor: “and tapping search immediately brings up the”.

### WWDC25: Build a SwiftUI app with the new design | Apple — 00:11:49.821

A global search presentation should make the app's relevant content available through that scope.

[Evidence at 00:11:49.821](https://www.youtube.com/watch?v=3MugGCtm26A&t=709s). Caption anchor: “When using this placement, you should make”.

### WWDC26: LLM search using Core Spotlight | Apple — 00:08:50.000

Model-assisted search guidance must fit the chosen model's context budget and real indexed content.

[Evidence at 00:08:50.000](https://www.youtube.com/watch?v=sij24ohbRSg&t=530s). Caption anchor: “that the model should consider during a”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
