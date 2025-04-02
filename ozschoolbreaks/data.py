from pathlib import Path
import yaml


def load_break_data():
    """Load school break data from YAML file."""
    yaml_path = Path(__file__).parent / "school_breaks.yaml"
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)
    
    return data

BREAK_DATA = load_break_data()