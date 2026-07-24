from .invalid_state_error import InvalidStateError

class ProfileNotFoundError(InvalidStateError):
    """Raised when a requested connection profile does not exist."""
    pass
