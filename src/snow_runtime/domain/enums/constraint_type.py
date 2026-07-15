from enum import StrEnum


class ConstraintType(StrEnum):
    """
    Classifies the type of constraint applied to a column or table in Snowflake.

    PRIMARY_KEY — uniquely identifies each row in the table; implies NOT NULL.
    FOREIGN_KEY — enforces a referential link to a primary key in another table.
    UNIQUE      — ensures all values in the column(s) are distinct.
    CHECK       — validates that column values satisfy a specified boolean expression.
    NOT_NULL    — disallows NULL values in the column.
    DEFAULT     — specifies a default value when no value is provided on insert.
    UNKNOWN     — constraint type could not be determined or is unsupported.
    """

    PRIMARY_KEY = "primary_key"
    FOREIGN_KEY = "foreign_key"
    UNIQUE = "unique"
    CHECK = "check"
    NOT_NULL = "not_null"
    DEFAULT = "default"
    UNKNOWN = "unknown"
