from dataclasses import dataclass

@dataclass(forzen=True , slots=True)
class Context():
    database : str | None
    schema : str  | None
    warehouse : str | None
    role : str | None
    