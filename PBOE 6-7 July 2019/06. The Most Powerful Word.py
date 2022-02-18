#lower_alpha = [97 - 122]
#upper_alpha = [65 - 90]
from math import floor

word = input()
lower_vowels = ('a', 'e', 'i', 'o', 'u', 'y')
upper_vowels = ('A', 'E', 'I', 'O', 'U', 'Y')

max_sum = 0
while word != "End of words":
    ascii_sum = 0
    length = len(word)
    for letter in word:
        ascii_sum += ord(letter)
    if word[0] in lower_vowels or word[0] in upper_vowels:
        ascii_sum *= length
    else:
        ascii_sum = floor(ascii_sum / length)
    if ascii_sum > max_sum:
        max_sum = ascii_sum
        powerful_word = word
    word = input()

print(f"The most powerful word is {powerful_word} - {max_sum}")
