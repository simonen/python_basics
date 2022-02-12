turns = int(input())
points = 0
result = 0
count_one = 0
count_two = 0
count_three = 0
count_four = 0
count_five = 0
count_six = 0
for turn in range(0, turns):
    number = int(input())
    #print(f"Round #{turn}")
    if 0 <= number <= 9:
        points += number * 0.2
        count_one +=1
    elif 10 <= number <= 19:
        count_two += 1
        points += number * 0.3
    elif 20 <= number <= 29:
        count_three += 1
        points += number * 0.4
    elif 30 <= number <= 39:
        count_four += 1
        points += 50
    elif 40 <= number <= 50:
        count_five += 1
        points += 100
    else:
        count_six += 1
        points *= 0.5
    #result += points

    #print(f"Points: {points}")

print(f"{points:.2f}")
print(f"From 0 to 9: {count_one / turns * 100:.2f}%")
print(f"From 10 to 19: {count_two / turns * 100:.2f}%")
print(f"From 20 to 29: {count_three / turns * 100:.2f}%")
print(f"From 30 to 39: {count_four / turns * 100:.2f}%")
print(f"From 40 to 50: {count_five / turns * 100:.2f}%")
print(f"Invalid numbers: {count_six / turns * 100:.2f}%")
