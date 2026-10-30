---
name: build-responsive-camera
description: "Build, review, or improve an Apple camera capture experience, including session launch, hardware controls and optional Lock Screen capture. Use for camera behavior and responsiveness."
---

# Build Responsive Camera

## Goal

Make capture ready promptly and preserve correct saved output across supported camera entry points.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify photo/video requirements, supported devices, camera entry points and existing capture architecture. Request permissions contextually and provide denied/unavailable states. Discover actual device/format capabilities rather than assuming a specific front camera.

2. Configure and run the capture session without blocking UI and serialize changes appropriately. Prioritize first usable preview; defer unrelated resources and controls until preview begins. Measure cold launch and first-frame time before optimizing.

3. Choose capture format, orientation and sensor-compensation behavior for supported hardware and the intended output. Measure quality and energy tradeoffs rather than applying one RAW or frame-rate rule to every capture mode.

4. Handle all events after opting into physical capture controls. Keep controls related to capture and provide usable on-screen alternatives. Never start a camera session solely to gain access to a control.

5. For a requested Lock Screen extension, respect its process, authorization and session-content boundaries. Transfer captured content deliberately to the full app; do not reuse unrestricted app storage or network assumptions. Test interruptions, partial photo permissions, save failure, locked-device flow and actual output orientation.

## Verify the outcome

- Preview becomes usable promptly under measured conditions.
- Every adopted input method performs the expected capture.
- Saved output and interrupted sessions preserve user intent.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
