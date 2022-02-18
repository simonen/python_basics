budget = float(input())
night_count = int(input())
price_per_night = float(input())
additional_cost = int(input())

if night_count > 7:
    price_per_night *= 0.95

cost = night_count * price_per_night
total = cost + budget * additional_cost / 100
difference = abs(budget - total)

if budget >= total:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
