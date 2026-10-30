# Source lessons

These are condensed source-era lessons from the supplied Apple library. Check current documentation before implementation. The workflow is editorial synthesis rather than verbatim Apple requirements.

## 5. WWDC25: Get to know the new design system | Apple

Apple's design system connects visual geometry, interface hierarchy, and consistent behavior across devices. Adopting Liquid Glass is an opportunity to revisit component structure and navigation as well as appearance.

[Original session](https://www.youtube.com/watch?v=DS2ildqCrB0) · Original library transcript: `transcripts/05-DS2ildqCrB0.md`

- Use fixed, capsule, and concentric shapes intentionally. Nested shapes should share comfortable margins and radii that relate to their enclosing surface. [Evidence at 00:03:42.268](https://www.youtube.com/watch?v=DS2ildqCrB0&t=222s)

- Keep content and the floating functional layer clearly separated. Anchor presentations to the controls that trigger them so their relationship is understandable. [Evidence at 00:07:00.397](https://www.youtube.com/watch?v=DS2ildqCrB0&t=420s)

- Express toolbar hierarchy through layout and grouping. Group related actions, move secondary actions into menus, and keep primary actions distinct. [Evidence at 00:09:33.847](https://www.youtube.com/watch?v=DS2ildqCrB0&t=573s)

- Use tab-bar accessories for persistent features such as playback. Keep screen-specific actions with the content they affect. [Evidence at 00:10:40.861](https://www.youtube.com/watch?v=DS2ildqCrB0&t=640s)

- Apply scroll-edge effects only where floating UI overlaps content. Choose an appropriate soft or hard boundary and avoid mixing or stacking them. [Evidence at 00:12:22.981](https://www.youtube.com/watch?v=DS2ildqCrB0&t=742s)

- Extend suitable imagery and backgrounds behind inset sidebars, while keeping text and controls above the extension effect. [Evidence at 00:13:04.721](https://www.youtube.com/watch?v=DS2ildqCrB0&t=784s)

- Preserve shared component anatomy, action meanings, and core interactions across platforms. Use familiar symbols, with text labels when an icon would be ambiguous. [Evidence at 00:16:35.760](https://www.youtube.com/watch?v=DS2ildqCrB0&t=995s)

Visual examples: [Concentric shapes](https://www.youtube.com/watch?v=DS2ildqCrB0&t=218s) — The construction lines show related corner centers and the spacing between nested shapes.; [Toolbar grouping](https://www.youtube.com/watch?v=DS2ildqCrB0&t=585s) — The share and Select actions sit together on one capsule-shaped toolbar surface.; [Extending sidebar backgrounds](https://www.youtube.com/watch?v=DS2ildqCrB0&t=780s) — The sidebar material carries color from the adjacent image while controls remain readable.

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

## 14. WWDC26: Design intuitive search experiences | Apple

Search placement communicates both how to access it and what it searches. The session combines platform-specific placement guidance with suggestions, filtering, and graceful empty states to reduce the effort of finding content.

[Original session](https://www.youtube.com/watch?v=lx45sKEnZkU) · Original library transcript: `transcripts/14-lx45sKEnZkU.md`

- Choose search placement based on the app's navigation and search scope. On iPhone, consider reachable toolbar or tab placements for frequent searches. [Evidence at 00:03:55.665](https://www.youtube.com/watch?v=lx45sKEnZkU&t=235s)

- Use a search landing tab when discovery content is useful; use a prominent search tab when people usually want to start typing immediately. [Evidence at 00:06:13.967](https://www.youtube.com/watch?v=lx45sKEnZkU&t=373s)

- Place scoped search near the content it searches. On iPad and Mac, use toolbar, sidebar, or dedicated-section placement to clarify which results will change. [Evidence at 00:07:40.314](https://www.youtube.com/watch?v=lx45sKEnZkU&t=460s)

- Preserve familiar search-field elements and behavior even when applying custom branding. [Evidence at 00:02:36.048](https://www.youtube.com/watch?v=lx45sKEnZkU&t=156s)

- Offer useful recent searches and relevant predictive suggestions. Let people clear their history, visually separate typed text from predictions, and keep results prominent. [Evidence at 00:12:11.032](https://www.youtube.com/watch?v=lx45sKEnZkU&t=731s)

- Start broad and let people refine results with contextual filters or scope controls. Tokens can complement visible filters but are less discoverable. [Evidence at 00:14:31.905](https://www.youtube.com/watch?v=lx45sKEnZkU&t=871s)

- Provide a clear no-results state and show the current query so people can recognize typos or revise their search. [Evidence at 00:15:12.375](https://www.youtube.com/watch?v=lx45sKEnZkU&t=912s)

Visual examples: [Search landing experiences](https://www.youtube.com/watch?v=lx45sKEnZkU&t=391s) — Apple TV fills its search landing page with browsable genres before a query is entered.; [Search placement and scope](https://www.youtube.com/watch?v=lx45sKEnZkU&t=520s) — Mail places search in a multi-column interface where the surrounding content defines its scope.; [Filters and search tokens](https://www.youtube.com/watch?v=lx45sKEnZkU&t=840s) — A sender token narrows the message results while preserving the search field and keyboard.

## 24. A guide to layout in SwiftUI | Meet with Apple

Build predictable layouts by understanding how containers propose space, children report preferred sizes, and modifiers affect that conversation.

[Original session](https://www.youtube.com/watch?v=d3JQBEw8jhM) · Original library transcript: `transcripts/24-d3JQBEw8jhM.md`

- Reason about layout recursively: containers propose sizes, subviews report their preferred sizes, and containers place the results. [Evidence at 00:05:46.280](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=346s)

- Account for each view’s sizing behavior; make an image resizable and choose fit or fill when preserving its aspect ratio matters. [Evidence at 00:06:53.990](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=413s)

- Raise layout priority for content that should receive space first when sibling views compete for limited room. [Evidence at 00:12:44.400](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=764s)

- Provide ViewThatFits alternatives in preference order so the interface can choose a simpler layout instead of truncating important text. [Evidence at 00:15:27.000](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=927s)

- Use text-baseline alignment for adjacent labels with different visual sizes. [Evidence at 00:17:19.400](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=1039s)

- Favor adaptive layouts over explicit frames; use overlays and backgrounds when decorative content should inherit the base view’s size. [Evidence at 00:17:43.990](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=1063s)

- Debug layout with colored borders, translucent overlays, selectable previews, and Xcode’s view debugger. [Evidence at 00:19:25.150](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=1165s)

Visual examples: [Size proposals and responses](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=461s) — The stage diagram shows a size proposal moving from a container to its subviews.; [ViewThatFits alternatives](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=930s) — ViewThatFits evaluates child alternatives in their declared order.; [Text-baseline alignment](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=1035s) — The dotted baseline shows aligned text across different controls.

## 25. WWDC22: The SwiftUI cookbook for navigation | Apple

Navigation becomes model state: links add values, destinations map those values to views, and split-view selection adapts across device sizes.

[Original session](https://www.youtube.com/watch?v=6Rp71CvKIKs) · Original library transcript: `transcripts/25-6Rp71CvKIKs.md`

- Bind a NavigationStack to a path of values to support programmatic pushes, deep links, and popping back to the root. [Evidence at 00:02:06.693](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=126s)

- Separate a NavigationLink’s value from its destination view with navigationDestination; use a typed array for one value type or NavigationPath for heterogeneous values. [Evidence at 00:09:23.830](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=563s)

- Combine NavigationSplitView with list selection for multicolumn navigation that automatically adapts to narrow presentations. [Evidence at 00:13:14.127](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=794s)

- Compose a NavigationStack inside a split-view column when the detail area needs its own push/pop history. [Evidence at 00:14:51.190](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=891s)

- Register destinations outside lazy containers so the stack can find them regardless of which rows or tiles have loaded. [Evidence at 00:16:28.087](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=988s)

- Restore navigation using stable model identifiers rather than serializing entire model values, and handle identifiers whose objects have been deleted. [Evidence at 00:21:28.354](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=1288s)

- Encapsulate navigation state in a Codable model and persist it per scene with SceneStorage, restoring and saving from a view-lifecycle task. [Evidence at 00:18:15.661](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=1095s)

Visual examples: [A data-driven navigation path](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=138s) — NavigationStack binds its path while links carry values instead of separate active flags.; [Split-view selection](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=797s) — The selected category and recipe appear together on iPad while iPhone pushes through the hierarchy.; [Restoring navigation by identifier](https://www.youtube.com/watch?v=6Rp71CvKIKs&t=1291s) — Decoding recipe identifiers reconstructs the navigation path using the shared data model.

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

## 30. WWDC25: Principles of inclusive app design | Apple

Identify mismatches between an interface’s assumptions and people’s abilities, and collaborate with affected people to close those gaps.

[Original session](https://www.youtube.com/watch?v=pD43DI-VA20) · Original library transcript: `transcripts/30-pD43DI-VA20.md`

- Consider vision, hearing, motor, speech, and cognitive abilities as spectra, including temporary and situational limitations. [Evidence at 00:02:35.619](https://www.youtube.com/watch?v=pD43DI-VA20&t=155s)

- Look for the inclusion gap between what a person can do and what the environment assumes they can do. [Evidence at 00:05:05.235](https://www.youtube.com/watch?v=pD43DI-VA20&t=305s)

- Include people with disabilities in decisions affecting them, rather than substituting assumptions for lived experience. [Evidence at 00:07:48.231](https://www.youtube.com/watch?v=pD43DI-VA20&t=468s)

- Support multiple ways to receive information and interact, such as visual content, speech, captions, haptics, and hands-free controls. [Evidence at 00:08:34.044](https://www.youtube.com/watch?v=pD43DI-VA20&t=514s)

- Let people customize presentation and interaction to suit their individual needs, including text, density, colors, and reading modes. [Evidence at 00:12:57.640](https://www.youtube.com/watch?v=pD43DI-VA20&t=777s)

- Adopt accessibility APIs and test assistive technologies such as VoiceOver and Switch Control, alongside support for larger text. [Evidence at 00:17:30.079](https://www.youtube.com/watch?v=pD43DI-VA20&t=1050s)

- Track known inclusion gaps as ongoing work so the team can plan improvements and make conscious design decisions. [Evidence at 00:08:45.121](https://www.youtube.com/watch?v=pD43DI-VA20&t=525s)

Visual examples: [The inclusion gap](https://www.youtube.com/watch?v=pD43DI-VA20&t=317s) — The stair-step barrier illustrates the gap between a person and an environment designed around assumptions.; [Multiple ways to interact](https://www.youtube.com/watch?v=pD43DI-VA20&t=739s) — The recipe app exposes a Hands Free mode for advancing steps without touching the screen.; [Customizable presentation](https://www.youtube.com/watch?v=pD43DI-VA20&t=802s) — Accessibility Reader changes font, size, and color to match an individual reading preference.

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


## iPad design addition — 2026-10-06

### 00:01:34.519

Choose a sidebar for a hierarchy that benefits from exposed destinations.

[Evidence at 00:01:34.519](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=94s). Caption anchor: “deeply nested content”.

### 00:03:16.388

Adapt to available width rather than orientation alone.

[Evidence at 00:03:16.388](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=196s). Caption anchor: “change in width”.

### 00:03:49.027

Resizing should preserve context and allow restoration of the expanded presentation.

[Evidence at 00:03:49.027](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=229s). Caption anchor: “non-destructive”.

These design refinements preserve existing behavior and compatibility. Verify actual resize/input transitions; a static screenshot does not prove them.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### Design for iPhone Duo | Apple — 00:04:15.000

Adapt to the offered size classes and safe regions instead of inferring layout solely from a device name.

[Evidence at 00:04:15.000](https://www.youtube.com/watch?v=do3UqxfYc3I&t=255s). Caption anchor: “Instead, always target these size classes. Build”.

### WWDC25: Elevate the design of your iPad app | Apple — 00:03:42.080

Resizing should preserve the person's layout choices and working context rather than permanently changing them.

[Evidence at 00:03:42.080](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=222s). Caption anchor: “Apps that don’t use a tab bar”.

### WWDC25: What’s new in SwiftUI | Apple — 00:12:27.000

Spatial overlays and alignment depend on the supported platform; avoid carrying visionOS assumptions into every target.

[Evidence at 00:12:27.000](https://www.youtube.com/watch?v=cETgTtu6atM&t=747s). Caption anchor: “and adjust the overlay’s alignment based on”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
