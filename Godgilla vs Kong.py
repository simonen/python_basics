budget = float(input())
extras = int(input())
costume_cost = float(input())

budget *= 0.9                   # 10% decor cost
expenses = extras * costume_cost

#print(f"{budget:.2f}")

# if extras > 150:
#     costume_cost *= 0.9
#     if budget < extras * costume_cost:
#         print("Not enough money!")
#         print(f"Wingard needs {(extras * costume_cost - budget):.2f} leva more.")
#     else:
#         print("Action!")
#         print(f"Wingard starts filming with {(budget - extras * costume_cost):.2f} leva left.")
# else:
#     if budget < extras * costume_cost:
#         print("Not enough money!")
#         print(f"Wingard needs {(extras * costume_cost - budget):.2f} leva more.")
#     else:
#         print("Action!")
#         print(f"Wingard starts filming with {(budget - extras * costume_cost):.2f} leva left.")

if extras > 150:
    costume_cost *= 0.9
if budget < extras * costume_cost:
    print("Not enough money!")
    print(f"Wingard needs {(extras * costume_cost - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget - extras * costume_cost):.2f} leva left.")