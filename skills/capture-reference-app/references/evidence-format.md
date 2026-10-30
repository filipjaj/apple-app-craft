# Reference evidence format

Use the project's existing documentation layout; `docs/screens/INDEX.md` is a fallback. Keep capture files with the index only when their content is appropriate for that location. Do not commit private reference screenshots by default.

For each relevant surface record:

- ID and captured file/tool artifact, app version if known, capture date, dimensions, known scale, appearance, and active/inactive state.
- Entry route, preconditions, visible selection, and exit/cancellation.
- Layout relationships, controls, labels, observed commands/shortcuts.
- Behavior actually exercised and result; observations separate from inferred data models.
- Target implementation decision: retain, adapt, defer, with its acceptance criterion or story ID.

End with navigation and command maps and a coverage list of inaccessible/unobserved states. For visual work compare equivalent window sizes, content, scale, appearance, and focus. Measure stable edges/row pitch rather than antialiased text pixels; fonts and colors inferred from compressed images remain estimates until validated. Set fidelity goals from the user's request, preserving native focus, accessibility, and branded-asset ownership.
