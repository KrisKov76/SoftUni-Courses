class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return "".join(f"Title: {self.title}, Author: {self.author}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_: Book):
        self.books.append(book_)

    def find_book(self, title: str):
        try:
            book = [b for b in self.books if b.title.lower == title.lower][0]
            return book
        except IndexError:
            return f'Книгата не e намерена'


book1 = Book("Baba Vanga", "Kovachev")
book2 = Book("Kuma Lisa", "Petrushev")
book1.turn_page(20)

library = Library()
library.add_book(book1)
library.add_book(book2)
print(library.books)
