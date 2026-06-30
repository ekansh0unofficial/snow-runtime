from dataclasses import dataclass

from snow_runtime.domain.value_objects.query_execution import QueryExecution


@dataclass(frozen=True, slots=True)
class ExecutionReport:
    """Aggregates the results of all queries executed within a single SqlScript.

    total_duration_ms is the wall-clock time for the entire script, which may
    be less than the sum of per-query durations due to network overlap.
    rolled_back is True when a failure triggered a rollback under the
    ExecutionOptions.rollback policy, False otherwise.
    """

    executions: tuple[QueryExecution, ...]
    total_duration_ms: int
    rolled_back: bool

    def __post_init__(self):
        if len(self.executions) == 0:
            raise ValueError("executions cannot be empty")
        if self.total_duration_ms < 0:
            raise ValueError("total_duration_ms cannot be negative")

    @property
    def success(self) -> bool:
        """True only when every query in the script completed successfully."""
        return all(e.success for e in self.executions)
