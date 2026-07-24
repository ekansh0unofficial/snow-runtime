from .dependency_error import DependencyError

class ConnectivityError(DependencyError):
    """Raised when the network is unreachable or a connection to Snowflake cannot be established."""
    pass