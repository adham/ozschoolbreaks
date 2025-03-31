import pytest
from datetime import date
from ozschoolbreaks import get_breaks

def test_get_breaks_valid():
    breaks = get_breaks("NSW")
    assert len(breaks) == 4
    assert breaks[0]["term"] == 1
    assert isinstance(breaks[0]["start"], date)
    assert isinstance(breaks[0]["end"], date)

def test_get_breaks_invalid_state():
    with pytest.raises(ValueError, match="Invalid state"):
        get_breaks("ACT")

def test_get_breaks_year():
    breaks = get_breaks("NSW", year=2026)
    assert len(breaks) == 4
    assert breaks[0]["start"].year == 2026
