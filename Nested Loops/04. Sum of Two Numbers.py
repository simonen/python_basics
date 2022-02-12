int_start = int(input())
int_end = int(input())
count = 0
magic_num = int(input())
is_found = False
for i in range(int_start, int_end + 1):
    for j in range(int_start, int_end + 1):
        count += 1
        if i + j == magic_num:
            print(f"Combination N:{count} ({i} + {j} = {magic_num})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{count} combinations - neither equals {magic_num}")


