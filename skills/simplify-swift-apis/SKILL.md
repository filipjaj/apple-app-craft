---
name: simplify-swift-apis
description: "Refactor or design Swift types, protocols, and generic interfaces around concrete domain invariants. Use for repetitive overloads, unnecessary type erasure, or difficult API relationships."
---

# Simplify Swift APIs

## Goal

Make the public capability simpler while retaining useful compile-time guarantees.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Identify real callers, duplicated implementations, and invariants between inputs and outputs. Begin with concrete types; generalize only a demonstrated shared capability.
2. Choose value or reference semantics based on independent values versus shared identity. Use protocols for capabilities rather than imposing a class hierarchy for reuse.
3. Use opaque types for a fixed hidden implementation, named generic parameters for repeated type relationships, and existential storage when heterogeneous values are actually needed.
4. Express meaningful associated-type and same-type requirements so incompatible domain values fail at compile time. Constrain returned capability enough for callers without exposing implementation unnecessarily.
5. Check source compatibility and simplify at a real boundary. Retain deliberate type erasure where it serves storage or module interfaces; do not remove it merely because it exists.

## Verify the outcome

- Compile representative callers and conformances.
- Exercise the domain behavior before and after the change.
- Check that the interface rejects the incompatible relationships it is intended to prevent.

Do not introduce a protocol for every type or an abstraction with only speculative future consumers.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
