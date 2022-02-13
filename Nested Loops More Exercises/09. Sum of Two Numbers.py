init_start = int(input())
init_end = int(input())
magic_number = int(input())
combinations = 0
is_magic = False
for number in range(init_start, init_end + 1):
    number_a = 0
    number_b = 0
    for i in range(init_start, init_end + 1):
        combinations += 1
        if init_end > init_start:
            if number + i == magic_number:
                number_a = number
                number_b = i
                print(f"Combination N:{combinations} ({number_a} + {number_b} = {magic_number})")
                is_magic = True
                break
    if is_magic:
        break
if not is_magic:
    print(f"{combinations} combinations - neither equals {magic_number}")
