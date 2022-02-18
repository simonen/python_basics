football_team = input()
matches = int(input())

wins = 0
draws = 0
losses = 0
points = 0
games_played = 0

for number in range(1, matches + 1):
    turnout = input()
    if turnout == "W":
        wins += 1
        points += 3
    elif turnout == "D":
        points += 1
        draws += 1
    elif turnout == "L":
        losses += 1
    games_played += 1

if matches > 0:
    win_rate = wins / games_played * 100
if matches == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losses}")
    print(f"Win rate: {win_rate:.2f}%")
