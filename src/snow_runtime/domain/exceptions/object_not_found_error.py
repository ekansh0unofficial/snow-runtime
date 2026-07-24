from .invalid_state_error import InvalidStateError

class ObjectNotFoundError(InvalidStateError):
    """Raised when a requested domain object (history entry, schema, table, etc.) does not exist."""
    pass