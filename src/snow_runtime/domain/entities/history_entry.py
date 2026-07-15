from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import UUID

from .command import Command


@dataclass(frozen=True, slots=True)
class HistoryEntry:
    """Immutable record of a single command execution stored in the history log.

    duration is a convenience field; it equals completed_at - started_at.
    success is True when the command completed without error.
    profile_name and context_name are snapshot strings so the record remains
    meaningful even if the originating profile or context is later renamed.
    """

    entry_id: UUID
    command: Command
    success: bool
    started_at: datetime
    completed_at: datetime
    duration: timedelta
    profile_name: str
    session_id: UUID
    context_name: str
