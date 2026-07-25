from dataclasses import dataclass

from snow_runtime.domain.enums import DataType

from ...exceptions.validation_error import ValidationError


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
        if not self.name or not self.name.strip():
            raise ValidationError("name cannot be empty or whitespace")
        if self.default_value == "":
            raise ValidationError("default_value cannot be an empty string")
