start_int = int(input())
end_int = int(input())

first_digit = 0
second_digit = 0
third_digit = 0
fourth_digit = 0

first_digit2 = 0
second_digit2 = 0
third_digit2 = 0
fourth_digit2 = 0
word = "Simeon"
#isolate the upper limit digits

for letter in str(end_int):
    number_to_string = str(end_int)
    for index, digit in enumerate(number_to_string):
        if int(index) == 0:
            first_digit = int(digit)
        if int(index) == 1:
            second_digit = int(digit)
        if int(index) == 2:
            third_digit = int(digit)
        if int(index) == 3:
            fourth_digit = int(digit)

for letter2 in str(start_int):
    number_to_string3 = str(start_int)
    for index3, digit3 in enumerate(number_to_string3):
        if int(index3) == 0:
            first_digit2 = int(digit3)
        if int(index3) == 1:
            second_digit2 = int(digit3)
        if int(index3) == 2:
            third_digit2 = int(digit3)
        if int(index3) == 3:
            fourth_digit2 = int(digit3)

# print(first_digit, second_digit, third_digit, fourth_digit)
# print(first_digit2, second_digit2, third_digit2, fourth_digit2)

for number in range(start_int, end_int + 1):
    odd = 0
    number_to_string2 = str(number)
    for index2, digit2 in enumerate(number_to_string2):
        if int(index2) == 0:
            if int(digit2) % 2 != 0 and (first_digit2 <= int(digit2) <= first_digit):
                odd += 1
        if int(index2) == 1:
            if int(digit2) % 2 != 0 and (second_digit2 <= int(digit2) <= second_digit):
                odd += 1
        if int(index2) == 2:
            if int(digit2) % 2 != 0 and (third_digit2 <= int(digit2) <= third_digit):
                odd += 1
        if int(index2) == 3:
            if int(digit2) % 2 != 0 and (fourth_digit2 <= int(digit2) <= fourth_digit):
                odd += 1
    if odd == 4:
        print(number, end=" ")