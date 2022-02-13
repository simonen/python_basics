first = int(input())
second = int(input())
for num in range(first, second + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=", ")
