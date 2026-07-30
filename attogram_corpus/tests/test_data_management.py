import unittest
from attogram_corpus.data_management import FoodVibeDataRecord


class TestFoodVibeDataRecord(unittest.TestCase):
    def test_to_dict_and_from_dict(self):
        record = FoodVibeDataRecord(
            photo_id="photo123",
            yummy_ness=7,
            masarap_ness=8,
            lekker_ness=9,
            dish_name="Adobo",
            cuisine="Filipino",
            date="2026-07-26",
            city="Amsterdam",
            consent=True,
            license_granted=True,
        )
        d = record.to_dict()
        self.assertEqual(d["photo_id"], "photo123")
        self.assertEqual(d["yummy_ness"], 7)
        self.assertEqual(d["masarap_ness"], 8)
        self.assertEqual(d["lekker_ness"], 9)
        self.assertEqual(d["dish_name"], "Adobo")
        self.assertEqual(d["cuisine"], "Filipino")
        self.assertEqual(d["date"], "2026-07-26")
        self.assertEqual(d["city"], "Amsterdam")
        self.assertTrue(d["consent"])
        self.assertTrue(d["license_granted"])

        record2 = FoodVibeDataRecord.from_dict(d)
        self.assertEqual(record2.photo_id, "photo123")
        self.assertEqual(record2.yummy_ness, 7)
        self.assertEqual(record2.masarap_ness, 8)
        self.assertEqual(record2.lekker_ness, 9)
        self.assertEqual(record2.dish_name, "Adobo")
        self.assertEqual(record2.cuisine, "Filipino")
        self.assertEqual(record2.date, "2026-07-26")
        self.assertEqual(record2.city, "Amsterdam")
        self.assertTrue(record2.consent)
        self.assertTrue(record2.license_granted)
