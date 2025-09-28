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
        print(f"User {self.name} created.")     

