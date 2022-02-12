foil = int(input()) * 15 / 10 + 30 / 10
paint = int(input()) * 11 * 145 / 100
diluent = int(input()) * 5
hours = int(input())
bags = 0.4

materials = foil + paint + diluent + bags

maistori = (materials * 30 / 100) * hours

total_sum = materials + maistori

print(foil)
print(paint)
print(diluent)
print(hours)
print(bags)
print(maistori)

print(total_sum)

