from crud import create_students
from schemas import Squad, SquadCreate
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
        sql = "INSERT INTO squads (name, car_name) VALUES (%s, %s) RETURNING *"
        cursor.execute(sql, (squad.name, squad.car_name))
        students = await create_students(squad.students, cursor.fetchone()["id"])
        return Squad(**cursor.fetchone(), students=students)
