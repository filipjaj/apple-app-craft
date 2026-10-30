---
name: harden-app-memory-safety
description: "Review or improve Swift/C/C++ memory safety, sanitizer coverage and supported Enhanced Security protections. Use for unsafe-code hardening, not an ordinary ARC retention leak."
---

# Harden App Memory Safety

## Goal

Reduce exploitable memory defects at the app’s actual unsafe-code boundaries without masking the underlying bugs.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify unsafe Swift, C/C++ code and native dependencies exposed to untrusted input. Prefer memory-safe APIs and keep unsafe interoperability behind small, documented boundaries. Do not introduce unsafe code simply to imitate a performance example.

2. Test boundary conditions with supported sanitizers and representative malformed input. Address Sanitizer and Thread Sanitizer serve different defect classes and may require separate configurations. They are development diagnostics, not shipping runtime hardening.

3. Review current SDK, hardware and deployment support for memory integrity enforcement, typed allocation and pointer authentication. Assess custom allocators, pointer tagging, casts, hashing and arithmetic before enabling protections. Preserve signing and required third-party compatibility.

4. Fix detected defects rather than shipping a softer mode to conceal crashes. Constrain accepted formats and attack surface where appropriate. If processing is contained, treat returned data as untrusted too; isolation does not authenticate the result.

5. Verify the affected native paths under diagnostic configurations and supported device protections. Preserve failure artifacts and distinguish unsupported hardware from passing coverage. Report remaining unsafe boundaries and measured compatibility impacts.

## Verify the outcome

- Unsafe boundaries are small and deliberate.
- Detected sanitizer defects are resolved with causal fixes.
- Supported runtime protections work without hiding existing corruption.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
