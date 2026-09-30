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

    def test_lab_is_executable_and_follows_show_learn_do_prove(self):
        joined = "\n".join(path.read_text() for path in sorted(PAGES.glob("*.adoc")))
        for heading in ("== Show", "== Learn", "== Do", "== Prove"):
            self.assertIn(heading, joined)
        self.assertGreaterEqual(joined.count('role="execute"'), 10)

    def test_lab_exercises_the_real_governed_api_and_evidence(self):
        joined = "\n".join(path.read_text() for path in sorted(PAGES.glob("*.adoc")))
        for required in (
            "/healthz",
            "/api/v1/modernize",
            "/api/v1/evidence/",
            "/metrics",
            "condition=model-unavailable",
            "request_sha256",
        ):
            self.assertIn(required, joined)

    def test_lab_truthfully_distinguishes_live_from_rehearsal(self):
        joined = "\n".join(path.read_text() for path in sorted(PAGES.glob("*.adoc")))
        for required in (
            'source_state == "LIVE"',
            'ai_participated == true',
            'source_state == "REHEARSAL"',
            'ai_participated == false',
        ):
            self.assertIn(required, joined)

    def test_console_is_part_of_the_observation_workflow(self):
        observe = (PAGES / "03-observe.adoc").read_text()
        self.assertIn("OpenShift Console", observe)
        self.assertIn("VirtualMachineInstances", observe)
        self.assertIn("NetworkPolicies", observe)

    def test_cleanup_is_executable_and_preserves_platform_resources(self):
        reclaim = (PAGES / "07-reclaim.adoc").read_text()
        self.assertIn('role="execute"', reclaim)
        self.assertIn("rm -f", reclaim)
        self.assertIn("Launchpad", reclaim)
        self.assertIn("must not uninstall", reclaim)


if __name__ == "__main__":
    unittest.main()
