from typing import Optional


class ConfigApplication:
    def __init__(self, config_service, secret_service):
        self.config_service = config_service
        self.secret_service = secret_service

    def create_profile(self, name, organisation, account, username, password):
        pass

    def update_profile(
        self,
        name: str,
        organisation: Optional[str],
        account: Optional[str],
        username: Optional[str],
        password: Optional[str],
    ):
        pass

    def delete_profile(self, name: str):
        pass

    def rename_profile(self, name: str, new_name: str):
        pass

    def get_current_profile(self):
        pass

    def use_profile(self, name: str):
        pass

    def list_profiles(self):
        pass

    def get_config(self, name: str):
        pass
