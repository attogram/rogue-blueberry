"""
Consent and license management for Food Vibe dataset contributors.

Handles:
- Recording consent status
- Recording license grants
- Revocation of consent
"""

from typing import Dict


class ConsentManager:
    def __init__(self):
        # Maps photo_id to consent and license status
        self._consent_records = {}

    def record_consent(self, photo_id: str):
        record = self._consent_records.get(photo_id, {"consent": False, "license_granted": False})
        record["consent"] = True
        self._consent_records[photo_id] = record

    def record_license(self, photo_id: str):
        record = self._consent_records.get(photo_id, {"consent": False, "license_granted": False})
        record["license_granted"] = True
        self._consent_records[photo_id] = record

    def revoke_consent(self, photo_id: str):
        if photo_id in self._consent_records:
            self._consent_records[photo_id]["consent"] = False
            self._consent_records[photo_id]["license_granted"] = False

    def has_consent(self, photo_id: str) -> bool:
        return self._consent_records.get(photo_id, {}).get("consent", False)

    def has_license(self, photo_id: str) -> bool:
        return self._consent_records.get(photo_id, {}).get("license_granted", False)

    def get_all_records(self) -> Dict[str, Dict[str, bool]]:
        return self._consent_records.copy()
