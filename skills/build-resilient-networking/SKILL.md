---
name: build-resilient-networking
description: "Implement or repair Apple app networking, typed API clients and resumable transfers using URLSession, Network or gRPC. Use for cancellation, failures, connection lifetime and replay-safe recovery."
---

# Build Resilient Networking

## Goal

Complete the intended network operation or recover predictably without duplicating its effects.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify the operation’s protocol, request/response contract, authentication and replay safety. Preserve the existing appropriate client stack. Validate HTTP status, content type and decoded semantics; successful transport or generated types alone do not prove task success.

2. Own sessions or clients at the correct shared lifetime to reuse connections, and cancel work when its task no longer needs the result. Choose network constraints and background behavior for the actual platform and purpose; do not disconnect every client indiscriminately or assume async means off-main execution.

3. Use bounded retries informed by transient error, server guidance and operation idempotency. Handle authentication refresh without loops and guard against replaying destructive requests. Early data must be replay-safe; do not use handshake acceleration to bypass transaction safety.

4. For downloads, retain resume data and the temporary file as required, validate byte-range support and resource identity such as ETag, and restart safely when resumption is invalid. Move completed files to durable storage at the supported callback boundary and handle filesystem failure separately.

5. Test cancellation, timeout, offline transitions, malformed responses, server errors and interrupted transfers under realistic connectivity. Verify exactly-once domain effects through idempotent server contracts where needed; report measured transport behavior rather than claiming it from a mocked happy path.

## Verify the outcome

- Failures are classified and recover without duplicate side effects.
- Obsolete requests cannot overwrite current state.
- Transfer recovery preserves valid bytes and handles invalid resume state.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
