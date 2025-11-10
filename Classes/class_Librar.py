class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_user = []

    def add_book(self, book):
        self.book = book
        self.list_of_books.append(self.book)
        return self.list_of_books
    
    def add_user(self, user):
        self.user = user
        self.list_of_user.append(self.user)
        return self.list_of_user
        
    def borrow_book(self, user_id, book_isbn):
        self.user_id = user_id
        self.book_isbn = book_isbn
        for book in range(len(self.list_of_books)):
            if self.book_isbn == self.list_of_books[book]["ISBN"] and self.user_id == self.list_of_user[book]["id"] and self.book["is_available"] == True:
                self.book["is_available"] = False
                self.user["borrowed_books"].append(self.book)
                print(self.user["borrowed_books"])
                
                return f"Borrowed name: {self.user_id}, Number of books he took: {self.book_isbn}, Is the book available? {self.book["is_available"]}"
            else:
                return f"error"
        
    def return_book(self, user_id, book_isbn):
        self.user_id = user_id
        self.book_isbn = book_isbn
        for r_book in range(len (self.user["borrowed_books"])):
            if user_id == self.list_of_user[r_book]["id"] and self.book_isbn == self.list_of_books[r_book]["ISBN"] and self.book["is_available"] == False:
                self.list_of_books.append(self.book)
                self.user["borrowed_books"].remove(self.book)
                self.book["is_available"] = True
                return f"Borrowed name: {self.user_id}, Returned book number: {self.book_isbn}, Is the book available? {self.book["is_available"]}"
            else:
                return f"error"
        
    def list_available_books(self):
        available_books = []
        for i in self.list_of_books:
            if self.book.is_available == True:
                available_books.append(self.book.__str__())
        return available_books