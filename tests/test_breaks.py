import pytest
from datetime import date
from ozschoolbreaks import get_breaks, BreakPeriod

def test_get_breaks_valid():
    breaks = get_breaks("NSW")
    assert len(breaks) == 4
    assert isinstance(breaks[0], BreakPeriod)
    assert isinstance(breaks[0].start, date)
    assert isinstance(breaks[0].end, date)

def test_get_breaks_invalid_state():
    with pytest.raises(ValueError, match="Invalid state"):
        get_breaks("ACT")

def test_get_breaks_single_year():
    breaks = get_breaks("NSW", years=2026)
    assert len(breaks) == 4
    assert breaks[0].start.year == 2026
    assert breaks[0].end.year == 2026

def test_get_breaks_multiple_years():
    breaks = get_breaks("NSW", years=[2025, 2026])
    assert len(breaks) == 8  # 4 breaks per year
    assert breaks[0].start.year == 2025
    assert breaks[4].start.year == 2026
