"""Offline tests for daily_update — no network, stdlib unittest only.

Run: python -m unittest test_daily_update -v
"""

import json
import tempfile
import unittest
from pathlib import Path

import daily_update as dd


class TestArchive(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        # Redirect the module's output paths into a throwaway directory.
        dd.ARCHIVE = self.tmp / "archive"
        dd.DATA = self.tmp / "data"
        dd.README = self.tmp / "README.md"

    def test_six_readings_registered(self):
        self.assertEqual(len(dd.READINGS), 6)
        for key in ("crypto", "quote", "nasa", "car_news", "onthisday", "github"):
            self.assertIn(key, dd.READINGS)

    def test_update_readme_replaces_block_once(self):
        dd.README.write_text(
            "Intro\n<!-- LATEST:START -->\nOLD\n<!-- LATEST:END -->\nOutro\n",
            encoding="utf-8",
        )
        snap = {
            "date": "2026-07-23",
            "quote": {"text": "Hi", "author": "Me"},
            "crypto": {"bitcoin": {"usd": 100, "usd_24h_change": 1.2}},
            "onthisday": {"year": 685, "text": "A thing happened", "title": "T", "url": "http://x"},
            "github": {"login": "deadsunx", "public_repos": 8, "followers": 0, "html_url": "http://gh"},
        }
        dd.update_readme(snap)
        txt = dd.README.read_text(encoding="utf-8")
        self.assertIn("Intro", txt)
        self.assertIn("Outro", txt)
        self.assertIn("2026-07-23", txt)
        self.assertIn("A thing happened", txt)
        self.assertNotIn("OLD", txt)
        self.assertEqual(txt.count("<!-- LATEST:START -->"), 1)

    def test_append_crypto_csv_is_idempotent(self):
        snap = {"date": "2026-07-23", "crypto": {"bitcoin": {"usd": 100, "usd_24h_change": 1.0, "usd_market_cap": 5}}}
        dd.append_crypto_csv(snap)
        dd.append_crypto_csv(snap)  # same day+coin must NOT duplicate
        rows = (dd.DATA / "crypto.csv").read_text(encoding="utf-8").strip().splitlines()
        self.assertEqual(rows[0].split(",")[0], "date")  # header present
        self.assertEqual(len(rows), 2)                    # header + 1 (deduped)
        # A different day adds a new row.
        dd.append_crypto_csv({"date": "2026-07-24", "crypto": {"bitcoin": {"usd": 110, "usd_24h_change": 0.5, "usd_market_cap": 6}}})
        rows = (dd.DATA / "crypto.csv").read_text(encoding="utf-8").strip().splitlines()
        self.assertEqual(len(rows), 3)                    # header + 2 days

    def test_write_index_tracks_captured(self):
        dd.ARCHIVE.mkdir(parents=True)
        (dd.ARCHIVE / "2026-07-23.json").write_text(
            json.dumps({"date": "2026-07-23", "crypto": {"usd": 1}, "quote": {"error": "down"}}),
            encoding="utf-8",
        )
        dd.write_index()
        idx = json.loads((dd.ARCHIVE / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(len(idx), 1)
        self.assertEqual(idx[0]["date"], "2026-07-23")
        self.assertIn("crypto", idx[0]["captured"])       # ok reading counted
        self.assertNotIn("quote", idx[0]["captured"])     # errored reading excluded


if __name__ == "__main__":
    unittest.main()
