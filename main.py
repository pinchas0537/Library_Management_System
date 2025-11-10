from Classes.class_book import Book
from Classes.class_Librar import Library
from Classes.user import User

# if __name__ == "__main__":    
#     #book 1 and 2
#     book1 = Book("WAR","DAVID",1)
#     book2 = Book("LOVE","DAN",2)
#     #user 1 and 2
#     user1 = User("MOSHA")
#     user2 = User("NOA")
#     #variable obyckt
#     libary = Library()

#     libary.add_book(book1.__str__())
#     libary.add_book(book2.__str__())
#     #print(libary.list_of_books)

#     libary.add_user(user1.__str__())
#     libary.add_user(user2.__str__())
#     #print(libary.list_of_user)

#     # print(libary.borrow_book(user1.id,book1.__str__()["ISBN"]))

#     #print(libary.return_book(user1.id,book1.__str__()["ISBN"]))
#     print(libary.list_available_books())
#     # print(book1.is_available)
#     # print(book2.is_available)
 
# Create a library
lib = Library()

# Add books
b1 = Book("1984", "George Orwell", "123")
b2 = Book("The Hobbit", "J.R.R. Tolkien", "456")
lib.add_book(b1)
lib.add_book(b2)

# Add users
u1 = User("Alice", 1)
u2 = User("Bob", 2)
lib.add_user(u1)
lib.add_user(u2)

# Borrow and return
print(lib.borrow_book(1, "123"))
print(lib.list_available_books())
print(lib.return_book(1, "123"))
print(lib.list_available_books())
