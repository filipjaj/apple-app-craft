# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

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

### WWDC26: Communicate your brand identity on iOS | Apple — 00:09:09.398

Build recognizable personality on a foundation of useful platform interaction patterns.

[Evidence at 00:09:09.398](https://www.youtube.com/watch?v=xifha3e7EJA&t=549s). Caption anchor: “People remember how a product makes them”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
