# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 6. WWDC24: SwiftUI essentials | Apple

SwiftUI views are declarative descriptions that compose into larger interfaces and update as their data changes. The framework combines adaptive components with lower-level customization and interoperability, allowing incremental adoption.

[Original session](https://www.youtube.com/watch?v=HyQgpxX__-A) · Original library transcript: `transcripts/06-HyQgpxX__-A.md`

- Describe the UI you want using value-type views. Use imperative actions to change state, then let SwiftUI update the interface. [Evidence at 00:04:50.212](https://www.youtube.com/watch?v=HyQgpxX__-A&t=290s)

- Compose small reusable views and modifiers. Modifier order defines the resulting hierarchy, and splitting views does not inherently hurt performance. [Evidence at 00:05:17.048](https://www.youtube.com/watch?v=HyQgpxX__-A&t=317s)

- Choose a clear source of truth. Use State for view-owned storage and Binding when a child must read and edit state owned elsewhere. [Evidence at 00:10:49.045](https://www.youtube.com/watch?v=HyQgpxX__-A&t=649s)

- Make animation part of a state change and choose transitions appropriate to the content, such as a numeric transition for a changing score. [Evidence at 00:12:06.405](https://www.youtube.com/watch?v=HyQgpxX__-A&t=726s)

- Use semantic built-in components to gain platform-appropriate behavior, accessibility, and localization. Use previews to inspect different environments quickly. [Evidence at 00:13:19.874](https://www.youtube.com/watch?v=HyQgpxX__-A&t=799s)

- Share views and concepts across platforms, then adapt for each platform's input and layout conventions. A Watch crown or Mac windowing model may require specific treatment. [Evidence at 00:18:58.648](https://www.youtube.com/watch?v=HyQgpxX__-A&t=1138s)

- Adopt SwiftUI incrementally using representable views and hosting controllers to bridge UIKit or AppKit. Combine it with other SDK frameworks as the app needs them. [Evidence at 00:22:00.211](https://www.youtube.com/watch?v=HyQgpxX__-A&t=1320s)

Visual examples: [Modifier order and composition](https://www.youtube.com/watch?v=HyQgpxX__-A&t=409s) — The stacked image variants and modifier arrows show clipping, shadow, and overlay composition.; [State and bindings](https://www.youtube.com/watch?v=HyQgpxX__-A&t=661s) — The @State rating property, button mutations, and numeric label are visible together.; [Adapting across platforms](https://www.youtube.com/watch?v=HyQgpxX__-A&t=1150s) — The platform collage compares different control and navigation treatments rather than repeating one fixed layout.

## 22. WWDC21: Demystify SwiftUI | Apple

Understand how SwiftUI connects ephemeral view values to persistent state and selectively updates a dependency graph.

[Original session](https://www.youtube.com/watch?v=XwdVz0Ef1vU) · Original library transcript: `transcripts/22-XwdVz0Ef1vU.md`

- Distinguish explicit identity supplied by data or IDs from structural identity determined by a view’s type and position. [Evidence at 00:04:21.194](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=261s)

- Preserve one view’s identity when representing different states of the same element, so transitions and state remain continuous. [Evidence at 00:11:30.089](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=690s)

- Prefer ViewBuilder and generic structure over unnecessary AnyView wrappers, which erase information useful to SwiftUI and the compiler. [Evidence at 00:12:42.295](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=762s)

- State storage follows the lifetime of a view’s identity; switching between separately identified branches replaces that storage. [Evidence at 00:22:47.766](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=1367s)

- Choose stable, unique identifiers for dynamic data; computed random IDs and collection offsets can cause incorrect transitions and state loss. [Evidence at 00:34:18.957](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=2058s)

- Treat view inputs as dependencies: a changed input invalidates dependent views, and value comparison can avoid unnecessary downstream work. [Evidence at 00:30:36.468](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=1836s)

- Move a conditional into a modifier such as opacity when the condition represents one view in different states, using an inert value when appropriate. [Evidence at 00:38:26.104](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=2306s)

Visual examples: [AnyView and ViewBuilder](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=765s) — The code contrasts type erasure through AnyView with concrete conditional view types.; [Identity and state lifetime](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=1370s) — The branch code and storage diagram show how view identity controls state lifetime.; [The dependency graph](https://www.youtube.com/watch?v=XwdVz0Ef1vU&t=1848s) — The graph connects view nodes to the state values that drive their updates.

## 27. WWDC25: Optimize SwiftUI performance with Instruments | Apple

A measurement-driven walkthrough of formatter caching, granular observation, and the Cause & Effect Graph in Instruments 26.

[Original session](https://www.youtube.com/watch?v=3b1ecu-Jobk) · Original library transcript: `transcripts/27-3b1ecu-Jobk.md`

- Start with the SwiftUI instrument’s Update Groups and long-update lanes to determine whether SwiftUI work is responsible for a responsiveness problem. [Evidence at 00:03:00.643](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=180s)

- Inspect a long body update’s time range in Time Profiler to identify the expensive functions contributing to it. [Evidence at 00:07:10.508](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=430s)

- Move repeated formatting out of view bodies, reuse expensive formatter objects, and cache derived strings when their underlying inputs change. [Evidence at 00:11:50.172](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=710s)

- Consider both individual update cost and total update count: many fast view updates can collectively miss a frame deadline. [Evidence at 00:15:58.182](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=958s)

- Use the Cause & Effect Graph to find what invalidated a declarative view; an imperative call-stack backtrace may not reveal that cause. [Evidence at 00:24:45.311](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=1485s)

- Make observable dependencies granular, such as a favorite status per item, instead of having every row read a shared collection. [Evidence at 00:29:47.902](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=1787s)

- Avoid putting rapidly changing geometry or timer values in the environment, where checks across many dependent views can accumulate. [Evidence at 00:33:59.250](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=2039s)

- Record another trace after a change and verify the expected updates disappeared before treating the performance fix as complete. [Evidence at 00:14:48.120](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=888s)

Visual examples: [Inspecting a slow view body](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=442s) — Instruments shows the slow update interval alongside the Time Profiler call tree.; [Cause & Effect Graph](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=1481s) — The diagram traces a state-change signal through view-body evaluation and rendering.; [Granular observation](https://www.youtube.com/watch?v=3b1ecu-Jobk&t=1799s) — Only the first card depends on the changed favorite value, so the other cards stay unchanged.

## 28. WWDC24: Catch up on accessibility in SwiftUI | Apple

Use semantic controls and targeted accessibility information to make complex interactions understandable and efficient with assistive technologies.

[Original session](https://www.youtube.com/watch?v=PHAA6nXTbdk) · Original library transcript: `transcripts/28-PHAA6nXTbdk.md`

- Style built-in controls before replacing them with custom views, preserving the accessibility attributes and actions supplied automatically. [Evidence at 00:04:34.462](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=274s)

- Test the actual interface with VoiceOver to discover missing information, confusing associations, or excessive navigation. [Evidence at 00:05:37.375](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=337s)

- Label meaningful shapes and combine related content and buttons into one element when this makes navigation clearer. [Evidence at 00:08:12.622](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=492s)

- Use conditional accessibility modifiers to override a symbol’s label only when its application-specific meaning differs from the useful default. [Evidence at 00:10:50.735](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=650s)

- Expose hover-only controls as custom actions on the main element, and append important hidden information without erasing its existing label. [Evidence at 00:14:10.594](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=850s)

- Describe each distinct drag or drop point and consider equivalent custom actions for finite destinations. [Evidence at 00:17:49.675](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=1069s)

- Use App Intent-based accessibility actions for interactive widgets, whose views do not update like ordinary app views. [Evidence at 00:19:59.596](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=1199s)

Visual examples: [Combining accessibility elements](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=504s) — The accessibility diagram merges child labels into one meaningful element.; [Making hover content accessible](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=846s) — The accessibilityActions code exposes attachments otherwise revealed only by hovering.; [Accessible drop points](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=1072s) — Named accessibilityDropPoint modifiers identify separate destinations within a custom control.

## 29. WWDC26: Principles of great design | Apple

A framework for choosing and refining product experiences around people’s goals, context, trust, and emotional response.

[Original session](https://www.youtube.com/watch?v=Xa9L2yx_QH8) · Original library transcript: `transcripts/29-Xa9L2yx_QH8.md`

- Define a clear purpose before adding features, since every feature consumes someone’s time, attention, and trust. [Evidence at 00:00:47.326](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=47s)

- Give people agency and support exploration with recoverable actions; reserve disruptive confirmations for consequential mistakes. [Evidence at 00:02:51.052](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=171s)

- Request only necessary private information in context, explain its purpose, and anticipate ways a feature could harm people. [Evidence at 00:04:35.207](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=275s)

- Build on familiar metaphors and consistent behavior so people can predict how controls work. [Evidence at 00:07:59.153](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=479s)

- Adapt to device context, different abilities, and personal workflows rather than assuming one interface arrangement serves everyone. [Evidence at 00:09:56.240](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=596s)

- Achieve simplicity through clarity and reduced effort; sometimes adding context makes an interface easier to understand. [Evidence at 00:13:21.369](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=801s)

- Invest in responsive behavior and visual details, then maintain and evolve that quality over the product’s lifetime. [Evidence at 00:15:21.084](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=921s)

- Design toward a meaningful emotional response; delight emerges from care across the experience rather than decorative flourishes added at the end. [Evidence at 00:16:15.070](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=975s)

Visual examples: [Forgiving destructive actions](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=192s) — The confirmation sheet offers recovery before a consequential change to a document.; [Consistent control behavior](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=491s) — The tab indicator and selected content demonstrate predictable control feedback.; [Simplicity through context](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=804s) — The added duration beside the play control makes the action easier to understand.

## 31. WWDC22: Explore navigation design for iOS | Apple

Organize content around clear top-level purposes, then choose transitions that match either deeper exploration or a focused task.

[Original session](https://www.youtube.com/watch?v=Kd02qR_LyA0) · Original library transcript: `transcripts/31-Kd02qR_LyA0.md`

- Give each tab a meaningful top-level content area and distribute functionality so one catchall tab does not obscure the hierarchy. [Evidence at 00:03:31.311](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=211s)

- Avoid duplicating unrelated actions into a Home tab merely to promote discoverability; do not automatically transport people to another tab. [Evidence at 00:10:42.242](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=642s)

- Preserve access and state across tabs during hierarchical exploration, and use clear labels to explain what each tab contains. [Evidence at 00:11:05.732](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=665s)

- Use pushes for deeper levels of content and workflows that require frequent movement between views; match disclosure indicators to this behavior. [Evidence at 00:14:40.480](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=880s)

- Use titles and meaningful back labels to orient people, and respect reversed progression for right-to-left languages. [Evidence at 00:17:15.835](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=1035s)

- Use a modal for a focused, self-contained task or immersive content, with clear preferred and cancel actions. [Evidence at 00:13:41.421](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=821s)

- Warn before discarding entered data, but dismiss an untouched form directly; reserve an X close control for content with minimal interaction. [Evidence at 00:22:14.200](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=1334s)

- Limit stacked modals while allowing an appropriate nested task when it preserves consistency and focus. [Evidence at 00:23:15.995](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=1395s)

Visual examples: [Balancing top-level tabs](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=486s) — The revised tab bar gives Places, Itineraries, and Profile separate top-level destinations.; [Hierarchical push navigation](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=892s) — The navigation tree shows movement from a parent screen into deeper content.; [Discarding input and dismissing modals](https://www.youtube.com/watch?v=Kd02qR_LyA0&t=1337s) — The discard-changes sheet protects entered form data and offers a return to editing.

## 33. WWDC25: Design foundations from idea to interface | Apple

A practical design critique shows how familiar components and deliberate content organization turn an attractive screen into a usable app.

[Original session](https://www.youtube.com/watch?v=dGcqqA3Sl-o) · Original library transcript: `transcripts/33-dGcqqA3Sl-o.md`

- Evaluate whether each screen explains where the person is, what they can do, and where they can go next. [Evidence at 00:02:20.993](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=140s)

- Inventory features and workflows, understand real usage context, then remove nonessential features and group related ones before styling. [Evidence at 00:04:05.829](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=245s)

- Use tabs for navigation and put screen-specific actions in a toolbar; choose explicit labels and familiar symbols. [Evidence at 00:06:01.932](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=361s)

- Use progressive disclosure to reveal detail when relevant while keeping expanded views connected to their originating screen. [Evidence at 00:09:01.466](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=541s)

- Match layouts to content: lists support scanning structured information, while collections suit visual items with restrained text. [Evidence at 00:10:22.586](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=622s)

- Reduce choice overload by grouping content according to time, progress, or meaningful relationships. [Evidence at 00:12:07.193](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=727s)

- Build hierarchy with system text styles, support Dynamic Type, and protect text legibility over imagery. [Evidence at 00:15:20.037](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=920s)

- Use semantic system colors for adaptable interface roles and add a cohesive brand palette where it preserves legibility and appearance settings. [Evidence at 00:17:06.896](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=1026s)

Visual examples: [Tabs versus screen actions](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=373s) — The tab bar separates Records, Swaps, and Saves as top-level destinations.; [Progressive disclosure](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=564s) — The labeled disclosure control leads from a compact record group to its detailed contents.; [Type hierarchy and legibility](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=916s) — Caption, title, and subtitle labels establish a readable type hierarchy over artwork.
