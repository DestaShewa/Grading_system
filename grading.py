def calculate_result(math, english, science):

    total = math + english + science
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    status = "PASS" if average >= 50 else "FAIL"

    return total, average, grade, status