start_digit = int(input())
end_digit = int(input())
first_digit = 0
second_digit = 0
third_digit = 0
fourth_digit = 0

for number in range(start_digit * 1000, (end_digit + 1) * 1000 + 1):
    number_to_string = str(number)
    valid = 0
    for index, digit in enumerate(number_to_string):
        if index == 0:
            first_digit = int(digit)
        elif index == 1:
            second_digit = int(digit)
        elif index == 2:
            third_digit = int(digit)
        elif index == 3:
            fourth_digit = int(digit)
    if start_digit <= first_digit <= end_digit and start_digit <= second_digit <= end_digit and start_digit <= third_digit <= end_digit:
        if start_digit <= fourth_digit <= end_digit:
            valid += 1
            if first_digit > fourth_digit:
                valid += 1
            if (second_digit + third_digit) % 2 == 0:
                valid += 1
            if first_digit % 2 == 0 and fourth_digit % 2 != 0:
                valid += 1
            elif first_digit % 2 != 0 and fourth_digit % 2 == 0:
                valid += 1
        if valid == 4:
            print(number, end=" ")
