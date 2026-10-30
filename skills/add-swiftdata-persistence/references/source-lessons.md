# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

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

### WWDC26: Code-along: Add persistence with SwiftData | Apple — 00:05:51.204

Include intended persisted properties in the schema using supported model types and serialization rules.

[Evidence at 00:05:51.204](https://www.youtube.com/watch?v=TrxEHvZvQVw&t=351s). Caption anchor: “and all model properties, must be Codable.”.

### WWDC26: What’s new in SwiftData | Apple — 00:05:42.000

Codable attributes require forward/backward compatibility and are not a replacement for every queryable model type.

[Evidence at 00:05:42.000](https://www.youtube.com/watch?v=9MB7e-DcQ2Q&t=342s). Caption anchor: “The Codable implementation of the type must”.

### WWDC23: Build an app with SwiftData | Apple — 00:08:19.000

Configure the model container with the actual types that the view hierarchy needs to access.

[Evidence at 00:08:19.000](https://www.youtube.com/watch?v=q2ZcfYApexQ&t=499s). Caption anchor: “Now, let's set up the modelContainer to”.

### WWDC23: Meet SwiftData | Apple — 00:02:54.000

Uniqueness and relationship delete rules are deliberate domain constraints that must preserve expected data.

[Evidence at 00:02:54.000](https://www.youtube.com/watch?v=Y7FLskzCTGE&t=174s). Caption anchor: “I can add @Attribute to name and”.

### WWDC23: Model your schema with SwiftData | Apple — 00:01:52.000

Resolve existing duplicate values before imposing a new uniqueness constraint.

[Evidence at 00:01:52.000](https://www.youtube.com/watch?v=vRTUJRIQEnA&t=112s). Caption anchor: “I did not ensure each trip name”.

### WWDC25: SwiftData: Dive into inheritance and schema migration | Apple — 00:06:17.000

Choose inheritance versus a property from actual query semantics rather than subclassing every category.

[Evidence at 00:06:17.000](https://www.youtube.com/watch?v=OR0C6V6lp1k&t=377s). Caption anchor: “If we only harness deep searches, meaning”.

### WWDC24: Track model changes with SwiftData history | Apple — 00:09:56.000

Persist history position so subsequent processing considers only the intended new changes.

[Evidence at 00:09:56.000](https://www.youtube.com/watch?v=K2FzpebEL_4&t=596s). Caption anchor: “return only the changes that have occurred”.

### WWDC24: Create a custom data store with SwiftData | Apple — 00:01:43.000

Keep the model/context/store boundary clear; a custom store must satisfy the capabilities the app needs.

[Evidence at 00:01:43.000](https://www.youtube.com/watch?v=_t2NflA8AcI&t=103s). Caption anchor: “And a typical app is composed of”.

### WWDC24: What’s new in SwiftData | Apple — 00:03:25.000

Compound uniqueness can express domain identity, but its effects on updates need deliberate validation.

[Evidence at 00:03:25.000](https://www.youtube.com/watch?v=-IMOuvRQilc&t=205s). Caption anchor: “This makes it really easy to avoid”.

### WWDC23: Dive deeper into SwiftData | Apple — 00:05:18.000

Model configuration controls read-only and cloud-container behavior for the relevant schema.

[Evidence at 00:05:18.000](https://www.youtube.com/watch?v=yxtCRHloVEw&t=318s). Caption anchor: “that a persistence file should be loaded”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
