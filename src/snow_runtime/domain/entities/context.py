from dataclasses import dataclass


@dataclass(eq=False, slots=True)
class Context:
    """Represents a named, reusable Snowflake execution environment owned by a ConnectionProfile.

    All fields are required and must be non-empty strings. Authentication and
    connection details live in ConnectionProfile, not here.
    """

    name: str
    database: str
    schema: str
    warehouse: str
    role: str

    def __post_init__(self):
        for field_name in ("name", "database", "schema", "warehouse", "role"):
            value = getattr(self, field_name)
            if not value or not value.strip():
                raise ValueError(f"{field_name} cannot be empty or whitespace")
