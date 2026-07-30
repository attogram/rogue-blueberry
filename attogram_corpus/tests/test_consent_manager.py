import unittest
from attogram_corpus.consent_manager import ConsentManager


class TestConsentManager(unittest.TestCase):
    def setUp(self):
        self.cm = ConsentManager()

    def test_record_and_check_consent(self):
        self.cm.record_consent("photo1")
        self.assertTrue(self.cm.has_consent("photo1"))
        self.assertFalse(self.cm.has_license("photo1"))

    def test_record_and_check_license(self):
        self.cm.record_license("photo2")
        self.assertTrue(self.cm.has_license("photo2"))
        self.assertFalse(self.cm.has_consent("photo2"))

    def test_revoke_consent(self):
        self.cm.record_consent("photo3")
        self.cm.record_license("photo3")
        self.cm.revoke_consent("photo3")
        self.assertFalse(self.cm.has_consent("photo3"))
        self.assertFalse(self.cm.has_license("photo3"))

    def test_get_all_records(self):
        self.cm.record_consent("photo4")
        self.cm.record_license("photo4")
        records = self.cm.get_all_records()
        self.assertIn("photo4", records)
        self.assertTrue(records["photo4"]["consent"])
        self.assertTrue(records["photo4"]["license_granted"])
