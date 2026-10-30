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

## 9. WWDC26: Create UI prototypes using agents in Xcode | Apple

Coding agents and Xcode previews can shorten the feedback loop for UI prototyping. The session demonstrates exploring divergent designs, testing realistic content, and tuning interaction details while keeping creative judgment with the designer.

[Original session](https://www.youtube.com/watch?v=QleOvMW9vTU) · Original library transcript: `transcripts/09-QleOvMW9vTU.md`

- Specify features and stylistic intent before asking for a generated UI. Vague prompts can anchor the project to arbitrary layouts and unwanted features. [Evidence at 00:04:01.860](https://www.youtube.com/watch?v=QleOvMW9vTU&t=241s)

- Ask for multiple distinctly named previews. Compare alternatives, identify promising elements, and remix them through further iterations. [Evidence at 00:06:39.940](https://www.youtube.com/watch?v=QleOvMW9vTU&t=399s)

- Populate prototypes with believable content so the design can be evaluated in realistic use, including long text and large collections. [Evidence at 00:08:58.040](https://www.youtube.com/watch?v=QleOvMW9vTU&t=538s)

- Explicitly explore empty states and other edge cases. Keep sample models reusable and editable so later prototypes can share them. [Evidence at 00:08:27.180](https://www.youtube.com/watch?v=QleOvMW9vTU&t=507s)

- Get feedback from people using the prototype. Generated sample content is useful preparation, but real use reveals how the experience works for its audience. [Evidence at 00:11:07.820](https://www.youtube.com/watch?v=QleOvMW9vTU&t=667s)

- Build a tuning panel when repeatedly editing animation constants becomes cumbersome. Expose the parameters that affect the feel of the interaction. [Evidence at 00:14:04.700](https://www.youtube.com/watch?v=QleOvMW9vTU&t=844s)

- Break complex animations into named phases and tune delays or springs in isolation. A side-by-side panel keeps the controls and the result visible together. [Evidence at 00:14:34.120](https://www.youtube.com/watch?v=QleOvMW9vTU&t=874s)

- Keep ownership of product and design decisions. Use agents to explore and implement possibilities while you assess which experience serves people best. [Evidence at 00:02:33.740](https://www.youtube.com/watch?v=QleOvMW9vTU&t=153s)

Visual examples: [Comparing preview alternatives](https://www.youtube.com/watch?v=QleOvMW9vTU&t=411s) — The collage shows substantially different card and progress-layout directions for the same prototype.; [Prototyping edge cases](https://www.youtube.com/watch?v=QleOvMW9vTU&t=595s) — The Xcode preview presents one generated edge-case variant alongside its reusable model code.; [Tuning animation phases](https://www.youtube.com/watch?v=QleOvMW9vTU&t=834s) — The tuning panel exposes animation controls on the running phone prototype.

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

### WWDC25: Design foundations from idea to interface | Apple — 00:03:13.112

Expose where someone is and what they can do before making them browse a long screen.

[Evidence at 00:03:13.112](https://www.youtube.com/watch?v=dGcqqA3Sl-o&t=193s). Caption anchor: “— even though it seems useful. As”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
