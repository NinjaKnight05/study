# def divide(a, b):
#     result = a / b
#     return result

# print(divide(10, 2))
# print(divide(15, 3))

# try:
#     number = int('abc')
#     result = 10 / number
# except ValueError:
#     print('That was not a valid number.')
# except ZeroDivisionError:
#     print("Can't divide by zero.")

# def process_data(data):
#     try:
#         result = int(data)
#         return result * 2
#     except ValueError:
#         print('Logging: Invalid data received')
        # raise  # Re-raises the same ValueError

# try:
#     process_data('abc')
# except ValueError:
#     print('Handled at higher level')


# class InsufficientFundsError(Exception):
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#         super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientFundsError(balance, amount)
#     return balance - amount

# try:
#     new_balance = withdraw(100, 150)
# except InsufficientFundsError as e:
#     print(f'Transaction failed: {e}')

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def bark(self):
#              print(f'my name is {self.name.upper()} and i am {self.age} yrs old')

# obj_1=Dog('peter',1)
# obj_2=Dog('sheldon',3)
# obj_1.bark()
# obj_2.bark()

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

   def __len__(self):
       return self.pages

   def __str__(self):
       return f"'{self.title}' has {self.pages} pages"

   def __eq__(self, other):
       return self.pages == other.pages
  
book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True