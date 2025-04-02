# ozschoolbreaks

A Python package to get school break dates for Australian states.

## Installation
```bash
pip install ozschoolbreaks
```

## How to Use
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

## TODO
- [ ] Check dates
    - [x] VIC
    - [ ] NSW
    - [ ] QLD
    - [ ] SA
    - [ ] TAS
- [ ] Add missing states
- [x] Pass a range of years instead of one year