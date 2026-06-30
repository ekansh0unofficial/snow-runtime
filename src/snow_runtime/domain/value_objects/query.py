from dataclasses import dataclass

from snow_runtime.domain.enums import QueryType


@dataclass(frozen=True, slots=True)
class Query:
    """A single SQL statement paired with its classified operation type.

    Query has no knowledge of where the SQL came from (CLI, file, SDK).
    Classification is performed by QueryParser, not by this object.
    """

    sql: str
    query_type: QueryType
