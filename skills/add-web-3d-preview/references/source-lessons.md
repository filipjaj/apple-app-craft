# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 10. WWDC26: Get started with the HTML Model Element | Apple

The HTML model element brings native interactive 3D content into web pages. The walkthrough covers preparing USDZ assets, loading and interaction behavior, fallbacks, augmented reality, and production asset optimization.

[Original session](https://www.youtube.com/watch?v=AwAn6dgcq4c) · Original library transcript: `transcripts/10-AwAn6dgcq4c.md`

- Treat 3D assets as part of a content pipeline: capture, convert, or create them, and package geometry, materials, textures, and animations in USDZ. [Evidence at 00:02:26.128](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=146s)

- Embed a model using familiar HTML source patterns. Provide fallback content, indicate loading progress, and handle readiness failures. [Evidence at 00:05:04.464](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=304s)

- Use progressive enhancement for unsupported browsers. Test native and polyfilled behavior separately, including features a polyfill cannot reproduce. [Evidence at 00:05:58.106](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=358s)

- Use orbit interaction for a simple rotatable product view. Choose custom entity transforms when exact views are needed, accounting for clipping and positioning. [Evidence at 00:07:15.706](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=435s)

- Animate manual transforms over time for smooth transitions, and cancel an existing animation before starting another. [Evidence at 00:08:51.944](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=531s)

- Use authored animation playback and AR Quick Look to extend product exploration. Spatial platforms can provide depth and interactions beyond the flat page. [Evidence at 00:11:13.861](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=673s)

- Optimize asset size before deployment. Use usdcrush for compression and usdrecord to generate thumbnails or fallback images across a catalog. [Evidence at 00:13:10.408](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=790s)

Visual examples: [Embedding a model](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=316s) — The model source and ready-promise code appear beside the rendered product, connecting loading logic to the visible result.; [Orbit and entity transforms](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=495s) — The entityTransform assignment rotates the boot model using the DOMMatrix shown in code.; [Animation and spatial presentation](https://www.youtube.com/watch?v=AwAn6dgcq4c&t=676s) — The AR Quick Look markup appears beside a bottle placed on a real table.
