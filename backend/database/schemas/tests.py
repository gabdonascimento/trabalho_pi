from typing import Optional
from pydantic import BaseModel


class Test(BaseModel):
    """
    Represents a test.

    Attributes:
        id (int): The ID of the test.
        nome (str): The name of the test (Subida de rampa em 45°, Velocidade máxima com manobrabilidade, Tração)
        corrida_pontuacao (float): The race score of the test. It's defined by the race position.
        corrida_posicao (int): The race position of the test.
        valor (int): The value of the test.
        valor_descricao (str): The description of the test value. (Distância percorrida, Tempo feito, Peso retentor)
        penalidade (Optional[float], optional): The penalty of the test. Defaults to None. This value is added to "value" attribute.
        penalidade_descricao (Optional[str], optional): The description of the test penalty. Defaults to None. (Saída de pista)
        equipe (int): The ID of the squad associated with the test.
    """

    id: int
    nome: str
    corrida_pontuacao: float
    corrida_posicao: int
    valor: int
    valor_descricao: str
    penalidade: Optional[float] = None
    penalidade_descricao: Optional[str] = None
    equipe_id: int
