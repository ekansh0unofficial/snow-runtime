from dataclasses import dataclass, field

from snow_runtime.domain.enums import ConstraintType, ReferentialAction
from snow_runtime.domain.value_objects.metadata.table_reference import TableReference


@dataclass(frozen=True, slots=True)
class Constraint:
    """Describes a table or column constraint, including foreign key details when applicable.

    For non-foreign-key types (PRIMARY_KEY, UNIQUE, CHECK, NOT_NULL, DEFAULT),
    the four FK fields are None. A FOREIGN_KEY constraint must supply
    referenced_table and referenced_columns at minimum; on_delete and on_update
    default to NO_ACTION when not specified by the schema.
    """

    name: str
    type: ConstraintType
    columns: tuple[str, ...]

    # FK-only fields — None for every other constraint type
    referenced_table: TableReference | None = field(default=None)
    referenced_columns: tuple[str, ...] | None = field(default=None)
    on_delete: ReferentialAction | None = field(default=None)
    on_update: ReferentialAction | None = field(default=None)
