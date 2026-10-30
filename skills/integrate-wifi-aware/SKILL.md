---
name: integrate-wifi-aware
description: "Build, review, or improve nearby peer-to-peer connectivity using Apple Wi-Fi Aware. Use for device pairing, declared publisher/subscriber services, Network framework connections, accessory onboarding, and measured latency/power tuning; not ordinary internet networking."
---

# Integrate Wi-Fi Aware

## Goal

Pair the intended nearby devices and exchange app data reliably over an appropriately scoped, power-conscious Wi-Fi Aware connection.

## Workflow

1. Identify the actual nearby task, peer device types, service protocol, and required transfer or interaction. Inspect the installed SDK, supported OS/hardware, signing entitlements, and existing app transport. Resolve WiFiAware and related framework APIs with Context7 when available; otherwise consult current official documentation. The supplied framework documentation lists iOS/iPadOS 26 availability; check WACapabilities.supportedFeatures at runtime and provide an understandable unsupported-device path.

2. Declare only required Publish and/or Subscribe capabilities in com.apple.developer.wifi-aware and matching roles in WiFiAwareServices. Validate the service name component: 1–15 characters, letters/digits/hyphens, at least one letter, no leading/trailing hyphen. The full declaration adds an underscore, dot, and _tcp or _udp suffix, such as _example-service._tcp; the 15-character limit is for the component. Publishable/Subscribable values are empty dictionaries. Verify peers agree on the name and protocol; do not force-unwrap a service absent from configuration.

3. Use system pairing at the point the person selects or adds a device. Choose DeviceDiscoveryUI for app/device pairing, or AccessorySetupKit for hardware accessory onboarding, especially multiple transports. Scope discovery filters to the intended peers, let the system handle PIN confirmation and Wi-Fi link trust, and handle cancellation or failed pairing without reporting a connection.

4. Track WAPairedDevice.allDevices updates and stable peer identity through app-owned state. A paired device may be out of range or inactive; show paired, discovering, connecting, connected, and failed states separately. Handle removal in Settings and do not treat a friendly name, vendor label, or discovery match as application-level permission for every domain action.

5. Create the Network listener/browser with the declared service and explicit intended paired-device selection. Review discovered endpoints before connecting; the sample’s first-endpoint policy is not universal. Retain active connections, observe their state, and exchange data through the project’s documented protocol. System Wi-Fi authentication and encryption do not define application message framing, version compatibility, input validation, or authorization for app operations.

6. Scope listening, browsing, and connection tasks to the feature lifecycle. Avoid duplicate publishers for the same service and redundant subscriptions; stop discovery once the required connections are established, unless ongoing discovery is part of the task. Handle cancellation, peer departure, failed send/receive, and reconnect without orphan tasks or duplicate mutations. Existing background runtime rules still apply; pairing does not grant unlimited background execution.

7. Start with bulk performance mode and best-effort service class unless measurements show a task needs another configuration. For genuinely interactive voice/video, compare realtime and the relevant service class against latency and battery requirements. Keep the publisher and subscriber performance mode consistent; Apple’s sample warns mismatched modes have undefined behavior. Use background class for low-priority traffic when appropriate.

8. Measure signal strength, transmit latency and available performance reports from the actual Wi-Fi Aware path, alongside application-level throughput, completion, and protocol feedback. Test realistic range, interference, concurrent Wi-Fi traffic, and relevant multiple-peer cases. Change one relevant configuration at a time; avoid claiming throughput or energy improvement from API selection alone.

9. Verify with two supported physical peers or the intended certified accessory. Use project tests for deterministic protocol, state, cancellation, and recovery behavior, and appropriate device checks for discovery/pairing and radio performance. Keep older/unsupported devices usable through the agreed alternative; do not replace an existing working transport or add a cloud relay without task justification.

## Verify the outcome

- Validate actual target entitlements, service declarations, capability gates, and matching peer protocols.
- Exercise first pairing, canceled pairing, reconnect, paired-but-unreachable peers, removal from Settings, and connection loss.
- Exchange representative app data on intended physical peers; confirm recipient identity, protocol compatibility and the expected domain result.
- Verify discovery/task cleanup and repeated attempts without duplicate publishers, retained failed connections, or repeated writes.
- Record measured latency/throughput and tested conditions when tuning; distinguish simulator state tests from physical radio checks.

Do not equate paired with reachable, automatically connect to an arbitrary first endpoint, use realtime for every transfer, or present a successful simulator build as proof of Wi-Fi Aware connectivity.

## Deliverable

Leave the scoped implementation, review findings, or connection design. Report service roles, pairing and connection behavior, lifecycle ownership, checks performed, measured tradeoffs, and unsupported or untested cases.

Read [source lessons](references/source-lessons.md) for timestamped evidence and current setup/testing requirements.
