---
name: adapt-language-model-provider
description: "Implement or review a Foundation Models provider/executor adapter, including streaming, tool calls and errors. Use for provider interoperability rather than ordinary prompt tuning."
---

# Adapt Language Model Provider

## Goal

Preserve the app’s generation contract when connecting a different language-model provider.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify the existing generation contract, provider capabilities, authentication and current framework protocol requirements. Check supported SDKs and environments before adopting a new executor/provider API.

2. Translate the conversation and developer-requested options deliberately, including tool schemas, structured output, context limits and generation settings. Declare or fail unsupported capabilities rather than silently weakening the caller’s requirements.

3. Implement streaming with ordered, coherent events, cancellation and terminal failure semantics. Ensure tool-call identifiers and results remain paired and that the application retains control over authorized execution; provider output is not permission.

4. Use secure token acquisition and storage rather than embedding private keys in the app. Surface provider usage and relevant limits, and map errors to built-in categories when their meaning matches while retaining genuinely provider-specific failures.

5. Test complete and interrupted streams, structured output, multiple tool turns, unsupported options, rate limits and authentication failure. Compare the same app task across providers and disclose quality, latency, cost and privacy differences.

## Verify the outcome

- Required options are preserved or explicitly rejected.
- Streams and tool turns remain coherent under cancellation.
- Credentials and provider failures have safe handling.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
