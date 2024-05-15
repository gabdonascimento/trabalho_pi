from database.crud import create_students
from database.schemas import Squad, SquadCreate
from dependencies import connection


async def create_squad(squad: SquadCreate):
    """
    Create a new squad.

    Args:
        squad (SquadCreate): The data required to create a new squad.

    Returns:
        Squad: The created squad.
    """
    with connection.cursor() as cursor:
        sql = "INSERT INTO squads (nome, carro_id) VALUES (%s, %s) RETURNING *"
        cursor.execute(sql, (squad.nome, squad.carro_id))
        students = await create_students(squad.estudantes, cursor.fetchone()["id"])
        return Squad(**cursor.fetchone(), students=students)
