from Classes.class_book import Book
from Classes.class_Librar import Library
from Classes.user import User

if __name__ == "__main__":    
    book1 = Book("WAR","DAVID",1)
    book2 = Book("LOVE","DAN",2)
    
    user1 = User("MOSHA")
    user2 = User("NOA")
    
    libary = Library()

    libary.add_book(book1.__str__())
    libary.add_book(book2.__str__())
    print(libary.list_of_books)
    print(libary.add_user(user1.__str__()))
    print(libary.add_user(user2.__str__()))

    print(libary.borrow_book(user1.id,book1.__str__()["ISBN"]))
    
    print(book1.is_available)
    print(book2.is_available)