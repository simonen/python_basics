target_book = input()
search_book = input()
books = 0
while search_book != target_book:
    books += 1
    search_book = input()
    if search_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {books} books.")
        break

else:
    print(f"You checked {books} books and found it.")



