from .dependency_error import DependencyError

class ExecutionError(DependencyError):
    """Raised when Snowflake rejects or fails to execute a submitted query."""
    pass
