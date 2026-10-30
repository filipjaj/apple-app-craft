---
name: improve-app-store-discovery
description: "Review or improve App Store product assets, custom product pages and acquisition/monetization analysis. Use for store presence and measured experiments, not StoreKit entitlement implementation."
---

# Improve App Store Discovery

## Goal

Help the intended audience understand the app’s value and measure whether presentation changes improve meaningful acquisition.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify the audience, core value and requested acquisition or retention question. Review real app behavior and existing store assets so proposed screenshots, imagery and copy accurately represent the product.

2. Make the first visible assets communicate the app’s useful task. Consider default versus custom product pages for distinct audiences, with relevant deep links where supported. Check current asset and placement requirements before preparing exports.

3. Choose metrics and denominators that match the question: unique impressions, page views, downloads, cohort conversion or retention are different measures. Compare like storefronts, channels, devices and time windows, separating redownloads and cohort age when relevant.

4. Design a bounded presentation experiment with a hypothesis, primary metric and sufficient observation. Use the platform’s current uncertainty/confidence reporting without treating one historical threshold or a small winning slice as universal proof.

5. Connect acquisition findings to later task success, paid conversion or retention without promising causal results from observational cohorts. Prepare reviewable asset/configuration changes, then publish only when authorized. Report actual measurements, interpretation limits and the next justified change.

## Verify the outcome

- Assets accurately communicate the app’s useful behavior.
- Comparisons use consistent cohorts and denominators.
- Experiment conclusions respect uncertainty and downstream quality.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
