import unittest
import os
import json
import glob

class TestOmniSentinelIntegration(unittest.TestCase):
    def test_audit_files_exist(self):
        files = glob.glob("audit/WORM_*.json")
        self.assertGreater(len(files), 0, "No audit files found")

    def test_audit_file_format(self):
        files = glob.glob("audit/WORM_*.json")
        if not files:
            self.skipTest("No audit files to check")
        latest_file = max(files, key=os.path.getctime)
        with open(latest_file, 'r') as f:
            data = json.load(f)
            self.assertIn("batch_id", data)
            self.assertIn("timestamp", data)
            self.assertIn("hash", data)
            self.assertIn("prev_hash", data)
            self.assertEqual(data["data"]["pcr_match"], "TRUE")

    def test_gsri_threshold(self):
        files = glob.glob("audit/WORM_*.json")
        if not files:
            self.skipTest("No audit files to check")
        latest_file = max(files, key=os.path.getctime)
        with open(latest_file, 'r') as f:
            data = json.load(f)
            self.assertLess(data["data"]["g_sri"], 40.0, "G-SRI threshold violation!")

if __name__ == "__main__":
    unittest.main()
