# Tooling and portability

This plugin supplies instructions and references. It does not install runtimes, connect accounts, bundle an MCP server, or grant system access.

- Swift app compilation and runtime verification need an appropriate macOS/Xcode environment. Planning and source review can run elsewhere.
- Context7 is used for current SDK/framework/API/CLI details when available. Use current official documentation as fallback and disclose unsupported assumptions.
- SwiftProbe is preferred when installed. Its CLI and any separate skill are not bundled or required to install this plugin. Inspect its tool schemas before calling it. When unavailable, use the project's native build/test runner and report the substitution; do not claim a SwiftProbe result.
- Browser/native computer-use tools are supplied by the host and need their own access. If unavailable, use user-provided artifacts and report unobserved interactions.
- Read sibling skills directly using relative paths. Do not require a particular agent's Skill tool name or a globally installed duplicate collection.

Existing repository instructions and the user's explicitly chosen tools take precedence. Required checks that cannot run remain visible as gaps.
