"""
ozschoolbreaks

A Python package to get school break dates for Australian states.

This package provides utilities to retrieve school break periods for different
states in Australia.

How to use:
```python
from ozschoolbreaks import get_breaks

# breaks for a specific year
breaks = get_breaks(state="NSW", years=2023)

# breaks for multiple years
breaks = get_breaks(state="NSW", years=[2023, 2024])

# Print the breaks
for break_period in breaks:
    print(f"{break_period.start} to {break_period.end}")
```

"""

from importlib.metadata import version, PackageNotFoundError
from .breaks import get_breaks
from .breaks import BreakPeriod

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["get_breaks", "BreakPeriod"]