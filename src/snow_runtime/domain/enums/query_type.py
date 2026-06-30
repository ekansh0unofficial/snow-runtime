from enum import StrEnum


class QueryType(StrEnum):
    """Classifies a SQL statement by the category of operation it performs.

    DQL     — data query; SELECT statements that return a result set.
    DML     — data manipulation; INSERT, UPDATE, DELETE, MERGE.
    DDL     — data definition; CREATE, ALTER, DROP, TRUNCATE.
    DCL     — data control; GRANT, REVOKE.
    TCL     — transaction control; BEGIN, COMMIT, ROLLBACK.
    UTILITY — administrative or introspective statements; SHOW, DESCRIBE, EXPLAIN, USE.
    """

    DQL = "dql"
    DML = "dml"
    DDL = "ddl"
    DCL = "dcl"
    TCL = "tcl"
    UTILITY = "utility"
