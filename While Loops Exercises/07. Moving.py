height = int(input())
width = int(input())
depth = int(input())
volume = height * width * depth
while volume > 0:
    boxes = input()
    if boxes == "Done":
        break
    volume -= int(boxes)
 #   print(f"Remaining volume: {volume}")
if volume >= 0:
    print(f"{volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")