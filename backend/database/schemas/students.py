from pydantic import BaseModel
from database.schemas import OptionalModel


class Student(BaseModel):
    """
    Represents a student.

    Attributes:
        id (int): The unique identifier of the student.
        nome (str): The name of the student.
        RA (int): The registration number of the student.
    """

    id: int
    nome: str
    RA: int


class StudentCreate(BaseModel):
    """
    Represents the schema for creating a new student.

    Attributes:
        name (str): The name of the student.
        RA (int): The RA (Registration Number) of the student.
    """

    nome: str
    RA: int


class StudentUpdate(StudentCreate, OptionalModel):
    """
    Represents a schema for updating a student.

    Attributes:
        Inherits all attributes from the `StudentCreate`, but all attributes are optional.
    """

    pass
