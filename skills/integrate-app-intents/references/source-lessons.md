# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 15. WWDC26: Code-along: Make your app available to Siri | Apple

The walkthrough connects an app's content and actions to Siri through App Intents and App Schemas. It progresses from searchable entities to onscreen context, navigation, editing actions, and custom result views.

[Original session](https://www.youtube.com/watch?v=lF8ZFACmyFY) · Original library transcript: `transcripts/15-lF8ZFACmyFY.md`

- Map app content and actions to schemas the system understands. Schematized entities and intents let Siri interpret requests without app-specific natural-language handling. [Evidence at 00:03:24.036](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=204s)

- Keep entity definitions connected to the existing data layer through queries and shared dependencies, rather than introducing independent copies of app state. [Evidence at 00:05:42.683](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=342s)

- Donate indexed entities and update the search index whenever content is created, changed, or deleted. Declaring IndexedEntity alone does not populate the index. [Evidence at 00:06:43.751](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=403s)

- Use transient entities for contextual objects that do not need independent identity or lookup, such as an attendee's participation in a particular event. [Evidence at 00:08:29.624](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=509s)

- Add an open intent so Siri and Spotlight results navigate directly to the relevant item. Connect visible entities to onscreen context so people can refer to what they are viewing. [Evidence at 00:15:42.352](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=942s)

- Implement actions by resolving parameters, calling the app's data layer, and returning entities. The schema lets Siri handle interpretation, clarification, and confirmation. [Evidence at 00:17:57.622](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=1077s)

- Distinguish an omitted update parameter from an explicitly cleared value. Use parameter value state when nil has more than one possible meaning. [Evidence at 00:20:22.100](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=1222s)

- Use lightweight SwiftUI snippets to present custom results, and verify the conversational flows for creating, editing, opening, and deleting content. [Evidence at 00:21:34.188](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=1294s)

Visual examples: [Indexed entities](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=406s) — CalendarEntity declares IndexedEntity conformance alongside its display representation and query.; [Opening contextual content](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=954s) — The visible event list is linked to system context with appEntityIdentifierForSelectionType.; [SwiftUI result snippets](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=1306s) — The EventSnippetView implementation shows the gradient accent, event title, time, and optional location.

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

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC24: Design App Intents for system experiences | Apple — 00:01:57.000

Represent meaningful app capabilities as domain actions; broad session guidance does not require unrelated integration work.

[Evidence at 00:01:57.000](https://www.youtube.com/watch?v=yyr4trqPgjo&t=117s). Caption anchor: “that could be useful outside of your”.

### WWDC22: Meet Focus filters | Apple — 00:02:28.000

Focus filters should narrow relevant content according to the person's configured context.

[Evidence at 00:02:28.000](https://www.youtube.com/watch?v=GQNhG7XQ3N0&t=148s). Caption anchor: “to show only relevant mailboxes during a”.

### WWDC26: Build intelligent Siri experiences with App Schemas | Apple — 00:19:55.000

Distinguish importing incoming content to create a new entity from resolving an existing entity.

[Evidence at 00:19:55.000](https://www.youtube.com/watch?v=mqoX8zhM8zQ&t=1195s). Caption anchor: “Use IntentValueRepresentation importing when incoming content should”.

### WWDC25: Develop for Shortcuts and Spotlight with App Intents | Apple — 00:12:38.000

Required parameters without defaults need a useful summary for the relevant system action surface.

[Evidence at 00:12:38.000](https://www.youtube.com/watch?v=XRDEnbdnIOY&t=758s). Caption anchor: “must contain all required parameters that don’t”.

### WWDC26: What’s new in Shortcuts | Apple — 00:09:31.000

Entities that move through cross-device shortcuts need stable identity across every supported device.

[Evidence at 00:09:31.000](https://www.youtube.com/watch?v=mUoWMlZXQ28&t=571s). Caption anchor: “I can run the shortcut there and”.

### WWDC26: Code-along: Make your app available to Siri | Apple — 00:21:45.784

Keep result snippets simple and lightweight while integrating the domain action.

[Evidence at 00:21:45.784](https://www.youtube.com/watch?v=lF8ZFACmyFY&t=1305s). Caption anchor: “but also remember to keep it simple”.

### WWDC25: Get to know App Intents | Apple — 00:22:58.000

Multi-target intent adoption requires the appropriate runtime indexing and validation information for each target.

[Evidence at 00:22:58.000](https://www.youtube.com/watch?v=GnBykJCoCEM&t=1378s). Caption anchor: “you must provide the runtime with additional”.

### WWDC26: Discover new capabilities in the App Intents framework | Apple — 00:16:38.000

Route an intent to the process that has the authority and storage access required for its mutation.

[Evidence at 00:16:38.000](https://www.youtube.com/watch?v=6FkaEVs5G-c&t=998s). Caption anchor: “So I gave the widget read-only access”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
