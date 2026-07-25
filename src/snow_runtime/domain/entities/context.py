from dataclasses import dataclass

from ..exceptions.configuration_error import ConfigurationError


@dataclass(eq=False, slots=True)
class Context:
    """Represents a named, reusable Snowflake execution environment owned by a ConnectionProfile.

    All fields are required and must be non-empty strings. Authentication and
    connection details live in ConnectionProfile, not here.
    """

    name: str
    database: str | None = None
    schema: str | None = None
    warehouse: str | None = None
    role: str | None = None 

    def __post_init__(self):
        object.__setattr__(self, "name" , self.name.strip())
        if self.database is not None : object.__setattr__(self, "database" , self.database.strip())
        if self.warehouse is not None :  object.__setattr__(self, "warehouse" , self.warehouse.strip())
        if self.role is not None : object.__setattr__(self, "role" , self.role.strip())
         
        for field_name in ("name", "database", "schema", "warehouse", "role"):
            value = getattr(self, field_name)
            if not value or not value.strip():
                raise ConfigurationError(f"{field_name} cannot be empty or whitespace")
