"""Exercise package failures that would break installation or redistribution."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package_validator', ROOT / 'scripts/validate.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', '.venv', 'dist'))

    def errors(self):
        return module.validate(self.root)[0]

    def test_actual_package_is_valid(self):
        self.assertEqual([], self.errors())

    def test_missing_sibling_reference_fails(self):
        shutil.rmtree(self.root / 'skills/plan-native-app')
        self.assertTrue(any('reference' in e or 'catalog' in e for e in self.errors()))

    def test_manifest_version_drift_fails(self):
        path = self.root / '.codex-plugin/plugin.json'
        data = json.loads(path.read_text())
        data['version'] = '9.9.9'
        path.write_text(json.dumps(data))
        self.assertTrue(any('version' in e for e in self.errors()))

    def test_reference_outside_package_fails(self):
        (self.root / 'EXAMPLE.md').write_text('[outside](../../outside.md)\n')
        self.assertTrue(any('escaping reference' in e for e in self.errors()))

    def test_private_machine_path_fails(self):
        private = '/' + 'Users/' + 'example/private'
        (self.root / 'EXAMPLE.md').write_text(private)
        self.assertTrue(any('Private path' in e for e in self.errors()))

    def test_missing_upstream_notice_fails(self):
        (self.root / 'licenses/BAMA-MIT.txt').unlink()
        self.assertTrue(any('Missing notice' in e for e in self.errors()))

    def test_invalid_frontmatter_fails(self):
        (self.root / 'skills/plan-native-app/SKILL.md').write_text('not a skill')
        self.assertTrue(any('frontmatter' in e for e in self.errors()))


if __name__ == '__main__':
    unittest.main()
