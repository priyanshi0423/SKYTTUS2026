#1 function to check if a number is prime.

def is_prime(n):
    if n < 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num,"is prime")
else:
    print(num,"is not prime")

#2 function to reverse a string.

def reverse_string(s):
    return s[::-1]
text = input("Enter string: ")
reverse_text = reverse_string(text)
print("reverse_srting:", reverse_text)

#3 function to find factorial.

def factorial(n):
    if n <0:
        return "factorial is not define or negative number."
    
    result = 1
    for i in range(1, n+1):
            result *= i

    return result
num = int(input("Enter a number: "))
print("Factorial:",factorial(num))

#4 function to calculate simple interest.

def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

interest = simple_interest(p, r, t)
print("Simple Interest:", interest)

#5 function to ocheck if a word is palidrom.

def is_palindrom(word):
    word = word.lower()

    return word == word[::-1]
text = input("Enter a word: ")

if is_palindrom(text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#6 function to count vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))

#7 function to merge two list.

def merge_lists(list1, list2):
    return list1 + list2
list1 = [1, 2, 2]
list2 = [3, 4, 5]

merged = merge_lists(list1, list2)
print("Merged List:", merged)

#8 function to find GCD of two number.

def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD:", gcd(num1, num2))

#9 function to find area of rectangle.

def rectangle_area(length, width):
    return length * width
l = float(input("Enter the length: "))
w = float(input("Enter the width: "))

print("Area of rectangle:", rectangle_area(l, w))

#10 function to check armstrong number.

def is_armstrong(number):
    num_str = str(number)
    n = len(num_str)
    
    total = 0
    for digit in num_str:
        total += int(digit) ** n
    
    return total == number
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
