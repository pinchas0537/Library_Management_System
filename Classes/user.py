class User:
    def __init__(self,name, id, borrowed_books: list[Book]):
        self.name = name
        self.id = id
        self.borrowed_books = borrowed_books
    def __str__(self):
        return f"name: {self.name} id: {self.id} books: {self.borrowed_books}"
        