from .dependency_error import DependencyError

class ExportError(DependencyError):
    """Raised when writing query results to the export destination fails."""
    pass
