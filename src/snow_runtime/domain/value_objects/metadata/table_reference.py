from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TableReference:
    """Identifies a table by its fully-qualified Snowflake path (database.schema.table)."""

    database: str
    schema: str
    table: str

    def __post_init__(self):
        for field_name in ("database", "schema", "table"):
            value = getattr(self, field_name)
            if not value or not value.strip():
                raise ValueError(f"{field_name} cannot be empty or whitespace")
