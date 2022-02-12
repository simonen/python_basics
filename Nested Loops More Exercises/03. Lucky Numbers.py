n = int(input())
first_digit = 0
second_digit = 0
third_digit = 0
fourth_digit = 0

for number in range(1000, 10000):
    number_to_string = str(number)
    for index, digit in enumerate(number_to_string):
        if index == 0:
            first_digit = int(digit)
        elif index == 1:
            second_digit = int(digit)
        elif index == 2:
            third_digit = int(digit)
        elif index == 3:
            fourth_digit = int(digit)
    if first_digit != 0 and second_digit != 0 and third_digit != 0 and fourth_digit != 0:
        first_pair = first_digit + second_digit
        second_pair = third_digit + fourth_digit
        if first_pair == second_pair:
            if n % first_pair == 0:
                print(number, end=" ")
