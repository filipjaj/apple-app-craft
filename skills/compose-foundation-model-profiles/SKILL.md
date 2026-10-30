---
name: compose-foundation-model-profiles
description: "Build or repair multi-step Foundation Models experiences with dynamic instructions and profiles. Use when task modes need different tools, instructions, models, or reasoning while retaining conversation history."
---

# Compose Foundation Models Profiles

## Goal

Keep one session coherent as task state changes its active instructions, tools, model, and context view.

## Working context

Inspect the app’s actual SDK, deployment targets, existing AI feature, and data flow. Resolve Foundation Models or Evaluations with Context7 and query the relevant concept when available; otherwise use current official Apple documentation. Read [source lessons](references/source-lessons.md) for decision criteria. The supplied WWDC26 sessions describe OS 27 features: verify each symbol against the installed SDK and gate runtime availability. Preserve supported older systems and the existing product direction.

## Workflow

1. Map the existing journey into explicit task modes, their state owner, required facts, tools, allowed effects, and model capabilities. Use a static session for a task that does not need dynamic configuration; introduce profiles only where switching is necessary.

2. Compose DynamicInstructions from the state needed for the next request. Instructions and tools re-evaluate before model requests, so read current app state rather than capturing a stale copy. Keep stable instructions first and append conditional parts in place where useful for model caching.

3. Choose one active Profile through exhaustive conditional or switch branches in LanguageModelSession.DynamicProfile. Configure its model and reasoning for the current mode, reuse model instances when appropriate, and preserve conversation history through the session rather than manually copying it between unrelated sessions.

4. Treat transitions as app domain operations. A model-invoked mode-switch tool must validate that the transition is allowed and that required state exists. Expose only tools relevant to the mode and apply the same authorization and validation as the app’s ordinary actions.

5. Inspect effective configuration precedence: call-site generation arguments override the innermost profile modifiers, which override outer defaults. Lifecycle callbacks accumulate across nested profiles; keep side effects deliberate and cleanup correct rather than assuming a callback overrides its parent.

6. Define each profile’s context view before a model change. Use documented history transforms to exclude irrelevant or sensitive material without accidentally destroying global conversation state. Count tokens for the destination model, preserve references needed by tool calls, and handle PCC unavailability or quota without invalid transitions.

7. Verify mode changes on successive requests, cancellation, failed tool calls, returning to earlier modes, and a switch to a smaller model. Report active profile, effective configuration, and context decisions in scoped diagnostics that respect app data handling.

## Verify the outcome

- Each reachable mode resolves to exactly one active profile with the intended toolset.
- Verify current state is visible on the next request and model transitions retain necessary history.
- Exercise forbidden transitions, missing tool references, callback failure, cancellation, quota fallback, and context overflow.

Do not assume profile switching erases history, disables domain authorization, or automatically runs multiple agents in parallel.

## Deliverable

For implementation, leave the scoped change and report behavior, verification evidence, and limitations. For review or evaluation, return actionable findings and recorded results; distinguish planned checks from executed checks.
