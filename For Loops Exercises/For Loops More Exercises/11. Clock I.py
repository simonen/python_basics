seconds = 0
minutes = 0
hours = 0

print(f"{hours:2d} : {minutes:01d}")
for n in range(0, 1439):
    minutes += 1
    if minutes == 60:
        hours += 1
        minutes = 0
    print(f"{hours:2d} : {minutes:01d}")
