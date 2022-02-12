# A:  a b       ...A => B, r += 1
# B:  a b       ...B => C, r += 1
#     a b c d
# C:  a b
#     b b c d
#     a b
sectors = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
seats = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

last_sector = input()
last_sector_index = 0
last_seat_index = 0
rows_in_a = int(input())
odd_seats_count = int(input())
current_rows = rows_in_a
count = 0
for index, sector in enumerate(sectors):
    if sector == last_sector:
        last_sector_index = index
        break
for index2, seat in enumerate(seats):
    if index2 == odd_seats_count:
        last_seat_index = index2
        break

for index3, sector in enumerate(sectors):
    if index3 <= last_sector_index:
        for row in range(1, current_rows + 1):
            last_seat_index = odd_seats_count
            if row % 2 == 0:
                last_seat_index += 2
            for index4, seat2 in enumerate(seats):
                if index4 < last_seat_index:
                    print(sector + str(row) + seat2)
                    count += 1
                else:
                    break
        current_rows += 1
    else:
        stop_action = True
        break

print(count)


