---
name: apple-app-craft
description: "Load first for any work on an Apple-platform app in Swift or SwiftUI, before planning or writing code: build or scaffold a new iOS, iPadOS, macOS or watchOS app, add a feature, review an app or its user flow end to end, make a design more premium or less generic, fix state, navigation, concurrency, layout, performance or accessibility, add widgets, Live Activities, App Intents, App Clips, StoreKit, sync, push, camera, maps, on-device models, tests, or get a build to TestFlight and the App Store. Routes to the specialized workflows and names the system capabilities the app could use but does not yet. Also when the user mentions Apple App Craft."
---

# Apple App Craft

## Goal

Coordinate the specialized Apple App Craft skills toward the user’s requested app outcome. This entry point lets the user name the collection without remembering every skill name.

## How to use the collection

1. Identify the requested outcome and available app artifacts. For an existing project, inspect its conventions, primary journeys, and relevant implementation first. Preserve its product direction, supported targets, user data, and working behavior.
2. Use the catalog below to select the workflows relevant to the task. Read each selected SKILL.md before applying it. Start with the entrypoint and its necessary references; do not read every reference in the collection by default.
3. Tell the user briefly which workflows you are applying and why. Keep a focused fix focused; for a broad app improvement, begin with evidence-based review and prioritize the most consequential findings.
4. Carry authorized work through implementation and the selected skills’ verification criteria. Coordinate dependencies between design, state, navigation, persistence, and tests. The collection supplies methods, not a mandate to add those features to every app.
5. When the task creates an app, adds a feature, or reviews one broadly, run the opportunity check below and put its result in the plan or the report.
6. Inspect the integrated result and report the changed behavior, verification evidence, and limitations. Distinguish source inspection, rendered output, actual interaction, accessibility testing, and measured performance.

If a listed skill cannot be found, check the normal skill discovery locations for its exact name. Complete unaffected work and identify the missing component; do not claim it was applied. All linked skill directories are bundled beside this entry point in the plugin and in a complete filesystem installation.

## Bounded app delivery

For a multi-step app build or backlog, read [the delivery workflow](references/delivery-workflow.md). It connects reference evidence, a focused brief, checkable slices, implementation, and proportionate verification. Start at the stage supported by the available artifacts; a known bug does not need a new brief. Continue within the user's authorized milestone and stop when its criteria pass. Use the artifact shapes in that reference only when the project lacks equivalents.

## Opportunity check

These workflows cover capabilities that rarely get asked for by name, so they go unused unless you bring them up. When creating an app, planning a feature, or doing a broad review, compare what the app does against the signals below and tell the user which ones fit.

How to suggest:

- Offer at most three, the strongest first. One line each: the capability, what it would do in this app specifically, and the workflow name. No generic pitch.
- Suggest at plan time, before the build starts, so the user can fold it into scope. After a build or review, add any that the finished work revealed under a short "Could also use" heading.
- Suggest, do not build. Implement only what the user accepts. A declined suggestion is not raised again in that project.
- Check availability against the project's deployment target and SDK before suggesting; say so when a capability needs a newer OS than the app supports.
- If nothing fits, say nothing. An empty check is a valid result.

| Signal in the app or brief | Suggest | Workflow |
|---|---|---|
| The task starts at a physical place or object, from a QR code, NFC tag or shared link, or new users must act before installing (pay, check in, track a parcel, join an invite) | An App Clip for that one task | build-app-clip, then configure-app-clip-invocation for the QR/NFC/link launch and optimize-app-clip-size when the build is over budget |
| The task pairs a Bluetooth accessory or acts on an NFC tag | Accessory onboarding and protocol-specific handling | connect-app-accessories |
| The app shows, picks, or reacts to music (now playing, playlists, a soundtrack for a moment) | Apple Music playback and library access | integrate-music-playback |
| Notes, annotation, markup on photos or documents, signatures, sketches | A PencilKit/PaperKit canvas with editable strokes | build-drawing-canvas |
| The app owns a catalog of things people can point a camera at (products, food, places, plants, parcels) | Surfacing its entities in system visual search | integrate-visual-intelligence |
| The app calls its own backend, and that backend costs money per call (LLM, transcription), holds a hardcoded or shared token, or can be abused | App Attest so the server only serves genuine app instances | verify-app-attestation |
| Capturing a photo or video is the core action, not an occasional attachment | A purpose-built capture screen with fast launch and hardware controls instead of a system picker | build-responsive-camera |
| The app parses untrusted bytes (BLE or network protocols, file formats, firmware), wraps C/C++, or uses unsafe pointers | Sanitizer coverage and memory-safety hardening at that boundary | harden-app-memory-safety |
| Tests or development need a real backend, database or queue running locally | Reproducible local services in containers instead of hitting production or a hand-started server | isolate-local-app-services |
| The product has a web page, landing page or companion site, and a physical or 3D subject | A progressive 3D preview on the web side | add-web-3d-preview |
| The app sends short text or image tasks to a server model (summarize, classify, extract, tag, rewrite, suggest) | Running that task on device with Foundation Models, keeping the server as the alternative | build-foundation-model-feature |
| An on-device model feature needs more reasoning than the device model gives, or must explain quota and offline limits | Private Cloud Compute for the heavy requests | configure-private-cloud-compute |
| One assistant or chat in the app changes mode (planning, editing, answering) and needs different instructions or tools per mode | Profiles on one session instead of separate sessions | compose-foundation-model-profiles |
| The app already has a server model (Gemini, Workers AI, Claude) and wants the same session and tool API on device and server | A provider adapter behind the Foundation Models interface | adapt-language-model-provider |

The more common system surfaces follow the same rule when the app has something glanceable, ongoing or actionable and lacks them: design-app-widgets, design-live-activity, integrate-app-intents.

## Common requests

- **Improve an existing app:** review-apple-app and review-app-design establish the problems; improve-interface-hierarchy clarifies structure and choices. Select design or implementation skills according to the findings, then verify changed areas.
- **Design or build an app:** plan-native-app establishes a focused journey and runs the opportunity check; design-app-interface and design-native-controls define the screens and interactions. Use prototype-swiftui-flow when a design question needs a runnable exploration, then choose the necessary implementation and verification workflows.
- **Make choices clearer:** improve-interface-hierarchy handles content order, option comparison, and action priority; add improve-ux-copy or design-native-controls when labels or behavior contribute to confusion.
- **Build or improve intelligence:** build-foundation-model-feature defines a scoped task; configure-private-cloud-compute handles cloud availability and quota recovery, compose-foundation-model-profiles handles changing task modes, and evaluate-model-quality measures model and prompt choices. Select these only when the app needs intelligence.
- **Design a system snippet:** design-interactive-snippets covers compact results, confirmation, state refresh, and spoken feedback; use integrate-app-intents when entity lookup or underlying action integration also needs work.
- **Connect accessories or read NFC tags:** connect-app-accessories covers BLE, Core NFC, and AccessorySetupKit. For explicitly requested Wi-Fi Aware transport, use integrate-wifi-aware.
- **Embed web content:** integrate-webkit-swiftui covers page ownership, resource loading, navigation policies, JavaScript calls, and native content interaction. Use it for a SwiftUI app’s embedded web experience.
- **Improve performance:** profile-swiftui-performance diagnoses responsiveness; optimize-app-rendering-power targets rendering energy; profile-foundation-model-performance targets intelligence latency; guard-app-performance-regressions makes a critical journey measurable over releases. Select the relevant goal and measure it.
- **Improve iPad workspaces:** manage-app-windows preserves independent document contexts; design-app-command-menus organizes persistent commands and targets the active scene. Add adapt-apple-platform-design for width changes and design-native-controls for pointer behavior.
- **Inspect or rebuild a reference app:** capture-reference-app produces the observed screen/command inventory; plan-native-app translates the chosen behavior into slices. design-app-interface handles the native adaptation.
- **Build a Mac utility:** integrate-macos-utilities covers menu bar lifecycle, global shortcuts, panels, permissions, and cross-app boundaries; manage-app-windows handles ordinary document/scene windows.
- **Make an app scriptable:** build-app-automation defines requested CLI/bridge/MCP capabilities using the app's domain operations. Add it only when automation is part of the product request.
- **Verify a Mac app:** verify-macos-app connects SwiftProbe results, isolated runtime fixtures, actual window captures, and interactions. Report separate evidence for each claim.
- **Build or repair an App Clip:** build-app-clip defines the focused task, shared entry and full-app continuation; optimize-app-clip-size measures distribution size and launch cost; configure-app-clip-invocation handles discovery, domain association and launch testing. Select only the goals needed.
- **Review only:** use the appropriate review workflows and return prioritized evidence. Do not edit source unless requested.
- **Fix a known issue:** go directly to the relevant specialized skill rather than mandating a complete app audit.

If the user explicitly asks to go through every skill, consider each skill’s applicability and report which were applied or skipped and why. Do not introduce unrelated services, 3D features, or system integrations simply to exercise their skills.

- **Handle data and transport:** build-resilient-networking covers requests and transfers. Use sync-app-with-backend for an app-owned service and synchronize-app-data for CloudKit. Use extract-document-content for recognition.
- **Add system experiences:** design-app-widgets, build-responsive-camera, build-drawing-canvas, integrate-music-playback and integrate-map-experience apply only when the requested app needs that capability.
- **Improve trust and access:** protect-app-data-privacy, secure-app-authentication, verify-app-attestation, harden-app-memory-safety and secure-agentic-features each address a distinct boundary.
- **Prepare for delivery:** ship-apple-app covers a concrete signed build, device install, TestFlight, and App Store submission. automate-app-delivery covers repeatable CI. Use improve-app-store-discovery for storefront optimization. Use localize-app-experience and diagnose-app-failures for their respective release work. build-storekit-purchases owns paid-access behavior.
- **Use custom intelligence:** build-custom-model-feature handles model artifacts/inference, adapt-language-model-provider preserves provider semantics, and integrate-visual-intelligence returns relevant system search results.

- **Modernize an existing app:** modernize-legacy-apple-app covers Rx/UIKit migration with a pinned baseline and parity evidence. For a bounded SwiftUI addition use embed-swiftui-in-native-app. For Mac event handling and state restoration use modernize-appkit-behavior.
- **Deliver remote notifications:** deliver-apple-push-notifications covers APNs registration, provider delivery, and Live Activity push. design-live-activity covers the presentation.
- **Capture and transcribe audio:** capture-and-transcribe-audio covers recording, stop and recovery, Speech or WhisperKit, and authorized server hand-off.
- **Build a distinctive design system:** refine-app-brand covers app-owned color, type and spacing roles, reference adaptation, and a rendered design review.

## Skill catalog

Read the linked SKILL.md for the selected workflow. Names are shown without invocation syntax so the catalog works in Codex and Claude Code.

| Skill | Goal |
|---|---|
| [embed-swiftui-in-native-app](../embed-swiftui-in-native-app/SKILL.md) | Add a SwiftUI view, menu, or scene to an existing UIKit or AppKit app while preserving its lifecycle. |
| [modernize-appkit-behavior](../modernize-appkit-behavior/SKILL.md) | Update legacy AppKit input, keyboard access, quit behavior, and window restoration. |
| [ship-apple-app](../ship-apple-app/SKILL.md) | Archive, sign, upload, install, and prepare the selected build for TestFlight or App Review. |
| [deliver-apple-push-notifications](../deliver-apple-push-notifications/SKILL.md) | Deliver and diagnose APNs and ActivityKit push across app, token store, and provider. |
| [sync-app-with-backend](../sync-app-with-backend/SKILL.md) | Converge local changes with an app-owned backend through offline edits, retries, and account switches. |
| [connect-app-accessories](../connect-app-accessories/SKILL.md) | Authorize and connect BLE accessories or implement a supported NFC tag interaction. |
| [capture-and-transcribe-audio](../capture-and-transcribe-audio/SKILL.md) | Capture recoverable audio and produce transcripts with an on-device engine or an app-owned service. |
| [modernize-legacy-apple-app](../modernize-legacy-apple-app/SKILL.md) | Move an Rx/UIKit slice behind SwiftUI while checking parity against a pinned release. |
| [plan-native-app](../plan-native-app/SKILL.md) | Define the smallest coherent experience that lets the intended person accomplish their main task. |
| [prototype-swiftui-flow](../prototype-swiftui-flow/SKILL.md) | Produce a runnable prototype that answers a specific design question. |
| [review-apple-app](../review-apple-app/SKILL.md) | Find the most consequential obstacles to a reliable, understandable app experience. |
| [build-swiftui-state](../build-swiftui-state/SKILL.md) | Make each state value have a clear owner and the lifetime the user expects. |
| [fix-adaptive-layout](../fix-adaptive-layout/SKILL.md) | Keep essential content and actions usable as space and text size change. |
| [build-app-navigation](../build-app-navigation/SKILL.md) | Keep people oriented and preserve their place through exploration and focused tasks. |
| [improve-app-search](../improve-app-search/SKILL.md) | Let people understand what they search and efficiently reach useful results. |
| [adopt-liquid-glass](../adopt-liquid-glass/SKILL.md) | Create a clear floating control layer that remains legible over app content. |
| [refine-app-brand](../refine-app-brand/SKILL.md) | Make the app recognizably its own without making common tasks harder. |
| [create-layered-app-icon](../create-layered-app-icon/SKILL.md) | Deliver an identifiable icon that survives small sizes, platform masks, and appearance changes. |
| [improve-ux-copy](../improve-ux-copy/SKILL.md) | Make each message help the person decide or complete the next useful action. |
| [audit-app-accessibility](../audit-app-accessibility/SKILL.md) | Let people complete the same essential tasks with different abilities and input methods. |
| [design-live-activity](../design-live-activity/SKILL.md) | Show the current event’s most useful information at a glance on every supported presentation. |
| [integrate-app-intents](../integrate-app-intents/SKILL.md) | Make system-invoked actions resolve the same entities and obey the same domain rules as the app. |
| [add-swiftdata-persistence](../add-swiftdata-persistence/SKILL.md) | Preserve domain data across launches with predictable relationships and efficient reads. |
| [fix-swift-concurrency](../fix-swift-concurrency/SKILL.md) | Keep asynchronous work responsive and consistent without introducing unsafe sharing. |
| [profile-swiftui-performance](../profile-swiftui-performance/SKILL.md) | Reduce the measured work that causes the user-visible responsiveness problem. |
| [refine-swiftui-motion](../refine-swiftui-motion/SKILL.md) | Use motion to explain a state change without delaying the task. |
| [compose-swiftui-effects](../compose-swiftui-effects/SKILL.md) | Build an understandable graphics pipeline with controlled cost and readable content. |
| [simplify-swift-apis](../simplify-swift-apis/SKILL.md) | Make the public capability simpler while retaining useful compile-time guarantees. |
| [fix-swift-ownership](../fix-swift-ownership/SKILL.md) | Make required objects stay alive and unwanted objects release at intentional boundaries. |
| [test-swift-behavior](../test-swift-behavior/SKILL.md) | Prove a user-relevant invariant or failure recovery with isolated, repeatable tests. |
| [add-web-3d-preview](../add-web-3d-preview/SKILL.md) | Keep product exploration useful when 3D is loading, unavailable, or unsupported. |
| [isolate-local-app-services](../isolate-local-app-services/SKILL.md) | Run the needed local service with reproducible dependencies and bounded host access. |
| [design-app-interface](../design-app-interface/SKILL.md) | Turn a defined user task into a coherent, implementable screen design. |
| [review-app-design](../review-app-design/SKILL.md) | Identify the design changes that most reduce hesitation and effort in a specific task. |
| [design-native-controls](../design-native-controls/SKILL.md) | Make an interaction understandable, predictable, and usable through equivalent input methods. |
| [adapt-apple-platform-design](../adapt-apple-platform-design/SKILL.md) | Preserve the user’s task while making each supported platform feel appropriate to its context. |
| [improve-interface-hierarchy](../improve-interface-hierarchy/SKILL.md) | Make essential information easy to scan and choices understandable at the moment people need to act. |
| [build-foundation-model-feature](../build-foundation-model-feature/SKILL.md) | Turn one user task into a useful, validated intelligence feature with an appropriate model and a working alternative when intelligence is unavailable. |
| [configure-private-cloud-compute](../configure-private-cloud-compute/SKILL.md) | Use cloud reasoning only where it improves the task and keep the feature understandable and recoverable when PCC cannot serve a request. |
| [compose-foundation-model-profiles](../compose-foundation-model-profiles/SKILL.md) | Keep one session coherent as task state changes its active instructions, tools, model, and context view. |
| [evaluate-model-quality](../evaluate-model-quality/SKILL.md) | Choose and improve an intelligence configuration using repeatable evidence about task success, latency, and regressions. |
| [design-interactive-snippets](../design-interactive-snippets/SKILL.md) | Let people understand an intent’s outcome and complete a short follow-up task without losing their current context. |
| [integrate-wifi-aware](../integrate-wifi-aware/SKILL.md) | Pair the intended nearby devices and exchange app data reliably over an appropriately scoped, power-conscious Wi-Fi Aware connection. |
| [integrate-webkit-swiftui](../integrate-webkit-swiftui/SKILL.md) | Make embedded web content behave as a coherent part of the app, with predictable navigation, loading, interaction, and failure recovery. |
| [optimize-app-rendering-power](../optimize-app-rendering-power/SKILL.md) | Reduce measured rendering power while preserving visible updates, legibility, and essential background work. |
| [profile-foundation-model-performance](../profile-foundation-model-performance/SKILL.md) | Make an existing intelligence feature deliver useful results sooner without reducing task correctness or breaking session context. |
| [guard-app-performance-regressions](../guard-app-performance-regressions/SKILL.md) | Catch meaningful slowdowns in a critical user journey and produce enough evidence to diagnose them before release. |
| [manage-app-windows](../manage-app-windows/SKILL.md) | Let people open, identify and return to independent work contexts without replacing or losing their existing work. |
| [design-app-command-menus](../design-app-command-menus/SKILL.md) | Make app commands easy to find, predictable in position and correctly targeted to the person’s active work. |
| [build-app-clip](../build-app-clip/SKILL.md) | Let someone complete one contextual task immediately and continue in the full app without losing the task or its data. |
| [optimize-app-clip-size](../optimize-app-clip-size/SKILL.md) | Deliver the promised App Clip task quickly within the size budget required by its supported systems and invocation methods. |
| [configure-app-clip-invocation](../configure-app-clip-invocation/SKILL.md) | Make supported discovery surfaces launch the right App Clip experience and task, with verifiable behavior before and after full-app installation. |
| [design-app-widgets](../design-app-widgets/SKILL.md) | Surface one timely piece of app value and its most useful action without requiring the app to open. |
| [localize-app-experience](../localize-app-experience/SKILL.md) | Make the same app task understandable and usable in each requested language and locale. |
| [diagnose-app-failures](../diagnose-app-failures/SKILL.md) | Find an app failure’s cause from reproducible behavior and relevant diagnostic evidence. |
| [build-storekit-purchases](../build-storekit-purchases/SKILL.md) | Grant and maintain the correct paid access across purchase, renewal, cancellation and recovery. |
| [protect-app-data-privacy](../protect-app-data-privacy/SKILL.md) | Collect and use only the data needed for the user’s chosen task, with accurate disclosure and enforceable choices. |
| [secure-app-authentication](../secure-app-authentication/SKILL.md) | Let the intended account sign in and recover access while maintaining server-verified identity. |
| [harden-app-memory-safety](../harden-app-memory-safety/SKILL.md) | Reduce exploitable memory defects at the app’s actual unsafe-code boundaries without masking the underlying bugs. |
| [secure-agentic-features](../secure-agentic-features/SKILL.md) | Ensure model-selected tools obey the same authorization and confirmation rules as direct user actions. |
| [verify-app-attestation](../verify-app-attestation/SKILL.md) | Use server-validated app integrity signals to reduce abuse without blocking legitimate users indiscriminately. |
| [build-custom-model-feature](../build-custom-model-feature/SKILL.md) | Run a chosen on-device model with correct inputs, validated output and acceptable preparation and inference costs. |
| [adapt-language-model-provider](../adapt-language-model-provider/SKILL.md) | Preserve the app’s generation contract when connecting a different language-model provider. |
| [integrate-visual-intelligence](../integrate-visual-intelligence/SKILL.md) | Return relevant app entities quickly from a supported visual-intelligence search request. |
| [build-responsive-camera](../build-responsive-camera/SKILL.md) | Make capture ready promptly and preserve correct saved output across supported camera entry points. |
| [build-drawing-canvas](../build-drawing-canvas/SKILL.md) | Preserve editable drawing content and predictable interactions as the canvas zooms, scrolls and reopens. |
| [integrate-music-playback](../integrate-music-playback/SKILL.md) | Play the intended music through a coherent queue while respecting authorization and subscription capability. |
| [integrate-map-experience](../integrate-map-experience/SKILL.md) | Let people find and identify the intended place with trustworthy map context and useful recovery. |
| [automate-app-delivery](../automate-app-delivery/SKILL.md) | Produce a reproducible tested build and a deliberate distribution path for the intended audience. |
| [improve-app-store-discovery](../improve-app-store-discovery/SKILL.md) | Help the intended audience understand the app’s value and measure whether presentation changes improve meaningful acquisition. |
| [build-resilient-networking](../build-resilient-networking/SKILL.md) | Complete the intended network operation or recover predictably without duplicating its effects. |
| [synchronize-app-data](../synchronize-app-data/SKILL.md) | Converge intended local and cloud data while preserving edits, account boundaries and sharing permissions. |
| [extract-document-content](../extract-document-content/SKILL.md) | Turn a document image into useful structured information while preserving uncertainty and source context. |
| [design-app-charts](../design-app-charts/SKILL.md) | Communicate the intended data comparison accurately and legibly at the app’s real data volume. |
| [handle-background-work](../handle-background-work/SKILL.md) | Finish useful deferred work when the system grants time and preserve a recoverable state when it does not. |
| [integrate-drag-drop](../integrate-drag-drop/SKILL.md) | Move or copy the intended app content to a valid destination without corrupting its source or identity. |
| [build-accessible-reading](../build-accessible-reading/SKILL.md) | Let people read, navigate and select long-form content through their preferred supported reading mode. |

## Working boundaries

See [tooling and portability](references/tooling.md) when checking runtime prerequisites or using this collection on another machine.

Use the project’s actual SDK, deployment targets, and Swift language/isolation settings. For framework or CLI details, use Context7 when available and current official documentation as the fallback. Delegate only when authorized and the environment supports it; naming the collection does not request subagents or select a model.

Read [source lessons](references/source-lessons.md) when the collection’s purpose, task focus, or agent-assisted workflow needs grounding. Specialized decisions belong in the selected skills rather than being duplicated here.

## Mac workflow additions

| Skill | Goal |
|---|---|
| [capture-reference-app](../capture-reference-app/SKILL.md) | Derive a scoped screen, command, and behavior inventory from observed reference evidence. |
| [integrate-macos-utilities](../integrate-macos-utilities/SKILL.md) | Build requested system-facing Mac features with explicit lifecycle and permission recovery. |
| [build-app-automation](../build-app-automation/SKILL.md) | Expose requested app actions through a verified command contract and chosen transport. |
| [verify-macos-app](../verify-macos-app/SKILL.md) | Connect scoped acceptance to actual build, runtime, visual, and interaction evidence. |

Workflow additions are adapted from [Bama, with source and MIT license](references/bama-source.md).
