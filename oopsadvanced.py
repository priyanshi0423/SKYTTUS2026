#1. create a base class animal and subclass dag and cat.

class Animal:
    def speak(self):
        print("Animal make a sound")

class Dog(Animal):
    def speak(self):
        print("Dog is bark")

class cat(Animal):
    def speak(self):
        print("cat is meow")

dog1 = Dog()
cat1 = cat()
 
dog1.speak()
cat1.speak()

#2.create a class hierarchy for vehical-car-elcteric car.

class Vehical:
    def info(self):
        print("This is vehical")
class car(Vehical):
    def car_info(self):
        print("This is a car")
class electric_car(car):
    def elcrtic_info(self):
        print("This is an electric car")

ecar = electric_car()

ecar.info()
ecar.car_info()
ecar.elcrtic_info()

#3 implement method overriding in a base and derived class.


class Animal:
    def speak(self):
        print("Animal make a sound")

class Dog(Animal):
    def speak(self):
        print("Dog is bark")

class cat(Animal):
    def speak(self):
        print("cat is meow")

dog1 = Dog()
cat1 = cat()
 
dog1.speak()
cat1.speak()

#4 demonstrate multiple inheritance with two parent class.

class Father:
    def father_name(self):
        print("Father name is : raj")

class Mother:
    def mother_name(self):
        print("mother name is : gita")

class Child(Father,Mother):
    def child_name(self):
        print("Child name is : dax")

c = Child()

c.father_name()
c.mother_name()
c.child_name()

#5 create a polymorphic function that work with different shapes.

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Area of Ractangle: length * width ")
class circle(Shape):
    def area(self):
        print("Area of circle =3.14*r*r")
def calculate_area(Shape):
    Shape.area()

rect = Rectangle()
circle =circle()

calculate_area(rect)
calculate_area(circle)

#6. create a bank system with savings account and current account  class.

# Base class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print("Balance:", self.balance)

# Saving Account class
class SavingAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print("Interest added")

# Current Account class
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")


# Object creation
saving = SavingAccount("Priya", 10000)
current = CurrentAccount("Rahul", 8000)

saving.display_balance()
saving.add_interest()
saving.display_balance()

current.display_balance()
current.withdraw(3000)
current.display_balance()


#7. create a class with private attributes and getter / setter method.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private attribute

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid marks")

# Object creation
student = Student("Priya", 85)

print("Marks:", student.get_marks())

student.set_marks(90)
print("Updated Marks:", student.get_marks())

#8. create a teacher and student class to show inheritance.
# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Student class (inherits Person)
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        self.display_info()
        print("Roll No:", self.roll_no)


# Teacher class (inherits Person)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_info()
        print("Subject:", self.subject)


# Object creation
student = Student("sonu", 21, 100)
teacher = Teacher("Mr. Sharma", 40, "Python")

student.display_student()
print()
teacher.display_teacher()


#9. create a music player class and subclass spotify to override play method.

class Musicplayer:
    def play(self):
        print("Playing music from music player")

class spotify(Musicplayer):
    def play(self):
        print("Playing music from spotify")

player = Musicplayer()
player.play()

spotify_app = spotify()
spotify_app.play()

#10. demonstrate the user of super() in inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Student class (inherits Person)
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        self.display_info()
        print("Roll No:", self.roll_no)


# Teacher class (inherits Person)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_info()
        print("Subject:", self.subject)


# Object creation
student = Student("sonu", 21, 100)
teacher = Teacher("Mr. Sharma", 40, "Python")

student.display_student()
print()
teacher.display_teacher()
