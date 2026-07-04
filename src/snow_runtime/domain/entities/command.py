from dataclasses import dataclass
from abc import ABC, abstractmethod
from uuid import UUID


@dataclass(frozen=True, slots=True)
class Command(ABC):
    """Base class for all CLI commands dispatched to the runtime.

    Subclasses represent specific command types (e.g. RuntimeCommand, SqlCommand)
    and must declare their human-readable command_name. command_id uniquely
    identifies a single invocation for history and correlation purposes.
    """

    command_id: UUID

    @property
    @abstractmethod
    def command_name(self) -> str:
        """Human-readable name of the command (e.g. 'runtime start')."""