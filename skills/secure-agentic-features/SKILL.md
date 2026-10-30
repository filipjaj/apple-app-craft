---
name: secure-agentic-features
description: "Review or improve security of Foundation Models or other agentic app features, including prompt injection, tool authorization and context exposure. Use when a model can call tools or act on app data."
---

# Secure Agentic Features

## Goal

Ensure model-selected tools obey the same authorization and confirmation rules as direct user actions.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Inventory tools, accessible data, side effects and entry surfaces, including locked-device access. Separate low-risk reads from destructive, private or externally visible operations. Define authority from the actual user and account context, not from the model’s generated text.

2. Keep developer instructions separate from untrusted user input, retrieved documents and tool results. Treat all external content as data even if it asks the agent to change policy. Limit context to what the current task needs and protect secrets from prompts and logs.

3. Validate tool arguments, target identity and current authorization immediately before execution. Require appropriate authentication or confirmation for risky operations under the app’s existing contract. A schema-conforming call or a framework guardrail does not prove the action is permitted.

4. If the installed framework supports a pre-execution interception hook, use it to reject invalid calls before the executor acts; otherwise enforce the checks inside the domain/tool operation. Context transformations may be scoped to one inference iteration, so apply necessary protections at each relevant boundary.

5. Evaluate adversarial content, locked-device entry, stale authorization, wrong targets, repeated calls and forbidden tools. Verify actual side effects and absence of disallowed execution, not just a reassuring final response. Preserve safe failure and useful non-agent alternatives.

## Verify the outcome

- Unauthorized tool execution is rejected at the action boundary.
- Untrusted content cannot replace developer or user authority.
- Evaluations inspect side effects and forbidden actions.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
