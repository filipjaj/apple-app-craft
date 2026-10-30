---
name: profile-foundation-model-performance
description: "Diagnose and reduce Foundation Models response latency and token overhead using request traces, prewarming, session/prefix reuse, streaming, and Generable schema changes. Use for slow existing intelligence features; use evaluate-model-quality for broader prompt/model quality selection."
---

# Profile Foundation Models Performance

## Goal

Make an existing intelligence feature deliver useful results sooner without reducing task correctness or breaking session context.

## Working context

Inspect the actual deployment targets, SDK, project conventions, and available profiling tools. Resolve framework/API details with Context7 and query the relevant concept; use current official Apple documentation when coverage is insufficient. Read [source lessons](references/source-lessons.md) for timestamped reasoning. Preserve the requested scope and supported systems. Capture evidence before changing code; report unavailable device/tool checks clearly.

## Workflow

1. Define representative requests and a task-quality check on the actual model and device. Measure time to first useful visible result and total completion separately, including cold versus warm requests. Record model/OS, build, thermal state, input sizes and output sizes. The workshop concerns the on-device OS 26 model; do not transfer its performance assumptions to PCC or another provider.

2. Record a Foundation Models Instruments trace with relevant CPU/thermal tracks. Distinguish model loading, input processing, schema preparation, output generation and tool time. Inspect consumed, cached and generated tokens where supported. Use synthetic or authorized inputs: these trace files can contain unencrypted prompts and responses.

3. Keep concise task-specific instructions and guides, and ask only for the content the user needs. Reduce unnecessary nesting, repetitive fields and verbose generated names while retaining readable contracts and required facts. Tokenization varies; verify token counts rather than using character counts as a substitute. Renaming a persisted/public schema requires compatibility work.

4. Own the session for the intended interaction lifetime and keep stable instructions/tool definitions toward the prefix, with request-specific material in the prompt. Preserve essential history and task boundaries; session reuse must not mix unrelated users/tasks or permit concurrent conflicting requests. Do not accumulate history indefinitely merely to preserve a cache. Cache behavior depends on the provider and framework version.

5. When imminent use is likely and at least a second of lead time exists, consider prewarm(promptPrefix:) on the relevant session. Use a known matching prefix when useful. Prewarming is opportunistic and adds work; verify it moves loading off the user’s critical path, rather than warming every screen at launch.

6. Stream partial output where it helps the task and update UI from fields that are actually present. Measure first useful content separately from first token; streaming alone does not shorten total generation. Preserve cancellation, request identity and final-result validation, and avoid publishing incomplete output as a completed result.

7. Consider includeSchemaInPrompt: false only when the session already has sufficient schema guidance or examples for the same task/type. Recheck correctness on representative inputs, reset conditions and subsequent turns; keep the default when guidance remains useful. Guided generation constrains shape, not factual accuracy.

8. Change the identified bottleneck, replay comparable inputs, and record both latency/token differences and task correctness. Include unavailable-intelligence, cold start, context pressure and cancellation checks relevant to the change. Keep before/after traces and distinguish measured gains from estimates.

## Verify the outcome

- Report first useful result and completion latency, cold/warm conditions and relevant token counts.
- Validate task correctness before and after prompt/schema changes; do not trade away required facts for shorter output.
- Verify session boundaries, partial rendering, cancellation, failure recovery and context growth.

Do not disable schema guidance universally, call prewarm without useful lead time, or report streaming as a measured reduction in total generation time.

## Deliverable

Leave the scoped implementation or actionable review. Report changed behavior, baseline and candidate evidence, actual checks and limitations; distinguish a measurement plan from executed results.
