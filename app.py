from flask import Flask, render_template

from database import get_db, init_db
from routes.students import students_bp


app = Flask(__name__)

app.secret_key = "grading-system-secret-key"

init_db()

app.register_blueprint(students_bp)


@app.route("/")
def dashboard():

    connection = get_db()

    total_students = connection.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    overall_average = connection.execute(
        "SELECT AVG(average) FROM students"
    ).fetchone()[0]

    passed_students = connection.execute(
        "SELECT COUNT(*) FROM students WHERE status = 'PASS'"
    ).fetchone()[0]

    failed_students = connection.execute(
        "SELECT COUNT(*) FROM students WHERE status = 'FAIL'"
    ).fetchone()[0]

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


if __name__ == "__main__":
    app.run(debug=True)