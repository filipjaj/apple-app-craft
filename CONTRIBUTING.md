# Contributing

Keep each skill focused on an observable user outcome. Reuse the existing collection router; do not introduce a second mandatory workflow. Put conditional detail in linked references, preserve project targets and user authorization, and distinguish rendered, interaction, accessibility, and performance evidence.

For a new skill, add `skills/<name>/SKILL.md` with YAML `name` and `description`, add useful UI metadata in `agents/openai.yaml`, and link it from the collection router. Include source attribution and required notices for adaptations.

Run validation before submitting:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

A passing validator establishes package consistency, not runtime app correctness or model behavior. Test meaningful workflow changes on a realistic, isolated task and report what you actually observed.

Use a feature branch/worktree, keep changes scoped, and submit a pull request. Do not commit credentials, private app screenshots, production stores, generated caches, or personal agent configuration.
