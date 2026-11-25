---
name: connect-app-accessories
description: "Connect Apple apps to BLE devices or NFC tags using CoreBluetooth, Core NFC and AccessorySetupKit onboarding, with reconnect and physical-device verification."
---

# Connect BLE and NFC Accessories

## Workflow

Start with the intended action, platforms, device firmware and protocol contract. AccessorySetupKit handles supported accessory discovery and authorization on iOS and iPadOS. Verify current availability and declarations for the selected OS. Use CoreBluetooth for BLE data exchange. Use Core NFC or a supported system tag interaction for the NFC-specific action.

- For AccessorySetupKit, check Info.plist declarations and discovery descriptors against actual firmware advertising. Activate the session before using paired accessories and handle picker cancellation, removal, and migration from existing authorization. Resolve the authorized accessory identifier when CBCentralManager is powered on. Retain the CBPeripheral for the connection lifecycle. Gate newer OS features and preserve supported legacy onboarding where necessary.
- Model disconnected, connecting, service-ready and failure states. Verify advertised UUIDs, characteristics, read/write permissions, notification subscriptions and framing. Correlate responses to writes and bound reconnects. Re-establish subscriptions after reconnect. Check the peripheral’s supported write type, maximum write length and flow control. Use supported background modes and restoration only when the product needs background reconnect. For BLE mesh, test the firmware versions and actual topology involved.
- For an NFC tag, distinguish foreground Core NFC reader sessions from supported system background tag reading using a Universal Link. For foreground sessions check device capability, NFCReaderUsageDescription and the appropriate reader entitlement. Handle cancellation, timeout, multiple tags, unsupported tags and repeated scans. Treat payload as untrusted input and make repeated task actions safe. NFC reads alone do not prove BLE authorization.
- Test on the intended hardware with a clean install, picker denial, real data exchange, Bluetooth off/on, out-of-range/reconnect, and forgetting or replacing the accessory. For NFC include malformed and repeated tags. Report what was actually exercised on hardware.

## Deliverable

Report the selected onboarding and tag paths, supported firmware and platform matrix, and actual device outcomes.

## Sources

[Meet AccessorySetupKit](https://developer.apple.com/videos/play/wwdc2024/10203/), [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth) and [What’s new in Core NFC](https://developer.apple.com/videos/play/wwdc2020/10209/) and [Core NFC](https://developer.apple.com/documentation/corenfc). Verify the supported picker, capabilities and tag/session behavior for the deployment target.
