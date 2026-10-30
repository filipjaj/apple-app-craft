# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

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

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: Principles of inclusive app design | Apple — 00:10:24.687

Offer useful reading modes for people who do not read visually.

[Evidence at 00:10:24.687](https://www.youtube.com/watch?v=pD43DI-VA20&t=624s). Caption anchor: “so you can always read in the”.

### WWDC26: Refine accessibility for custom controls | Apple — 00:09:44.423

Custom multidirectional controls may need named accessibility actions instead of a single adjustable direction.

[Evidence at 00:09:44.423](https://www.youtube.com/watch?v=KZ0__d74oNA&t=584s). Caption anchor: “Adding the adjustable trait would only cover”.

### Prepare your app for Accessibility Nutrition Labels | Apple Developer — 00:25:49.311

Use a different layout at large text sizes when the original arrangement makes content hard to read.

[Evidence at 00:25:49.311](https://www.youtube.com/watch?v=-4FD6zhHKKM&t=1549s). Caption anchor: “to ensure content can fit more comfortably”.

### WWDC23: Build accessible apps with SwiftUI and UIKit | Apple — 00:05:33.000

Announcement priority should reflect the importance of the feedback rather than interrupting every update equally.

[Evidence at 00:05:33.000](https://www.youtube.com/watch?v=F6jzQOvBbUE&t=333s). Caption anchor: “is the least important, so we give”.

### WWDC25: Evaluate your app for Accessibility Nutrition Labels | Apple — 00:13:58.000

Validate Voice Control completion without substituting touch or pointer input for inaccessible steps.

[Evidence at 00:13:58.000](https://www.youtube.com/watch?v=wfTU7O7bJSU&t=838s). Caption anchor: “It’s important that I only use voice”.

### WWDC25: Make your Mac app more accessible to everyone | Apple — 00:10:13.000

Hover and trackpad-only interactions need equivalent discoverable ways to perform the task.

[Evidence at 00:10:13.000](https://www.youtube.com/watch?v=FyP9zLKD3PA&t=613s). Caption anchor: “they would never be able to access”.

### WWDC24: Catch up on accessibility in SwiftUI | Apple — 00:18:31.410

Try actual drag-and-drop with assistive technology and offer custom actions where they improve task access.

[Evidence at 00:18:31.410](https://www.youtube.com/watch?v=PHAA6nXTbdk&t=1111s). Caption anchor: “When building drag and drop experiences its”.

### WWDC23: Perform accessibility audits for your app | Apple — 00:10:42.000

Do not broadly ignore accessibility audit issues; investigate before filtering a specific justified exception.

[Evidence at 00:10:42.000](https://www.youtube.com/watch?v=IAqzXI3kFCk&t=642s). Caption anchor: “By default, issues should not be ignored.”.

### WWDC22: What's new in web accessibility | Apple — 00:05:46.000

A custom web control must keep its visual state and accessible value in agreement.

[Evidence at 00:05:46.000](https://www.youtube.com/watch?v=y9BZRA1wpLA&t=346s). Caption anchor: “First, we'll clamp the value we're given”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
