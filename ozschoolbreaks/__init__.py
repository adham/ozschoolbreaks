from datetime import date
from typing import TypedDict, List
from .data import BREAK_DATA
from .utils import validate_state

class BreakPeriod(TypedDict):
    term: int
    start: date
    end: date

def get_breaks(state: str, year: int | None = None) -> List[BreakPeriod]:
    """Get school break periods for a given state and year.

    Args:
        state: The state code (e.g., 'NSW', 'VIC', 'TAS', 'SA', 'QLD')
        year: The year to get breaks for (defaults to current year)

    Returns:
        A list of break periods with term number and start/end dates

    Raises:
        ValueError: If the state is invalid or no data exists for the year
    """
    validate_state(state)
    year = year if year is not None else date.today().year

    try:
        return BREAK_DATA[state][year]
    except KeyError:
        raise ValueError(f"No break data available for {state} in {year}")

__all__ = ["get_breaks"]