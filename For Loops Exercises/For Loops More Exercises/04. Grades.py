students = int(input())

top_grade = 0
good_grade = 0
average_grade = 0
failed_grade = 0
grade_sum = 0

top_students = 0
good_students = 0
average_students = 0
failed_students = 0

for student in range(0, students):
    grade = float(input())
    if grade >= 5.00:
        top_grade += grade
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        good_grade += grade
        good_students += 1
    elif 3.00 <= grade <= 3.99:
        average_grade += grade
        average_students += 1
    elif grade < 3:
        failed_students += 1
        failed_grade += grade
    grade_sum += grade

average_grades = grade_sum / students
print(f"Top students: {(top_students / students * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(good_students / students * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(average_students / students * 100):.2f}%")
print(f"Fail: {(failed_students / students * 100):.2f}%")
print(f"Average: {average_grades:.2f}")

print(f"Top students: {(top_grade / grade_sum * 100):.2f}%")