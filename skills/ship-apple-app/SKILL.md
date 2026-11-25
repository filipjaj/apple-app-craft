---
name: ship-apple-app
description: "Ship an Apple app build to TestFlight or the App Store, including signing, archive, upload, device installation, screenshots, privacy disclosures and App Review access."
---

# Ship to TestFlight or the App Store

## Workflow

Identify the authorized milestone, team and App Store Connect app, platform, bundle ID, release commit, scheme and version/build. Distinguish a registered-device install, an internal or external TestFlight build, App Review submission and public release. Reuse existing CI/signing and capture the candidate identity before archiving. Check the proposed CFBundleVersion against the target platform’s App Store Connect rules and uploaded builds.

1. Verify Release entitlements and provisioning for the app and extensions, including distribution capabilities and embedded manifests. Archive for the platform's generic device destination. Validate the archive and retain its identifier, version/build, commit and symbols. Use Xcode Organizer or the existing authorized upload channel. If the transfer outcome is uncertain, look up the build before retrying. Track upload, processing and availability separately. Resolve any missing export compliance using the actual encryption inventory and Apple’s rules before relying on TestFlight availability.
2. Install through the intended route. Use the signed development/ad hoc path for registered device installs and TestFlight for uploaded betas. On the intended device, verify launch and the flows whose entitlements, configuration or server environment differ in Release. For external beta, account for Beta App Review and test information.
3. For App Store submission, use current screenshot requirements for each supported platform and capture actual app flows with representative data. Inspect the built privacy report and manifests, including SDKs and required-reason APIs. Reconcile the separate App Store privacy label with actual app, SDK and backend collection, linkage and tracking.
4. Verify reviewer access on a clean install. Provide stable demo credentials or an authorized demo path, relevant instructions and access to the intended backend. Address MFA, invitations, hardware and geography if they block the flow. Seed enough stable demo data to exercise the submitted features. Enter credentials in TestFlight Test Information and App Review Information as applicable, and verify they remain usable for re-review. Check current account deletion rules for account creation and guideline 4.8 login requirements and exceptions for third-party sign-in.
5. Check the selected processed build, metadata, review information and release mode before any authorized submission. Return the build number, installed/tested evidence, App Store Connect state and the specific pending gate. Use automate-app-delivery for repeatable CI and Xcode Cloud setup.

## Deliverable

Stop at the requested distribution milestone. Give the archive and App Store Connect build identity, the device install result, and the review or release state.

## Sources

[Get started with TestFlight](https://developer.apple.com/videos/play/tech-talks/110343/), [Get started with privacy manifests](https://developer.apple.com/videos/play/wwdc2023/10060/?time=88), [export compliance](https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance), [distribution workflow](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases), [privacy details](https://developer.apple.com/app-store/app-privacy-details/) and [App Review](https://developer.apple.com/app-store/review/). Check current Xcode and App Store Connect requirements for the intended route.
