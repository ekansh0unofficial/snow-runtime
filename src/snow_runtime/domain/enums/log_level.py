from enum import StrEnum


class LogLevel(StrEnum):
    """
    Defines the severity levels used for application logging output.

    INFO    — routine operational messages confirming expected behavior.
    WARNING — unexpected but non-fatal conditions that may require attention.
    ERROR   — failures that prevented a specific operation from completing.
    """
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
