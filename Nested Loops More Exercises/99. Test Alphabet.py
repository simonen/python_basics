alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

start_letter = input()
end_letter = input()
exclude_letter = input()
count = 0
start_index = 0
end_index = 0
exclude_index = 0

for index, letter in enumerate(alphabet):
    if start_letter == letter:
        start_index = index
    if end_letter == letter:
        end_index = index
    if exclude_letter == letter:
        exclude_index = index

for index, letter in enumerate(alphabet):
    if start_index <= index <= end_index:
        for l in alphabet:
            print(letter, l)