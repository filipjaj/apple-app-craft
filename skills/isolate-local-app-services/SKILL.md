---
name: isolate-local-app-services
description: "Set up or review reproducible local app backend services with Apple Containerization when requested and supported. Use for development/test environment isolation rather than ordinary UI work."
---

# Isolate Local App Services

## Goal

Run the needed local service with reproducible dependencies and bounded host access.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Inspect the app’s actual backend needs, existing environment tooling, host support, and target image architecture. Keep an established working container workflow unless Apple Containerization is requested or solves a concrete requirement.
2. Distinguish the image’s filesystem/configuration from a running instance. Define the smallest service and explicit versions needed for reproducible development or integration testing.
3. Use current CLI documentation and inspect actual command schemas before issuing commands. Choose the CLI for ordinary service use and framework APIs only for a genuine container-management application.
4. Limit shared host directories to needed paths; distinguish disposable test data from persistent local data. Define resource allocation, service reachability, and health checks.
5. Start and verify the service, connect the app’s development configuration, and document restart and cleanup operations. Do not mutate production services or delete persistent data as part of local setup.

## Verify the outcome

- Check startup from the image and verify an actual app-to-service operation.
- Verify host mounts, architecture, reachability, and expected persistence after restart.
- Stop only task-created disposable resources and report environment limitations.

A per-container virtual machine does not eliminate risks from broadly shared host folders or exposed secrets.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
