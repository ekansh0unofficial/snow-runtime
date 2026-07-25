"""
    CRUD for a connection profile.
    Makes sure connection profile name is unique. 
    
    Manage contexts of a connection profile. (No specific context service -TBD)
    Also handles password related workflow using the secret_service. 

    Needs access to ConnectionProfile. Need access to Context. 

    It can raise : 
        Validation Errors : Wrong format for a connection Profile.
        InvalidState Errors : Profile already exists.
"""

from ..domain.entities.connection_profile import ConnectionProfile
from ..domain.entities.context import Context


class ConfigService():

    def __init__(self, config_provider, secret_service):
        self.config_provider = config_provider
        self.secret_service = secret_service
        

    def create_profile(self , name : str , organization : str , account : str , username: str , password : str | None = None) -> ConnectionProfile:
        """
            Creates a profile.
            Checks the validation by looking for same name in exisiting TOML
            Add the profile to TOML. 
            Also , handles password management using Secret Service. 
        """
        pass

    def get_profile(self, name : str ) -> ConnectionProfile:
        """
            Maps TOML to find profile. 

            Can raise ProfileNotFound error
            Does not return password
        """
        pass

    def list_profiles(self) -> list[ConnectionProfile]:
        """
            Returns entire TOML as list of connection profile.
            Can return None if TOML is empty.
        """    
        pass

    def get_context(self , profile_name : str , context_name : str) -> Context : 
        pass

    def list_context(self , profile_name : str) -> list[Context] : 
        pass

    def update_profile_password(self , name: str , old_password : str , new_password : str) :
        """
            Calls Secret_service to update password information of a profile
        """
        pass

    def update_profile_details(self , name: str , organization : str | None = None , account : str | None = None, username : str | None = None) -> ConnectionProfile:
        """
            Update login details of a user. If user updates something via Snowflake environment. How will it reflect here? 
            Does user update or will this function be triggered using a provider. snow sync command? 
        """
        pass

    def update_profile_name(self, name: str , new_name : str) : 
        pass

    def add_context(self , profile_name: str , context_name : str ,  database : str | None = None ,schema : str | None = None , warehouse : str | None = None, role : str | None = None ) -> Context: 
        pass

    def remove_context(self , profile_name : str , context_name : str)  : 
        pass

    def update_context(self , profile_name: str , context_name : str , database : str | None = None , schema : str | None = None , warehouse : str | None = None, role : str | None = None ) -> Context: 
        pass
    
    def delete_profile(self , profile_name : str) :
        """
            Remove profile from the TOML. 
            Delete password from the secret_service.
        """
        pass

    def set_active_profile(self , name : str):
        pass

    def get_active_profile(self) -> ConnectionProfile :
        pass

    def set_active_context(self , profile_name : str , context_name : str):
        pass

    def get_active_context(self , profile_name : str ):
        pass