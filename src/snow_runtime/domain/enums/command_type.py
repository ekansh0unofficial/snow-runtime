from enum import StrEnum


class CommandType(StrEnum):
    """
    Categorizes the top-level CLI commands available in the Snow Runtime application.

    RUNTIME     — manage the runtime lifecycle: start, stop, restart, status, logs, ls --session.
    CONFIG      — manage connection configs: add, edit, use, remove, ls.
    DATA        — query and inspect table data: preview, count, profile, stats, export.
    CONTEXT     — manage query contexts: set, use, save, show, ls.
    SQL         — execute SQL directly: sql "<str>", sql -f file.sql, sql --stdin.
    TRANSACTION — control transactions: begin, commit, rollback.
    METADATA    — inspect schema objects: ls, show, columns, constraints, deps, warehouse, role.
    EXPLORE     — interactive schema exploration: explore <table>, explore <db>, explore --web.
    HISTORY     — browse command history: history --session_id --context_name.
    DIAGNOSTIC  — run health checks: doctor.
    """
    RUNTIME = "runtime"
    CONFIG = "config"
    DATA = "data"
    CONTEXT = "context"
    SQL = "sql"
    TRANSACTION = "transaction"
    METADATA = "metadata"
    EXPLORE = "explore"
    HISTORY = "history"
    DIAGNOSTIC = "diagnostic"
