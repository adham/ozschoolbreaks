from datetime import date

def _date(date_str: str) -> date:
    """Convert a string date to a datetime.date object."""
    return date.fromisoformat(date_str)

# Placeholder school break data (replace with real dates)
BREAK_DATA = {
    "NSW": {
        2025: [
            {"term": 1, "start": _date("2025-04-14"), "end": _date("2025-04-25")},
            {"term": 2, "start": _date("2025-07-07"), "end": _date("2025-07-18")},
            {"term": 3, "start": _date("2025-09-29"), "end": _date("2025-10-10")},
            {"term": 4, "start": _date("2025-12-20"), "end": _date("2026-01-28")},
        ],
        2026: [
            {"term": 1, "start": _date("2026-04-13"), "end": _date("2026-04-24")},
            {"term": 2, "start": _date("2026-07-06"), "end": _date("2026-07-17")},
            {"term": 3, "start": _date("2026-09-28"), "end": _date("2026-10-09")},
            {"term": 4, "start": _date("2026-12-19"), "end": _date("2027-01-27")},
        ],
    },
    "VIC": {
        2025: [
            {"term": 1, "start": _date("2025-04-12"), "end": _date("2025-04-27")},
            {"term": 2, "start": _date("2025-07-05"), "end": _date("2025-07-20")},
            {"term": 3, "start": _date("2025-09-27"), "end": _date("2025-10-12")},
            {"term": 4, "start": _date("2025-12-20"), "end": _date("2026-01-25")},
        ],
    },
    "TAS": {
        2025: [
            {"term": 1, "start": _date("2025-04-15"), "end": _date("2025-04-26")},
            {"term": 2, "start": _date("2025-07-08"), "end": _date("2025-07-19")},
            {"term": 3, "start": _date("2025-09-30"), "end": _date("2025-10-11")},
            {"term": 4, "start": _date("2025-12-18"), "end": _date("2026-01-30")},
        ],
    },
    "SA": {
        2025: [
            {"term": 1, "start": _date("2025-04-14"), "end": _date("2025-04-25")},
            {"term": 2, "start": _date("2025-07-07"), "end": _date("2025-07-18")},
            {"term": 3, "start": _date("2025-09-29"), "end": _date("2025-10-10")},
            {"term": 4, "start": _date("2025-12-15"), "end": _date("2026-01-27")},
        ],
    },
    "QLD": {
        2025: [
            {"term": 1, "start": _date("2025-04-14"), "end": _date("2025-04-25")},
            {"term": 2, "start": _date("2025-07-07"), "end": _date("2025-07-18")},
            {"term": 3, "start": _date("2025-09-29"), "end": _date("2025-10-10")},
            {"term": 4, "start": _date("2025-12-15"), "end": _date("2026-01-27")},
        ],
    },
}