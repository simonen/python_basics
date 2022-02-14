budget = float(input())
season = input()
accommodation = ""
destination = ""
cost = 0
if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        destination = "Alaska"
        cost = budget * 0.65
    elif season == "Winter":
        destination = "Morocco"
        cost = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        destination = "Alaska"
        cost = budget * 0.80
    elif season == "Winter":
        destination = "Morocco"
        cost = budget * 0.60
else:
    accommodation = "Hotel"
    cost = budget * 0.90
    if season == "Summer":
        destination = "Alaska"
    elif season == "Winter":
        destination = "Morocco"

print(f"{destination} - {accommodation} - {cost:.2f}")