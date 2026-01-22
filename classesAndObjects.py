# Problem 1.1: Library Management System
# Scenario:
# You are building a library management system. Create a Book class that represents a book in the library.
# Requirements:
# The Book class should have attributes: title , author , isbn , available_copies
# Create a method borrow_book() that decreases available_copies by 1
# Create a method return_book() that increases available_copies by 1
# Create a method is_available() that returns True if available_copies > 0
# Create at least 3 book objects and demonstrate borrowing and returning books


# class Book:
#     def __init__(self, title, author, isbn, available_copies):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.avilable_copies = available_copies

#     def borrow_book(self):
#         if self.avilable_copies > 0:
#             self.avilable_copies -= 1
#             print(f"{self.title} borrowd successfully")
#         else:
#              print(f"{self.title} not available")

#     def return_book(self):
#         self.avilable_copies += 1
#         print(f"{self.avilable_copies} return successfully")

#     def is_available(self):
#         return self.avilable_copies > 0

# book1 = Book("Python Basics", "Ali", 1111, 3)
# book2 = Book("Data Science", "Ahmed", 2222, 1)
# book3 = Book("AI Intro", "Sara", 3333, 0)

# book1.borrow_book()
# book1.borrow_book()
# book1.return_book()
# print(book1.is_available())

# book2.borrow_book()
# book2.borrow_book()

# book3.borrow_book()


# ================================================================

# Problem 1.2: Bank Account System
# Scenario:
# Design a BankAccount class for a simple banking application.
# Requirements:
# The class should have attributes: account_number , account_holder_name , balance
# Create a method deposit(amount) that adds money to the balance
# Create a method withdraw(amount) that deducts money from balance (check if sufficient funds)
# Create a method get_balance() that returns the current balance
# Create a method display_account_info() that prints all account details
# Create at least 2 bank account objects and perform multiple transactions

# class BankAccount:
#     def __init__(self, acc_holder_name, acc_no,  acc_balance):
#         self.acc_holder_name = acc_holder_name
#         self.acc_no = acc_no
#         self.acc_balance = acc_balance

#     def deposit(self, amount):
#         self.acc_balance += amount
#         print("Rs.", amount , "deposited Successfully")
#         print("Total balance:", self.get_balance())

#     def withdraw(self, amount):
#         self.acc_balance -= amount
#         print("Rs.", amount , "withdraw Successfully")
#         print("Total balance:", self.get_balance())
    
#     def get_balance(self):
#         return self.acc_balance
    
#     def display_acc_info(self):
#         print(self.acc_holder_name)
#         print(self.acc_no)
#         print(self.acc_balance)


# acc1 = BankAccount("Ali", 1234, 10000)
# acc2 = BankAccount("Ahmad", 5678, 20000)

# acc1.deposit(50)
# acc1.withdraw(60)
# acc1.display_acc_info()

# acc2.deposit(50)
# acc2.withdraw(60)
# acc2.display_acc_info()

