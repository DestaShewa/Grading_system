name = input("Student name: ")

math = float(input("Math: "))
english = float(input("English: "))
science = float(input("Science: "))

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

if average >= 50:
    status = "PASS"
else:
    status = "FAIL"

print("\n===== RESULT =====")
print("Student:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("Status:", status)