# Source lessons

These are condensed source-era lessons from the supplied Apple library. Check current documentation before implementation. The workflow is editorial synthesis rather than verbatim Apple requirements.

## 1. WWDC25: Meet Liquid Glass | Apple

Liquid Glass combines optical effects, responsive motion, and adaptive contrast into a shared interface material. The session explains where to use it and how to preserve hierarchy, readability, and accessibility.

[Original session](https://www.youtube.com/watch?v=IrGYUq1mklk) · Original library transcript: `transcripts/01-IrGYUq1mklk.md`

- Reserve Liquid Glass for navigation and controls floating above content. Applying it throughout the content layer weakens the hierarchy. [Evidence at 00:13:07.800](https://www.youtube.com/watch?v=IrGYUq1mklk&t=787s)

- Design motion and appearance together: lensing, illumination, flexing, and morphing communicate interaction and relationships between controls. [Evidence at 00:03:16.759](https://www.youtube.com/watch?v=IrGYUq1mklk&t=196s)

- Use the Regular variant for general-purpose controls. Use Clear only over rich media when dimming is acceptable and the foreground content is bold and bright. [Evidence at 00:13:51.943](https://www.youtube.com/watch?v=IrGYUq1mklk&t=831s)

- Avoid stacking glass on glass. Use fills, transparency, and vibrancy for elements placed within a glass surface. [Evidence at 00:13:24.249](https://www.youtube.com/watch?v=IrGYUq1mklk&t=804s)

- Use the material's built-in tinting to emphasize primary actions. Tinting every control removes the distinction between important and secondary actions. [Evidence at 00:17:29.305](https://www.youtube.com/watch?v=IrGYUq1mklk&t=1049s)

- Use adaptive contrast and scroll-edge effects to separate floating controls from moving content; choose the hard edge style when pinned accessory views need stronger separation. [Evidence at 00:09:41.819](https://www.youtube.com/watch?v=IrGYUq1mklk&t=581s)

- Account for Reduce Transparency, Increase Contrast, and Reduce Motion. Standard Liquid Glass responds to these system accessibility settings automatically. [Evidence at 00:18:22.818](https://www.youtube.com/watch?v=IrGYUq1mklk&t=1102s)

Visual examples: [Optics and interaction](https://www.youtube.com/watch?v=IrGYUq1mklk&t=227s) — The glass surface brightens and changes shape in response to touch.; [Regular and Clear materials](https://www.youtube.com/watch?v=IrGYUq1mklk&t=843s) — Compare glass controls over neutral content and colorful media; notice how the background affects legibility.; [Scroll-edge separation](https://www.youtube.com/watch?v=IrGYUq1mklk&t=577s) — Notice the floating controls over the photo and the boundary between image content and the message below.

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

## 2026-10-06 focused refinement

User agency includes recovery from mistakes; inspect it when the task involves consequential actions. [Evidence at 00:02:41.193](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=161s). This clarifies an existing mapped source rather than adding a duplicate session.
