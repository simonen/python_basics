lower_vowels = ('a', 'e', 'i', 'o', 'u', 'y')
upper_vowels = ('A', 'E', 'I', 'O', 'U', 'Y')

word = input()
count = 0
for letter in word:
    if letter in lower_vowels or letter in upper_vowels:
        count += 1

print(count)