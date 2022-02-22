maiden_party_cost = float(input())
love_letters = int(input())
wax_roses = int(input())
keyholders = int(input())
caricatures = int(input())
charms = int(input())

items_ordered = love_letters + wax_roses + keyholders + caricatures + charms
total_income = love_letters * 0.6 + wax_roses * 7.20 + keyholders * 3.60 + caricatures * 18.20 + charms * 22

if items_ordered >= 25:
    total_income *= 0.65  # 35% discount

difference = abs(maiden_party_cost - total_income * 0.9)

if maiden_party_cost <= total_income:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
