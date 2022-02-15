n = int(input())
points = 0
reds = 0
oranges = 0
yellows = 0
whites = 0
blacks = 0
others = 0

for ball in range(1, n + 1):
    color = input()
    if color == "red":
        points += 5
        reds += 1
    elif color == "orange":
        points += 10
        oranges += 1
    elif color == "yellow":
        points += 15
        yellows += 1
    elif color == "white":
        points += 20
        whites += 1
    elif color == "black":
        points = points // 2
        blacks += 1
    else:
        points += 0
        others += 1

print(f"Total points: {points}")
print(f"Red balls: {reds}")
print(f"Orange balls: {oranges}")
print(f"Yellow balls: {yellows}")
print(f"White balls: {whites}")
print(f"Other colors picked: {others}")
print(f"Divides from black balls: {blacks}")
