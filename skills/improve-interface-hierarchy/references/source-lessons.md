# Source lessons

Condensed source-era lessons from the supplied Apple library. The choice-comparison and verification workflow is an editorial synthesis; these sessions do not establish a universally optimal number of choices or primary actions.

## 5. WWDC25: Get to know the new design system | Apple

Apple's design system connects visual geometry, interface hierarchy, and consistent behavior across devices. Adopting Liquid Glass is an opportunity to revisit component structure and navigation as well as appearance.

[Original session](https://www.youtube.com/watch?v=DS2ildqCrB0) · Library transcript: `transcripts/05-DS2ildqCrB0.md`

- Use fixed, capsule, and concentric shapes intentionally. Nested shapes should share comfortable margins and radii that relate to their enclosing surface. [Evidence at 00:03:42.268](https://www.youtube.com/watch?v=DS2ildqCrB0&t=222s)

- Keep content and the floating functional layer clearly separated. Anchor presentations to the controls that trigger them so their relationship is understandable. [Evidence at 00:07:00.397](https://www.youtube.com/watch?v=DS2ildqCrB0&t=420s)

- Express toolbar hierarchy through layout and grouping. Group related actions, move secondary actions into menus, and keep primary actions distinct. [Evidence at 00:09:33.847](https://www.youtube.com/watch?v=DS2ildqCrB0&t=573s)

- Use tab-bar accessories for persistent features such as playback. Keep screen-specific actions with the content they affect. [Evidence at 00:10:40.861](https://www.youtube.com/watch?v=DS2ildqCrB0&t=640s)

- Apply scroll-edge effects only where floating UI overlaps content. Choose an appropriate soft or hard boundary and avoid mixing or stacking them. [Evidence at 00:12:22.981](https://www.youtube.com/watch?v=DS2ildqCrB0&t=742s)

- Extend suitable imagery and backgrounds behind inset sidebars, while keeping text and controls above the extension effect. [Evidence at 00:13:04.721](https://www.youtube.com/watch?v=DS2ildqCrB0&t=784s)

- Preserve shared component anatomy, action meanings, and core interactions across platforms. Use familiar symbols, with text labels when an icon would be ambiguous. [Evidence at 00:16:35.760](https://www.youtube.com/watch?v=DS2ildqCrB0&t=995s)

Visual examples: [Concentric shapes](https://www.youtube.com/watch?v=DS2ildqCrB0&t=218s) — The construction lines show related corner centers and the spacing between nested shapes.; [Toolbar grouping](https://www.youtube.com/watch?v=DS2ildqCrB0&t=585s) — The share and Select actions sit together on one capsule-shaped toolbar surface.; [Extending sidebar backgrounds](https://www.youtube.com/watch?v=DS2ildqCrB0&t=780s) — The sidebar material carries color from the adjacent image while controls remain readable.

## 14. WWDC26: Design intuitive search experiences | Apple

Search placement communicates both how to access it and what it searches. The session combines platform-specific placement guidance with suggestions, filtering, and graceful empty states to reduce the effort of finding content.

[Original session](https://www.youtube.com/watch?v=lx45sKEnZkU) · Library transcript: `transcripts/14-lx45sKEnZkU.md`

- Choose search placement based on the app's navigation and search scope. On iPhone, consider reachable toolbar or tab placements for frequent searches. [Evidence at 00:03:55.665](https://www.youtube.com/watch?v=lx45sKEnZkU&t=235s)

- Use a search landing tab when discovery content is useful; use a prominent search tab when people usually want to start typing immediately. [Evidence at 00:06:13.967](https://www.youtube.com/watch?v=lx45sKEnZkU&t=373s)

- Place scoped search near the content it searches. On iPad and Mac, use toolbar, sidebar, or dedicated-section placement to clarify which results will change. [Evidence at 00:07:40.314](https://www.youtube.com/watch?v=lx45sKEnZkU&t=460s)

- Preserve familiar search-field elements and behavior even when applying custom branding. [Evidence at 00:02:36.048](https://www.youtube.com/watch?v=lx45sKEnZkU&t=156s)

- Offer useful recent searches and relevant predictive suggestions. Let people clear their history, visually separate typed text from predictions, and keep results prominent. [Evidence at 00:12:11.032](https://www.youtube.com/watch?v=lx45sKEnZkU&t=731s)

- Start broad and let people refine results with contextual filters or scope controls. Tokens can complement visible filters but are less discoverable. [Evidence at 00:14:31.905](https://www.youtube.com/watch?v=lx45sKEnZkU&t=871s)

- Provide a clear no-results state and show the current query so people can recognize typos or revise their search. [Evidence at 00:15:12.375](https://www.youtube.com/watch?v=lx45sKEnZkU&t=912s)

Visual examples: [Search landing experiences](https://www.youtube.com/watch?v=lx45sKEnZkU&t=391s) — Apple TV fills its search landing page with browsable genres before a query is entered.; [Search placement and scope](https://www.youtube.com/watch?v=lx45sKEnZkU&t=520s) — Mail places search in a multi-column interface where the surrounding content defines its scope.; [Filters and search tokens](https://www.youtube.com/watch?v=lx45sKEnZkU&t=840s) — A sender token narrows the message results while preserving the search field and keyboard.

## 29. WWDC26: Principles of great design | Apple

A framework for choosing and refining product experiences around people’s goals, context, trust, and emotional response.

[Original session](https://www.youtube.com/watch?v=Xa9L2yx_QH8) · Library transcript: `transcripts/29-Xa9L2yx_QH8.md`

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

[Original session](https://www.youtube.com/watch?v=Kd02qR_LyA0) · Library transcript: `transcripts/31-Kd02qR_LyA0.md`

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

[Original session](https://www.youtube.com/watch?v=dGcqqA3Sl-o) · Library transcript: `transcripts/33-dGcqqA3Sl-o.md`

- Evaluate whether each screen explains where the person is, what they can do, and where they can go next. [Evidence at 00:02:20.993](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=140s)

- Inventory features and workflows, understand real usage context, then remove nonessential features and group related ones before styling. [Evidence at 00:04:05.829](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=245s)

- Use tabs for navigation and put screen-specific actions in a toolbar; choose explicit labels and familiar symbols. [Evidence at 00:06:01.932](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=361s)

- Use progressive disclosure to reveal detail when relevant while keeping expanded views connected to their originating screen. [Evidence at 00:09:01.466](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=541s)

- Match layouts to content: lists support scanning structured information, while collections suit visual items with restrained text. [Evidence at 00:10:22.586](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=622s)

- Reduce choice overload by grouping content according to time, progress, or meaningful relationships. [Evidence at 00:12:07.193](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=727s)

- Build hierarchy with system text styles, support Dynamic Type, and protect text legibility over imagery. [Evidence at 00:15:20.037](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=920s)

- Use semantic system colors for adaptable interface roles and add a cohesive brand palette where it preserves legibility and appearance settings. [Evidence at 00:17:06.896](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=1026s)

Visual examples: [Tabs versus screen actions](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=373s) — The tab bar separates Records, Swaps, and Saves as top-level destinations.; [Progressive disclosure](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=564s) — The labeled disclosure control leads from a compact record group to its detailed contents.; [Type hierarchy and legibility](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=916s) — Caption, title, and subtitle labels establish a readable type hierarchy over artwork.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC26: Principles of great design | Apple — 00:02:08.475

Useful choices should let people enter and explore the experience at their own pace.

[Evidence at 00:02:08.475](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=128s). Caption anchor: “Offering choices is the best way to”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
