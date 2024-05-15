from typing import Optional
from pydantic import BaseModel
from database.schemas import OptionalModel, Student, StudentCreate


class Squad(BaseModel):
    """
    Represents a squad in the race.

    Attributes:
        id (int): The ID of the squad.
        nome (str): The name of the squad.
        nota (float): The grade of the squad.
        carro_id (str): The id of the car used by the squad.
    """

    id: Optional[int]
    nome: Optional[str]
    nota: Optional[float]
    carro_id: Optional[str]

    estudantes: Optional[list[Student]]


class SquadCreate(BaseModel):
    """
    Represents the data required to create a new squad.

    Attributes:
        name (str): The name of the squad.
        carro_id (str): The name of the id used by the squad.
        estudantes (Optional[list[StudentCreate]]): The list of students in the squad. This attribute is optional.
    """

    name: str
    carro_id: str

    estudantes: Optional[list[StudentCreate]]


class SquadUpdate(SquadCreate, OptionalModel):
    """
    Represents the schema for updating a squad.

    Inherits from `SquadCreate` and `OptionalModel`.
    """

    pass
