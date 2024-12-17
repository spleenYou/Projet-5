class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return None
        print("Le livre n'est pas présent dans la bibliothèque")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                return None
        print("Le livre n'est pas disponible")

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                return None
        print("Le livre n'a pas été emprumté")

    def available_books(self):
        print("Liste des livres disponibles :")
        for book in self.books:
            print(f"- {book.title}")

    def borrowed_books(self):
        print("Liste des livres emprumtés :")
        for book in self.borrow_books:
            print(f"- {book.title}")


book_list = [Book("Contes", "Hans Christian Andersen", 1994),
             Book("La saga de Njáll le Brûlé", "Anonyme", 2011),
             Book("Orgueil et préjugés", "Jane Austen", 2012),
             Book("Le Père Goriot", "Honoré de Balzac", 1999)]

library = Library()
for book in book_list:
    library.add_book(book)
library.available_books()
library.borrow_book("La saga de Njáll le Brûlé")
library.available_books()
library.borrowed_books()
