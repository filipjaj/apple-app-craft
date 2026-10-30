# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

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
