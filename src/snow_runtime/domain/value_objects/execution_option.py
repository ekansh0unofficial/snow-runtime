from dataclasses import dataclass 
from snow_runtime.domain.enums import LogLevel, ExportFormat

@dataclass(frozen=True , slots=True)
class ExecutionOptions():
    timeout: int | None
    rollback : bool
    log_level : LogLevel
    export_format : ExportFormat 