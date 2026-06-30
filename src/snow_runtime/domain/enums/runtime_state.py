from enum import StrEnum


class RuntimeState(StrEnum):
    """
    Represents the lifecycle state of the Snow Runtime environment.

    STARTING  — the runtime is initializing and attempting to connect to Snowflake.
    RUNNING   — connection is established and the runtime is actively communicating with Snowflake.
    STOPPING  — the runtime is in the process of safely disconnecting and shutting down.
    STOPPED   — default state; no active connection to Snowflake.
    ERROR     — an unrecoverable failure occurred during connection or operation.
    """
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    ERROR = "error"
