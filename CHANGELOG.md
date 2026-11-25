# Changelog

## Unreleased

- Make the collection entry point trigger on ordinary app requests instead of only when the collection is named, and sharpen the triggers of plan-native-app, review-apple-app and design-app-interface.
- Add an opportunity check: when planning, building or broadly reviewing an app, suggest up to three fitting system capabilities the user did not ask for (App Clips, App Attest, on-device models, Wi-Fi Aware, capture, canvas, visual search and others), and build only what is accepted.
- Add eight workflows for app distribution, remote push, custom-backend sync, BLE and NFC, audio transcription, incremental SwiftUI adoption, and legacy UIKit and AppKit modernization.
- Expand native branding with SwiftUI token roles, reference analysis, original artwork, and rendered-state review.
- Route Bluetooth and NFC requests to accessory onboarding and retain a dedicated Wi-Fi Aware workflow.

## 0.1.0 — 2026-10-30

- Publish the coordinated collection of 74 Apple app skills.
- Add a bounded delivery workflow with evidence-linked acceptance criteria.
- Include reference-app inspection, macOS utilities, app automation, and runtime/UI verification adapted from BAMA.
- Package portable, Codex, and Claude-compatible manifests and repository marketplaces.
- Document optional tooling and preserve upstream MIT notices.
- Add package validation and seven regression tests with CI.

Release checks: all 74 skills pass the skill-creator validator; 243 local references resolve; the portable manifest passes its published JSON schema; seven package tests pass. Codex CLI 0.162.1 successfully installs and discovers all 74 skills. Claude runtime and Swift application behavior are not tested by this release.
