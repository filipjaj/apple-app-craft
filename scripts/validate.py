#!/usr/bin/env python3
"""Validate a skills-only Apple App Craft checkout without executing its skills."""
from pathlib import Path
import json
import re
import sys
import yaml


def validate(root):
    root = Path(root).resolve()
    errors = []
    def fail(message):
        errors.append(message)
    def load_json(relative):
        try:
            return json.loads((root / relative).read_text())
        except (OSError, ValueError) as exc:
            fail(f'{relative}: {exc}')
            return {}
    portable = load_json('plugin.json')
    codex = load_json('.codex-plugin/plugin.json')
    claude = load_json('.claude-plugin/plugin.json')
    for field in ('name', 'version', 'description', 'license', 'repository'):
        value = portable.get(field)
        if not value or any(p.get(field) != value for p in (codex, claude)):
            fail(f'Plugin manifests disagree or omit {field}')
    if portable.get('name') != 'apple-app-craft':
        fail('Unexpected plugin identity')
    if not re.fullmatch(r'\d+\.\d+\.\d+', portable.get('version', '')):
        fail('Version must be major.minor.patch')
    for label, manifest in (('Codex', codex), ('Claude', claude)):
        if manifest.get('skills') != './skills/':
            fail(f'{label}: skills must resolve to ./skills/')
    for file in ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json'):
        market = load_json(file)
        entries = market.get('plugins', [])
        if market.get('name') != 'apple-app-craft' or len(entries) != 1:
            fail(f'{file}: expected one plugin in apple-app-craft marketplace')
            continue
        entry = entries[0]
        if entry.get('name') != portable.get('name'):
            fail(f'{file}: plugin name mismatch')
        source = entry.get('source')
        if source not in ('./', {'source': 'local', 'path': './'}):
            fail(f'{file}: source must be this package root')
    skill_paths = sorted((root / 'skills').glob('*/SKILL.md'))
    if not skill_paths:
        fail('No skills found')
    names = set()
    for path in skill_paths:
        text = path.read_text()
        match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
        try:
            meta = yaml.safe_load(match.group(1)) if match else None
        except yaml.YAMLError:
            meta = None
        if not isinstance(meta, dict):
            fail(f'{path.relative_to(root)}: invalid YAML frontmatter')
            continue
        name = meta.get('name', '')
        if name != path.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            fail(f'{path.relative_to(root)}: invalid/mismatched name')
        if name in names:
            fail(f'Duplicate skill name: {name}')
        names.add(name)
        if not isinstance(meta.get('description'), str) or not meta['description'].strip():
            fail(f'{name}: missing description')
        if '[TODO:' in text:
            fail(f'{name}: unfinished scaffold')
        ui_path = path.parent / 'agents/openai.yaml'
        if ui_path.exists():
            try:
                ui = yaml.safe_load(ui_path.read_text())
                if not isinstance(ui, dict) or not ui.get('interface', {}).get('display_name'):
                    fail(f'{name}: invalid UI metadata')
            except yaml.YAMLError:
                fail(f'{name}: malformed UI YAML')
    router_path = root / 'skills/apple-app-craft/SKILL.md'
    router = router_path.read_text() if router_path.exists() else ''
    catalog = set(re.findall(r'\]\(\.\./([^/]+)/SKILL\.md\)', router))
    if catalog != names - {'apple-app-craft'}:
        fail(f'Router/catalog mismatch: {sorted(catalog ^ (names - {"apple-app-craft"}))}')
    links = 0
    forbidden = re.compile(r'/Users/|schibsted\.ghe\.com|[\w.+-]+@schibsted\.com|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
    for path in root.rglob('*'):
        if '.git' in path.relative_to(root).parts or '__pycache__' in path.parts:
            continue
        if path.is_symlink():
            fail(f'Symlink not allowed in package: {path.relative_to(root)}')
            continue
        if not path.is_file() or path.suffix not in ('.md', '.json', '.yaml', '.yml', '.txt'):
            continue
        text = path.read_text()
        if forbidden.search(text):
            fail(f'Private path, credential, or organization detail: {path.relative_to(root)}')
        if path.suffix != '.md':
            continue
        for ref in re.findall(r'\]\(([^)\s]+)\)', text):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', ref) or ref.startswith('#'):
                continue
            target = (path.parent / ref.split('#', 1)[0]).resolve()
            links += 1
            if not target.is_relative_to(root) or not target.exists():
                fail(f'{path.relative_to(root)}: missing/escaping reference {ref}')
    for required in ('LICENSE', 'THIRD_PARTY_NOTICES.md', 'licenses/BAMA-MIT.txt'):
        if not (root / required).is_file():
            fail(f'Missing notice: {required}')
    return errors, {'skills': len(skill_paths), 'local_links': links, 'manifests': 5}


if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors, counts = validate(root)
    for error in errors:
        print(f'FAIL: {error}', file=sys.stderr)
    print(json.dumps({'ok': not errors, **counts}, sort_keys=True))
    sys.exit(bool(errors))
