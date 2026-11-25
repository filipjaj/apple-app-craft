---
name: modernize-appkit-behavior
description: "Modernize AppKit event tracking loops, keyboard navigation, graceful termination or window restoration in an existing macOS app."
---

# Modernize AppKit Behavior

## Workflow

Trace the broken or brittle user action through the responder chain. For each input, prefer the existing container's selection delegate, native context-menu API or dragging delegate. Use supported control events for standard controls, and a recognizer for custom gestures. A tracking loop using nextEvent(matching:until:inMode:dequeue:) that consumes events keeps the recognizer from seeing them. Replace handling per interaction and preserve modifier behavior, drag threshold and cancellation. Inspect overlapping hit regions, first responder, tab order, keyboard activation and VoiceOver. Gate newer APIs such as NSTextSelectionManager by runtime availability.

For graceful quit, distinguish a transient sheet from a decision that protects unsaved work. Change preventsApplicationTerminationWhenModal only where quitting safely can resume or discard the presentation. For state restoration, keep stable identities for restorable windows and data. For custom windows, set isRestorable, a stable identifier, an appropriate frame autosave name, and a restoration class conforming to NSWindowRestoration. Invalidate state when relevant values change and securely encode minimal UI state. Use the document lifecycle for document windows. Recreate or reuse each window through its restoration path, complete every request including failure, then decode UI state after its dependencies are available. Handle stale or missing identifiers.

Exercise ordinary launch, clean quit and restore with multiple windows, missing data, and any modal types whose behavior changed. Record the macOS “Close windows when quitting an application” setting when verifying restoration. Verify keyboard and pointer paths and gesture cancellation for input changes. Report actual OS and evidence. For redesign, route visual decisions to the brand or platform-design workflow.

## Deliverable

Report the input paths and restored windows verified, the handling of unsaved work, and the tested macOS versions.

## Sources

[Modernize your AppKit app](https://developer.apple.com/videos/play/wwdc2026/289/) at 1:06, 5:51 and 8:57. Check current SDK details through Context7 or Apple's AppKit documentation.
