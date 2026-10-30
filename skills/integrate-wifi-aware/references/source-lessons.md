# Source lessons

Reviewed the complete publisher-provided English caption transcript of WWDC25: Supercharge device connectivity with Wi-Fi Aware, plus current Apple framework, adoption, and sample articles on 2026-10-06. One paired-device state frame was inspected; this was not continuous viewing of every video frame. Session guidance does not replace installed-SDK or runtime capability checks.

## 00:03:07.084

Separate one-time trust establishment from later connections.

[Evidence at 00:03:07.084](https://www.youtube.com/watch?v=L0JQgZucb0c&t=187s). Caption anchor: “pairing a device”.

## 00:05:42.105

Declare required services and their publisher/subscriber roles before accessing them.

[Evidence at 00:05:42.105](https://www.youtube.com/watch?v=L0JQgZucb0c&t=342s). Caption anchor: “Info.plist”.

## 00:07:04.254

Gate the feature on actual device capability.

[Evidence at 00:07:04.254](https://www.youtube.com/watch?v=L0JQgZucb0c&t=424s). Caption anchor: “supportedFeatures”.

## 00:08:53.129

Use system pairing and choose the appropriate app or accessory flow.

[Evidence at 00:08:53.129](https://www.youtube.com/watch?v=L0JQgZucb0c&t=533s). Caption anchor: “two system frameworks”.

## 00:14:54.690

Paired-device inventory includes peers that are not reachable.

[Evidence at 00:14:54.690](https://www.youtube.com/watch?v=L0JQgZucb0c&t=894s). Caption anchor: “regardless of whether”.

## 00:18:46.555

Stop unnecessary listener/browser activity after required connections exist.

[Evidence at 00:18:46.555](https://www.youtube.com/watch?v=L0JQgZucb0c&t=1126s). Caption anchor: “conserve wireless resources”.

## 00:20:20.583

Low-latency mode costs energy; choose it for measured need.

[Evidence at 00:20:20.583](https://www.youtube.com/watch?v=L0JQgZucb0c&t=1220s). Caption anchor: “real time mode”.

## 00:20:51.247

Validate performance under realistic wireless conditions.

[Evidence at 00:20:51.247](https://www.youtube.com/watch?v=L0JQgZucb0c&t=1251s). Caption anchor: “environmental interference”.

## Current documentation and implementation reasoning

- [Wi-Fi Aware](https://developer.apple.com/documentation/wifiaware): check current supported hardware, framework availability, pairing frameworks, and background-runtime constraints.
- [Adopting Wi-Fi Aware](https://developer.apple.com/documentation/wifiaware/adopting-wi-fi-aware): exact entitlement capability strings, service component versus full-name syntax, empty role dictionaries, and the one-publisher-per-service constraint. Invalid declarations can crash the app; validate actual built target configuration.
- [Building peer-to-peer apps](https://developer.apple.com/documentation/wifiaware/building-peer-to-peer-apps): current pairing and Network flow, physical-device testing requirement, and matching publisher/subscriber performance modes. The sample connects to its first discovered endpoint, but explicitly says most apps should review the endpoint and connect only when needed.

The framework sample cannot run its real radio connections in Simulator. State/protocol unit tests remain useful, but physical peers are required to establish end-to-end discovery, pairing, transfer, and performance evidence. The sample also warns of undefined behavior for mismatched performance modes.

Application message validation, selected-peer domain authorization, and duplicate-write prevention are implementation reasoning based on the transport lifecycle; the video’s Wi-Fi-layer encryption is not a guarantee of those application properties. For hardware firmware/interoperability work, consult the current Apple Accessory Design Guidelines Wi-Fi Aware chapter; do not infer certification requirements from this app-focused skill.

Local provenance: `source-additions/transcripts/L0JQgZucb0c.md` and documentation snapshots under `source-additions/documents/`. These media assets are excluded from the portable skill package.
