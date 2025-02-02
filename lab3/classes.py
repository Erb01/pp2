#task1
class String:
    def __init__(self):
        self.text = ""
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())

str = String()
str.getString()
str.printString()

#task2
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
a = int(input())
shape = Shape()
print(shape.area())  
square = Square(a)
print(square.area())  

#task3
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
a = int(input())
b = int(input())
rectangle = Rectangle(a,b)
print(rectangle.area())   

#task4
import math
class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    def show(self):
        print(f"Point({self.x1}, {self.y1})")

    def move(self, x2, y2):
        self.x1 = x2  
        self.y1 = y2  
    def dist(self, other_point):
        return math.sqrt((self.x1 - other_point.x1) ** 2 + (self.y1 - other_point.y1) ** 2)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
p1 = Point(x1, y1)
p2 = Point(x2, y2)
p1.show()  
p2.show()
print(p1.dist(p2))
p1.move(10, 10)
p1.show()  

#task5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print(f"Insufficient funds! Current balance is {self.balance}.")
name = input()
balance = int(input())
account = Account(name,balance)
account.deposit(500) 
account.deposit(200)  
account.withdraw(1800) 
account.withdraw(100)  

#task6
prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
numbers = list(map(int,input().split()))
prime_nums = list(filter(prime, numbers))
print(prime_nums)
