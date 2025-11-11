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

    libary.add_user(user1.__str__())
    libary.add_user(user2.__str__())
    #print(libary.list_of_user)

    # borrow_book1 = libary.borrow_book(user1.id,book1.__str__()["ISBN"])

    # return_book1 = libary.return_book(user1.id,book1.__str__()["ISBN"])

    # print(libary.list_available_books())
  
 
    # print(libary.list_of_books)
    # libary.add_user(user1.__str__())
    # libary.add_user(user2.__str__())
    # print(libary.list_of_user)

    # print(libary.borrow_book(user1.id,book1.ISBN))
    # print(libary.return_book(user1.id,book1.ISBN))

