class HistoryApplication:
    """Access and manage the query execution history scoped to the active connection profile."""

    def __init__(self, history_service, config_service):
        """Initialise with a history service for persistence and a config service to scope history per profile."""
        self.history_service = history_service
        self.config_service = config_service  

    def list(self):
        """Return all history entries for the active connection profile."""
        pass

    def search(self, text: str):
        """Return history entries whose SQL contains the given search text."""
        pass

    def clear(self):
        """Delete all history entries for the active connection profile."""
        pass
