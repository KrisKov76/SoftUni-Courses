class Book:
    def __init__(self, name, author, pages):
        self.name = name  # data attribute
        self.author = author
        self.pages = pages


# вдигам инстанцията - инициализираме този обект
book = Book("My Book", "Me", 200)

print(book.name)
print(book.author)
print(book.pages)
