book = input()
next_book = input()
books_count = 0
while book != next_book:
    if next_book == 'No More Books':
        print(f"The book you search is not here!")
        print(f"You checked {books_count} books.")
        break
    next_book = input()
    books_count += 1


if next_book == book:
    print(f"You checked {books_count} books and found it.")