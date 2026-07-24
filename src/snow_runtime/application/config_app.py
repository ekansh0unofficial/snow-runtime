from typing import Optional


class ConfigApplication:
    """Manages connection profiles and runtime configuration. Entry point for all profile CRUD operations."""

    def __init__(self, config_service, secret_service):
        """Initialise with a config service for profile storage and a secret service for credential management."""
        self.config_service = config_service
        self.secret_service = secret_service

    def create_profile(self, name, organization, account, username, password):
        """Create and persist a new connection profile with the given Snowflake credentials."""
        pass

    def update_profile(
        self,
        name: str,
        organization: Optional[str],
        account: Optional[str],
        username: Optional[str],
        password: Optional[str],
    ):
        """Update one or more fields on an existing profile. Only non-None arguments are applied."""
        pass

    def delete_profile(self, name: str):
        """Permanently remove the named profile and its associated credentials."""
        pass

    def rename_profile(self, name: str, new_name: str):
        """Rename a profile while preserving all its stored credentials."""
        pass

    def get_current_profile(self):
        """Return the profile currently marked as active."""
        pass

    def use_profile(self, name: str):
        """Set the named profile as the active profile for subsequent operations."""
        pass

    def list_profiles(self):
        """Return all stored connection profiles."""
        pass

    def get_config(self, name: str):
        """Return the full configuration for the named profile."""
        pass
