walk_minutes = int(input())
walk_count = int(input())
cal_intake = int(input())

cal_burned = walk_minutes * 5 * walk_count

if cal_burned >= cal_intake / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {cal_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {cal_burned}.")


