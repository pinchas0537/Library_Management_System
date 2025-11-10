from uuid import uuid4

class User:

    def __init__(self,name):
        self.name = name
        self.id = str(uuid4())
        self.borrowed_books = list()
    def __str__(self):
        return {"name": self.name, "id": self.id, "books": self.borrowed_books}