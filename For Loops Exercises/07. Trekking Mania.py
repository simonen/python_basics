group_count = int(input())

group_musala = 0
group_two = 0
group_three = 0
group_four = 0
group_five = 0

total_climbers = 0

for group in range(0, group_count):
    climbers = int(input())
  #  print(f"group #: {group} has {climbers} climbers")
    if climbers <= 5:
        group_musala += climbers
    elif 6 <= climbers <= 12:
        group_two += climbers
    elif 13 <= climbers <= 25:
        group_three += climbers
    elif 26 <= climbers <= 40:
        group_four += climbers
    elif climbers >= 41:
        group_five += climbers
    total_climbers += climbers
 #   print(f"Total_climbers: {total_climbers:.2f}")
#print(f"Group Musala: {group_musala}")
musala = group_musala / total_climbers * 100
monblan = group_two / total_climbers * 100
kilimandjaro = group_three / total_climbers * 100
k_two = group_four / total_climbers * 100
everest = group_five / total_climbers * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimandjaro:.2f}%")
print(f"{k_two:.2f}%")
print(f"{everest:.2f}%")
