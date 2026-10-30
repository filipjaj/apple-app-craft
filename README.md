# Apple App Craft

A collection of **74 skills** for planning, building, reviewing, and verifying native Apple apps with Swift and SwiftUI. One entry point coordinates the specialized skills around a scoped user outcome.

```text
reference evidence (when needed) → focused brief → usable slice
    → implementation → build / tests / visual / interaction evidence → stop
```

Start at the stage your project needs. A known bug can go directly to its owning skill; a full milestone can use a linked backlog and acceptance evidence. The workflow preserves your deployment targets, architecture, design conventions, and existing authorization.

## Install in Codex

```sh
codex plugin marketplace add filipjaj/apple-app-craft
codex plugin add apple-app-craft@apple-app-craft
```

Start a new chat after installation. For a pinned version, add the marketplace with `--ref v0.1.0`. The repository provides a portable `plugin.json`, a Codex compatibility manifest, and a repository marketplace following [OpenAI's plugin packaging documentation](https://developers.openai.com/plugins/build/plugins).

Use one installation route. If you already installed these skills individually, remove or move those duplicate copies after preserving local edits. This plugin does not remove them automatically.

### Claude Code

The package also includes Claude-compatible manifests:

```text
/plugin marketplace add filipjaj/apple-app-craft
/plugin install apple-app-craft@apple-app-craft
```

Codex installation is smoke-tested with its actual CLI; the Claude manifest is structurally checked, with runtime verification left to a Claude environment.

## Use

```text
Use $apple-app-craft to build the next usable milestone of this Mac app.
Verify its acceptance criteria and stop at that milestone.
```

```text
Use $capture-reference-app to inspect this app's main journey and prepare
an evidence-linked rebuild handoff.
```

```text
Use $verify-macos-app to check this change with actual build, rendered,
and interaction evidence. Report checks that cannot run.
```

The collection covers product planning, native design, state, navigation, persistence, concurrency, accessibility, system integrations, intelligence, performance, and distribution. Recent workflow additions connect reference-app inspection, Mac utility lifecycles, requested app automation, and deterministic verification.

## Prerequisites and limits

This is a skills-only plugin. It installs no executables, hooks, services, account connections, or application templates. Swift runtime work needs an appropriate Mac/Xcode environment; planning and source review do not.

Context7, browser/native computer use, and SwiftProbe are optional tools supplied by the host. SwiftProbe is preferred when installed; otherwise use project-native build/test tools and report that substitution. No private SwiftProbe executable or repository is distributed. See [tooling and portability](skills/apple-app-craft/references/tooling.md).

Skills are guidance rather than enforceable security boundaries. They distinguish compilation, tests, rendered output, actual interaction, assistive technology, and measured performance. Missing evidence remains visible. Static validation does not prove runtime correctness or a model's future behavior.

## Develop

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

The validator checks manifests, skill metadata, local reference containment/resolution, catalog coverage, attribution, and private-path/credential patterns. CI runs the same checks. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Skill catalog

| Skill | When to use it |
|---|---|
| [adapt-apple-platform-design](skills/adapt-apple-platform-design/SKILL.md) | Adapt an established Apple app experience across iPhone, iPad, and Mac while preserving core task semantics. Use for platform and window-context design, rather than an isolated SwiftUI sizing bug. |
| [adapt-language-model-provider](skills/adapt-language-model-provider/SKILL.md) | Implement or review a Foundation Models provider/executor adapter, including streaming, tool calls and errors. Use for provider interoperability rather than ordinary prompt tuning. |
| [add-swiftdata-persistence](skills/add-swiftdata-persistence/SKILL.md) | Implement or repair SwiftData persistence, relationships, scoped queries, and error handling in an Apple app. Use to replace in-memory storage or fix unreliable saved state. |
| [add-web-3d-preview](skills/add-web-3d-preview/SKILL.md) | Add or review a progressively enhanced 3D model preview in a web app using supported native model capabilities and usable fallback content. |
| [adopt-liquid-glass](skills/adopt-liquid-glass/SKILL.md) | Adopt or review Apple Liquid Glass in SwiftUI navigation and controls. Use for a requested design-system update or custom glass interaction, with target-SDK availability checks. |
| [apple-app-craft](skills/apple-app-craft/SKILL.md) | Use the Apple App Craft collection through one entry point to plan, build, review, or improve an Apple app. Activate when the user mentions Apple App Craft or asks to use the collection; select and apply the relevant specialized skills for the task. |
| [audit-app-accessibility](skills/audit-app-accessibility/SKILL.md) | Audit or fix accessibility in Apple app flows and custom controls, including VoiceOver semantics, larger text, gesture alternatives, and system appearance preferences. |
| [automate-app-delivery](skills/automate-app-delivery/SKILL.md) | Configure or review Apple app CI and beta delivery with Xcode Cloud or the existing pipeline and TestFlight. Use for repeatable builds, test artifacts and authorized distribution. |
| [build-accessible-reading](skills/build-accessible-reading/SKILL.md) | Build or improve TextKit-based or custom long-form reading experiences, including reading order, pagination and text accessibility. Use for document reading UI; OCR extraction has a separate goal. |
| [build-app-automation](skills/build-app-automation/SKILL.md) | Add a CLI, local command bridge, or optional MCP interface to an existing native app so scripts or agents can use its real domain actions. Use when app automation is requested; do not add automation to ordinary UI work. |
| [build-app-clip](skills/build-app-clip/SKILL.md) | Build, review, or improve a focused App Clip in an existing iOS app, including shared entry routing, capability restrictions, task completion and transition to the full app. Use for App Clip product and target architecture; use the specialized size or invocation workflow for those isolated problems. |
| [build-app-navigation](skills/build-app-navigation/SKILL.md) | Design or implement Apple app tabs, navigation paths, split views, deep links, and state restoration. Use for confusing routes, lost navigation, or new multi-screen flows. |
| [build-custom-model-feature](skills/build-custom-model-feature/SKILL.md) | Integrate, author, or optimize a custom on-device model using Apple Core AI or the existing supported model runtime. Use for custom model artifacts and inference, not merely prompting the system Foundation Model. |
| [build-drawing-canvas](skills/build-drawing-canvas/SKILL.md) | Implement or review PencilKit/PaperKit drawing, markup templates, canvas overlays or handwriting recognition. Use for editable drawing content and canvas interaction. |
| [build-foundation-model-feature](skills/build-foundation-model-feature/SKILL.md) | Build or improve a scoped Apple app intelligence feature with Foundation Models: structured generation, image input, and task-specific tools. Use when implementing an actual user-facing AI task; use configure-private-cloud-compute for PCC availability and quota recovery. |
| [build-resilient-networking](skills/build-resilient-networking/SKILL.md) | Implement or repair Apple app networking, typed API clients and resumable transfers using URLSession, Network or gRPC. Use for cancellation, failures, connection lifetime and replay-safe recovery. |
| [build-responsive-camera](skills/build-responsive-camera/SKILL.md) | Build, review, or improve an Apple camera capture experience, including session launch, hardware controls and optional Lock Screen capture. Use for camera behavior and responsiveness. |
| [build-storekit-purchases](skills/build-storekit-purchases/SKILL.md) | Build, review, or repair Apple in-app purchases and subscriptions with StoreKit, including transaction verification and lifecycle testing. Use for entitlement behavior and purchase UI, not acquisition copy alone. |
| [build-swiftui-state](skills/build-swiftui-state/SKILL.md) | Implement or repair SwiftUI state ownership, bindings, observation, and view identity. Use for lost edits, stale UI, duplicate state, or state-driven feature work. |
| [capture-reference-app](skills/capture-reference-app/SKILL.md) | Inspect an existing native or web app to produce a screen inventory, navigation and command maps, and evidence-linked requirements. Use when rebuilding an app or deriving a design from a reference; not for binary reverse engineering. |
| [compose-foundation-model-profiles](skills/compose-foundation-model-profiles/SKILL.md) | Build or repair multi-step Foundation Models experiences with dynamic instructions and profiles. Use when task modes need different tools, instructions, models, or reasoning while retaining conversation history. |
| [compose-swiftui-effects](skills/compose-swiftui-effects/SKILL.md) | Implement a requested SwiftUI graphics effect by composing layout, shader inputs, timing, and content state. Use for custom visual effects rather than routine UI styling. |
| [configure-app-clip-invocation](skills/configure-app-clip-invocation/SKILL.md) | Configure, troubleshoot, or review App Clip discovery and launch through generated links, websites, QR/NFC/App Clip Codes and other apps. Use for experience registration, domain association, card presentation and end-to-end launch testing; not universal-link configuration for an app without an App Clip. |
| [configure-private-cloud-compute](skills/configure-private-cloud-compute/SKILL.md) | Add or review Private Cloud Compute in a Foundation Models feature. Use for choosing on-device versus cloud reasoning, entitlement and availability checks, context budgets, offline fallback, or daily quota and upgrade UI. |
| [create-layered-app-icon](skills/create-layered-app-icon/SKILL.md) | Prepare or review layered Apple app-icon artwork and an Icon Composer handoff. Use for icon design, appearance variants, or project integration. |
| [design-app-charts](skills/design-app-charts/SKILL.md) | Design or implement Apple app charts with Swift Charts, including function/vectorized plots, scales and accessible meaning. Use for chart communication and rendering, not general dashboards. |
| [design-app-command-menus](skills/design-app-command-menus/SKILL.md) | Design, implement, or review an iPad or Mac app’s menu bar, command organization, keyboard shortcuts and focused-window routing. Use for discoverable persistent commands and predictable enabled states; not general context menus or an ordinary button style. |
| [design-app-interface](skills/design-app-interface/SKILL.md) | Design or redesign Apple app screens with deliberate content hierarchy, typography, spacing, color roles, and complete UI states. Use after the product journey is known; for critique of existing designs use review-app-design. |
| [design-app-widgets](skills/design-app-widgets/SKILL.md) | Design, implement, or review WidgetKit widgets, including timelines, relevant content and interactive actions. Use for glanceable system widgets; use design-live-activity for a single ongoing event. |
| [design-interactive-snippets](skills/design-interactive-snippets/SKILL.md) | Design, implement, or review App Intents snippets for Siri, Spotlight, and Shortcuts. Use for compact results, confirmations, intent-backed buttons, state refresh, and spoken feedback; use integrate-app-intents for broader entity and action integration. |
| [design-live-activity](skills/design-live-activity/SKILL.md) | Design or refine a Live Activity across Lock Screen, Dynamic Island, and StandBy presentations. Use for glanceable ongoing-event experiences. |
| [design-native-controls](skills/design-native-controls/SKILL.md) | Choose and specify controls, feedback, gestures, and presentation behavior for an Apple app interaction. Use when an interaction model is undecided or a custom control needs a complete behavior contract. |
| [diagnose-app-failures](skills/diagnose-app-failures/SKILL.md) | Investigate Apple app crashes, test failures, misleading debugger output or missing diagnostic context using Xcode reports, LLDB and structured logging. Use for diagnosis before a fix. |
| [evaluate-model-quality](skills/evaluate-model-quality/SKILL.md) | Measure and improve an Apple app intelligence feature using representative datasets and explicit quality criteria. Use to compare prompts, model providers, reasoning levels, tool configurations, or catch nondeterministic regressions; use test-swift-behavior for ordinary deterministic code. |
| [extract-document-content](skills/extract-document-content/SKILL.md) | Implement or review document recognition with Apple Vision, including tables, text, machine-readable codes and recognized fields. Use for extracting content, not building a text editor. |
| [fix-adaptive-layout](skills/fix-adaptive-layout/SKILL.md) | Repair SwiftUI clipping, truncation, alignment, or unstable measurement; implement layouts that adapt to content, window size, and Dynamic Type. |
| [fix-swift-concurrency](skills/fix-swift-concurrency/SKILL.md) | Diagnose and repair Swift actor isolation, Sendable errors, cancellation, and asynchronous work ordering; support incremental Swift language-mode migration. |
| [fix-swift-ownership](skills/fix-swift-ownership/SKILL.md) | Diagnose Swift retain cycles, premature lifetime assumptions, and unsafe weak/unowned access; improve ownership in code with actual lifetime symptoms. |
| [guard-app-performance-regressions](skills/guard-app-performance-regressions/SKILL.md) | Add or improve repeatable Apple app performance checks around a critical user journey, with scoped UI measurements, representative devices, baseline comparisons and trace-based regression triage. Use for performance regression testing and build-system changes; not ordinary functional test coverage. |
| [handle-background-work](skills/handle-background-work/SKILL.md) | Implement or repair Apple app background refresh or processing with BackgroundTasks and supported transfer APIs. Use for scheduler lifecycle and expiration, not ordinary foreground async work. |
| [harden-app-memory-safety](skills/harden-app-memory-safety/SKILL.md) | Review or improve Swift/C/C++ memory safety, sanitizer coverage and supported Enhanced Security protections. Use for unsafe-code hardening, not an ordinary ARC retention leak. |
| [improve-app-search](skills/improve-app-search/SKILL.md) | Design or repair Apple app search scope, placement, suggestions, filters, and result states. Use when finding content is confusing or a searchable feature needs implementation. |
| [improve-app-store-discovery](skills/improve-app-store-discovery/SKILL.md) | Review or improve App Store product assets, custom product pages and acquisition/monetization analysis. Use for store presence and measured experiments, not StoreKit entitlement implementation. |
| [improve-interface-hierarchy](skills/improve-interface-hierarchy/SKILL.md) | Improve an existing app screen or flow when information competes for attention, options are difficult to compare, or the next step is unclear. Reorganize content, action emphasis, and choice presentation; use design-app-interface for composing an entirely new screen. |
| [improve-ux-copy](skills/improve-ux-copy/SKILL.md) | Write or improve Apple app labels, onboarding, empty states, errors, and confirmations. Use when wording affects task understanding, recovery, or product personality. |
| [integrate-app-intents](skills/integrate-app-intents/SKILL.md) | Expose Apple app entities and actions to system experiences such as Siri and Spotlight using App Intents. Use for entity lookup, indexing, direct opening, and conversational app actions. |
| [integrate-drag-drop](skills/integrate-drag-drop/SKILL.md) | Implement or improve SwiftUI drag-and-drop, reordering and transferable content. Use for drag semantics and destination validation, including accessible alternatives. |
| [integrate-macos-utilities](skills/integrate-macos-utilities/SKILL.md) | Build or repair macOS menu bar utilities, global shortcuts, floating panels, clipboard workflows, screen capture, login items, or cross-app window control. Use for system-facing Mac features; ordinary scene navigation belongs to manage-app-windows. |
| [integrate-map-experience](skills/integrate-map-experience/SKILL.md) | Implement or refine MapKit search, geocoding, place details and app-to-Maps links. Use for geographic discovery and place interactions. |
| [integrate-music-playback](skills/integrate-music-playback/SKILL.md) | Build or repair Apple Music integration using MusicKit, including authorization, subscription checks and player ownership. Use for music playback behavior, not a generic audio-engine profile. |
| [integrate-visual-intelligence](skills/integrate-visual-intelligence/SKILL.md) | Integrate or improve Apple Visual Intelligence entity search and ranked results. Use when the system supplies visual or semantic content to discover app data. |
| [integrate-webkit-swiftui](skills/integrate-webkit-swiftui/SKILL.md) | Embed, migrate, review, or improve web content in a SwiftUI app using WebKit WebView and WebPage. Use for page ownership, loading and navigation state, custom local resource schemes, JavaScript calls, find-in-page, and synchronized scrolling; not general website development. |
| [integrate-wifi-aware](skills/integrate-wifi-aware/SKILL.md) | Build, review, or improve nearby peer-to-peer connectivity using Apple Wi-Fi Aware. Use for device pairing, declared publisher/subscriber services, Network framework connections, accessory onboarding, and measured latency/power tuning; not ordinary internet networking. |
| [isolate-local-app-services](skills/isolate-local-app-services/SKILL.md) | Set up or review reproducible local app backend services with Apple Containerization when requested and supported. Use for development/test environment isolation rather than ordinary UI work. |
| [localize-app-experience](skills/localize-app-experience/SKILL.md) | Prepare, translate, or review Apple app localization using String Catalogs and locale-aware presentation. Use for language and internationalization work, including translation-assisted workflows. |
| [manage-app-windows](skills/manage-app-windows/SKILL.md) | Build, review, or improve Apple app multiwindow and document-opening behavior, including scene-local state, descriptive window titles, restoration and iPad window-control accommodation. Use when opening another document or window must preserve existing work; not an isolated layout bug. |
| [optimize-app-clip-size](skills/optimize-app-clip-size/SKILL.md) | Measure and reduce an App Clip’s uncompressed distribution size and time to useful content. Use when an App Clip exceeds its applicable size limit, downloads too slowly, or includes unnecessary assets and dependencies; not a general SwiftUI rendering investigation. |
| [optimize-app-rendering-power](skills/optimize-app-rendering-power/SKILL.md) | Measure and reduce battery cost from unnecessary Apple app rendering, especially Liquid Glass resampling, hidden animations, and scroll edge effects. Use for rendering-related energy problems; use profile-swiftui-performance for responsiveness bottlenecks. |
| [plan-native-app](skills/plan-native-app/SKILL.md) | Turn an Apple app idea or feature brief into a focused user journey, information architecture, and implementable acceptance criteria. Use before interface construction or when feature scope is unclear. |
| [profile-foundation-model-performance](skills/profile-foundation-model-performance/SKILL.md) | Diagnose and reduce Foundation Models response latency and token overhead using request traces, prewarming, session/prefix reuse, streaming, and Generable schema changes. Use for slow existing intelligence features; use evaluate-model-quality for broader prompt/model quality selection. |
| [profile-swiftui-performance](skills/profile-swiftui-performance/SKILL.md) | Diagnose and improve measured SwiftUI responsiveness using Instruments or equivalent project profiling. Use for scrolling hitches, slow updates, and excessive invalidation. |
| [protect-app-data-privacy](skills/protect-app-data-privacy/SKILL.md) | Review or improve Apple app data access, privacy manifests, SDK data practices and consent-dependent flows. Use for implementation privacy work; not drafting legal advice. |
| [prototype-swiftui-flow](skills/prototype-swiftui-flow/SKILL.md) | Build or iterate a SwiftUI interaction prototype using realistic fixtures and rendered previews. Use to compare design alternatives or evaluate a flow before production integration. |
| [refine-app-brand](skills/refine-app-brand/SKILL.md) | Improve an Apple app’s visual identity through content, typography, color, symbols, and interaction while keeping familiar native controls. |
| [refine-swiftui-motion](skills/refine-swiftui-motion/SKILL.md) | Improve SwiftUI transitions and state-driven animation for clarity, responsiveness, and reduced-motion support. Use for awkward timing, broken continuity, or intentional interaction polish. |
| [review-app-design](skills/review-app-design/SKILL.md) | Critique an Apple app interface from screenshots, prototypes, or rendered screens for hierarchy, clarity, consistency, and task usability. Use for design feedback; use review-apple-app for broader code and reliability review. |
| [review-apple-app](skills/review-apple-app/SKILL.md) | Review an Apple app or feature across its user journey, SwiftUI implementation, and native interaction quality. Use for an explicitly requested broad review; report evidence and prioritized fixes. |
| [secure-agentic-features](skills/secure-agentic-features/SKILL.md) | Review or improve security of Foundation Models or other agentic app features, including prompt injection, tool authorization and context exposure. Use when a model can call tools or act on app data. |
| [secure-app-authentication](skills/secure-app-authentication/SKILL.md) | Implement, review, or improve passkeys and Apple AuthenticationServices account flows, including credential upgrades and recovery. Use for account authentication; App Attest verifies app integrity separately. |
| [simplify-swift-apis](skills/simplify-swift-apis/SKILL.md) | Refactor or design Swift types, protocols, and generic interfaces around concrete domain invariants. Use for repetitive overloads, unnecessary type erasure, or difficult API relationships. |
| [synchronize-app-data](skills/synchronize-app-data/SKILL.md) | Implement, review, or repair Apple app CloudKit/Core Data sync, CKSyncEngine state or cloud-sharing behavior. Use for cross-device convergence; local schema modeling belongs to persistence work. |
| [test-swift-behavior](skills/test-swift-behavior/SKILL.md) | Add or improve meaningful Swift unit and integration tests, using Swift Testing where supported and preserving the project’s existing UI and performance checks. |
| [verify-app-attestation](skills/verify-app-attestation/SKILL.md) | Implement or review Apple App Attest client/server flows, assertions and replay protection. Use for app integrity and abuse signals, not user authentication or a general privacy audit. |
| [verify-macos-app](skills/verify-macos-app/SKILL.md) | Verify a changed macOS app with build/test results, deterministic window captures, and exercised interactions tied to acceptance criteria. Use for a Mac release check or runtime/UI validation; a small source-only fix needs only proportionate checks. |

## License and credits

MIT © 2026 Filip John. Selected workflows are adapted from [BAMA](https://github.com/daveebbelaar/bama), MIT © 2026 Dave Ebbelaar. Required notices are preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [licenses/BAMA-MIT.txt](licenses/BAMA-MIT.txt).

Existing editorial source lessons link to public Apple documentation and WWDC sessions. This project is independent of Apple and OpenAI.
