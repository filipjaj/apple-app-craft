---
name: automate-app-delivery
description: "Configure or review Apple app CI and beta delivery with Xcode Cloud or the existing pipeline and TestFlight. Use for repeatable builds, test artifacts and authorized distribution."
---

# Automate App Delivery

## Goal

Produce a reproducible tested build and a deliberate distribution path for the intended audience.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Inspect the repository, schemes, test plans, signing and existing CI requirements. Define the intended build/test/archive actions and audience, and choose supported toolchain versions deliberately. Do not replace working CI merely because the source session uses Xcode Cloud.

2. Configure start conditions and required dependency/repository access. Use pinned project dependencies and reproducible setup scripts with meaningful failure handling. Scope credentials and secret environment variables; avoid printing them or depending on a developer’s local cache.

3. Run the actual schemes and meaningful tests on supported destinations, preserving result bundles and failure artifacts. Distinguish product failures from environment/signing problems and compare the cloud configuration with a known local build.

4. Prepare the distribution postaction and tester instructions for the requested audience, including known issues and what to exercise. Internal-only artifacts are not automatically valid for external distribution, and beta approval is distinct from App Store release.

5. Verify the configured workflow with an authorized build before declaring it working. Preserve explicit boundaries for upload, notifications and release actions; publishing to testers or the store requires the user’s authorization. Report the tested build identity, artifact locations and remaining distribution steps.

## Verify the outcome

- A clean environment reproduces the intended build and tests.
- Dependencies, signing and secrets are deliberately scoped.
- Distribution targets the authorized audience and build.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
