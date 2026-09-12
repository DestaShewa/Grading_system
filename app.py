from flask import Flask, render_template, request, redirect, url_for

from database import get_db, init_db
from grading import calculate_result


app = Flask(__name__)

init_db()


@app.route("/")
def dashboard():

    connection = get_db()

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    return render_template(
        "dashboard.html",
        students=students
    )


@app.route("/students")
def student_list():

    connection = get_db()

    students = connection.execute(
        "SELECT * FROM students ORDER BY name"
    ).fetchall()

    connection.close()

    return render_template(
        "students/list.html",
        students=students
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

        student_id = request.form["student_id"]
        name = request.form["name"]

        math = float(request.form["math"])
        english = float(request.form["english"])
        science = float(request.form["science"])

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