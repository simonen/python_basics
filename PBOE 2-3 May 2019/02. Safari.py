budget = float(input())
fuel_liters = float(input())
week_day = input()

cost = fuel_liters * 2.1 + 100

if week_day == "Saturday":
    cost *= 0.9
elif week_day == "Sunday":
    cost *= 0.8

difference = abs(budget - cost)

if budget >= cost:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")