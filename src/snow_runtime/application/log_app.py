class LogApplication:
    """Access and manage the runtime log stream."""

    def __init__(self, logging_service):
        """Initialise with a logging service that provides access to the runtime log."""
        self.logging_service = logging_service

    def tail(self):
        """Return the most recent log entries from the runtime log."""
        pass

    def clear(self):
        """Delete all entries from the runtime log."""
        pass
