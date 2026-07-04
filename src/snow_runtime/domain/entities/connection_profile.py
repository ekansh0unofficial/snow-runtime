from dataclasses import dataclass

from .context import Context


@dataclass(eq=False, slots=True)
class ConnectionProfile:
    """Stores the credentials and named contexts for a Snowflake connection.

    contexts is the set of pre-defined execution environments (Context objects)
    that belong to this profile. default_context is the name of the context
    activated automatically when the profile is loaded; None means no default
    is set and the user must select a context explicitly.
    """

    name: str
    organization: str
    account: str
    username: str
    contexts: tuple[Context, ...]
    default_context: str | None

    def __post_init__(self):
        for field_name in ("name", "organization", "account", "username"):
            value = getattr(self, field_name)
            if not value or not value.strip():
                raise ValueError(f"{field_name} cannot be empty or whitespace")
