import string

alphabets = list(string.ascii_letters)
print(alphabets)
symbol = input()
## lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
if symbol not in alphabets:
    print(f"{symbol} not found in the list")
else:
    print("da")
