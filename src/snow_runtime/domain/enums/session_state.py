from enum import StrEnum


class SessionState(StrEnum):
    """
    Represents the authentication and connection state of a Snowflake session.

    AUTHENTICATING  — a config has been loaded and the session is undergoing MFA/auth handshake.
    ACTIVE          — authentication succeeded; the session has live access to the runtime.
    EXPIRED         — the MFA token or session token has expired and must be renewed.
    DISCONNECTED    — no session is currently running on the runtime.
    ERROR           — an error occurred (e.g. incorrect MFA, network failure).
    """
    AUTHENTICATING = "authenticating"
    ACTIVE = "active"
    EXPIRED = "expired"
    DISCONNECTED = "disconnected"
    ERROR = "error"
