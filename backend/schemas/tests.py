from typing import Optional
from pydantic import BaseModel


class Test(BaseModel):
    """
    Represents a test.

    Attributes:
        id (int): The ID of the test.
        name (str): The name of the test (Subida de rampa em 45°, Velocidade máxima com manobrabilidade, Tração)
        race_score (float): The race score of the test. It's defined by the race position.
        race_position (int): The race position of the test.
        value (float): The value of the test.
        value_description (str): The description of the test value. (Distância percorrida, Tempo feito, Peso retentor)
        penalty (Optional[float], optional): The penalty of the test. Defaults to None. This value is added to "value" attribute.
        penalty_description (Optional[str], optional): The description of the test penalty. Defaults to None. (Saída de pista)
        squad_id (int): The ID of the squad associated with the test.
    """

    id: int
    name: str
    race_score: float
    race_position: int
    value: float
    value_description: str
    penalty: Optional[float] = None
    penalty_description: Optional[str] = None
    squad_id: int
