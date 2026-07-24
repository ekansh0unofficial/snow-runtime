from .dependency_error import DependencyError

class MetadataError(DependencyError):
    """Raised when fetching schema, table, or catalog metadata from Snowflake fails."""
    pass
