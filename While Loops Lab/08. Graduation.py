name = input()
year = 1
total_grade = 0
fail = 0
while year <= 12:
    if fail > 1:
        print(f"{name} has been excluded at {year} grade")
        break
    grade = float(input())
    if grade < 4.00:
        fail += 1
    elif grade >= 4:
        total_grade += grade
        if year == 12:
            print(f"{name} graduated. Average grade: {(total_grade / year):.2f}")
            break
        year += 1

