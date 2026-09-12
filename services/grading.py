def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if not marks:
        return 0

    return calculate_total(marks) / len(marks)


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