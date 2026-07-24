class ExploreApplication:
    """Browse the Snowflake object hierarchy: databases, schemas, tables, and column definitions."""

    def __init__(self, catalog_service, schema_service, session_service):
        """Initialise with services for catalog browsing, schema resolution, and session access."""
        self.catalog_service = catalog_service
        self.schema_service = schema_service
        self.session_service = session_service

    def databases(self):
        """Return all databases visible to the active session."""
        pass

    def schemas(self, database: str):
        """Return all schemas within the given database."""
        pass

    def tables(self, database: str, schema: str):
        """Return all tables and views within the given database and schema."""
        pass

    def describe(self, database: str, schema: str, table: str):
        """Return the column definitions and constraints for the given table."""
        pass
