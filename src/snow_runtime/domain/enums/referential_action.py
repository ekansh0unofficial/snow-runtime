from enum import StrEnum


class ReferentialAction(StrEnum):
    """
    Defines the referential integrity action taken on dependent rows when a
    referenced row is updated or deleted in a foreign key relationship.

    NO_ACTION   — no action is taken; constraint violation raises an error (default SQL behavior).
    RESTRICT    — prevents the update/delete if dependent rows exist.
    CASCADE     — propagates the update/delete to all dependent rows.
    SET_NULL    — sets the foreign key column(s) in dependent rows to NULL.
    SET_DEFAULT — sets the foreign key column(s) in dependent rows to their default value.
    """
    NO_ACTION = "no_action"
    RESTRICT = "restrict"
    CASCADE = "cascade"
    SET_NULL = "set_null"
    SET_DEFAULT = "set_default"
