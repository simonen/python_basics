width = float(input())
length = float(input())
height = float(input())
average_height = float(input())

ship_volume = width * length * height
room_volume = 2 * 2 * (average_height + 0.40)
astronauts = ship_volume // room_volume


if 3 <= astronauts <= 10:
    print(f"The spacecraft holds {astronauts:.0f} astronauts.")
elif astronauts < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")


