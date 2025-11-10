class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_user = []


    def add_book(self, book: Book):
        self.book = book
        self.list_of_books.append(self.book)
        return self.list_of_books
    
    def add_user(self, user: User):
        self.user = user
        self.list_of_user.append(self.user)
        return self.list_of_user
        
    def borrow_book(self, user_id, book_isbn):
        self.user_id = user_id
        self.book_isbn = book_isbn
        for book in self.list_of_books:
            if self.book_isbn == self.book.ISBN and self.user_id == self.user.id:
                self.book.is_available = False
                self.user.borrowed_books.append(book)
            else:
                return f"error"
        return f"Borrowed name: {self.user_id}, Number of books he took: {self.book_isbn}, Is the book available? {self.book.is_available}"
            
    def return_book(self, user_id, book_isbn):
        self.user_id = user_id
        self.book_isbn = book_isbn
        for r_book in self.user.borrowed_books:
            if user_id == self.user.id and self.book_isbn == self.book.ISBN and self.book.is_available == False:
                self.list_of_books.append(r_book)
                self.user.borrowed_books.remove(r_book)
                self.book.is_available = True
            else:
                return f"error"
        return f"Borrowed name: {self.user_id}, Returned book number: {self.book_isbn}, Is the book available? {self.book.is_available}"
        
    def list_available_books(self):
        available_books = []
        for i in self.list_of_books:
            if self.book.is_available == True:
                available_books.append(self.book.__str__())
        return available_books
    
    # def search_book(title or author):