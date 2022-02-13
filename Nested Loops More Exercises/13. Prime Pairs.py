primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

first_pair_start = int(input())
second_pair_start = int(input())
first_pair_end = int(input())
second_pair_end = int(input())
first_pair_limit = first_pair_start + first_pair_end
second_pair_limit = second_pair_start + second_pair_end

for num in range(first_pair_start, first_pair_limit + 1):
    for i in range(second_pair_start, second_pair_limit + 1):
        if num in primes and i in primes:
            print(str(num)+str(i), end="")
            print()
