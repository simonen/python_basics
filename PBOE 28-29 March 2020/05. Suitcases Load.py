capacity = float(input())
case_count = 1

while capacity > 0:
    case_volume = input()
    if case_volume == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break
    if case_count % 3 == 0 and case_count != 0:
        capacity -= float(case_volume) * 1.1
    else:
        capacity -= float(case_volume)
    if capacity < 0:
        print(f"No more space!")
        break
    case_count += 1

print(f"Statistic: {case_count - 1} suitcases loaded.")
