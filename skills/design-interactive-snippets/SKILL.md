---
name: design-interactive-snippets
description: "Design, implement, or review App Intents snippets for Siri, Spotlight, and Shortcuts. Use for compact results, confirmations, intent-backed buttons, state refresh, and spoken feedback; use integrate-app-intents for broader entity and action integration."
---

# Design Interactive Snippets

## Goal

Let people understand an intent’s outcome and complete a short follow-up task without losing their current context.

## Workflow

1. Identify the routine task, host system experience, existing intent, entity identity, and expected outcome. Inspect supported platforms, installed SDK, deployment targets, and existing shortcut return values. Verify current App Intents APIs through Context7 when available or official Apple documentation otherwise. Read the source lessons for design and lifecycle decisions.

2. Choose a static result when displaying an outcome is sufficient, or an interactive snippet when a relevant follow-up action helps. Use confirmation before the intent performs an action requiring a decision, with an outcome-specific verb; show the result after commitment. Parameter adjustment is separate from executing the final action. Preserve cancellation and existing domain authorization.

3. Design for glanceability: prioritize the result or decision, readable system text, consistent responsive margins, and a small set of relevant controls. The session recommends staying within roughly 340 points before scrolling; treat this as session-era design guidance, not a hard height that clips larger text. Offer the relevant app destination when the task requires deeper content.

4. Check branded backgrounds for legibility at a distance as well as ordinary contrast and appearance changes. Use flexible layout and container-relative geometry where appropriate. Make action and selection states understandable without color alone, and provide accessible button labels.

5. For implementation, return the documented snippet result from the existing AppIntent while retaining its prior typed return value for shortcut compatibility. Construct the interactive view through SnippetIntent and wire Button or Toggle actions to AppIntents that invoke existing domain operations, rather than relying on ordinary local view closures.

6. Keep display-oriented SnippetIntent.perform() fast and free of side effects: the system may create and perform it repeatedly. Pass minimal immutable identity and fetch current dynamic state through shared dependencies. Perform mutations in the action intent, then render the actual result; verify repeated view generation cannot submit another order or duplicate a write.

7. Provide useful IntentDialog for screen-free execution and make the visual snippet understandable without hearing the dialog. Some Siri paths may not show the dialog or snippet; keep typed results meaningful and enforce consequential decisions through supported intent confirmation rather than assuming a visual button always appears.

8. Reload when underlying data or progress changes using supported snippet APIs. Verify the documented reload behavior: it can present an absent snippet and dismiss another visible snippet. Avoid unrelated background refresh that unexpectedly replaces the person’s current system interaction.

9. Exercise results, parameter changes, confirmation, cancellation, failed actions, fresh state, and repeated snippet execution in available Siri, Spotlight, or Shortcuts contexts. For a design-only request, leave a concrete layout and state/voice specification; when implementation is requested, complete the change and appropriate project checks.

## Verify the outcome

- The result is understandable visually and through spoken feedback; actions are labeled by their outcomes.
- Cancellation performs no final mutation; repeated display or refresh does not duplicate an action.
- Existing shortcut output remains compatible and snippet buttons see current shared app state.
- Inspect long/localized text, accessibility text sizes, VoiceOver, light/dark appearance, and delayed or failed requests where supported.
- Distinguish previews and mocked lifecycle checks from actual system invocation; report unavailable host/device checks.

Do not turn a snippet into a full app screen, hard-code the session’s height guidance as an accessibility constraint, or use snippet refresh as an excuse to repeat domain mutations.

## Deliverable

Leave the scoped snippet design, implementation, or review findings. Explain result versus confirmation behavior, refresh ownership, voice support, checks performed, and remaining limitations.

Read [source lessons](references/source-lessons.md) for timestamped design evidence and the official implementation article.
