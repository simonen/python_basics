budget = float(input())
season = input()
car_class = ""
cabrio = 0
jeep = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        cabrio = budget * 0.35
    elif season == "Winter":
        jeep = budget * 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        cabrio = budget * 0.45
    elif season == "Winter":
        jeep = budget * 0.8
else:
    car_class = "Luxury class"
    jeep = budget * 0.9

print(f"{car_class}")
if season == "Summer" and budget <= 500:
    print(f"Cabrio - {cabrio:.2f}")
else:
    print(f"Jeep - {jeep:.2f}")
