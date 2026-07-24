from .dependency_error import DependencyError

class AuthenticationError(DependencyError):
    """Raised when Snowflake rejects the provided credentials during login."""
    pass
