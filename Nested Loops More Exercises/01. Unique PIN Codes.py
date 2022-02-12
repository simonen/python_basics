first_digit = int(input())
second_digit = int(input())
third_digit = int(input())
primes = [2, 3, 5, 7]

prime_sum = 0
first_pin = 0
second_pin = 0
third_pin = 0
for number in range(100, 1000):
    number_to_string = str(number)
    for index, digit in enumerate(number_to_string):
        if int(index) == 0:
            if int(digit) % 2 == 0 and int(digit) <= first_digit:
                first_pin += 1
        if int(index) == 1:
            if int(digit) == 2:
                second_pin += 1
            if int(digit) % 2 != 0 and int(digit) > 1 and int(digit) <= second_digit and int(digit) != 9:
                second_pin += 1
        if int(index) == 2:
            if int(digit) % 2 == 0 and int(digit) > 0 and int(digit) <= third_digit:
                third_pin += 1

    if first_pin + second_pin + third_pin == 3:
        print(number_to_string.replace("", " ")[1: -1])
    first_pin = 0
    third_pin = 0
    second_pin = 0
