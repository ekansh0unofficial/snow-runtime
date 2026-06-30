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

    def __post_init__(self):
        if self.name == "":
            raise ValueError("name cannot be an empty string")
        if self.default_value is not None and self.default_value == "":
            raise ValueError("default_value cannot be an empty string")
