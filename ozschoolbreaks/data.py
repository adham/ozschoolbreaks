from datetime import date
import yaml
from pathlib import Path

def _date(date_str: str) -> date:
    """Convert a string date to a datetime.date object."""
    return date.fromisoformat(date_str)

def load_break_data():
    """Load school break data from YAML file."""
    yaml_path = Path(__file__).parent / "school_breaks.yaml"
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)
    
    return data

BREAK_DATA = load_break_data()