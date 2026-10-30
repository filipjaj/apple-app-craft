# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 3. WWDC25: Say hello to the new look of app icons | Apple

The new app-icon language uses layered glass materials and dynamic lighting to create depth. Designing for the shared grids and appearance modes helps an icon retain its identity across devices and personalization settings.

[Original session](https://www.youtube.com/watch?v=l-9tYm0U998) · Original library transcript: `transcripts/03-l-9tYm0U998.md`

- Build icons from a background and intentional foreground layers. Let their stacking communicate depth and structure. [Evidence at 00:06:09.099](https://www.youtube.com/watch?v=l-9tYm0U998&t=369s)

- Simplify source artwork so system materials can supply highlights, shadows, and depth. Remove baked-in effects that compete with the dynamic glass treatment. [Evidence at 00:08:46.456](https://www.youtube.com/watch?v=l-9tYm0U998&t=526s)

- Prefer clear shapes and purposeful perspectives. Highly realistic 3D illustrations can compete with the material's own dimensionality. [Evidence at 00:06:46.970](https://www.youtube.com/watch?v=l-9tYm0U998&t=406s)

- Use translucency and blur selectively to reveal layering. Reduce excessive overlaps so intersections and reflective edges remain readable. [Evidence at 00:08:15.225](https://www.youtube.com/watch?v=l-9tYm0U998&t=495s)

- Use rounded details and sufficiently bold strokes so lighting travels smoothly along edges and small-scale details survive. [Evidence at 00:09:42.045](https://www.youtube.com/watch?v=l-9tYm0U998&t=582s)

- Use the updated grids to preserve optical balance across rounded-rectangle and circular icons. Redraw unusual Mac icon silhouettes to make full use of the masked canvas. [Evidence at 00:04:16.586](https://www.youtube.com/watch?v=l-9tYm0U998&t=256s)

- Evaluate light, dark, clear, and tinted appearances. Use suitable background gradients and preserve recognizable colors and shapes as the appearance changes. [Evidence at 00:10:24.087](https://www.youtube.com/watch?v=l-9tYm0U998&t=624s)

Visual examples: [Icon layer structure](https://www.youtube.com/watch?v=l-9tYm0U998&t=394s) — The Podcast icon separates into background and foreground layers with depth.; [Simplifying source artwork](https://www.youtube.com/watch?v=l-9tYm0U998&t=538s) — The nested house shapes show how simple artwork gains highlights and depth from the icon material.; [Appearance variants](https://www.youtube.com/watch?v=l-9tYm0U998&t=627s) — The light and dark background tiles illustrate the different appearance treatments.

## 4. WWDC25: Create icons with Icon Composer | Apple

Icon Composer adds a material and appearance-tuning stage between your design tool and Xcode. A single layered icon document can serve multiple platforms and appearance modes.

[Original session](https://www.youtube.com/watch?v=4usD1hP1nYY) · Original library transcript: `transcripts/04-4usD1hP1nYY.md`

- Start with Apple's icon templates, then separate artwork by depth and color. This gives you control over materials and appearance variants later. [Evidence at 00:05:09.673](https://www.youtube.com/watch?v=4usD1hP1nYY&t=309s)

- Export scalable vector layers as SVG; outline text before export. Use transparent PNGs for raster artwork or elements that cannot be expressed as SVG. [Evidence at 00:06:42.933](https://www.youtube.com/watch?v=4usD1hP1nYY&t=402s)

- Keep source artwork flat and avoid baking in glass effects. Leave rounded-rectangle and circular masks out of exports because the system applies them. [Evidence at 00:07:06.523](https://www.youtube.com/watch?v=4usD1hP1nYY&t=426s)

- Use groups to control how elements stack and receive glass properties. Tune the material at group level and selectively disable glass on individual layers when needed. [Evidence at 00:08:26.069](https://www.youtube.com/watch?v=4usD1hP1nYY&t=506s)

- Create appearance-specific variants for fills, opacity, blend modes, and shadows. Check dark and monochrome legibility rather than relying solely on automatic conversion. [Evidence at 00:11:51.941](https://www.youtube.com/watch?v=4usD1hP1nYY&t=711s)

- Preview against different backgrounds, at small sizes, and with moving light. Make optical adjustments when translating artwork to the circular Watch canvas. [Evidence at 00:12:26.442](https://www.youtube.com/watch?v=4usD1hP1nYY&t=746s)

- Deliver the saved .icon file to Xcode and select it in the project editor. Verify the result on the app's target platforms and appearances. [Evidence at 00:13:18.528](https://www.youtube.com/watch?v=4usD1hP1nYY&t=798s)

Visual examples: [Preparing layered artwork](https://www.youtube.com/watch?v=4usD1hP1nYY&t=321s) — The Translate artwork separates speech-bubble elements and background into distinct layers.; [Groups and glass properties](https://www.youtube.com/watch?v=4usD1hP1nYY&t=518s) — The exploded stack beside the layer list makes the icon group’s depth order explicit.; [Previewing the finished icon](https://www.youtube.com/watch?v=4usD1hP1nYY&t=749s) — The circular Watch icon is paired with composition controls for optical positioning.
