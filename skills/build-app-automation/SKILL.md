---
name: build-app-automation
description: "Add a CLI, local command bridge, or optional MCP interface to an existing native app so scripts or agents can use its real domain actions. Use when app automation is requested; do not add automation to ordinary UI work."
---

# Build App Automation

Expose the requested app capabilities through a small, inspectable command contract. Reuse the app's validation, data ownership, side effects, and Undo rules.

## Contract before transport

Read [command and transport decisions](references/command-contract.md) when designing the interface. Inventory only requested operations. Define stable IDs, bounded results, actionable errors, and read/write/destructive classifications. Do not introduce model fields or expose private model identifiers just to imitate a template.

Choose an existing transport when it fits. A local command bridge to the running app can preserve one owner of mutable state; do not open its live SwiftData store in a second process by default. CLI and MCP are separate user choices. Neither a CLI nor a network listener is mandatory for an MCP request. Fetch current docs through Context7 for the selected SDK/protocol/library and concept; use official specifications for gaps.

## Implement

1. Parse and validate inputs at the boundary, then call the same domain operation the UI uses. Respect actor isolation without putting blocking transport work on the UI thread. Return success only after the command's stated persistence or completion guarantee is met.
2. Provide discoverable help and examples. Machine output has a documented schema and stable success/error results; diagnostics go outside the protocol channel. Use bounded pagination and unambiguous IDs. Reject ambiguous abbreviated IDs.
3. Bind a local transport to the intended user and app instance. Restrict endpoint and parent-directory permissions, reject unexpected paths/peers as supported, bound message size and timeouts, and handle stale endpoints and concurrent callers. Local access does not authenticate human intent.
4. Separate test and production stores, sockets, and process identity. Auto-launch only if it is part of the chosen contract, with an opt-out where useful. Avoid changing shell startup files, registering clients, or exporting production data unless within the request.
5. Give consequential actions a concrete preview and an explicit execution step when the app's contract requires it. Keep remote sending distinct from drafting. Authorization still comes from the human or calling application's permissions; protocol annotations and a boolean flag do not establish it.
6. Exercise reads and writes against disposable fixtures. Verify both persisted results and the live UI update. Cover invalid input, missing/ambiguous IDs, unavailable app, retries, timeout, and duplicate submission where relevant. Test through the selected real transport, not just the command handler.

## Done when

Help alone is sufficient to complete a representative task, the chosen transport has passed its contract checks, UI and command results agree, and installation/registration steps and remaining gaps are reported. Use SwiftProbe for Swift tests; do not run an autonomous agent against live user data as an acceptance test.

Workflow attribution: [Bama source and license](references/bama-source.md).
