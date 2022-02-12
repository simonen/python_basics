cake_width = int(input())
cake_height = int(input())
total_pieces = cake_width * cake_height
while total_pieces > 0:
    pieces_taken = input()
    if pieces_taken == "STOP":
        break
    total_pieces -= int(pieces_taken)
if total_pieces >= 0:
    print(f"{total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
