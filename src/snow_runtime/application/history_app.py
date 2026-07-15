class HistoryApplication:
    def __init__(self, history_service, config_service):
        self.history_service = history_service
        self.config_service = (
            config_service  # history is associated with ConnectionProfile
        )

    def list(self):
        pass

    def search(self, text: str):
        pass

    def clear(self):
        pass
