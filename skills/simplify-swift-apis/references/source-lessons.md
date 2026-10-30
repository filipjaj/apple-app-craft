# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

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

## 19. WWDC22: Embrace Swift generics | Apple

The session evolves a farm model from repetitive concrete functions into type-safe generic code. It explains how protocols describe capabilities and when some or any preserves the semantics you need.

[Original session](https://www.youtube.com/watch?v=AvRirfTKR9g) · Original library transcript: `transcripts/19-AvRirfTKR9g.md`

- Begin with concrete types and generalize when repeated implementations reveal a genuine shared capability. [Evidence at 00:03:04.785](https://www.youtube.com/watch?v=AvRirfTKR9g&t=184s)

- Use protocols to model capabilities without imposing reference semantics or an unsuitable inheritance hierarchy. [Evidence at 00:08:44.924](https://www.youtube.com/watch?v=AvRirfTKR9g&t=524s)

- Use associated types to express relationships that depend on the conforming type, so incompatible values are rejected at compile time. [Evidence at 00:09:28.034](https://www.youtube.com/watch?v=AvRirfTKR9g&t=568s)

- Use some for a fixed underlying type; use named generic parameters when the same type must be referenced in several places. [Evidence at 00:18:02.815](https://www.youtube.com/watch?v=AvRirfTKR9g&t=1082s)

- An opaque result must have a consistent underlying type. A result builder can encode differing branches into a single composite result type. [Evidence at 00:17:28.481](https://www.youtube.com/watch?v=AvRirfTKR9g&t=1048s)

- Use any when heterogeneous storage needs runtime flexibility, understanding that type erasure removes some static relationships and may require allocation. [Evidence at 00:22:51.270](https://www.youtube.com/watch?v=AvRirfTKR9g&t=1371s)

- Pass existential values into generic functions to recover a fixed underlying type within the call. Prefer some until the storage flexibility of any is required. [Evidence at 00:26:12.838](https://www.youtube.com/watch?v=AvRirfTKR9g&t=1572s)

Visual examples: [Associated-type relationships](https://www.youtube.com/watch?v=AvRirfTKR9g&t=571s) — The Animal protocol associates each conforming animal with a specific Feed type.; [Opaque and generic parameters](https://www.youtube.com/watch?v=AvRirfTKR9g&t=1085s) — The farm’s feed function takes some Animal, keeping an unknown but fixed concrete type in the call.; [Existential storage](https://www.youtube.com/watch?v=AvRirfTKR9g&t=1374s) — The boxed heterogeneous animals show existential storage and the extra indirection for larger payloads.

## 20. WWDC22: Design protocol interfaces in Swift | Apple

This follow-up to Embrace Swift generics shows how to hide implementation details while retaining useful static relationships. Its examples explain existential limitations and how carefully constrained protocols make abstract code safe.

[Original session](https://www.youtube.com/watch?v=5jkTI3Ojmqg) · Original library transcript: `transcripts/20-5jkTI3Ojmqg.md`

- An existential erases the relationship to its concrete type. Associated results can be erased to their upper bound while preserving the stated constraints. [Evidence at 00:04:09.716](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=249s)

- Consuming an associated-type value needs a guaranteed concrete relationship; an arbitrary existential value is insufficient. Unbox through an opaque parameter. [Evidence at 00:06:34.328](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=394s)

- Return an opaque type to expose the capability clients need while hiding a complex implementation such as a lazy collection. [Evidence at 00:10:14.214](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=614s)

- Constrain primary associated types to expose enough information, such as collection element type, without revealing the full concrete type. [Evidence at 00:11:18.178](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=678s)

- Use a constrained existential when different calls must return different concrete implementations with the same useful interface. [Evidence at 00:14:11.084](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=851s)

- Model related concrete types with same-type requirements so operations can be chained with compile-time guarantees. [Evidence at 00:21:39.766](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=1299s)

- Check that a protocol captures the actual invariants of the data model; merely requiring several conformances can leave invalid relationships possible. [Evidence at 00:20:14.214](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=1214s)

Visual examples: [Consuming associated values](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=390s) — The two erased boxes illustrate why an arbitrary AnimalFood value cannot safely satisfy a particular animal’s concrete feed type.; [Opaque collection results](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=617s) — The property returns some Collection rather than exposing the LazyFilterSequence implementation.; [Same-type requirements](https://www.youtube.com/watch?v=5jkTI3Ojmqg&t=1302s) — The protocol constraint CropType.FeedType == Self connects harvesting back to the correct feed type.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC21: Write a DSL in Swift using result builders | Apple — 00:15:43.000

A result-builder interface should expose useful composition while keeping generated intermediate mechanics inside its implementation.

[Evidence at 00:15:43.000](https://www.youtube.com/watch?v=JODl427Ff_0&t=943s). Caption anchor: “are only ever used in this function;”.

### WWDC23: Write Swift macros | Apple — 00:12:14.000

Use macros for supported repetitive declarations without weakening useful type guarantees.

[Evidence at 00:12:14.000](https://www.youtube.com/watch?v=w29qvXIADFY&t=734s). Caption anchor: “I also have an EasySlope type that”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
