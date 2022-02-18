from math import ceil

wall_height = int(input())
wall_width = int(input())
percent = int(input())  # percent
total = wall_width * wall_height * 4
total_area_to_paint = ceil(total - total * percent / 100)
paint = input()  # in square meters
while paint != "Tired!":
    liters = int(paint)
    total_area_to_paint -= liters
    if total_area_to_paint <= 0:
        break
    #total_area_to_paint -= int(paint)
    paint = input()
if total_area_to_paint == 0:
    print(f"All walls are painted! Great job, Pesho!")
elif total_area_to_paint > 0:
    print(f"{total_area_to_paint} quadratic m left.")
else:
    print(f"All walls are painted and you have {abs(total_area_to_paint)} l paint left!")
