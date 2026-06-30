from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Context:
    """Represents the active Snowflake execution environment for a session.

    All fields are optional; None means the session inherits the account default
    or the value set by a prior USE statement. Authentication and connection
    details live in ConnectionProfile, not here.
    """

    database: str | None
    schema: str | None
    warehouse: str | None
    role: str | None

    def __post_init__(self):
        for name in ("database", "schema", "warehouse", "role"):
            if getattr(self, name) is not None and getattr(self, name) == "":
                raise ValueError(f"{name} cannot be an empty string")


