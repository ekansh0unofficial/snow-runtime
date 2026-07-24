class RuntimeApplication:
    """Controls the lifecycle of the Snow Runtime process: start, stop, restart, and status."""

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
        """Initialise with all services and providers required to manage the full runtime lifecycle."""
        self.config_service = config_service
        self.session_service = session_service
        self.secret_service = secret_service
        self.process_provider = process_provider
        self.runtime_provider = runtime_provider
        self.logging_service = logging_service
        self.diagnostic_service = diagnostic_service

    def start(self):
        """Start the runtime. Raises RuntimeAlreadyRunningError if it is already active."""
        pass

    def stop(self):
        """Gracefully stop the runtime. Raises RuntimeNotStartedError if it is not running."""
        pass

    def restart(self):
        """Stop and then start the runtime."""
        pass

    @property
    def status(self):
        """Return the current RuntimeState of the runtime."""
        pass
