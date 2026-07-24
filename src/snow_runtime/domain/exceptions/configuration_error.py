from .validation_error import ValidationError

class ConfigurationError(ValidationError):
    """Raised when a connection profile or configuration value is missing or structurally invalid."""
    pass