n = int(input())
count = 0
iterations = 0
for i in range (0, n + 1):
    iterations += 1
    for j in range (0 , n + 1):
        iterations += 1
        for k in range (0, n + 1):
            iterations += 1
            if i + j + k == n:
                count += 1
print(count)
print(iterations)