num_a = int(input())
num_b = int(input())
max_passwords = int(input())

first_char = 35
second_char = 64
count = 0
is_max_pass = False
for x in range(1, num_a + 1):
    for y in range(1, num_b + 1):
        if first_char > 55:
            first_char = 35
        if second_char > 96:
            second_char = 64
        print(chr(first_char) + chr(second_char) + str(x) + str(y) + chr(second_char) + chr(first_char) + "|",
              end="")
        first_char += 1
        second_char += 1
        max_passwords -= 1
        if max_passwords == 0:
            is_max_pass = True
            break
    if is_max_pass:
        break
