from .invalid_state_error import InvalidStateError

class RuntimeNotStartedError(InvalidStateError):
    """Raised when an operation is requested but the runtime has not been started."""
    pass
