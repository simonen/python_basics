primes = [2, 3, 5, 7]
hundreds = int(input())
tens = int(input())
ones = int(input())

for num in range(1, hundreds + 1):
    if num % 2 == 0:
        for i in primes:
            if i <= tens:
                for j in range(1, ones + 1):
                    if j % 2 == 0:
                        print(num, i, j)
