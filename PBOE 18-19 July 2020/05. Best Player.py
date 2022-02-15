player = input()

top_score = 0
hat_trick = 0
best_player = ""

while player != "END":
    goals = int(input())
    if goals >= 10:
        best_player = player
        top_score = goals
        hat_trick = 1
        break
    if goals > top_score:
        top_score = goals
        best_player = player
    if goals >= 3:
        hat_trick = 1

    player = input()

print(f"{best_player} is the best player!")
if top_score >= 10 or hat_trick == 1:
    print(f"He has scored {top_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {top_score} goals.")