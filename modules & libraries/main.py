#1.create a custom math module and import in another file.
import custom_math

print(custom_math.add(10, 5))
print(custom_math.substract(10, 5))
print(custom_math.multiply(10, 5))
print(custom_math.divide(10, 5))

#2. create a module to perform string operation.

import string

text = "Madam"

print("Uppercase:",string.to_upper(text))
print("lowercase:",string.to_lower(text))
print("Reversed:",string.reverse_string(text))
print("Total Characters:", string.count_characters(text))
print("Is Palindrome:", string.is_palindrome(text))
print("Vowel Count:", string.count_vowels(text))

#3 use random module to generate 5 random integer.

import random

random_numbers = []

for i in range(5):
    print(random.randint(1, 100))

#4 use datetime module to display current date and time.

import datetime

current_datetime = datetime.datetime.now()

print("Current Date and Time:")
print(current_datetime)

#5 use math module to find factorial of number.

import math

num = int(input("Enter a number: "))
fact = math.factorial(num)
print("Factorial of",num,"is:", fact)

#6 create a package shapes with modules for circle and rectangle.

from shape import circle, rectangle

# Circle
r = 5
print("Circle Area:", circle.area(r))
print("Circle Perimeter:", circle.perimeter(r))

# Rectangle
l = 10
w = 4
print("Rectangle Area:", rectangle.area(l, w))
print("Rectangle Perimeter:", rectangle.perimeter(l, w))

#7 import multiple functions from one module and use them.

# Import multiple functions from one module

from math_operations import add, subtract, multiply

a = 10
b = 5

print("Add:", add(a, b))
print("Subtract:", subtract(a, b))
print("Multiply:", multiply(a, b))

#8 WAP to shuffle a list using random module.

import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list: ",numbers)

#9 WAP to calculate the difference between two date.

from datetime import date

date1 = date(2024, 1, 1)
date2 = date(2026, 1, 20)

difference = date2 - date1
print("Difference in days:",difference.days) 

#10 use os module to list files in a liberary.

import os
path = "."
files = os.listdir(path)
print("Files in the directory:")
for file in files:
    print(file)