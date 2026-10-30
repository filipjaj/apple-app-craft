# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

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

## 38. WWDC22: Compose custom layouts with SwiftUI | Apple

Participate directly in SwiftUI’s layout engine to measure and place children while supporting natural spacing, larger text, and animated layout changes.

[Original session](https://www.youtube.com/watch?v=ao0s5rMCIgc) · Original library transcript: `transcripts/38-ao0s5rMCIgc.md`

- Use Grid when measuring every cell allows coordinated sizing in both dimensions; use lazy grids when deferred creation of scrollable content is the priority. [Evidence at 00:04:14.454](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=254s)

- Control column alignment and spanning deliberately, including gridColumnAlignment and gridCellColumns for cells that need different behavior. [Evidence at 00:07:23.744](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=443s)

- Implement sizeThatFits to report a custom container’s size and placeSubviews to position children through the supplied subview proxies. [Evidence at 00:11:02.496](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=662s)

- Measure ideal sizes with an unspecified proposal, and respect subviews’ spacing preferences for platform-appropriate layout. [Evidence at 00:14:01.909](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=841s)

- Place children relative to the supplied bounds rather than assuming a zero origin; introduce layout caching only when profiling justifies it. [Evidence at 00:12:42.629](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=762s)

- Use the Layout protocol for child-driven sizing instead of feeding GeometryReader measurements back upward in a potentially unstable layout loop. [Evidence at 00:19:41.582](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1181s)

- Offer horizontal and vertical alternatives through ViewThatFits when larger text makes the preferred layout too wide. [Evidence at 00:21:16.109](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1276s)

- Pass per-child metadata with LayoutValueKey, and use AnyLayout to change arrangement while preserving child identity and enabling smooth transitions. [Evidence at 00:25:09.510](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1509s)

Visual examples: [Custom layout methods](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=674s) — The sizeThatFits signature and container diagram show where a custom layout receives its size proposal.; [Adapting to larger text](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1279s) — The large-text preview switches the buttons to a vertical alternative through ViewThatFits.; [Switching layouts with preserved identity](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=1521s) — AnyLayout switches between horizontal and radial layouts while retaining the same child views.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### Strike a pose with adaptive layouts on iPhone Duo | Apple — 00:07:16.000

Use supported reserved-region state and safe layout information, checking actual API availability.

[Evidence at 00:07:16.000](https://www.youtube.com/watch?v=d1xi9GAfSRI&t=436s). Caption anchor: “By default, only active ones will be”.

### A guide to layout in SwiftUI | Meet with Apple — 00:06:15.120

Understand how each child responds to the proposed size instead of assuming all views shrink identically.

[Evidence at 00:06:15.120](https://www.youtube.com/watch?v=d3JQBEw8jhM&t=375s). Caption anchor: “A color view always claims whatever it's”.

### WWDC22: Compose custom layouts with SwiftUI | Apple — 00:08:06.420

Use content measurements to support equal-width controls when the design requires them.

[Evidence at 00:08:06.420](https://www.youtube.com/watch?v=ao0s5rMCIgc&t=486s). Caption anchor: “Instead, the buttons should all have widths”.

### WWDC26: What’s new in Xcode 27 | Apple — 00:11:02.000

Test the app across supported resized presentations instead of assuming fixed phone dimensions.

[Evidence at 00:11:02.000](https://www.youtube.com/watch?v=9zjeImiYtow&t=662s). Caption anchor: “it's also important to consider how it”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
