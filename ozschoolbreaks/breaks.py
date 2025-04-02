from datetime import date
from typing import NamedTuple, Sequence, Union, List
from .data import BREAK_DATA
from .utils import validate_state

class BreakPeriod(NamedTuple):
    """Represents a school break period with start and end dates."""
    start: date
    end: date

def get_breaks(state: str, years: Union[int, List[int]] = None) -> Sequence[BreakPeriod]:
    """Get school break periods for a given state and year(s).

    Args:
        state: The state code (e.g., 'NSW', 'VIC', 'TAS', 'SA', 'QLD')
        years: The year or list of years to get breaks for (defaults to current year)

    Returns:
        A list of break periods with term number and start/end dates

    Raises:
        ValueError: If the state is invalid or no data exists for the year(s)
    """
    validate_state(state)

    # Normalize years to always be a list
    if years is None:
        years = [date.today().year]
    elif isinstance(years, int):
        years = [years]

    break_periods = []
    for y in years:
        try:
            break_periods.extend(
                [BreakPeriod(start=break_data["start"], end=break_data["end"]) for break_data in BREAK_DATA[state][y]]
            )
        except KeyError:
            valid_states = list(BREAK_DATA.keys())
            valid_years = list(BREAK_DATA.get(state, {}).keys())
            raise ValueError(
                f"No break data available for {state} in {y}. "
                f"Valid states: {valid_states}. Valid years for {state}: {valid_years}"
            )

    return break_periods