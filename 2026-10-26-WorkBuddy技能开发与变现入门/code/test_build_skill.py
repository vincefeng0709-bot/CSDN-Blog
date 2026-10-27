"""Black-box test of the original teaching package, not of WorkBuddy."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile

HERE = Path(__file__).resolve().parent


class PackageTests(unittest.TestCase):
    def test_example_package_round_trip(self):
        builder = HERE / "build_skill.py"
        self.assertTrue(builder.is_file(), "Skill package builder is not implemented yet")
        source = HERE / "meeting-action-checklist"
        with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as temp:
            output = Path(temp) / "skill.zip"
            result = subprocess.run(
                [sys.executable, str(builder), "--output", str(output)],
                capture_output=True, text=True, encoding="utf-8", check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            report = json.loads(result.stdout)
            expected = sorted(p.relative_to(source.parent).as_posix() for p in source.rglob("*") if p.is_file())
            self.assertEqual(report["files"], expected)
            self.assertEqual(report["sha256"], hashlib.sha256(output.read_bytes()).hexdigest())
            with zipfile.ZipFile(output) as archive:
                self.assertEqual(archive.namelist(), expected)
                self.assertIsNone(archive.testzip())
                for name in expected:
                    self.assertEqual(archive.read(name), (source.parent / name).read_bytes())


if __name__ == "__main__":
    unittest.main(verbosity=2)
