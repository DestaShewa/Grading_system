from database import get_db
from grading import calculate_result


def get_all_students():
    connection = get_db()

    students = connection.execute("""
        SELECT *
        FROM students
        ORDER BY name
    """).fetchall()

    connection.close()

    return students


def get_student(student_id):
    connection = get_db()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    connection.close()

    return student


def search_students(search="", status=""):

    connection = get_db()

    query = "SELECT * FROM students WHERE 1=1"
    parameters = []

    if search:
        query += """
            AND (student_id LIKE ? OR name LIKE ?)
        """

        parameters.append(f"%{search}%")
        parameters.append(f"%{search}%")

    if status:
        query += " AND status = ?"
        parameters.append(status)

    query += " ORDER BY name"

    students = connection.execute(
        query,
        parameters
    ).fetchall()

    connection.close()

    return students


def create_student(student_id, name, math, english, science):

    total, average, grade, status = calculate_result(
        math,
        english,
        science
    )

    connection = get_db()

    connection.execute("""
        INSERT INTO students (
            student_id,
            name,
            math,
            english,
            science,
            total,
            average,
            grade,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student_id,
        name,
        math,
        english,
        science,
        total,
        average,
        grade,
        status
    ))

    connection.commit()
    connection.close()