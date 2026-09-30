import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "showroom/content/modules/ROOT/pages"


class ShowroomTests(unittest.TestCase):
    def test_lab_is_separate_and_complete(self):
        expected = ["01-prerequisites.adoc", "02-declare.adoc", "03-observe.adoc", "04-compare.adoc", "05-refuse.adoc", "06-review.adoc", "07-reclaim.adoc"]
        self.assertTrue(all((PAGES / name).exists() for name in expected))
        joined = "\n".join((PAGES / name).read_text() for name in expected)
        for term in ("ALLOW_REVIEW", "REFUSE", "ABSTAIN", "HUMAN_REVIEW_REQUIRED", "zero", "REHEARSAL"):
            self.assertIn(term, joined)

    def test_supplemental_roadshow_was_not_copied(self):
        files = [path for path in (ROOT / "showroom").rglob("*") if path.is_file()]
        self.assertLess(len(files), 20)
        self.assertFalse(any("2026_spring" in path.as_posix() for path in files))

    def test_playbook_declares_runtime_detectable_content_path(self):
        playbook = yaml.safe_load((ROOT / "showroom/default-site.yml").read_text())
        source = playbook["content"]["sources"][0]
        self.assertEqual(source["url"], "/showroom/repo")
        self.assertEqual(source["start_path"], "showroom/content")

    def test_antora_version_matches_showroom_runtime_path(self):
        component = yaml.safe_load((ROOT / "showroom/content/antora.yml").read_text())
        self.assertEqual(component["name"], "virtualization-ai-301")
        self.assertEqual(component["version"], "main")


if __name__ == "__main__":
    unittest.main()
