# class Car:
#   color = "red"
#   model = "Gls"
#   brand = "mercedes"

# car1 = Car()
# print(car1.model)
# print(car1.brand)


# class Student:
#   def __init__(self, fullname):
#     self.name = fullname
#     print("adding new student in Database")

# s1 = Student("Karan")
# print(s1.name)


# class Student:
#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks

#   def get_average(self):
#     print(sum(self.marks) / len(self.marks))

# data1 = Student("Karan", [90, 80, 70])
# print(data1.name)
# print(data1.marks)
# data1.get_average()


# class Account:
#   def __init__(self, balance, account_no):
#     self.balance = balance
#     self.account_no = account_no

#   def debit(self, amount):
#     self.balance -= amount
#     print("Rs", amount, "Debited")

#   def credit(self, amount):
#     self.balance += amount
#     print("Rs", amount, "Credited")

#   def get_balance(self):
#     print("your balance is Rs", self.balance)

# acc1 = Account(10000, "12345")
# acc1.debit(2000)
# acc1.credit(5000)
# acc1.get_balance()


# class Student:
#   def __init__(self, name):
#     self.name = name
# s1 = Student("Aman")
# print(s1.name)
# del s1.name
