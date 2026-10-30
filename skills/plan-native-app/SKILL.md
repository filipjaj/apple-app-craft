---
name: plan-native-app
description: "Turn an Apple app idea or feature brief into a focused user journey, information architecture, and implementable acceptance criteria. Use before interface construction or when feature scope is unclear."
---

# Plan a Native App

## Goal

Define the smallest coherent experience that lets the intended person accomplish their main task.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect the existing product, target devices, and brief. Identify the person, their context, the outcome they need, and the current obstacle. Infer routine details; ask only for decisions that materially change the experience.
2. Inventory proposed content and actions. Connect each to the main outcome; defer features without a clear role. Describe the primary journey with entry, success, cancellation, and recovery.
3. Group stable content destinations separately from contextual actions. Choose tabs, hierarchy, and focused presentations based on the journey. For each screen answer: where am I, what can I do, and where can I go?
4. Identify inclusion mismatches, needed permissions, and opportunities for recovery or undo. Request private information at the point its purpose is understandable.
5. Produce a brief with screen responsibilities, a route sketch, meaningful data states, and observable acceptance criteria. Resolve architecture only to the extent needed for the next implementation.

## Implementation handoff

For a multi-step build, reuse the existing brief/backlog layout or use `docs/BRIEF.md` and `docs/STORIES.md`. Record the main outcome, supported platforms, entry surfaces, domain nouns, data ownership, required system hooks, out-of-scope items, and assumptions. Preserve requested accounts, sync, sharing, and other product requirements.

Slice the chosen journey into independently observable outcomes. Each story has an ID, dependencies, status, relevant screens, acceptance criteria, and a verification method per criterion (unit, integration, rendered, interaction, manual). Keep a control and its only usable surface in the same slice. Mark blocked or deferred work explicitly. A screenshot proves appearance, not saving or navigation.

For a reference-based build, use `capture-reference-app` when available and link criteria to the screen/command evidence. A new design need not invent a reference. Plan only enough milestones to establish the next usable outcome; keep UI terms consistent without requiring a glossary for a tiny change.

For bounded implementation across stories, follow [the collection workflow](../apple-app-craft/references/delivery-workflow.md). [Adaptation provenance](../apple-app-craft/references/bama-source.md).

## Verify the outcome

- Walk through the primary task without unexplained jumps or missing decisions.
- Exercise first use, empty content, failure, cancellation, and larger text in the proposed flow.
- Every proposed feature has a stated user benefit; distinguish assumptions from known constraints.

Do not replace the user’s product idea with a generic template or invent extra features.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
