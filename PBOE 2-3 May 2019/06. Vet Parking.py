days = int(input())
hours = int(input())
fee = 0
grand_total = 0
for day in range(1, days + 1):
    cost = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            fee = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            fee = 1.25
        else:
            fee = 1
        cost += fee
    grand_total += cost
    print(f"Day: {day} - {cost:.2f} leva")

print(f"Total: {grand_total:.2f} leva")

"Day: {индексът на деня} – {общата сума за деня} leva"