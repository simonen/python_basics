name = input()
max_points = -100000

while name != "Stop":
    current_player = name  # Ivan, #Ivo
    points = 0
    for letter in name:
        number = int(input())
        if number == ord(letter):
            points += 10
        else:
            points += 2
    if points > max_points:
        max_points = points
        best_player = name   # Ivan
    if points == max_points:
        draw_winner = name
    name = input()


if points == max_points:
    print(f"The winner is {draw_winner} with {points} points!")
else:
    print(f"The winner is {best_player} with {max_points} points!")