import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.services.hospital_finder import find_hospitals_for_disease


def test_find_hospitals_for_disease():
    hospitals = find_hospitals_for_disease("fever", "new delhi")

    assert hospitals is not None
    assert isinstance(hospitals, list)


def test_hospital_data_structure():
    hospitals = find_hospitals_for_disease("fever", "new delhi")

    if hospitals:
        hospital = hospitals[0]

        assert isinstance(hospital, dict)
        assert "name" in hospital
