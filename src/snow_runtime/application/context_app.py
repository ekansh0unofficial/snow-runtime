from typing import Optional


class ContextApplication:
    def __init__(self, config_service):
        self.config_service = config_service

    def new_context(
        self,
        name: str,
        database: Optional[str],
        schema: Optional[str],
        warehouse: Optional[str],
        role: Optional[str],
    ):
        pass

    def delete_context(self, name: str):
        pass

    def list_context(self):
        pass

    def rename_context(self, name: str, new_name: str):
        pass

    def edit_context(
        self,
        name: str,
        database: Optional[str],
        schema: Optional[str],
        role: Optional[str],
        warehouse: Optional[str],
    ):
        pass

    def get_context(self, name: str):
        pass

    # get current context is function of session
