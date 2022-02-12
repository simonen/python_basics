flower = input()  # Roses, Dahlias, Tulips, Narcissus или Gladiolus;
flower_count = int(input())
budget = int(input())
cost = 0
is_flower_valid = 1
is_budget_enough = 1
if flower == "Roses":
    cost = flower_count * 5
    if flower_count > 80:
        cost = flower_count * 5 * 0.9
elif flower == "Dahlias":
    cost = flower_count * 3.80
    if flower_count > 90:
        cost = flower_count * 3.80 * 0.85
elif flower == "Tulips":
    cost = flower_count * 2.80
    if flower_count > 80:
        cost = flower_count * 2.80 * 0.85
elif flower == "Narcissus":
    cost = flower_count * 3
    if 0 <= flower_count < 120:
        cost = flower_count * 3 * 1.15
elif flower == "Gladiolus":
    cost = flower_count * 2.50
    if 0 <= flower_count < 80:
        cost = flower_count * 2.50 * 1.2
else:
    is_flower_valid = 0  # same as cost == 0 (original value) hence the entire if-statement is false => no flowers from the list

difference = budget - cost

if is_flower_valid == 0:
    print("Error")
elif difference >= 0:
    print(f"Hey, you have a great garden with {flower_count} {flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {(cost - budget):.2f} leva more.")
