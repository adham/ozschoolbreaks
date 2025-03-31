VALID_STATES = {"NSW", "VIC", "TAS", "SA", "QLD"}

def validate_state(state: str) -> None:
    """Validate that the state is one of the supported states."""
    if state not in VALID_STATES:
        raise ValueError(f"Invalid state. Must be one of {VALID_STATES}")