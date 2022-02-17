budget = float(input())
extras = int(input())
costume_cost = float(input())  # per extra

set_design = budget * 0.1

if extras > 150:
    costume_cost *= 0.9

total = extras * costume_cost + set_design
difference = abs(budget - total)
if budget >= total:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")