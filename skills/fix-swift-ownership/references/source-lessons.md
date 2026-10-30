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

## 18. WWDC24: A Swift Tour: Explore Swift’s features and design | Apple

A worked social-graph example introduces Swift’s core design choices. The session connects data modeling and explicit error handling to reusable abstractions, safe concurrency, and expressive library APIs.

[Original session](https://www.youtube.com/watch?v=boiLzazJ9j4) · Original library transcript: `transcripts/18-boiLzazJ9j4.md`

- Prefer value semantics and immutability when independent data is appropriate; choose classes for shared mutable state, identity, or inheritance. [Evidence at 00:02:14.547](https://www.youtube.com/watch?v=boiLzazJ9j4&t=134s)

- Represent recoverable failures explicitly with throwing functions and contextual error values. Unwrap optionals before use instead of assuming a value exists. [Evidence at 00:09:19.379](https://www.youtube.com/watch?v=boiLzazJ9j4&t=559s)

- Organize code into modules and packages, and choose access levels that match the intended API boundary. [Evidence at 00:09:53.421](https://www.youtube.com/watch?v=boiLzazJ9j4&t=593s)

- Understand ARC for reference types and break ownership cycles with appropriate weak references. [Evidence at 00:13:37.686](https://www.youtube.com/watch?v=boiLzazJ9j4&t=817s)

- Use protocols and constrained generic extensions to share algorithms across value and reference types without forcing a class hierarchy. [Evidence at 00:18:14.186](https://www.youtube.com/watch?v=boiLzazJ9j4&t=1094s)

- Model suspending operations with async/await and protect shared mutable data with isolation such as actors; Sendable captures safe crossing of concurrency boundaries. [Evidence at 00:21:49.360](https://www.youtube.com/watch?v=boiLzazJ9j4&t=1309s)

- Use property wrappers, result builders, and macros to package reusable behavior and expressive APIs. [Evidence at 00:26:06.136](https://www.youtube.com/watch?v=boiLzazJ9j4&t=1566s)

Visual examples: [Value and reference semantics](https://www.youtube.com/watch?v=boiLzazJ9j4&t=190s) — The struct declaration groups the user value properties in the example program.; [ARC and ownership cycles](https://www.youtube.com/watch?v=boiLzazJ9j4&t=829s) — Changing Pet.owner to weak turns one edge of the Pet–Owner cycle into a non-owning reference.; [Concurrency isolation](https://www.youtube.com/watch?v=boiLzazJ9j4&t=1360s) — The actor-isolation diagnostic rejects access to an isolated property from outside its actor.

## 34. WWDC21: ARC in Swift: Basics and beyond | Apple

Design ownership and APIs around guaranteed lifetimes rather than incidental behavior from a particular compiler’s ARC optimizations.

[Original session](https://www.youtube.com/watch?v=GFq6sV2jD_c) · Original library transcript: `transcripts/34-GFq6sV2jD_c.md`

- Prefer value types when appropriate to avoid unintended sharing; ARC manages the lifetime of class instances through retain and release operations. [Evidence at 00:00:20.354](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=20s)

- An object’s guaranteed minimum lifetime ends at its last use, so do not assume it remains alive until a closing brace. [Evidence at 00:04:09.349](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=249s)

- Break reference cycles deliberately: weak references become nil after deallocation, while accessing an expired unowned reference traps. [Evidence at 00:08:49.129](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=529s)

- Do not rely on a weakly referenced object remaining alive after its guaranteed lifetime; optional binding can hide the resulting logic error. [Evidence at 00:11:19.779](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=679s)

- Use withExtendedLifetime when an explicit extension is necessary, while recognizing the maintenance cost of requiring callers to remember it everywhere. [Evidence at 00:12:30.817](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=750s)

- Prefer APIs that access objects through strong references or redesign cyclic ownership into tree-like relationships. [Evidence at 00:13:57.303](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=837s)

- Avoid sequencing external behavior around deinitializer timing; use explicit lifecycle operations or defer for effects that must occur in a defined order. [Evidence at 00:19:07.246](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=1147s)

Visual examples: [Use-based object lifetimes](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=252s) — The arrows mark an object lifetime from initialization to its last use rather than the end of scope.; [Breaking a reference cycle](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=563s) — The account back-reference becomes nil as the traveler reference count reaches zero.; [Redesigning ownership](https://www.youtube.com/watch?v=GFq6sV2jD_c&t=840s) — The ownership diagram pairs a strong account reference with a weak traveler back-reference before redesign.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC24: Consume noncopyable types in Swift | Apple — 00:07:51.000

Consuming a noncopyable value ends the previous variable's ownership and use must follow that contract.

[Evidence at 00:07:51.000](https://www.youtube.com/watch?v=I9XGyizHxmU&t=471s). Caption anchor: “Well, copying is not supported, so Swift”.

### WWDC24: What’s new in Swift | Apple — 00:18:44.000

Generic containers for noncopyable values depend on the actual language version and supported ownership rules.

[Evidence at 00:18:44.000](https://www.youtube.com/watch?v=17fZZ1v_N2U&t=1124s). Caption anchor: “opens the file, and finishes initialization if”.

### WWDC25: Improve memory usage and performance with Swift | Apple — 00:15:28.000

Copy-on-write avoids immediate element duplication but later mutation can still incur copies.

[Evidence at 00:15:28.000](https://www.youtube.com/watch?v=LzBZjwEY9as&t=928s). Caption anchor: “to one copy of an array don’t”.

### WWDC24: Explore Swift performance | Apple — 00:17:48.000

Borrowing and defensive copies affect ownership cost; profile a real call boundary before changing it.

[Evidence at 00:17:48.000](https://www.youtube.com/watch?v=nb3bRQa0iGQ&t=1068s). Caption anchor: “ideally that should just pass the information”.

### WWDC24: Analyze heap memory | Apple — 00:13:09.000

Repeated stair-step memory growth suggests retained or abandoned allocations worth investigating across identical journeys.

[Evidence at 00:13:09.000](https://www.youtube.com/watch?v=X_JYRz-Hd0o&t=789s). Caption anchor: “the memory spikes are gone! We never”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
