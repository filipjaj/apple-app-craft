---
name: improve-interface-hierarchy
description: "Improve an existing app screen or flow when information competes for attention, options are difficult to compare, or the next step is unclear. Reorganize content, action emphasis, and choice presentation; use design-app-interface for composing an entirely new screen."
---

# Improve Interface Hierarchy

## Goal

Make essential information easy to scan and choices understandable at the moment people need to act.

## Working context

Inspect the existing app’s content, brand, supported platforms, and conventions. Read [source lessons](references/source-lessons.md) when you need the reasoning behind grouping, action hierarchy, or progressive disclosure. The workflow is editorial synthesis of the supplied Apple sessions. For implementation API details, use Context7 when available and current official documentation as a fallback; check the actual deployment target and SDK.

## Workflow

1. Establish the task and inspect the actual screen, neighboring states, and relevant implementation. Identify what the person is trying to decide, what they already know, and what information they need. Preserve product capabilities and constraints; do not delete features to make a mockup look simpler.
2. Inventory visible content and controls. Separate orientation, decision-critical information, available options, immediate actions, and secondary detail. Identify unrelated items that share emphasis or placement, repeated labels, and controls whose scope is ambiguous.
3. Define a reading and decision order. Group items by meaningful domain relationships, progress, or time. Put needed context before commitment and keep actions near the content they affect. Use spacing and alignment to communicate relationships before adding boxes and separators.
4. Make options comparable: use the same relevant attributes, explicit labels, consistent ordering, and visible selected states. Distinguish selecting an option from committing an action. Explain consequential differences near the choice; use defaults only when justified by the person’s context and easy to change.
5. Give the current decision a clear action hierarchy. Emphasize its most useful next action while keeping alternatives discoverable. Multiple peer actions can be appropriate; do not impose one primary button on every screen. Label actions by outcomes and distinguish navigation, filtering, and mutation.
6. Use progressive disclosure for details that are unnecessary until a particular stage or choice. Keep decision-critical costs, restrictions, consequences, and recovery information available before commitment. Use sectioning, search, or relevant filters for large choice sets instead of hiding all options in a menu.
7. Apply typography, semantic colors, restrained emphasis, and suitable list/collection layouts after resolving the information structure. Preserve accessibility reading order, text scaling, recognizable controls, and distinctions that work without color.
8. For a review-only request, give a prioritized annotated critique or before/after structure. When asked to improve the app, implement the smallest coherent change and inspect rendered output. Check adjacent states and routes; do not stop at proposed advice when changes are requested.

## Verify the outcome

- A walkthrough makes location, scope, available choices, selection, and the next useful action apparent.
- People can compare important options using consistent attributes and see consequences before commitment.
- Essential decisions remain usable with long labels, empty/error states, large text, and light/dark appearance.
- Exercise selection, commitment, cancellation, and recovery; verify grouping and visual order agree with actual behavior.
- Report what was observed, changed, and checked. Reduced visual clutter or fewer taps alone does not prove improved decision quality.

Do not equate minimalism with clarity: removing explanatory context, hiding essential choices, or using manipulative defaults can make decisions harder.

## Deliverable

Provide the scoped design critique or implemented improvement, with a concise before/after explanation of content order, grouping, option comparison, and action priority. Identify retained capabilities, verification evidence, and remaining uncertainty.
