# Integration decisions

These are routing questions, not a current API/permission compatibility table. Verify exact availability, entitlements, and behavior for the app's target and distribution.

| Feature | Investigate | Runtime check |
|---|---|---|
| Menu bar | SwiftUI MenuBarExtra versus an existing AppKit status-item lifecycle; menu versus persistent panel | Keyboard operation, Settings/Quit reachability, item removal/recreation |
| Shortcut | A registered shortcut for a discrete action versus event monitoring/taps when the behavior actually requires them | Conflicts, text editing, app inactive, repeat/held keys, cleanup |
| Floating panel | Activation and focus contract, screen/space ownership, placement from current display geometry | Escape, text entry, previous-app focus, multiple displays |
| Other apps' windows | Accessibility capabilities and missing/inaccessible window attributes | Denied/revoked access, target closes mid-action, coordinate systems |
| Screen capture | ScreenCaptureKit capabilities and the scope/permission needed for the chosen capture | Correct window/display, cancellation, permission changes, no unrelated windows |
| Clipboard | Change tracking, supported types, ownership and retention of sensitive content | No write loops, unsupported data, explicit paste behavior, disabled collection |
| Login items | ServiceManagement lifecycle, signing and distribution requirements | Registration state and user refusal, feature off, relaunch |
| URL/intents | Existing URL routing or App Intents integration and validation | Invalid payload, missing entity, same domain outcome as the UI |

Do not infer API entitlement requirements from an adjacent feature: capture, key observation, key injection, and window control have distinct boundaries. Verify microphone/system-audio needs separately. For App Intents use `integrate-app-intents` when installed; for scene/document windows use `manage-app-windows`.
