time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = int(time_first + time_second + time_third)
minutes = total_time // 60

seconds_remaining = total_time % 60

# if seconds_remaining < 10:
#     print(f"{minutes}:0{seconds_remaining}")
# else:
#     print(f"{minutes}:{seconds_remaining}")

# Eleganten variant s formatirane bez if proverki

print(f"{minutes}:{seconds_remaining:02d}")