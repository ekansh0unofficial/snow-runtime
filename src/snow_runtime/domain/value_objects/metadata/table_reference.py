from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TableReference:
    """Identifies a table by its fully-qualified Snowflake path (database.schema.table)."""

    database: str
    schema: str
    table: str
