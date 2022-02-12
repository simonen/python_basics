# seconds = 0
# minutes = 0
# hours = 0
#
# print(f"{(hours):2d} : {minutes:01d} : {seconds:1d}")
#
# for n in range(0, 24 * 60 * 60 - 1):
#     seconds += 1
#     if seconds == 60:
#         minutes += 1
#         seconds = 0
#         if minutes == 60:
#             hours += 1
#             minutes = 0
#     print(f"{(hours):2d} : {minutes:01d} : {seconds}")
seconds = 0
minutes = 0
hours = 0
print(f"{hours:2d} : {minutes:01d} : {seconds}")
for n in range(0, 24 * 60 * 60 - 1):

    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0
    print(f"{hours:2d} : {minutes:01d} : {seconds}")
