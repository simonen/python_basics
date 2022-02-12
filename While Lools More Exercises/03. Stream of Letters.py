alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
            'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
valid_word = ''
word = ''
n_count = 0
o_count = 0
c_count = 0

while word != "End":
    letter = input()
    if letter == 'End':
        break
    if letter not in alphabet:
        letter = ''
    if letter == "n" and n_count == 0:
        n_count = 1
        letter = ''
    if letter == "o" and o_count == 0:
        o_count = 1
        letter = ''
    if letter == "c" and c_count == 0:
        c_count = 1
        letter = ''
    word += letter
    if n_count + o_count + c_count == 3:
        word += ' '
        n_count = 0
        o_count = 0
        c_count = 0
        valid_word = word

print(valid_word)
