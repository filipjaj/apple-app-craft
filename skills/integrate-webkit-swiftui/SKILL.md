---
name: integrate-webkit-swiftui
description: "Embed, migrate, review, or improve web content in a SwiftUI app using WebKit WebView and WebPage. Use for page ownership, loading and navigation state, custom local resource schemes, JavaScript calls, find-in-page, and synchronized scrolling; not general website development."
---

# Integrate WebKit with SwiftUI

## Goal

Make embedded web content behave as a coherent part of the app, with predictable navigation, loading, interaction, and failure recovery.

## Workflow

1. Inspect the requested web task, existing embedding code, supported platforms, deployment target, installed SDK, and Swift isolation settings. Resolve WebKit API details with Context7 when available or current official Apple documentation otherwise. WebPage is MainActor-isolated; preserve an existing compatible WKWebView wrapper when older targets or required capabilities still need it rather than raising the deployment target just to migrate.

2. Use WebView with a URL for straightforward display. Use an app-owned WebPage when the task needs loading control, observable state, history, policies, or JavaScript. Give the page and model the lifetime the document or browsing session requires; do not recreate a page or reload its URL on every SwiftUI body evaluation. Configure the data store and page preferences deliberately, preserving existing sign-in and persistence expectations.

3. Load URL requests, HTML with the intended base URL, or data with correct MIME type, encoding, and base URL. Show useful progress, readiness, and recoverable errors. Observe loading/navigation through APIs available in the actual SDK: current docs list WebPage.navigations and load-returned event sequences, while the video demonstrates currentNavigationEvent with Observations. Do not assume every started navigation finishes; handle redirects, provisional failure, later failure, cancellation and superseded loads.

4. Associate page-derived state and asynchronous work with the active navigation/document. Refresh titles, table of contents, and loading indicators from the current page; discard an older page’s late JavaScript or metadata result after another navigation. Cancel feature-owned observation tasks when their owner ends, and avoid repeatedly registering observers.

5. Define which schemes and origins belong inside the app and which links should open elsewhere. Use WebPage.NavigationDeciding with parsed URLs and an explicit main-page policy, not substring host tests or the sample’s fictional domain. Cancel the embedded navigation before routing an external link through the app’s supported openURL behavior. Account for redirects, authentication challenges, and missing URLs without changing existing trust or permission rules.

6. When local/custom resources are needed, register a URLSchemeHandler in WebPage.Configuration before creating the page. Use a supported custom URLScheme rather than intercepting a built-in scheme. Resolve only intended bundled or authorized resources, with response metadata before resource data; finish or fail the async sequence and honor cancellation. Test relative CSS/image requests, missing resources, and request paths that escape the intended resource scope.

7. Use callJavaScript with an arguments dictionary for values instead of interpolating them into script source. Validate optional/dynamic results into the required Swift types and handle JavaScript errors or a changed document. Specify frame/content-world behavior where the task requires it; do not give unrelated web content access to privileged app actions merely because it renders in the same view.

8. Apply findNavigator, scrolling/bounce behavior, and supported WebView-specific scroll APIs only where they help the task. For table-of-contents synchronization, distinguish user scrolling from programmatic selection updates to avoid feedback loops; recompute positions when layout or content changes. Keep focus, keyboard use, safe-area controls, larger text, and platform-specific input behavior usable.

9. Complete the scoped change and inspect actual rendered content and navigation. Exercise remote and local loads, internal/external links, redirects and failures, back/forward history when offered, JavaScript type/error cases, cancellation, and rapid page switching. For a migration compare required existing behavior before removing its wrapper; report platform checks that could not run.

## Verify the outcome

- Stable page ownership preserves expected content, history and authentication state across ordinary SwiftUI updates.
- Exercise failed/slow loads, redirects, cancellation, and rapid switching without stale titles, sections or loading state.
- Local resource handlers produce valid responses, resolve relative assets, reject unintended paths, and terminate on error/cancellation.
- External links reach the intended destination once; in-app navigation remains within the agreed policy.
- Verify JavaScript arguments/results and find/scroll behavior on rendered content, including missing sections and layout changes.
- Distinguish inspected code, mocks, previews, and actual WebKit/device behavior; do not claim platform parity from one run.

Do not copy session-era API spelling without SDK checks, reload on every render, trust arbitrary page scripts, or report web integration success from compilation alone.

## Deliverable

Leave the scoped web-content implementation, migration, or review findings. Report page lifetime, loading and navigation behavior, resource/JavaScript boundaries, tested interactions and remaining compatibility limits.

Read [source lessons](references/source-lessons.md) for timestamped evidence and current API documentation.
