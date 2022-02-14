hrizantemi = int(input())
roses = int(input())
tulips = int(input())
season = (input())
holiday = (input())

flower_count = roses + tulips + hrizantemi
roses_count = roses
tulips_count = tulips

if season == "Spring" or season == "Summer":
    tulips *= 2.50
    hrizantemi *= 2
    roses *= 4.10
if season == "Autumn" or season == "Winter":
    tulips *= 4.15
    hrizantemi *= 3.75
    roses *= 4.50

total_cost = tulips + hrizantemi + roses

if season == "Spring" and tulips_count >= 7:
    total_cost *= 0.95
if season == "Winter" and roses_count >= 10:
    total_cost *= 0.9
if flower_count >= 20:
    total_cost *= 0.8
if holiday == "Y":
    total_cost *= 1.15
grand_total = total_cost + 2

print(f"{grand_total:.2f}")