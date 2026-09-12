students = []


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def calculate_status(average):
    return "PASS" if average >= 50 else "FAIL"


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"{subject} mark: "))

            if 0 <= mark <= 100:
                return mark

            print("Mark must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def create_student():
    name = input("Student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Student name: ").strip()

    math = get_mark("Math")
    english = get_mark("English")
    science = get_mark("Science")

    total = math + english + science
    average = total / 3

    student = {
        "name": name,
        "math": math,
        "english": english,
        "science": science,
        "total": total,
        "average": average,
        "grade": calculate_grade(average),
        "status": calculate_status(average)
    }

    students.append(student)

    print("Student added successfully.")


def show_student(student):
    print("\n-----------------------------")
    print("Name:", student["name"])
    print("Math:", student["math"])
    print("English:", student["english"])
    print("Science:", student["science"])
    print("Total:", student["total"])
    print("Average:", round(student["average"], 2))
    print("Grade:", student["grade"])
    print("Status:", student["status"])
    print("-----------------------------")


def show_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        show_student(student)


def search_student():
    name = input("Enter student name: ").strip().lower()

    found = False

    for student in students:
        if name in student["name"].lower():
            show_student(student)
            found = True

    if not found:
        print("Student not found.")


def edit_student():
    name = input("Enter student name to edit: ").strip().lower()

    for student in students:

        if student["name"].lower() == name:

            print("\nEnter new marks:")

            student["math"] = get_mark("Math")
            student["english"] = get_mark("English")
            student["science"] = get_mark("Science")

            student["total"] = (
                student["math"]
                + student["english"]
                + student["science"]
            )

            student["average"] = student["total"] / 3

            student["grade"] = calculate_grade(
                student["average"]
            )

            student["status"] = calculate_status(
                student["average"]
            )

            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ").strip().lower()

    for student in students:

        if student["name"].lower() == name:

            students.remove(student)

            print("Student deleted successfully.")
            return

    print("Student not found.")


while True:

    print("\n==============================")
    print("       GRADING SYSTEM")
    print("==============================")
    print("1. Add student")
    print("2. Show students")
    print("3. Search student")
    print("4. Edit student")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        edit_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")