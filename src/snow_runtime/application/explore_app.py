class ExploreApplication:
    def __init__(self, catalog_service, schema_service, session_service):
        self.catalog_service = catalog_service
        self.schema_service = schema_service
        self.session_service = session_service

    def databases(self):
        pass

    def schemas(self, database: str):
        pass

    def tables(self, database: str, schema: str):
        pass

    def describe(self, database: str, schema: str, table: str):
        pass
