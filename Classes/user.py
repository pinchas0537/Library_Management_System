from uuid import uuid4
import json
class User:

    def __init__(self,name):
        self.name = name
        self.id = str(uuid4())
        self.borrowed_books = []
    def __str__(self):
        return {"name": self.name, "id": self.id, "borrowed_books": self.borrowed_books}