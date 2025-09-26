import datetime
import random

class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (Available: {self.copies})"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append((book, datetime.date.today()))
            print(f"📚 {self.name} borrowed '{book.title}'")
        else:
            print(f"❌ Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        for borrowed, date in self.borrowed_books:
            if borrowed == book:
                book.copies += 1
                self.borrowed_books.remove((borrowed, date))
                print(f"✅ {self.name} returned '{book.title}'")
                return
        print(f"⚠️ {self.name} has not borrowed '{book.title}'.")

    def __str__(self):
        return f"User: {self.na
