---
name: configure-app-clip-invocation
description: "Configure, troubleshoot, or review App Clip discovery and launch through generated links, websites, QR/NFC/App Clip Codes and other apps. Use for experience registration, domain association, card presentation and end-to-end launch testing; not universal-link configuration for an app without an App Clip."
---

# Configure App Clip Invocation

## Goal

Make supported discovery surfaces launch the right App Clip experience and task, with verifiable behavior before and after full-app installation.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. Resolve App Clips with Context7 and query the concept being implemented; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for dated evidence and current-rule distinctions. Preserve the user’s product direction and existing working behavior.

## Workflow

1. List the exact invocation surfaces, supported iOS versions, contextual parameters and card variants needed by the product. Choose among generated default links, demo links, associated website links and advanced experiences using Apple’s current invocation matrix. Every clip needs a default experience. Advanced experiences serve additional domains, locations or business-specific cards when required; do not carry forward the 2021 blanket rule that every QR/NFC invocation requires an advanced experience.

2. For a generated default link, use the actual URL provided by App Store Connect rather than constructing one from a remembered example. Default links work from iOS 16.4 and can carry permitted app-specific parameters. Demo links cannot carry parameters and are for app demos, including their special size/invocation conditions. Generated links require review and release for real testing; local Xcode launch does not prove they work publicly.

3. For custom website invocation, configure the associated domains on the full app and clip targets, and publish the AASA appclips entry using the App Clip’s full application identifier, including its application identifier prefix. Add each exact host and serve its own association file; preserve existing AASA entries. A working www host does not validate a different bare host. Inspect redirects and the encoded physical-code host separately; a successful Safari redirect is not proof that a scanned code is associated.

4. Configure only the experiences and card metadata needed for the intended surfaces. Match imagery, subtitle and action to the task the URL actually opens; localize when relevant. Use website banner/card metadata for an associated website and verify the rendered meta tag, including identifiers. Card appearance has system and user-choice conditions; a remembered preference or private browsing can change what is shown. Do not treat the card as app UI that can be rewritten dynamically at launch.

5. Use the existing lifecycle’s browsing-web user activity to pass invocation context into shared clip/full-app routing. Preserve Apple-owned link parameters, validate app-specific values, and handle absent URLs or repeated invocations. For launching another clip from an app on supported systems, use Link Presentation for a rich preview and supported default/demo links with Link or UIApplication.open as appropriate. Do not promise that opening any advanced URL directly gives identical behavior.

6. For physical codes, choose NFC-integrated versus scan-only placement by reach and context. Generate from the registered URL or a deliberate local test URL with the current App Store Connect or generator workflow. Keep codes visible, upright, undamaged and large enough for the actual scanning distance; verify the printed artifact on a device, not just its SVG preview. Scan and inspect the encoded URL before distributing it.

7. Test distinct layers: _XCAppClipURL for routing in Xcode, local experiences for card/code interaction on a test device, TestFlight for beta launch paths, and released configuration for domain and experience validation. Local experiences override configured experiences; remove them before assessing production. They do not establish Maps/location/Spotlight discovery or full-app universal-link behavior. Exercise installed-full-app invocations independently and distinguish cold/warm launch, missing parameters, fallback-to-web and expired targets.

8. When discovery fails, diagnose the exact failed layer: metadata, registration, URL matching, host entitlement/AASA agreement, caching or app routing. Check App Store Connect validation status and current tools before syntax-specific commands; account for propagation time and developer cache overrides without repeatedly changing unrelated settings. Prepare server and App Store Connect changes concretely and make external publication only within the user’s authorized scope.

## Verify the outcome

- Each required surface opens its intended experience and task on supported OS versions.
- Every custom host has matching entitlements, valid AASA identifiers and correct metadata.
- Test evidence distinguishes Xcode routing, local card flow, beta distribution and released discovery.
- The full app handles the same invocation and local overrides do not mask production failure.

Do not infer production discovery from _XCAppClipURL, assume redirects validate all hosts, or confuse default links with parameter-free demo links.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, compatibility decisions, performed checks and remaining limits. Use the project’s required build/test tools (including SwiftProbe when configured); source review alone does not prove device or distribution behavior.
