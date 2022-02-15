season = input()
group = input()
students = int(input())
nights = int(input())
cost = 0
sport = ""

if season == "Winter":
    if group == "girls":
        cost = students * 9.60
        sport = "Gymnastics"
    elif group == "boys":
        cost = students * 9.60
        sport = "Judo"
    elif group == "mixed":
        cost = students * 10
        sport = "Ski"
elif season == "Spring":
    if group == "girls":
        cost = students * 7.20
        sport = "Athletics"
    elif group == "boys":
        cost = students * 7.20
        sport = "Tennis"
    elif group == "mixed":
        cost = students * 9.50
        sport = "Cycling"

elif season == "Summer":
    if group == "girls":
        cost = students * 15
        sport = "Volleyball"
    elif group == "boys":
        cost = students * 15
        sport = "Football"
    elif group == "mixed":
        cost = students * 20
        sport = "Swimming"

if students >= 50:
    cost *= 0.5
elif 20 <= students < 50:
    cost *= 0.85
elif 10 <= students < 20:
    cost *= 0.95
total = cost * nights
print(f"{sport} {total:.2f} lv.")