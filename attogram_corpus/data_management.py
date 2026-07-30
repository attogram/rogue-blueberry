"""
Data management utilities for Food Vibe trilingual taxonomy dataset.

Includes:
- Data schema definition
- Consent and license record keeping
- Metadata handling
"""

import json
from typing import Dict, Any, Optional


class FoodVibeDataRecord:
    """
    Represents a single Food Vibe data record with ratings and metadata.
    """

    def __init__(self, photo_id: str, yummy_ness: int, masarap_ness: int, lekker_ness: int,
                 dish_name: Optional[str] = None, cuisine: Optional[str] = None,
                 date: Optional[str] = None, city: Optional[str] = None,
                 consent: bool = False, license_granted: bool = False):
        self.photo_id = photo_id
        self.yummy_ness = yummy_ness
        self.masarap_ness = masarap_ness
        self.lekker_ness = lekker_ness
        self.dish_name = dish_name
        self.cuisine = cuisine
        self.date = date
        self.city = city
        self.consent = consent
        self.license_granted = license_granted

    def to_dict(self) -> Dict[str, Any]:
        return {
            "photo_id": self.photo_id,
            "yummy_ness": self.yummy_ness,
            "masarap_ness": self.masarap_ness,
            "lekker_ness": self.lekker_ness,
            "dish_name": self.dish_name,
            "cuisine": self.cuisine,
            "date": self.date,
            "city": self.city,
            "consent": self.consent,
            "license_granted": self.license_granted,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FoodVibeDataRecord':
        return FoodVibeDataRecord(
            photo_id=data.get("photo_id", ""),
            yummy_ness=data.get("yummy_ness", 0),
            masarap_ness=data.get("masarap_ness", 0),
            lekker_ness=data.get("lekker_ness", 0),
            dish_name=data.get("dish_name"),
            cuisine=data.get("cuisine"),
            date=data.get("date"),
            city=data.get("city"),
            consent=data.get("consent", False),
            license_granted=data.get("license_granted", False),
        )
