# Bounded Apple app delivery

Use this for an authorized multi-step build or milestone. Keep a targeted fix direct. This workflow adds no product features, standing autonomy, recurring automation, or mandatory tool installation.

## Enter at the current stage

| Available evidence | Next useful work |
|---|---|
| Idea or incomplete brief | `plan-native-app`: main journey, scope, risks and observable success |
| Reference app or screenshots | `capture-reference-app`: only the chosen journey, observed facts versus assumptions |
| Brief and acceptance criteria | Select the first dependency-ready end-to-end slice |
| Existing code with a known defect | Relevant implementation skill and focused proof |
| Candidate build | `verify-macos-app` on Mac, or relevant platform verification |

Read only the selected skill and relevant references. Use Context7 for current framework/API/CLI questions, with official docs as fallback. Retain the project's platform targets, architecture, test system, and design choices. For a new app select a project form from its actual targets, capabilities, extensions, signing and distribution needs; do not run a template installer by default. Existing web scaffolding is not a native Mac scaffold.

## One slice at a time

1. Inspect repository instructions and current state. Follow the user's worktree/branch rules before edits. Preserve unrelated work.
2. Agree on the scope from existing authorization and artifacts. Choose a dependency-ready story in the requested milestone. If the milestone is unspecified, deliver the smallest coherent outcome implied by the request; do not silently take on the entire backlog.
3. Define entry, action, visible success, cancellation/recovery, state changes, and required evidence. Link a reference when one exists. Resolve unclear decisions that change scope; infer routine details from the project.
4. Implement through the existing ownership boundaries. Use only the necessary design/state/navigation/data/system skills. Keep the app runnable. Add schema, infrastructure, or an automation surface only when acceptance requires it.
5. Run focused checks. For Swift tests use SwiftProbe after reading its skill/schema. Verify changed UI with real rendered output and changed behavior through its relevant entry point. Broaden to dependent journeys when the change can affect them. Keep unmet criteria visible.
6. Fix and recheck the affected area. After three unsuccessful repair rounds for the same problem, record the evidence and blocker, then do independent useful work. Do not mark the slice done or loop indefinitely.
7. Record completed acceptance evidence together with the change. If committing is in scope, stage only intended paths and keep a slice and its status/evidence consistent in the commit. Avoid automatic `git add -A`, installation, app restarts, or client registration as bookkeeping.
8. Continue until the authorized outcome/milestone is complete. At that boundary, check the primary journey and shared surfaces proportionately, report completed and blocked criteria, and stop. A milestone ending is not authorization for an architecture rewrite or a new milestone.

## Minimal artifacts

Reuse project equivalents. Create only artifacts that make the handoff or continued work useful.

**Brief:** intended person and outcome, main journey, supported targets, entry surfaces, data/system constraints, identity direction, non-goals, and unresolved assumptions.

**Story example:**

```markdown
### S-004 Complete a task from the active list
Depends: S-001
Status: todo
Entry: selected row; toolbar action or keyboard command
Acceptance:
- [integration] Completing the selected task saves its new state across relaunch.
- [interaction] The command acts on the focused window and Undo restores the task.
- [rendered] Completed styling remains legible in supported appearances.
Evidence: pending until checks run
```

Use `todo`, `doing`, `done`, `blocked`, or `deferred` consistently, or the project's equivalents. Assign dependencies only where real. Manual/unavailable checks stay visible and do not become a pass. A blocked required criterion prevents an unqualified done claim.

**Verification:** criterion, method, verdict, source/configuration, artifact path, limitation. Separate compilation, unit/integration tests, rendered output, real interaction, assistive technology, and performance measurements.

For a recurring defect, record the actual symptom, cause, fix, and regression evidence in existing project notes. Do not turn one incident into a universal rule or add a fix log for every small change.

Source: [Bama adaptation and license](bama-source.md).
