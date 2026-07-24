from .invalid_state_error import InvalidStateError

class SessionError(InvalidStateError):
    """Raised when an operation requires an active session that does not exist or is in the wrong state."""
    pass
