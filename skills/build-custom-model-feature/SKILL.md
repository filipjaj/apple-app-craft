---
name: build-custom-model-feature
description: "Integrate, author, or optimize a custom on-device model using Apple Core AI or the existing supported model runtime. Use for custom model artifacts and inference, not merely prompting the system Foundation Model."
---

# Build Custom Model Feature

## Goal

Run a chosen on-device model with correct inputs, validated output and acceptable preparation and inference costs.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Confirm the task, model provenance/license, artifact format and actual SDK/deployment support. Inspect the model’s functions, input/output types and shapes. Keep an existing runtime when it meets the task; do not upgrade deployment targets merely to use a session’s new API.

2. Implement the same preprocessing, normalization, tokenization and layout assumptions used to validate the model. Compare representative outputs against the reference implementation, including malformed input and numerical edge cases. Guided output structure still requires semantic validation.

3. Decide whether bundling or feature-triggered download is appropriate. Communicate download/preparation state and handle cancellation, unavailable storage, offline use and changed models. Avoid downloading a large model for people who never use the feature.

4. Prepare or specialize supported models before interactive inference and manage caches deliberately. Handle cache invalidation and purging without assuming a persistent bookmark guarantees availability. Validate the replacement before switching active model state and keep a recoverable last-known version when the product requires it.

5. Measure cold preparation, warm inference, peak memory and quality on representative supported devices. Optimize function boundaries, allocation and data layout only when the trace justifies it, and compare again against the correctness baseline. Report unsupported systems and a usable fallback.

## Verify the outcome

- Reference and device outputs meet task-specific correctness checks.
- Download and cache loss recover without corrupting active state.
- Preparation and inference costs are measured separately.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
