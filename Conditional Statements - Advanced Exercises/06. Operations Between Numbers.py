# first_number = int(input())
# second_number = int(input())
# operator = input()
# num_type = ""
# result = 0
# if operator == "*":
#     result = first_number * second_number
# elif operator == "+":
#     result = first_number + second_number
# elif operator == "-":
#     result = first_number - second_number
#
# if second_number == 0:
#     if operator == "/" or operator == "%":
#         print(f"Cannot divide {first_number} by zero")
# else:
#     if operator == "%":
#         result = first_number % second_number
#         print(f"{first_number} {operator} {second_number} = {result}")
#     elif operator == "/":
#         result = first_number / second_number
#         print(f"{first_number} {operator} {second_number} = {result:.2f}")
# if operator != "/" and operator != "%":
#     if result % 2 == 0:
#         num_type = "even"
#     else:
#         num_type = "odd"
#     print(f"{first_number} {operator} {second_number} = {result} - {num_type}")

first_number = int(input())
second_number = int(input())
operator = input()
num_type = ""
result = 0
if operator == "*":
    result = first_number * second_number
elif operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "/" or operator == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        if operator == "%":
            result = first_number % second_number
            print(f"{first_number} {operator} {second_number} = {result}")
        elif operator == "/":
            result = first_number / second_number
            print(f"{first_number} {operator} {second_number} = {result:.2f}")
#if operator != "/" and operator != "%":
if operator != "/" and operator != "%":
    if result % 2 == 0:
        num_type = "even"
    else:
        num_type = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {num_type}")
