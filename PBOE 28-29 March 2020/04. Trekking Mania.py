groups = int(input())

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_climbers = 0

for group in range(1, groups + 1):
    climbers = int(input())
    if climbers <= 5:
        musala_count += climbers
    elif 6 <= climbers <= 12:
        monblan_count += climbers
    elif 13 <= climbers <= 25:
        kilimanjaro_count += climbers
    elif 26 <= climbers <= 40:
        k2_count += climbers
    elif climbers >= 41:
        everest_count += climbers
    total_climbers += climbers

musala_percent = musala_count / total_climbers * 100
monblan_percent = monblan_count / total_climbers * 100
kilimanjaro_percent = kilimanjaro_count / total_climbers * 100
k2_percent = k2_count / total_climbers * 100
everest_percent = everest_count / total_climbers * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")



