vacation_cost = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
mignons = int(input())
trucks = int(input())

sales = puzzles + dolls + bears + mignons + trucks
commission = puzzles * 2.60 + dolls * 3 + bears * 4.10 + mignons * 8.20 + trucks * 2
profit = commission * 90 / 100    # -10% rent

#print(sales)
# if sales > 49:
#     profit *= 0.75
#     if vacation_cost <= profit:
#         print(f"Yes! {(profit - vacation_cost):.2f} lv left.")
#     else:
#         print(f"Not enough money! {(vacation_cost - profit):.2f} lv needed.")
# else:
#     if vacation_cost <= profit:
#         print(f"Yes! {(profit - vacation_cost):.2f} lv left.")
#     else:
#         print(f"Not enough money! {(vacation_cost - profit):.2f} lv needed.")


if sales > 49:
    profit *= 0.75
if vacation_cost > profit:
    print(f"Not enough money! {(vacation_cost - profit):.2f} lv needed.")
else:
    print(f"Yes! {(profit - vacation_cost):.2f} lv left.")


