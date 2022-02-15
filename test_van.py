#test_vehicle.py
import pytest
from Van import Van

def test_van():
    myVan = Van("00D1122","Renault","Kango", 100000, 75)
    assert myVan.get_make_model() == "Renault Kango"
    assert myVan.get_miles() == 100000
    assert myVan.get_capacity() == 75
