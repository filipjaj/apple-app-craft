---
name: review-app-design
description: "Critique an Apple app interface from screenshots, prototypes, or rendered screens for hierarchy, clarity, consistency, and task usability. Use for design feedback; use review-apple-app for broader code and reliability review."
---

# Review an App Design

## Goal

Identify the design changes that most reduce hesitation and effort in a specific task.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Establish the task, screen sequence, target platform, intended audience, and available artifacts. Read visible content and controls before judging style. Separate screenshot evidence from behavior that must be exercised.
2. Walk the interface from entry to outcome. At each screen assess orientation, visible next action, information required for decisions, and continuity with prior context.
3. Inspect hierarchy through grouping, type roles, relative emphasis, density, semantic color, and imagery. Identify competing primary actions, weak differentiation, hidden essential controls, and text that depends on one background.
4. Check consistency of control meanings, selection feedback, navigation versus actions, and presentation dismissal. Where the task involves edits, consequential actions, or personal data, check recoverability, meaningful user control, and permission requests at the point their purpose is clear. Simplicity can require more explanatory context; do not reward hiding essential options merely for a sparse appearance. Consider accessibility and platform adaptation only to the extent the evidence permits; request or inspect the relevant states where they affect the finding.
5. For each finding give the location, evidence, task consequence, and a specific correction. Mark severity by blocked task, likely confusion, or finishing detail rather than taste. Distinguish a defect from an optional design direction.
6. When improvement is requested, implement the highest-impact scoped changes and inspect the result. Otherwise leave an ordered critique with concrete before/after recommendations. Do not make source changes during a review-only request.

## Verify the outcome

- Every critique refers to an observable element and a reason connected to the task.
- Check the revised screen against the original problem and its neighboring screens.
- State which states or interactions were unavailable; a static image cannot establish focus, gestures, or assistive navigation.

Do not score visual taste as objective quality or claim usability research from your own inspection.

## Deliverable

Leave the requested design artifact, evidence-based critique, interaction specification, or implemented change. Explain the important decisions, checks performed, and remaining uncertainty.
