alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

start_letter = input()
end_letter = input()
exclude_letter = input()
count = 0
start_index = 0
end_index = 0
exclude_index = 0

combination = ""
for index, letter in enumerate(alphabet):
    if start_letter == letter:
        start_index = index
    if end_letter == letter:
        end_index = index
    if exclude_letter == letter:
        exclude_index = index

for index, letter in enumerate(alphabet):
    if start_index <= index <= end_index and index != exclude_index:
        for index2, letter2 in enumerate(alphabet):
            if start_index <= index2 <= end_index and index2 != exclude_index:
                for index3, letter3 in enumerate(alphabet):
                    if start_index <= index3 <= end_index and index3 != exclude_index:
                        print(letter + letter2 + letter3, end=" ")
                        count += 1
print(count)
