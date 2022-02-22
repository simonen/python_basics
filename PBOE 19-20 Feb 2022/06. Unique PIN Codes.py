first_digit_limit = int(input())
second_digit_limit = int(input())
third_digit_limit = int(input())

digits_concat = str(first_digit_limit) + str(second_digit_limit) + str(third_digit_limit)
upper_limit = int(digits_concat)
prime_numbers = [2, 3, 5, 7]

for number in range(222, upper_limit + 1):
    ok = 0
    number_to_string = str(number)
    first_digit = int(number_to_string[0])
    second_digit = int(number_to_string[1])
    third_digit = int(number_to_string[2])
    if first_digit_limit >= first_digit > 1 and first_digit % 2 == 0:
        ok += 1
    if second_digit in prime_numbers and second_digit_limit >= second_digit > 1:
        ok += 1
    if third_digit_limit >= third_digit > 1 and third_digit % 2 == 0:
        ok += 1
    if ok == 3:
        print(first_digit, second_digit, third_digit)
