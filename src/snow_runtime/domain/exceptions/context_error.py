from .invalid_state_error import InvalidStateError

class ContextError(InvalidStateError):
    """Raised when a context is not set or is invalid for the requested operation."""
    pass
