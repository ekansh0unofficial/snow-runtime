from dataclasses import dataclass

from snow_runtime.domain.value_objects.query import Query


@dataclass(frozen=True, slots=True)
class SqlScript:
    """The primary execution unit; wraps one or more Query objects.

    A single SQL statement is represented as a script containing exactly one
    query. This removes the distinction between single-query and batch execution
    so all execution paths follow the same workflow.
    """

    queries: tuple[Query, ...]
