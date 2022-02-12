length = int(input())
width = int(input())
height = int(input())
# cm3 / 1000 = dm3 = liters
tank_volume = (length * width * height) / 1000

sand = float(input()) * tank_volume / 100
water_volume = tank_volume - sand

print(water_volume)