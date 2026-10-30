---
name: adapt-apple-platform-design
description: "Adapt an established Apple app experience across iPhone, iPad, and Mac while preserving core task semantics. Use for platform and window-context design, rather than an isolated SwiftUI sizing bug."
---

# Adapt Design Across Apple Platforms

## Goal

Preserve the user’s task while making each supported platform feel appropriate to its context.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect supported platforms, window sizes, usage context, and existing platform requirements. Identify stable content destinations, actions, domain state, and mental models that should stay consistent.
2. Map presentation changes deliberately: compact hierarchy versus multicolumn exploration, search scope/placement, persistent accessories, and contextual toolbars. Adapt to available space and task complexity rather than detecting one device model.
3. Account for touch reachability, pointer precision, keyboard navigation, and multiple windows only where the actual platform and product support them. Preserve action meanings while allowing platform-specific control anatomy.
4. On iPad, choose navigation for the content hierarchy and available width: a sidebar can expose deep content, while adaptive tabs can reclaim space. Keep resizing non-destructive; restore the expanded arrangement when space returns without losing selection, input or context. Account for native window controls in toolbar layout rather than duplicating a permanent safe-area strip. Keep navigation selection and history coherent when columns collapse or return. Separate scene-local state from shared domain state so one window’s navigation does not unexpectedly move another.
5. Specify layouts and content priorities for long text, accessibility text sizes, light/dark appearance, and right-to-left progression where applicable. Use adaptive arrangements that retain essential information.
6. Produce a platform comparison with intentional differences and common behavior. Implement supported variants when requested, then inspect each actual target rather than claiming cross-platform success from one preview.

## Verify the outcome

- Complete the same core task in each supported platform presentation.
- Exercise resizing and compact/expanded changes while checking selection, focus, and unfinished input.
- Verify relevant input modes and independent windows when supported; report platform checks that could not run.

Do not stretch the phone screen to fill a desktop window or force identical placements across fundamentally different contexts.

## Deliverable

Leave the requested design artifact, evidence-based critique, interaction specification, or implemented change. Explain the important decisions, checks performed, and remaining uncertainty.
