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

## 32. WWDC24: Add personality to your app through UX writing | Apple

Practical writing exercises turn an app’s purpose and audience into voice attributes, then balance those attributes for different situations.

[Original session](https://www.youtube.com/watch?v=jWKBMTDdA8s) · Original library transcript: `transcripts/32-jWKBMTDdA8s.md`

- Define voice as the relatively stable expression of brand and values, and tone as how that voice adapts to a situation. [Evidence at 00:01:30.859](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=90s)

- Write down the app’s purpose and audience before brainstorming personality traits, then group those traits into a few defining attributes. [Evidence at 00:05:47.067](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=347s)

- Refine generic welcome copy into a specific statement of what the app helps its audience accomplish. [Evidence at 00:12:12.263](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=732s)

- Adjust tone by balancing qualities such as clarity, helpfulness, simplicity, and friendliness rather than abandoning the app’s voice. [Evidence at 00:04:59.822](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=299s)

- Prioritize direct facts for consequential information and clear recovery instructions when someone cannot complete a task. [Evidence at 00:17:44.082](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=1064s)

- Use warmth and energy where they support the moment, such as a welcome or achievement, while keeping useful information central. [Evidence at 00:19:55.431](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=1195s)

- Read copy aloud, avoid jargon, and write inclusively so personality does not make the interface harder to understand. [Evidence at 00:20:04.965](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=1204s)

Visual examples: [Grouping voice attributes](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=450s) — Sticky-note traits are grouped into Smart and Motivating themes that define the app voice.; [Refining welcome copy](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=735s) — The revised welcome sentence states the specific outcome the investment app supports.; [Tone for recovery instructions](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=1067s) — The alert states the connectivity problem and offers a Settings action for recovery.

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

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC24: Add personality to your app through UX writing | Apple — 00:05:07.209

Keep a consistent voice while adapting tone to the moment and task.

[Evidence at 00:05:07.209](https://www.youtube.com/watch?v=jWKBMTDdA8s&t=307s). Caption anchor: “Voice represents the consistent elements that are”.

### WWDC22: Writing for interfaces | Apple — 00:06:46.000

Useful clarity and privacy information can warrant more text than a decorative short message.

[Evidence at 00:06:46.000](https://www.youtube.com/watch?v=Nt5hlSLzhpo&t=406s). Caption anchor: “and give you some important information about”.

### WWDC25: Make a big impact with small writing changes | Apple — 00:04:14.000

Remove conversational interjections and politeness when they contribute no useful meaning.

[Evidence at 00:04:14.000](https://www.youtube.com/watch?v=iaafpzDJHS8&t=254s). Caption anchor: “Interjections are abrupt words or phrases like”.

### WWDC26: Craft clear names for features and labels in your app | Apple — 00:07:04.000

Evaluate feature names against the understanding and confidence the task should create.

[Evidence at 00:07:04.000](https://www.youtube.com/watch?v=UFZvFqg6few&t=424s). Caption anchor: “What should people feel? Like when you”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
