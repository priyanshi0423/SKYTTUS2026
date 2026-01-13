#1 WAP to handle division by zero error.

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter a number: "))

    result = a / b
    print("result:", result)
except ZeroDivisionError :
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error:Enter valid integer")

#2 WAP to handle invalid integer input.

try:

    num = int(input("Enter interger number: "))
    print("valid input:",num)
except ValueError:
    print("Error : invalid integer ! try again.")

#3 WAP to open a file and handle the "file not found" error.

try:
    file = open("sample.txt","r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error:File not found . please check the filename and path")

#4 WAP to demonstrate multiple exception block.

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter a number: "))

    result = a / b
    print("result:", result)
except ZeroDivisionError :
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error:Enter valid integer")
except Exception as e:
    print("unexpected error:",e)

#5 WAP to use finally for resource cleanup.

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Error: File not found")

finally:
    print("Closing file")
    try:
        file.close()
    except:
        pass

#6 WAP to create a custom exception for invalid age(<18).

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    print("Access granted. You are eligible.")

except InvalidAgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Error: Please enter a valid integer age")

#7 WAP to handle index error when accessing a list.

try:
    numbers = [10, 20, 30, 40, 50]

    index = int(input("Enter index to access: "))
    print(f"Element at  index ", index, "is:", numbers[index])

except IndexError:
    print("Error:Index is out of range.")
except ValueError:
    print("Error:Enter a valid integer index. ")

#8 WAP that takes two numbers and handle all possible error.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:",num1 + num2)
    print("substraction:",num1 - num2)
    print("multiply:",num1 * num2)
    print("Division:",num1 / num2)

except ZeroDivisionError :
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error:Enter valid integer")
except Exception as e:
    print("unexpected error:",e)

#9 WAP to log errors to a file instead of printing.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)

except Exception as e:
    # Log the error to a file instead of printing
    with open("errors.txt", "a") as f:
        f.write(f"Error occurred: {e}\n")

#10 WAP that validate an email formate and raises and exception for invalid ones.

class InvalidEmailerror(Exception):
    pass
try:
    email = input("Enter your Email: ")

    if "@" not in email or "." not in email:
         raise InvalidEmailerror("Invalid email format")
    print("Email is valid")    
except InvalidEmailerror as e:
    print(e)

