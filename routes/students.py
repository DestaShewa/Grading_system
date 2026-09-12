from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from database import get_db
from grading import calculate_result


students_bp = Blueprint(
    "students",
    __name__,
    url_prefix="/students"
)


@students_bp.route("")
def student_list():

    search = request.args.get("search", "")
    status = request.args.get("status", "")

    connection = get_db()

    query = "SELECT * FROM students WHERE 1=1"
    parameters = []

    if search:
        query += " AND (student_id LIKE ? OR name LIKE ?)"
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

    return render_template(
        "students/list.html",
        students=students,
        search=search,
        status=status
    )


@students_bp.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student_id = request.form.get("student_id", "").strip()
        name = request.form.get("name", "").strip()

        if not student_id or not name:
            flash("Student ID and name are required.")
            return redirect(url_for("students.add_student"))

        try:
            math = float(request.form["math"])
            english = float(request.form["english"])
            science = float(request.form["science"])

        except (ValueError, KeyError):
            flash("Marks must be valid numbers.")
            return redirect(url_for("students.add_student"))

        marks = [math, english, science]

        if any(mark < 0 or mark > 100 for mark in marks):
            flash("Marks must be between 0 and 100.")
            return redirect(url_for("students.add_student"))

        connection = get_db()

        existing = connection.execute(
            "SELECT id FROM students WHERE student_id = ?",
            (student_id,)
        ).fetchone()

        if existing:
            connection.close()
            flash("Student ID already exists.")
            return redirect(url_for("students.add_student"))

        total, average, grade, status = calculate_result(
            math,
            english,
            science
        )

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

        flash("Student added successfully.")

        return redirect(url_for("students.student_list"))

    return render_template("students/add.html")


@students_bp.route("/<int:id>")
def student_result(id):

    connection = get_db()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    connection.close()

    if student is None:
        return "Student not found", 404

    return render_template(
        "students/result.html",
        student=student
    )


@students_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    connection = get_db()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    if student is None:
        connection.close()
        return "Student not found", 404

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        try:
            math = float(request.form["math"])
            english = float(request.form["english"])
            science = float(request.form["science"])

        except (ValueError, KeyError):
            connection.close()
            flash("Marks must be valid numbers.")
            return redirect(url_for("students.edit_student", id=id))

        marks = [math, english, science]

        if any(mark < 0 or mark > 100 for mark in marks):
            connection.close()
            flash("Marks must be between 0 and 100.")
            return redirect(url_for("students.edit_student", id=id))

        total, average, grade, status = calculate_result(
            math,
            english,
            science
        )

        connection.execute("""
            UPDATE students
            SET name = ?,
                math = ?,
                english = ?,
                science = ?,
                total = ?,
                average = ?,
                grade = ?,
                status = ?
            WHERE id = ?
        """, (
            name,
            math,
            english,
            science,
            total,
            average,
            grade,
            status,
            id
        ))

        connection.commit()
        connection.close()

        flash("Student updated successfully.")

        return redirect(url_for("students.student_list"))

    connection.close()

    return render_template(
        "students/edit.html",
        student=student
    )


@students_bp.route("/delete/<int:id>")
def delete_student(id):

    connection = get_db()

    connection.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    connection.commit()
    connection.close()

    flash("Student deleted successfully.")

    return redirect(url_for("students.student_list"))