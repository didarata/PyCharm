class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


# https://judge.softuni.org/Contests/Practice/Index/1934#2

book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)