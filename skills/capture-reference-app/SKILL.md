---
name: capture-reference-app
description: "Inspect an existing native or web app to produce a screen inventory, navigation and command maps, and evidence-linked requirements. Use when rebuilding an app or deriving a design from a reference; not for binary reverse engineering."
---

# Inspect a Reference App

Capture the reference experience needed for the requested rebuild or design. Preserve the distinction between visible facts, observed behavior, and model assumptions.

## Workflow

1. Set the target app, relevant journey, and observation boundary from the request. Prefer connected tools when sufficient; otherwise use the available browser or native computer-use tool and read its current documentation. Use demonstration content where available. Opening an editor can autosave: inspect without editing real records unless authorized.
2. Inventory the relevant destinations and states: main pages, detail, creation/cancellation, menus, context menus, Settings, empty/error states, and light/dark appearance where relevant. Scope to the requested feature; do not survey unrelated account or payment screens.
3. Capture the target window or surface. Record actual capture dimensions and scale; never assume every screenshot is 2x. Use tool-returned images or supported file export, and label a capture unavailable when it cannot be saved. Avoid unrelated desktop content; keep private reference captures out of public deliverables.
4. Write a screen index with reachability, structural layout, controls, observed shortcuts, behavior, and evidence paths. Read [the evidence format](references/evidence-format.md) when producing the inventory. An inaccessible state is a coverage gap, not a guessed screenshot.
5. Build navigation and command maps from observations. Label inferred entities/fields as hypotheses. Translate the selected behavior into observable acceptance criteria, using `plan-native-app` if available; explicitly defer irrelevant reference features.
6. For visual adaptation, measure the relationships that affect the requested result: pane widths, aligned edges, row pitch, text roles, selection, and contrast. Map measurements to existing semantic tokens. Preserve keyboard focus and native control semantics. Choose tolerances appropriate to the requested fidelity and capture conditions; raw pixel difference is a diagnostic, not proof of correct behavior.

## Done when

The index covers the agreed journey or names gaps, each proposed behavior points to evidence or a stated assumption, and the implementation handoff identifies what to retain, adapt, or omit. Distinguish screenshots from exercised behavior. Preserve the user's brand and use assets they can reuse.

Workflow attribution: [Bama source and license](references/bama-source.md).
