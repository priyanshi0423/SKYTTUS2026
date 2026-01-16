#1.  cerate a class with attributes like brand, model, and speed and method to accelerate / brake.

class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    def accelerate(self, increase):
        self.speed += increase
        print(f"speed increase to{self.speed} km/h")
    def brake(self, decrease):
        self.speed -= decrease
        print(f"speed decrease to{self.speed} km/h")

car = Car("mercedes", "G-class", 400)

car.accelerate(65)
car.accelerate(80)

#2 create a bankaccount class with deposite and withdraw methods.

class BankAccount:
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. current balance{self.balance}")
        else:
            print("Deposite amount must be positive.")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Amount must be positive.")
        else:
            self.balance -= amount
            print(f"withdraw {amount}. current balance:{self.balance}")

account1 =BankAccount("sonu", 10000)

account1.deposit(200)
account1.withdraw(500)

#3 create a student class with a method to calculate average marks.

class students:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    def average_marks(self):
        total = sum(self.marks)
        average_marks = total / len(self.marks)
        print("aeverage marks:",average_marks)

student1 = students("priyanshi",[70,56,76,84])

student1.average_marks()

#4 create a rectangle class with method to find area and perimeter.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
       print("area of rectangle:",self.length*self.width) 
    def perimeter(self):
      print("perimeter of rectangle:",2*(self.length+self.width))
rec1 = Rectangle(20,3)

rec1.area()
rec1.perimeter()

#5 create an employee class that display salary details.

class Employees:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_salary(self):
        print("Employee name:",self.name)
        print("Employee salary:",self.salary)

employee1 = Employees("jiya",20000)

employee1.display_salary()

#6 create a book class to store tittle, authore, and price and display details.

class Books:
    def __init__(self,tittle_name,authore_name,price):
        self.tittle_name = tittle_name
        self.authore_name = authore_name
        self.price = price
    def display_bookdetails(self):
        print("Book tittle:",self.tittle_name)
        print("Authore name:",self.authore_name)
        print("Price of book:",self.price)

book1 = Books("atomic habit","james clear",200)

book1.display_bookdetails()

#7 create a circle class to find area and circumference.

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("Area of circle:",3.14 * self.radius * self.radius)
    def circumference(self):
        print("circumference of circle:",2 * 3.14 * self.radius)

circle1 = Circle(4)

circle1.area()
circle1.circumference()

#8 create a laptop class with a method to apply discounts on price.

class Laptop:
    def __init__(self,price,discount):
        self.price = price
        self.discount = discount
    def show_price(self):
        print("Price of laptop:",self.price)
    def show_discount(self):
        discount_amount = self.price * self.discount / 100
        final_price = self.price * self.discount
        print("Discount Price:",discount_amount)
        print("price afetr discount is:",final_price)

laptop1 = Laptop(50000, 20)

laptop1.show_price()
laptop1.show_discount()
    
#9 create a flight class with seat booking functionality.

class Flight:
    def __init__(self, flight_name, total_seat):
        self.flight_name = flight_name
        self.total_seat = total_seat   
        self.booked_seat = 0
    
    def book_seat(self, seats):       
        if seats <= (self.total_seat - self.booked_seat):
            self.booked_seat += seats
            print(seats, "seat successfully booked.")
            print("Seats remaining:", self.total_seat - self.booked_seat)
        else:
            print("Booking failed! Seats are not available.")

    def flight_details(self):
        print("Flight name:", self.flight_name)
        print("Total seats:", self.total_seat)
        print("Booked seats:", self.booked_seat)
        print("Available seats:", self.total_seat - self.booked_seat)


f1 = Flight("Indigo 101", 50)

f1.flight_details()
f1.book_seat(5)
f1.book_seat(48)
f1.flight_details()

#10 create a shop class with a method to add and list product.
class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print(self.products)

shop1 = Shop("XYZ's Store")

shop1.add_product("Laptop")
shop1.add_product("Phone")
shop1.list_products()