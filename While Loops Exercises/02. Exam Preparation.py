poor_grade = int(input())
problem = ""
total_score = 0
fails = 0
problem_count = 0
last_problem = ""
while fails < poor_grade:
    problem = input()
    if problem == "Enough":
        print(f"Average score: {(total_score / problem_count):.2f}")
        print(f"Number of problems: {problem_count}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    problem_count += 1
    total_score += grade
    last_problem = problem

    if grade <= 4:
        fails += 1
else:
    print(f"You need a break, {fails} poor grades.")
