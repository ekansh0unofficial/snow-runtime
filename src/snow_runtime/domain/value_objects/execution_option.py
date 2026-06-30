from dataclasses import dataclass

from snow_runtime.domain.enums import LogLevel, ExportFormat


@dataclass(frozen=True, slots=True)
class ExecutionOptions:
    """Controls runtime behavior for a script execution.
    timeout is in seconds; None means no limit is applied.
    rollback determines whether a failed execution triggers a full rollback
    of all statements executed within the same script.
    """

    timeout: int | None
    rollback: bool
    log_level: LogLevel
    export_format: ExportFormat | None
