# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC24: Run, Break, Inspect: Explore effective debugging in LLDB | Apple — 00:16:10.000

Use breakpoint conditions to focus on the relevant subset of repeated events.

[Evidence at 00:16:10.000](https://www.youtube.com/watch?v=PsW3RQN9R_Q&t=970s). Caption anchor: “but we are only interested in a”.

### WWDC23: Fix failures faster with Xcode test reports | Apple — 00:04:42.000

Use the unified test activity, screenshot and failure context to choose a causal starting point.

[Evidence at 00:04:42.000](https://www.youtube.com/watch?v=xtF4Q-GkgJo&t=282s). Caption anchor: “It highlights important patterns, so you quickly”.

### WWDC23: Debug with structured logging | Apple — 00:12:10.000

Separate structured logging by meaningful component so relevant evidence can be located precisely.

[Evidence at 00:12:10.000](https://www.youtube.com/watch?v=VDMjaCrqmJE&t=730s). Caption anchor: “First, you should always create separate log”.

### WWDC22: Debug Swift debugging with LLDB | Apple — 00:18:43.000

Ship or retain the debug artifacts appropriate to the intended stepping and inspection workflow.

[Evidence at 00:18:43.000](https://www.youtube.com/watch?v=xuw10oITaUY&t=1123s). Caption anchor: “you should ask yourself what level of”.

### WWDC24: Xcode essentials | Apple — 00:29:11.000

Code coverage identifies exercised code, but a count alone does not prove useful behavior was asserted.

[Evidence at 00:29:11.000](https://www.youtube.com/watch?v=EN7-6Oj7cL0&t=1751s). Caption anchor: “A 0 means that code was never”.

### Current documentation checked

- [Official making dependencies available to xcode cloud documentation](https://developer.apple.com/documentation/xcode/making-dependencies-available-to-xcode-cloud).
- [Official Setting up your project to use Xcode Cloud documentation](https://developer.apple.com/documentation/xcode/Setting-up-your-project-to-use-Xcode-Cloud).
- [Official xcode cloud workflow reference documentation](https://developer.apple.com/documentation/xcode/xcode-cloud-workflow-reference).
- [Official environment variable reference documentation](https://developer.apple.com/documentation/xcode/environment-variable-reference).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
