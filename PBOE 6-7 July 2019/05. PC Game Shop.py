games_sold = int(input())

heartstone = 0
fornite = 0
overwatch = 0
others = 0


for num in range(1, games_sold + 1):
    game = input()
    if game == "Hearthstone":
        heartstone += 1
    elif game == "Fornite":
        fornite += 1
    elif game == "Overwatch":
        overwatch += 1
    else:
        others += 1
print(f"Hearthstone - {(heartstone / games_sold * 100):.2f}%")
print(f"Fornite - {(fornite / games_sold * 100):.2f}%")
print(f"Overwatch - {(overwatch / games_sold * 100):.2f}%")
print(f"Others - {(others / games_sold * 100):.2f}%")