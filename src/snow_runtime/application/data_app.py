from snow_runtime.domain.enums import ExportFormat


class DataApplication:
    def __init__(
        self,
        execution_service,
        session_service,
        catalog_service,
        schema_service,
        export_service,
    ):
        self.execution_service = execution_service
        self.session_service = session_service
        self.catalog_service = catalog_service
        self.schema_service = schema_service
        self.export_service = export_service

    def preview(self, table: str, limit: int = 10):
        pass

    def count(self, table: str):
        pass

    def profile(self, table: str):
        pass

    def stats(self, table: str):
        pass

    def export(self, query: str, format: ExportFormat, destination: str):
        pass
