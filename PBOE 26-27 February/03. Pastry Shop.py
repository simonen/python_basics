cake_type = input()
cake_ordered = int(input())
day = int(input())

order = 0
cake_cost = 0

if day <= 15:
    if cake_type == "Cake":
        cake_cost = 24
    elif cake_type == "Souffle":
        cake_cost = 6.66
    elif cake_type == "Baklava":
        cake_cost = 12.60
elif day > 15:
    if cake_type == "Cake":
        cake_cost = 28.70
    elif cake_type == "Souffle":
        cake_cost = 9.80
    elif cake_type == "Baklava":
        cake_cost = 16.98

cost = cake_ordered * cake_cost


if day <= 22:
    if 100 <= cost <= 200:
        cost *= 0.85
    if cost > 200:
        cost *= 0.75
if day <= 15:
    cost *= 0.9

print(f"{cost:.2f}")