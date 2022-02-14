season = input()
kilometers = float(input())
rate = 0
if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        rate = kilometers * 0.75
    elif season == "Summer":
        rate = kilometers * 0.9
    else:
        rate = kilometers * 1.05
if 5000 < kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        rate = kilometers * 0.95
    elif season == "Summer":
        rate = kilometers * 1.1
    else:
        rate = kilometers * 1.25

elif 10000 < kilometers <= 20000:
    rate = kilometers * 1.45

earnings = rate * 0.9 * 4

print(f"{earnings:.2f}")

