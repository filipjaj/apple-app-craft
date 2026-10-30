---
name: add-web-3d-preview
description: "Add or review a progressively enhanced 3D model preview in a web app using supported native model capabilities and usable fallback content."
---

# Add a Web 3D Preview

## Goal

Keep product exploration useful when 3D is loading, unavailable, or unsupported.

## Working context

Inspect the relevant project conventions, supported platforms, deployment target, SDK, and Swift language/isolation settings before choosing APIs. Read [source lessons](references/source-lessons.md) for the reasoning relevant to this goal; these are session-era evidence, not a guarantee of current API availability. For framework, SDK, API, or CLI details, resolve the library with Context7 and query the specific concept when that tool is available. If it is unavailable or insufficient, use current official documentation and disclose uncertainty; never invent API spelling. Preserve the user’s product direction and existing compatibility requirements.

## Workflow

1. Confirm the user’s exploration task, target browsers, asset formats, and existing frontend. Verify current support rather than inferring it from a session title.
2. Prepare the asset pipeline and inspect geometry, textures, orientation, size, and authored animations. Define a useful poster or ordinary product content as fallback.
3. Implement feature detection, loading, readiness, and failure behavior. Keep essential product information and actions available independently of the interactive model.
4. Choose native orbit for simple rotation or explicit transforms for exact viewpoints. Preserve clipping and position, and cancel an existing transform animation before replacing it.
5. Use AR or spatial presentation only where supported and useful. Optimize asset transfer size and generate fallback imagery with available supported tools; test native and polyfilled implementations separately.

## Verify the outcome

- Test support present, support absent, slow asset loading, and failed loading.
- Check repeated viewpoint changes, reset, keyboard access, and fallback action usability.
- Record tested browser/device versions and asset size; avoid asserting native/polyfill parity.

Do not make purchasing or essential information depend on browser-specific 3D support.

## Deliverable

For implementation, leave the scoped change and report the resulting behavior, verification evidence, and any remaining limitation. For review or planning, provide the concrete findings or decisions needed for the next step without editing beyond the request.
