from schemas import StudentCreate
from dependencies import connection


async def create_student(student: StudentCreate):
    pass


async def create_students(students: list[StudentCreate], squad_id: int):
    """
    Create students.

    Args:
        students (list[StudentCreate]): The data required to create a list of students.

    Returns:
        Student: The created students.
    """
    with connection.cursor() as cursor:
        sql = "INSERT INTO students (name, age) VALUES (%s, %s) RETURNING *"

        data = [(student.name, student.age, squad_id) for student in students]
        cursor.executemany(sql, data)
        return cursor.fetchone()
