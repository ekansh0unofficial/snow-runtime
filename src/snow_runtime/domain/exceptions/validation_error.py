from .snow_runtime_error import SnowRuntimeError

class ValidationError(SnowRuntimeError):
    """Raised when caller-provided input fails domain validation rules."""
    pass
