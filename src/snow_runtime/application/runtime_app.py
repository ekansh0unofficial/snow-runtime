class RuntimeApplication:
    def __init__(
        self,
        config_service,
        session_service,
        secret_service,
        process_provider,
        runtime_provider,
        logging_service,
        diagnostic_service,
    ):
        self.config_service = config_service
        self.session_service = session_service
        self.secret_service = secret_service
        self.process_provider = process_provider
        self.runtime_provider = runtime_provider
        self.logging_service = logging_service
        self.diagnostic_service = diagnostic_service

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        pass

    @property
    def status(self):
        pass
