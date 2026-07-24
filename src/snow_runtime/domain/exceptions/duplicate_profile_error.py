from .invalid_state_error import InvalidStateError

class DuplicateProfileError(InvalidStateError):
    """Raised when attempting to create a connection profile whose name already exists."""
    pass
