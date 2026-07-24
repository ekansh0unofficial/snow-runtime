from typing import Optional


class ContextApplication:
    """Manages named Snowflake execution contexts (database, schema, warehouse, role combinations)."""

    def __init__(self, config_service):
        """Initialise with a config service used to persist and retrieve context definitions."""
        self.config_service = config_service

    def new_context(
        self,
        name: str,
        database: Optional[str],
        schema: Optional[str],
        warehouse: Optional[str],
        role: Optional[str],
    ):
        """Create a new named context. Any omitted Snowflake properties default to the account defaults."""
        pass

    def delete_context(self, name: str):
        """Permanently remove the named context."""
        pass

    def list_context(self):
        """Return all stored contexts."""
        pass

    def rename_context(self, name: str, new_name: str):
        """Rename a context while preserving its properties."""
        pass

    def edit_context(
        self,
        name: str,
        database: Optional[str],
        schema: Optional[str],
        role: Optional[str],
        warehouse: Optional[str],
    ):
        """Update one or more properties on an existing context. Only non-None arguments are applied."""
        pass

    def get_context(self, name: str):
        """Return the context with the given name."""
        pass

    # get current context is function of session
