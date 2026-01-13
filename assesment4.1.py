#2.1 check if a person is eligible to vote

age = int(input("Enter the age: "))

if age >= 18:
    print("Person is eligible for vote")
else:
    print("person is not eligible for vote")

#2.2 grade calculator based on marks:90+ =A,80+ =B, else c

marks = int(input("Enter the marks: "))

if marks >= 90:
    print("Student Garde is A")
elif marks >= 80:
    print("Student Garde is B")
else:
    print("Student Garde is C")

#2.3 simulate a traffic light: red=stop, yellow= wait,green= go.

light = input("Enter the light colour: ")

if light == "red":
    print("STOP")
elif light == "yellow":
    print("WAIT")
elif light == "green":
    print("GO")
else:
    print("Invalid colour")

#2.4 ATM withrawal check:sufficient balance or not.

balance = int(input("Enter a balance: "))
withdraw = int(input("Enter withdrwal amount: "))

if withdraw <= balance:
    print("withdraw is sucessful")
    print("Remainig balance:" , balance - withdraw)
else:
    print("Insufficient balance")

#2.5 check if number is positive, negative & zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")

# 2.6 check if a number is lies within a given range.

num = int(input("Enter a number: "))
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

if lower <= num <= upper:
    print(f"{num} lies within the range {lower} to {upper}")
else:
    print(f"{num} does not lie within the range {lower} to {upper}")

#2.7 username & password verification.

correct_username = "Priyanshi"
Correct_password = "abc@123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == Correct_password:
    print("Sccuessfuly Login")
elif username != correct_username and password != Correct_password:
    print("Invalid username and password")
elif username != correct_username and password == Correct_password:
    print("Invalid username")
else:
    print("Invalid password")

#2.8 electicity bill calculate based on unit consumed.

units = float(input("Enter number of unit consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print(f"Electricity bill for {units} units: ₹{bill}")

# 2.9 simple calculator(add , substract, multiply, divide).

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero")
else:
    print("Invalid input")

# check type of triangle(equilateral, isosceles, scalene).

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")
