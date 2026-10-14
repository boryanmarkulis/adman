import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExportContractTest(unittest.TestCase):
    def test_standalone_brain_lives_at_project_root(self):
        for path in ("CLAUDE.md", "AGENTS.md", "SUBJECT.md", "VOICE.md", "knowledge", "skills", "rules"):
            self.assertTrue((ROOT / path).exists(), path)
        self.assertFalse((ROOT / "export").exists())
        self.assertFalse((ROOT / "skills" / "lead-gen-ad").exists())
        for private_builder_file in ("selection.tsv", "DEVELOPMENT.md", "BUILD-CHECKLIST.md", "scripts/alias_map.py", "scripts/scrub.py", "scripts/port_skills.py"):
            self.assertFalse((ROOT / private_builder_file).exists(), private_builder_file)

    def test_documented_knowledge_search_command_runs(self):
        result = subprocess.run(
            [sys.executable, "scripts/knowledge_search.py", "--pages", "-k", "3", "short-form hook"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("===", result.stdout)

    def test_verifier_accepts_the_shipped_brain(self):
        result = subprocess.run(
            [sys.executable, "scripts/verify_export.py", "--root", str(ROOT)],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_starter_does_not_claim_private_connections_or_brand_assets(self):
        connections = (ROOT / "connections.md").read_text().lower()
        renderer = (ROOT / "scripts" / "render_graphic.py").read_text().lower()
        self.assertNotIn("| existing |", connections)
        self.assertNotIn("n8n already", connections)
        self.assertNotIn("solar installer", renderer)
        self.assertNotIn("brand (set)", renderer)
        research_skill = (ROOT / "skills" / "last30days" / "SKILL.md").read_text()
        self.assertNotIn("hooks/scripts/check-config.sh", research_skill)
        self.assertNotIn("docs/reference/eval.md", research_skill)
        self.assertNotIn("docs/reference/old-nux-wizard-v3.0.0.md", research_skill)
        self.assertNotIn("docs/reference/json-export.md", research_skill)
        for developer_script in ("build-skill.sh", "compare.sh", "test-v1-vs-v2.sh"):
            self.assertFalse(
                (ROOT / "skills" / "last30days" / "scripts" / developer_script).exists(),
                developer_script,
            )

    def test_verifier_rejects_private_identifiers_and_dead_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "knowledge").mkdir()
            (root / "skills").mkdir()
            (root / "rules").mkdir()
            for name in ("CLAUDE.md", "AGENTS.md", "SUBJECT.md", "VOICE.md"):
                (root / name).write_text("placeholder\n")
            (root / "knowledge" / "bad.md").write_text(
                "A note about zzprivatetestclientzz with [[missing-private-page]].\n"
            )
            result = subprocess.run(
                [sys.executable, ROOT / "scripts" / "verify_export.py", "--root", str(root)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("private identifier", result.stdout)
        self.assertIn("dead wiki link", result.stdout)


if __name__ == "__main__":
    unittest.main()
