from flask import Flask, render_template, request, redirect, url_for, flash

from database import get_db, init_db
from grading import calculate_result


app = Flask(__name__)

app.secret_key = "grading-system-secret-key"

init_db()


@app.route("/")
def dashboard():

    connection = get_db()

    # Total students
    total_students = connection.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    # Average of all students
    overall_average = connection.execute(
        "SELECT AVG(average) FROM students"
    ).fetchone()[0]

    # Number of passed students
    passed_students = connection.execute(
        "SELECT COUNT(*) FROM students WHERE status = 'PASS'"
    ).fetchone()[0]

    # Number of failed students
    failed_students = connection.execute(
        "SELECT COUNT(*) FROM students WHERE status = 'FAIL'"
    ).fetchone()[0]

    # Recent students
    recent_students = connection.execute("""
        SELECT *
        FROM students
        ORDER BY id DESC
        LIMIT 5
    """).fetchall()

    connection.close()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        overall_average=overall_average,
        passed_students=passed_students,
        failed_students=failed_students,
        recent_students=recent_students
    )

@app.route("/students")
def student_list():

    search = request.args.get("search", "")
    status = request.args.get("status", "")

    connection = get_db()

    query = "SELECT * FROM students WHERE 1=1"
    parameters = []

    # Search by student ID or name
    if search:
        query += " AND (student_id LIKE ? OR name LIKE ?)"
        parameters.append(f"%{search}%")
        parameters.append(f"%{search}%")

    # Filter by status
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
@app.route("/students/<int:id>")
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

@app.route("/students/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student_id = request.form.get("student_id", "").strip()
        name = request.form.get("name", "").strip()

        # Check required fields
        if not student_id or not name:
            flash("Student ID and name are required.")
            return redirect(url_for("add_student"))

        try:
            math = float(request.form["math"])
            english = float(request.form["english"])
            science = float(request.form["science"])

        except (ValueError, KeyError):
            flash("Marks must be valid numbers.")
            return redirect(url_for("add_student"))

        # Validate marks
        marks = [math, english, science]

        if any(mark < 0 or mark > 100 for mark in marks):
            flash("Marks must be between 0 and 100.")
            return redirect(url_for("add_student"))

        # Calculate result
        total, average, grade, status = calculate_result(
            math,
            english,
            science
        )

        connection = get_db()

        # Check duplicate student ID
        existing_student = connection.execute(
            "SELECT id FROM students WHERE student_id = ?",
            (student_id,)
        ).fetchone()

        if existing_student:
            connection.close()
            flash("Student ID already exists.")
            return redirect(url_for("add_student"))

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

        return redirect(url_for("student_list"))

    return render_template("students/add.html")

@app.route("/students/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    connection = get_db()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    if request.method == "POST":

        name = request.form["name"]
        math = float(request.form["math"])
        english = float(request.form["english"])
        science = float(request.form["science"])

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

        return redirect(url_for("student_list"))

    connection.close()

    return render_template(
        "students/edit.html",
        student=student
    )
@app.route("/students/delete/<int:id>")
def delete_student(id):

    connection = get_db()

    connection.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("student_list"))


if __name__ == "__main__":
    app.run(debug=True)