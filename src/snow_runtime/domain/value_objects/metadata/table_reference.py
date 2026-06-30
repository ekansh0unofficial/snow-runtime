from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TableReference:
    """Identifies a table by its fully-qualified Snowflake path (database.schema.table)."""

    database: str
    schema: str
    table: str

    def __post_init__(self):
        for name in ("database", "schema", "table"):
            if getattr(self, name) == "":
                raise ValueError(f"{name} cannot be an empty string")
