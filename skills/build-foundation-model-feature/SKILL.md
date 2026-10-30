---
name: build-foundation-model-feature
description: "Build or improve a scoped Apple app intelligence feature with Foundation Models: structured generation, image input, and task-specific tools. Use when implementing an actual user-facing AI task; use configure-private-cloud-compute for PCC availability and quota recovery."
---

# Build a Foundation Models Feature

## Goal

Turn one user task into a useful, validated intelligence feature with an appropriate model and a working alternative when intelligence is unavailable.

## Working context

Inspect the app’s actual SDK, deployment targets, existing AI feature, and data flow. Resolve Foundation Models or Evaluations with Context7 and query the relevant concept when available; otherwise use current official Apple documentation. Read [source lessons](references/source-lessons.md) for decision criteria. The supplied WWDC26 sessions describe OS 27 features: verify each symbol against the installed SDK and gate runtime availability. Preserve supported older systems and the existing product direction.

## Workflow

1. Define the input, desired output, and what the person does with the result. Establish a simple quality baseline before choosing a model; compare the on-device model first when it supports the task. Keep a manual or conventional path for people without model availability.

2. Select only required modalities and tools. For images, use supported Attachment inputs with correct orientation and a valid image URL or pixel buffer as appropriate. The framework handles scaling and color conversion; crop only when isolating a relevant region benefits the task. Measure larger-image token and latency costs.

3. Use guided generation for domain-shaped output and validate semantic constraints before displaying or saving it. A Generable schema constrains shape; it does not establish factual accuracy. Keep uncertainty or unsupported categories representable when the product needs them.

4. Give tools narrow contracts against existing domain operations. Use OCR or barcode tools when their precision is relevant, and labeled image references when tools must resolve an attachment. Use Spotlight retrieval only when indexed app knowledge is needed; verify indexing, access, freshness, and source grounding before relying on it.

5. Manage session lifetime, streaming, cancellation, and concurrent requests through the app’s existing state ownership. Budget instructions, history, images, tool output, and generated output against the model’s reported capacity using supported token APIs. Preserve essential facts when reducing history; do not silently truncate arbitrary input.

6. Handle model unavailability, refusal, generation failure, and invalid output with an actionable UI that retains the user’s input. When selecting a third-party model, verify capability, privacy, authentication, and billing separately; never embed private provider secrets in the app binary.

7. Implement the scoped feature and exercise representative inputs. Compare output quality and latency on the intended devices; involve evaluate-model-quality when selecting prompts or models needs a repeatable benchmark.

## Verify the outcome

- Complete the core task with supported text/image inputs and a semantically valid structured result.
- Exercise unavailable intelligence, malformed or missing images, cancellation, refusal, and context pressure without losing input.
- Verify tool effects against the real data layer and distinguish device checks from mocked response tests.

Do not add a chat screen, external provider, search index, or agent architecture unless the user’s task calls for it.

## Additional source decisions

Validate generated meaning as well as schema shape, check actual model availability, and keep developer instructions separate from untrusted input. External provider credentials belong in a secure acquisition/storage flow. Evaluate forbidden tool calls and task failures explicitly rather than inferring success from fluent output.

## Deliverable

For implementation, leave the scoped change and report behavior, verification evidence, and limitations. For review or evaluation, return actionable findings and recorded results; distinguish planned checks from executed checks.
