from snow_runtime.domain.value_objects import ExecutionOptions, ExecutionReport


class SQLApplication:
    def __init__(
        self, execution_service, session_service, history_service, logging_service
    ):
        self.execution_service = execution_service
        self.session_service = session_service
        self.history_service = history_service
        self.logging_service = logging_service

    def execute(
        self, sql: str, options: ExecutionOptions | None = None
    ) -> ExecutionReport:
        pass
