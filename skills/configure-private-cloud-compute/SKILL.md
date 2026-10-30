---
name: configure-private-cloud-compute
description: "Add or review Private Cloud Compute in a Foundation Models feature. Use for choosing on-device versus cloud reasoning, entitlement and availability checks, context budgets, offline fallback, or daily quota and upgrade UI."
---

# Configure Private Cloud Compute

## Goal

Use cloud reasoning only where it improves the task and keep the feature understandable and recoverable when PCC cannot serve a request.

## Working context

Inspect the app’s actual SDK, deployment targets, existing AI feature, and data flow. Resolve Foundation Models or Evaluations with Context7 and query the relevant concept when available; otherwise use current official Apple documentation. Read [source lessons](references/source-lessons.md) for decision criteria. The supplied WWDC26 sessions describe OS 27 features: verify each symbol against the installed SDK and gate runtime availability. Preserve supported older systems and the existing product direction.

## Workflow

1. Evaluate the existing task with the on-device model before escalating to PCC for demonstrated reasoning or context needs. Verify the managed entitlement, current developer eligibility, supported device/region, actual SDK, and OS availability. The supplied article lists PCC on iOS, macOS, watchOS, and visionOS 27 or later; keep an older-system path.

2. Create a PCC-backed LanguageModelSession through the documented model initializer and check the selected model’s availability before requesting. Keep tools and output schemas consistent where supported; do not introduce developer API keys or a separate login for PCC.

3. Start reasoning evaluation at moderate and compare light/deep only against the task’s quality and latency requirements. Reasoning consumes context too. Budget instructions, history, attachments, tool results, reasoning, and final output using supported context-size/token APIs; a larger model is not unlimited.

4. Map network failure, device/system unavailability, daily quota exhaustion, cancellation, and other errors to distinct states. Retry locally only if the on-device model is available and the input and task fit its capabilities. Reduce context deliberately or offer a conventional alternative for large tasks; never blindly replay a 32K cloud conversation into a smaller local model.

5. Inspect quotaUsage before requesting and handle quotaLimitReached during a request. Show persistent status beside the affected action for approaching/reached limits; preserve input, avoid repeat requests known to fail, and offer the framework’s limitIncreaseSuggestion only when supplied. Use resetDate only when known. Daily quota exhaustion is not transient rate limiting.

6. Keep fallback bounded and preserve completed tool effects: restarting model generation must not duplicate writes, purchases, or other domain operations. Do not silently route personal data to a third-party service as a PCC substitute.

7. Exercise the Xcode scheme’s simulated approaching/reached quota states, offline operation, older OS behavior, and mid-request errors. Inspect the actual affected UI including accessibility labels and recovery after availability or quota changes.

## Verify the outcome

- Confirm the configured entitlement and runtime gates; report cloud execution as untested if the required device or access is missing.
- Exercise available, unavailable, approaching quota, exceeded quota, unknown reset date, and network failure states.
- Verify local fallback fits its budget and capability, preserves input, and does not duplicate completed side effects.

Do not describe PCC as unlimited or offline, treat an iCloud upgrade as mandatory, or claim every Foundation Models provider inherits Apple’s PCC privacy properties.

## Deliverable

For implementation, leave the scoped change and report behavior, verification evidence, and limitations. For review or evaluation, return actionable findings and recorded results; distinguish planned checks from executed checks.
