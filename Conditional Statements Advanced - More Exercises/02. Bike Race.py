junior_bikers = int(input())
senior_bikers = int(input())
road_type = input()
money_total = 0

if road_type == "trail":
    money_total = junior_bikers * 5.50 + senior_bikers * 7
if road_type == "cross-country":
    money_total = senior_bikers * 9.50 + junior_bikers * 8
    if senior_bikers + junior_bikers >= 50:
        money_total *= 0.75
if road_type == "downhill":
    money_total = senior_bikers * 13.75 + junior_bikers * 12.25
if road_type == "road":
    money_total = senior_bikers * 21.50 + junior_bikers * 20

money_total *= 0.95

print(f"{money_total:.2f}")
