# Changelog

## 0.1.0 — 2026-10-30

- Publish the coordinated collection of 74 Apple app skills.
- Add a bounded delivery workflow with evidence-linked acceptance criteria.
- Include reference-app inspection, macOS utilities, app automation, and runtime/UI verification adapted from BAMA.
- Package portable, Codex, and Claude-compatible manifests and repository marketplaces.
- Document optional tooling and preserve upstream MIT notices.
- Add package validation and seven regression tests with CI.

Release checks: all 74 skills pass the skill-creator validator; 243 local references resolve; the portable manifest passes its published JSON schema; seven package tests pass. Codex CLI 0.162.1 successfully installs and discovers all 74 skills. Claude runtime and Swift application behavior are not tested by this release.
