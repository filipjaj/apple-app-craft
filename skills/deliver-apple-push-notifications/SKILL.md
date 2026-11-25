---
name: deliver-apple-push-notifications
description: "Implement or debug APNs from an Apple app and its provider, including Cloudflare Worker delivery, environment routing, token lifecycle and ActivityKit push."
---

# Deliver Apple Push Notifications

## Workflow

Trace app registration through server token storage, provider request and device behavior. Check the signed aps-environment entitlement and the device's permission and presentation state independently. Register each launch and upsert the current token under installation, authenticated account association, topic and environment. Handle rotation, sign-out and device reinstall. Keep tokens and provider credentials out of logs.

For a Cloudflare Worker, verify outbound HTTP/2 to APNs in the actual deployed runtime. If unsupported, use an authenticated HTTP/2 provider relay and keep retry responsibility in one place. Use server-only secrets. For ES256 provider authentication, reuse the signed JWT across requests and coordinate refresh for connections that share credentials. Refresh at intervals of 20–60 minutes as Apple specifies, before expiry. Keep certificate delivery only when the selected runtime can present the certificate and negotiate the required protocol. Select the matching sandbox/production host and apns-topic, push type, priority and expiration. Capture the APNs ID, status and reason without logging raw tokens. Quarantine invalid token records for their topic/environment, account for registration time versus a 410 invalidation timestamp, and retry transient failures with bounded backoff. Avoid retrying permanent payload or authentication errors unchanged.

For Live Activities, keep push-to-start and per-activity update tokens separate from each other and from app device tokens. Observe and reconcile rotations, associate update tokens with the correct activity and stop or expire delivery when it ends. Check <bundle-id>.push-type.liveactivity, liveactivity push type, payload event and timestamp, content-state decoding and runtime availability of remote start, broadcast or token updates. A start payload includes the attributes type and attributes. Choose priority with the Live Activity update budget in mind and respect the user’s frequent-updates setting. For ordinary background pushes, use priority 5.

For sandbox success and production failure, compare the built entitlement, token namespace, host, topic and key scope first. A 429 TooManyProviderTokenUpdates points to JWT refresh behavior. A 200 with no visible change calls for checking OS presentation or ActivityKit decoding, timestamps and activity state.

Validate with one signed install per supported environment, a known delivery, a rejected token, token replacement and logout. Validate ActivityKit start/update/end and stale or out-of-order updates on device. Distinguish provider acceptance from OS presentation.

## Deliverable

Leave the registration-to-provider flow and report an environment-specific delivery trace, APNs response and observed device behavior.

## Sources

[Live Activities essentials](https://developer.apple.com/videos/play/wwdc2026/223/?time=579), [APNs provider requests](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns), and [ActivityKit push](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications). Resolve current framework and Worker transport details before choosing APIs.
