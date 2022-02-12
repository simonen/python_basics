number = int(input())
is_valid = False
for num in range(1110, 10000):
    number_to_string = str(num)
    count = 0
    for index, digit in enumerate(number_to_string):
        if int(digit) == 0:
            is_valid = False
            break
        if number % int(digit) == 0:
            is_valid = True
        else:
            is_valid = False
            break
    if is_valid:
        print(num, end=" ")
