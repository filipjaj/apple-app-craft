---
name: build-swiftui-state
description: "Implement or repair SwiftUI state ownership, bindings, observation, and view identity. Use for lost edits, stale UI, duplicate state, or state-driven feature work."
---

# Build Reliable SwiftUI State

## Goal

Make each state value have a clear owner and the lifetime the user expects.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Trace each mutable value from creation to reads, writes, and disposal. Separate temporary UI state, shared domain state, preferences, and persisted data.
2. Choose ownership at the narrowest stable scope that serves its consumers. Pass inputs for read-only use, bindings for edits owned elsewhere, and an injected observable model for genuinely shared dependencies.
3. Match storage APIs to the project’s deployment target and existing observation system. Avoid mixing wrappers mechanically or recreating model instances during transient view evaluation.
4. Check structural and explicit identity through branches, lists, and layout changes. Use stable domain IDs; an ID reset is appropriate only when deliberate state replacement is required.
5. Keep dependencies close to views that read them. Extract focused subviews when that reduces unrelated updates. Preserve derived-state invariants when model structure changes.

## Verify the outcome

- Edit in one view and verify the intended observers update without duplicate stores.
- Reorder, insert, delete, change layout, and switch branches while checking selection and edits.
- Verify expected lifetime across navigation and relaunch; UI-owned state alone does not provide persistence.

Do not add random IDs, blanket AnyView wrappers, or force-refresh toggles to conceal an ownership defect.

## Additional source decisions

Distinguish transient view values from persistent state identity. Keep mixed UIKit/AppKit/SwiftUI controls on one coherent domain value, and inspect actual property reads when using Observation. Modifier order, container composition and focused-value scope can change behavior without changing the model; diagnose that boundary before adding another state owner.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
