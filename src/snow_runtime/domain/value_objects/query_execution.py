from dataclasses import dataclass

from snow_runtime.domain.value_objects.query import Query


@dataclass(frozen=True, slots=True)
class QueryExecution:
    """Records the outcome of executing a single Query.

    rows holds the result set for DQL statements as a sequence of column-name-
    to-value mappings. For DML/DDL/TCL/UTILITY it is None; use affected_rows
    for row-count feedback instead.

    duration is wall-clock time in milliseconds from statement dispatch to
    first-row-received (DQL) or completion (all other types).
    """

    query: Query
    success: bool
    duration_ms: int
    affected_rows: int | None
    rows: tuple[dict[str, object], ...] | None
    message: str | None
