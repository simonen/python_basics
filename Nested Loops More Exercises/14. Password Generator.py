n = int(input())
l = int(input())

# lower ascii range(97, 123)

for num in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(97, 97 + l):
            char1 = chr(j)
            for k in range(97, 97 + l):
                char2 = chr(k)
                for p in range(1, n + 1):
                    if p > num and p > i:
                        print(str(num) + str(i) + char1 + char2 + str(p), end=" ")
