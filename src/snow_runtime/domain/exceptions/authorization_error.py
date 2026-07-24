from .dependency_error import DependencyError

class AuthorizationError(DependencyError):
    """Raised when a Snowflake object exists but the authenticated user lacks permission to access it."""
    pass