# hours = int(input())
# minutes = int(input())
# minutes_ext = minutes + 15
# if minutes_ext >= 60:
#     hours += 1
#     minutes = minutes_ext % 60
#     if hours == 24:
#         print(f"{hours % 24}:{minutes:02d}")
#     else:
#         print(f"{hours}:{minutes:02d}")
#
# else:
#     print(f"{hours}:{minutes_ext:02d}")
#

hours = int(input())
minutes = int(input())
minutes += 15
hours += minutes // 60
minutes %= 60
if hours > 23:
    hours %= 24
print(f"{hours}:{minutes:02d}")
