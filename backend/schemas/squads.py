from typing import Optional
from pydantic import BaseModel
from backend.schemas.students import StudentCreate
from schemas import OptionalModel, Student


class Squad(BaseModel):
    """
    Represents a squad in the race.

    Attributes:
        id (int): The ID of the squad.
        name (str): The name of the squad.
        grade (float): The grade of the squad.
        car_name (str): The name of the car used by the squad.
    """

    id: Optional[int]
    name: Optional[str]
    grade: Optional[float]
    car_name: Optional[str]

    # subresource
    students: Optional[list[Student]]


class SquadCreate(BaseModel):
    """
    Represents the data required to create a new squad.

    Attributes:
        name (str): The name of the squad.
        car_name (str): The name of the car used by the squad.
        students (Optional[list[StudentCreate]]): The list of students in the squad. This attribute is optional.
    """

    name: str
    car_name: str

    # subresource
    students: Optional[list[StudentCreate]]


class SquadUpdate(SquadCreate, OptionalModel):
    """
    Represents the schema for updating a squad.

    Inherits from `SquadCreate` and `OptionalModel`.
    """

    pass
