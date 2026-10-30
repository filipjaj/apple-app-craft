---
name: integrate-macos-utilities
description: "Build or repair macOS menu bar utilities, global shortcuts, floating panels, clipboard workflows, screen capture, login items, or cross-app window control. Use for system-facing Mac features; ordinary scene navigation belongs to manage-app-windows."
---

# Integrate macOS Utilities

Connect a requested utility feature to macOS with the smallest suitable integration and a verifiable lifecycle.

## Establish the integration contract

Inspect the app's scene and process model, distribution channel, sandbox/entitlements, deployment target, signing, and existing integration code. Resolve the relevant framework with Context7 and query the specific capability before using API syntax. Consult current official Apple documentation when coverage is insufficient. Do not transplant Bama's permission table as a current platform guarantee.

Use [integration decisions](references/integration-decisions.md) for the relevant feature. Record its trigger, permission/capability requirements, lifecycle owner, cancellation, failure feedback, and cleanup. Prefer a narrower API when it provides the required behavior.

## Implement and exercise

- Route menu, shortcut, panel, and any requested URL/intent entry points to the same validated domain operation. Add only the entry points the feature needs. Preserve the active document, text editing, Undo, and existing shortcut meanings.
- A menu bar utility needs a reachable Settings/Quit path. Decide Dock behavior and single-instance behavior deliberately. A panel needs explicit focus, activation, dismissal, and multi-display behavior; test Return/Escape and focus returning to the previous app.
- Permission handling is feature-specific: explain purpose at use, detect denial/revocation, offer recovery, and keep unrelated features usable. Refresh on relevant activation or retry; poll only when necessary and bounded. Never reset the user's grants or disable sandboxing as a routine fix.
- Own observers, event monitors, hotkeys, streams, timers, and assertions. Release or stop them on cancellation, feature disablement, and shutdown. Keep slow cross-process work outside latency-sensitive UI paths using framework-supported concurrency.
- Preserve signing and installation conventions. Diagnose identity, entitlement, path, or permission failures before changing them. Avoid overwriting a running production utility to test a change.

## Evidence

Exercise the actual trigger, denied permission, disabled state, cancellation, and repeated activation. For cross-app actions, use a disposable target and verify the affected window/content. Use SwiftProbe for Swift tests after reading its skill; use `verify-macos-app` when available for UI/runtime evidence. Simulation or a screenshot does not prove a global shortcut or permission prompt works.

Workflow attribution: [Bama source and license](references/bama-source.md).
