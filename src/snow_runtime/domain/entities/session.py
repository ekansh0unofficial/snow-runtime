from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from ..enums import SessionState
from .context import Context


@dataclass(eq=False, slots=True)
class Session:
    """Represents an active or historical Snowflake session within the runtime.

    context holds the execution environment (database, schema, warehouse, role)
    active for this session; None when no context has been set yet.
    last_activity_at is updated on every command dispatch so idle sessions can
    be detected and expired.
    """

    session_id: UUID
    state: SessionState
    context: Context | None
    created_at: datetime
    last_activity_at: datetime
