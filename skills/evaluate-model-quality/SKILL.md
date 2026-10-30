---
name: evaluate-model-quality
description: "Measure and improve an Apple app intelligence feature using representative datasets and explicit quality criteria. Use to compare prompts, model providers, reasoning levels, tool configurations, or catch nondeterministic regressions; use test-swift-behavior for ordinary deterministic code."
---

# Evaluate Model Quality

## Goal

Choose and improve an intelligence configuration using repeatable evidence about task success, latency, and regressions.

## Working context

Inspect the app’s actual SDK, deployment targets, existing AI feature, and data flow. Resolve Foundation Models or Evaluations with Context7 and query the relevant concept when available; otherwise use current official Apple documentation. Read [source lessons](references/source-lessons.md) for decision criteria. The supplied WWDC26 sessions describe OS 27 features: verify each symbol against the installed SDK and gate runtime availability. Preserve supported older systems and the existing product direction.

## Workflow

1. Define the feature boundary and user-relevant success criteria before generating samples. Separate semantic accuracy, grounding, constraint compliance, tool correctness, refusal behavior, latency, and token cost where they matter. Establish project-specific acceptance thresholds rather than adopting example percentages as universal targets.

2. Build a versioned dataset covering common tasks, ambiguous or unsupported inputs, context limits, relevant languages/images, and known failures. Use appropriately authorized or synthetic data and retain a holdout set that is not used to tune prompts. Document expected behavior and dataset gaps.

3. Use code evaluators for computable properties and calibrated model judges or human review for subjective quality. Audit representative judge decisions and actual responses: a refusal, empty output, or formatting trick must not earn task-success credit by evading the metric.

4. Implement the suite with the installed Evaluations framework when supported by the project’s SDK. Resolve current API details before writing code. If unavailable, run the same dataset and explicit scoring through the project’s existing harness; retain the framework adoption as a stated limitation rather than raising the deployment target.

5. Compare a baseline and candidate on the same dataset with enough repetitions to expose variation. Record model/provider and OS versions where observable, prompt/profile version, dataset version, generation settings, reasoning level, latency, usage, and errors. Keep deterministic tool/state tests distinct from statistical model scores.

6. Inspect failures by category, form a specific hypothesis, and change one relevant factor. Rerun the relevant full suite after prompt, tool, profile, or model changes; check holdout results at useful milestones. Choose the least costly configuration that meets the agreed criteria, not the configuration with the most reasoning.

7. Keep raw outputs and scored summaries with appropriate data handling. Add confirmed failures to the regression dataset and report sample size, run variation, tradeoffs, and what was not measured. Make no device or production-quality claim from a few handpicked examples.

## Verify the outcome

- Baseline and candidate use comparable input sets, scoring, and recorded configurations.
- Inspect failed and unexpectedly perfect cases; verify subjective judges against human-reviewed examples.
- Report per-category quality and latency/cost alongside aggregate scores and holdout limitations.

Do not assert model correctness from compilation, schema validity, a single successful run, or an uncalibrated model judge.

## Deliverable

For implementation, leave the scoped change and report behavior, verification evidence, and limitations. For review or evaluation, return actionable findings and recorded results; distinguish planned checks from executed checks.
