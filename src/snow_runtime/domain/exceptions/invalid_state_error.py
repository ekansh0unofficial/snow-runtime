from .snow_runtime_error import SnowRuntimeError

class InvalidStateError(SnowRuntimeError):
    """Raised when an operation is not valid given the current state of the system."""
    pass

