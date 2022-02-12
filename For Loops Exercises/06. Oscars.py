actor = input()
starting_points = float(input())
examiners = int(input())
final_points = 0
total_points = 0

for number in range(0, examiners):
    examiner = input()
    #    print(f"Letters in {examiner} {len(examiner)}")
    points = float(input())
    final_points = (len(examiner) * points) / 2
    #    print(f"{examiner} gave: {final_points:.1f}")
    total_points += final_points
    if total_points + starting_points >= 1250.5:
        break
#   print(f"Total Points: {total_points:.1f}")


if total_points + starting_points < 1250.5:
    print(f"Sorry, {actor} you need {(1250.5 - total_points - starting_points):.1f} more!")
# print(f"{1250.5 - total_points - starting_points}")
else:
    print(f"Congratulations, {actor} got a nominee for leading role with {(total_points + starting_points):.1f}!")
