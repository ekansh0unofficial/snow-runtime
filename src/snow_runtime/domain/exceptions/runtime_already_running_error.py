from .invalid_state_error import InvalidStateError

class RuntimeAlreadyRunningError(InvalidStateError):
    """Raised when attempting to start the runtime while it is already running."""
    pass
