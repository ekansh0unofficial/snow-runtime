from snow_runtime.domain.enums import ExportFormat


class DataApplication:
    """Provides data inspection and export operations against Snowflake tables."""

    def __init__(
        self,
        execution_service,
        session_service,
        catalog_service,
        schema_service,
        export_service,
    ):
        """Initialise with services for query execution, session management, catalog lookup, schema resolution, and export."""
        self.execution_service = execution_service
        self.session_service = session_service
        self.catalog_service = catalog_service
        self.schema_service = schema_service
        self.export_service = export_service

    def preview(self, table: str, limit: int = 10):
        """Return the first `limit` rows from the given table."""
        pass

    def count(self, table: str):
        """Return the total row count for the given table."""
        pass

    def profile(self, table: str):
        """Return a column-level data profile (nulls, distinct counts, types) for the given table."""
        pass

    def stats(self, table: str):
        """Return summary statistics (min, max, mean, etc.) for numeric columns in the given table."""
        pass

    def export(self, query: str, export_format: ExportFormat, destination: str):
        """Execute the given SQL and write results to `destination` in the specified format."""
        pass
