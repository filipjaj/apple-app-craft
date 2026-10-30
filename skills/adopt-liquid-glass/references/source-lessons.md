# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

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

## 41. WWDC25: Build a SwiftUI app with the new design | Apple

Audit automatic changes first, then use targeted APIs to extend content, organize controls, and compose custom glass effects consistently.

[Original session](https://www.youtube.com/watch?v=3MugGCtm26A) · Original library transcript: `transcripts/41-3MugGCtm26A.md`

- Build with the Xcode 26 SDKs and audit the automatic updates to standard navigation, controls, and presentations before adding customization. [Evidence at 00:02:56.987](https://www.youtube.com/watch?v=3MugGCtm26A&t=176s)

- Use backgroundExtensionEffect to extend artwork behind a floating sidebar while keeping the source image’s content visible. [Evidence at 00:04:14.515](https://www.youtube.com/watch?v=3MugGCtm26A&t=254s)

- Configure tab-bar minimization and bottom accessories together, adapting accessory content to its placement when the bar collapses. [Evidence at 00:05:54.558](https://www.youtube.com/watch?v=3MugGCtm26A&t=354s)

- Remove custom backgrounds that conflict with the new sheet material and automatic toolbar scroll-edge effects. [Evidence at 00:10:51.740](https://www.youtube.com/watch?v=3MugGCtm26A&t=651s)

- Group related toolbar actions with ToolbarSpacer and reserve tint for meaningful emphasis instead of decorative coloring. [Evidence at 00:10:24.101](https://www.youtube.com/watch?v=3MugGCtm26A&t=624s)

- Apply search at the scope it serves, choosing a toolbar search experience or a dedicated search tab that adapts across platforms. [Evidence at 00:12:13.819](https://www.youtube.com/watch?v=3MugGCtm26A&t=733s)

- Adopt standard controls’ new capabilities, including slider ticks, neutral values, and container-concentric shapes. [Evidence at 00:16:27.957](https://www.youtube.com/watch?v=3MugGCtm26A&t=987s)

- Apply glassEffect to custom controls and group nearby glass in a GlassEffectContainer so sampling and blending remain consistent; use namespace-linked IDs for morphing transitions. [Evidence at 00:20:29.666](https://www.youtube.com/watch?v=3MugGCtm26A&t=1229s)

Visual examples: [Background extension](https://www.youtube.com/watch?v=3MugGCtm26A&t=250s) — The backgroundExtensionEffect modifier extends the image behind the sidebar.; [Meaningful toolbar groups](https://www.youtube.com/watch?v=3MugGCtm26A&t=620s) — The Mail interface demonstrates related toolbar actions and a distinct primary action.; [Composing custom glass](https://www.youtube.com/watch?v=3MugGCtm26A&t=1232s) — GlassEffectContainer combines the sampling region of neighboring glass controls.

## 2026-10-06 focused refinement

An accessory should adapt its content to its actual collapsed or expanded tab-bar placement. [Evidence at 00:05:54.558](https://www.youtube.com/watch?v=3MugGCtm26A&t=354s). This clarifies an existing mapped source rather than adding a duplicate session.

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: Meet Liquid Glass | Apple — 00:09:33.725

Preserve contrast where floating controls overlap content, using the appropriate edge treatment.

[Evidence at 00:09:33.725](https://www.youtube.com/watch?v=IrGYUq1mklk&t=573s). Caption anchor: “the effect intelligently switches to apply a”.

### WWDC25: Build an AppKit app with the new design | Apple — 00:02:48.000

Separate interactive toolbar controls from noninteractive titles and status content when applying glass.

[Evidence at 00:02:48.000](https://www.youtube.com/watch?v=VqTn9NgiE1s&t=168s). Caption anchor: “so any work that you’ve done to”.

### WWDC25: Get to know the new design system | Apple — 00:11:43.309

Avoid stacking different scroll edge effects on top of one another.

[Evidence at 00:11:43.309](https://www.youtube.com/watch?v=DS2ildqCrB0&t=703s). Caption anchor: “Scroll views automatically show an edge effect”.

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
