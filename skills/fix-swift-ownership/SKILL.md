---
name: fix-swift-ownership
description: "Diagnose Swift retain cycles, premature lifetime assumptions, and unsafe weak/unowned access; improve ownership in code with actual lifetime symptoms."
---

# Fix Swift Ownership

## Goal

Make required objects stay alive and unwanted objects release at intentional boundaries.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Reproduce the lifetime symptom and draw the strong-reference graph across models, delegates, closures, and tasks. Identify who should own each object.
2. Use value semantics where sharing is unnecessary. Break cycles at a relationship that is semantically non-owning; choose weak for optional disappearance and unowned only for a guaranteed lifetime relationship.
3. Check use-based lifetime assumptions. A scope’s closing brace does not guarantee an object remains alive to that point, and optional chaining can conceal an unexpected weak-reference disappearance.
4. Prefer a strong access path or tree-like ownership design. Use explicit lifetime extension only when a narrowly defined API contract requires it and the need can be verified.
5. Give external effects explicit lifecycle operations or defer when ordering matters. Apply borrowing/storage features only after checking compiler support and a measured copying problem.

## Verify the outcome

- Repeatedly create, use, and dispose the feature while checking expected retained objects.
- Exercise callbacks and cancellation after owner dismissal.
- Use available memory tooling or a focused lifecycle test and report its limits.

Do not add weak everywhere or rely on deinitializer timing for externally visible sequencing.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
