from snow_runtime.domain.value_objects import ExecutionOptions, ExecutionReport


class SQLApplication:
    """Executes SQL statements against Snowflake and records results in history."""

    def __init__(
        self, execution_service, session_service, history_service, logging_service
    ):
        """Initialise with services for query execution, session access, history persistence, and logging."""
        self.execution_service = execution_service
        self.session_service = session_service
        self.history_service = history_service
        self.logging_service = logging_service

    def execute(
        self, sql: str, options: ExecutionOptions | None = None
    ) -> ExecutionReport:
        """Execute the given SQL statement and return a full ExecutionReport. Persists the result to history."""
        pass
