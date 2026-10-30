# App command contract

For each command record: purpose, input schema, domain action, target scope, read/write/destructive classification, completion guarantee, output, failure modes, and fixture-based check. Keep command registration, help, and an optional MCP schema derived from one maintained definition when that reduces drift.

- IDs remain stable across launches. Reuse existing durable identity. Reject ambiguous prefixes rather than choosing the first match.
- Lists are bounded and return pagination state. Large results are referenced by an artifact when appropriate.
- Read operations have no hidden mutation or launch side effect unless explicitly documented.
- Writes reuse validation and durable state ownership. Specify how retry behaves; a timeout may mean the action completed but its response was lost. Do not blindly repeat a consequential action.
- Destructive or externally visible operations return a reviewable target/preview before any required execution step. Machine-readable annotations describe behavior; they do not enforce authorization.
- A CLI machine mode returns documented structured output with consistent error/exit behavior. MCP uses its SDK's current transport and protocol rules; do not invent JSON framing from a CLI contract.
- Local IPC must isolate the correct OS user, app instance, and test store. Socket file permissions alone do not protect against every same-user process. Inspect parent directories, endpoint replacement, payload bounds, and supported peer validation. Do not add a network endpoint for convenience.
- Debug-only test commands should not ship enabled accidentally. Production automation is a separate product capability with its own contract.

Test parsing, domain outcomes, transport round trips, and UI refresh at their respective layers. Include an unavailable app, invalid input, a stale endpoint, and failure after submission when the transport can produce that ambiguity. Avoid adding XPC, sockets, or a second binary if an existing app boundary already meets the requirement.
