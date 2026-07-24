from .snow_runtime_error import SnowRuntimeError

class DependencyError(SnowRuntimeError):
    """Raised when an external dependency (Snowflake, network) fails or refuses a request."""
    pass
