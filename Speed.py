speed = float(input())

if speed <= 10:
    print("slow")
if speed > 10:
    if speed <= 50:
        print("average")
if speed > 50:
    if speed <= 150:
        print("fast")
if speed > 150:
    if speed <= 1000:
        print("ultra fast")
if speed > 1000:
    print("extremely fast")