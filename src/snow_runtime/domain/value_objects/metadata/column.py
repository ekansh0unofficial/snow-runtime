from dataclasses import dataclass

from snow_runtime.domain.enums import DataType


@dataclass(frozen=True, slots=True)
class Column:
    """Describes a single column within a Snowflake table.

    default_value is stored as a string representation of the SQL default
    expression, or None when no default is defined.
    """

    name: str
    data_type: DataType
    nullable: bool
    default_value: str | None
