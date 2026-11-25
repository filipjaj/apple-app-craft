---
name: embed-swiftui-in-native-app
description: "Embed scoped SwiftUI features in an existing UIKit or AppKit application while preserving the native lifecycle, shared state and command routing."
---

# Embed SwiftUI in a Native App

## Workflow

Choose one view, menu or scene boundary. Preserve the host's app delegate, navigation and ownership of dependencies. Use the existing model across both frameworks. Keep ephemeral presentation state local and send actions through the same domain commands.

- In UIKit, use UIHostingController with valid containment and sizing, or UIHostingConfiguration for compatible cells. In AppKit, choose NSHostingView for a view boundary or NSHostingController for a controller boundary. Check fitting size, constraints, environment and focus. Drive reused cells from item identity and the current model. Let the native presenter coordinate dismissal and unsaved changes. Verify the cell layout’s self-sizing separately from hosting-controller sizing.
- For @Observable, verify whether each native callback tracks the property reads. Check UIKit/AppKit deployment and opt-in policy before removing manual invalidations. Set NSObservationTrackingEnabled for opt-in on macOS 15 and UIObservationTrackingEnabled on iOS 18 where applicable. Apple documents automatic tracking by default in the 2026 releases. Verify the built Info.plist and the actual callback on the supported OS before removing fallback invalidation.
- Preserve responder and keyboard behavior. In AppKit, verify SDK/runtime availability before adopting NSHostingMenu, NSHostingSceneRepresentation or an AppKit gesture adapter. Keep existing command validation, active-window targeting and shortcuts. Avoid registering scenes or actions twice. Use design-app-command-menus for command hierarchy and active-window targets.
- Exercise the previous host entry, bidirectional edits, repeated presentation and dismissal, and keyboard and VoiceOver paths at the minimum supported OS. Verify that embedded content resizes and observation works for cross-control changes.

## Deliverable

Leave the hosted feature and report the native entry path, shared-state behavior, supported fallback and tested deployment targets.

## Sources

[Use SwiftUI with AppKit and UIKit](https://developer.apple.com/videos/play/wwdc2026/272/) at 2:33, 5:41, 7:48, 9:16 and 11:30. Verify exact API availability and containment for the target SDK with Context7 or Apple documentation. Use the legacy modernization workflow when the request needs a parity harness and release candidate.
