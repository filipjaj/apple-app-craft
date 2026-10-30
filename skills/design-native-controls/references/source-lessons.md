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

## 11. WWDC26: Communicate your brand identity on iOS | Apple

Brand identity in an iOS app comes from both its visual language and the way it feels to use. The session explains how to create a distinct personality while keeping navigation familiar and the interface accessible.

[Original session](https://www.youtube.com/watch?v=xifha3e7EJA) · Original library transcript: `transcripts/11-xifha3e7EJA.md`

- Use the content layer as the main canvas for brand identity. Keep navigation and common actions grounded in familiar platform patterns. [Evidence at 00:02:51.308](https://www.youtube.com/watch?v=xifha3e7EJA&t=171s)

- Spend custom-component effort where it makes the product meaningfully better. Use standard controls for conventional tasks to inherit expected behavior. [Evidence at 00:05:14.023](https://www.youtube.com/watch?v=xifha3e7EJA&t=314s)

- Shape brand perception through imagery, writing, and motion. Make each serve the product, and remember that stuttering or delayed interactions also affect how it feels. [Evidence at 00:08:11.603](https://www.youtube.com/watch?v=xifha3e7EJA&t=491s)

- Move brand color into content and use tint to communicate primary actions, selection, and status. Support a considered dark appearance. [Evidence at 00:09:42.067](https://www.youtube.com/watch?v=xifha3e7EJA&t=582s)

- Make custom typography scale with Dynamic Type and allow the layout to accommodate larger text without losing information. [Evidence at 00:12:50.733](https://www.youtube.com/watch?v=xifha3e7EJA&t=770s)

- Keep custom icons recognizable, consistent, and readable at small sizes. Respect platform-specific action meanings, or use SF Symbols for a flexible built-in set. [Evidence at 00:15:07.536](https://www.youtube.com/watch?v=xifha3e7EJA&t=907s)

- Use logos sparingly within the app. Express the brand in refined ways that leave room for useful information and avoid disrupting familiar behavior. [Evidence at 00:16:03.919](https://www.youtube.com/watch?v=xifha3e7EJA&t=963s)

Visual examples: [Color and action hierarchy](https://www.youtube.com/watch?v=xifha3e7EJA&t=594s) — The coffee app puts its brand imagery in the content and leaves navigation controls on a restrained floating surface.; [Typography at larger sizes](https://www.youtube.com/watch?v=xifha3e7EJA&t=773s) — The large product heading and wrapping description demonstrate branded typography that accommodates larger text.; [Custom icons and SF Symbols](https://www.youtube.com/watch?v=xifha3e7EJA&t=910s) — Compare the different Share symbols for iOS, Android, and the web; identical-looking actions do not use identical icons across platforms.

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

## 39. WWDC26: Refine accessibility for custom controls | Apple

Translate the information conveyed visually by a control into an equivalent assistive-technology experience, including alternatives to complex touch gestures.

[Original session](https://www.youtube.com/watch?v=KZ0__d74oNA) · Original library transcript: `transcripts/39-KZ0__d74oNA.md`

- Ensure every custom control communicates its purpose, current value, available actions, and feedback to assistive technologies. [Evidence at 00:15:52.286](https://www.youtube.com/watch?v=KZ0__d74oNA&t=952s)

- Make a custom slider an accessibility element with a label and value, then provide adjustable increment and decrement actions. [Evidence at 00:05:47.604](https://www.youtube.com/watch?v=KZ0__d74oNA&t=347s)

- Set an appropriate activation point for a passthrough gesture so precise touch adjustment begins at the current control position. [Evidence at 00:07:10.580](https://www.youtube.com/watch?v=KZ0__d74oNA&t=430s)

- Announce meaningful value changes during direct manipulation without overwhelming people with every intermediate update. [Evidence at 00:07:34.639](https://www.youtube.com/watch?v=KZ0__d74oNA&t=454s)

- Expose separate custom actions for a two-dimensional control instead of treating two axes as a single adjustable value. [Evidence at 00:10:24.739](https://www.youtube.com/watch?v=KZ0__d74oNA&t=624s)

- Use direct touch for gesture-rich regions where it fits the interaction; require activation to prevent accidental input and silence VoiceOver only when the control supplies its own audio feedback. [Evidence at 00:13:45.511](https://www.youtube.com/watch?v=KZ0__d74oNA&t=825s)

- Provide custom actions alongside direct touch whenever possible, allowing Switch Control, Voice Control, and people unable to perform those gestures to reach the same functionality. [Evidence at 00:14:35.433](https://www.youtube.com/watch?v=KZ0__d74oNA&t=875s)

Visual examples: [An accessible custom slider](https://www.youtube.com/watch?v=KZ0__d74oNA&t=350s) — The adjustable action maps accessibility increment and decrement gestures to changes in the custom slider.; [Actions for a two-axis control](https://www.youtube.com/watch?v=KZ0__d74oNA&t=627s) — Four named accessibility actions move the equalizer control along its two axes.; [Direct-touch activation](https://www.youtube.com/watch?v=KZ0__d74oNA&t=868s) — The direct-touch modifier requires activation before gestures reach the virtual-cat control.


## iPad design addition — 2026-10-06

### 00:09:40.277

Hover should identify the individual target within a control cluster.

[Evidence at 00:09:40.277](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=580s). Caption anchor: “more than one button”.

### 00:10:05.671

Do not depend on the former pointer magnetism; verify direct tracking.

[Evidence at 00:10:05.671](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=605s). Caption anchor: “no longer magnetize”.

### 00:10:13.308

Exercise actual pointer behavior, including custom hover treatments.

[Evidence at 00:10:13.308](https://www.youtube.com/watch?v=QYUFSEcwx4U&t=613s). Caption anchor: “test your app”.

These design refinements preserve existing behavior and compatibility. Verify actual resize/input transitions; a static screenshot does not prove them.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: Build a UIKit app with the new design | Apple — 00:15:11.000

Use supported presentation and search placement rather than assuming every action sheet has an identical origin.

[Evidence at 00:15:11.000](https://www.youtube.com/watch?v=uhMo6IEcR1w&t=911s). Caption anchor: “If you don’t specify a source, the”.

### WWDC26: What’s new in SwiftUI | Apple — 00:06:59.000

Keep genuinely important toolbar actions reachable with supported placement on the target SDK.

[Evidence at 00:06:59.000](https://www.youtube.com/watch?v=s8BB8q2MyXc&t=419s). Caption anchor: “Lastly, for my Share button, I want”.

### WWDC21: SwiftUI on the Mac: Build the fundamentals | Apple — 00:09:59.000

Present typed domain values in native table cells with meaningful localized formatting.

[Evidence at 00:09:59.000](https://www.youtube.com/watch?v=ChY_lxk0Pf8&t=599s). Caption anchor: “and it will be handed a plant.”.

### WWDC23: The SwiftUI cookbook for focus | Apple — 00:11:16.000

Use focus movement to support the intended editing task rather than treating keyboard appearance as incidental.

[Evidence at 00:11:16.000](https://www.youtube.com/watch?v=C8Ut2NmDxpo&t=676s). Caption anchor: “to help me remember what to get”.

### WWDC23: What’s new in SwiftUI | Apple — 00:16:21.000

A confirmation-suppression preference has semantic meaning and should only apply where the task allows it.

[Evidence at 00:16:21.000](https://www.youtube.com/watch?v=8zmTLzEQ7vk&t=981s). Caption anchor: “to important confirmation dialogs, and including a”.

### WWDC22: SwiftUI on iPad: Add toolbars, titles, and more | Apple — 00:04:29.000

Toolbar role affects placement and overflow, so choose it for the actual task.

[Evidence at 00:04:29.000](https://www.youtube.com/watch?v=j81SI1mdRJA&t=269s). Caption anchor: “Instead, they live in the overflow menu.”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
