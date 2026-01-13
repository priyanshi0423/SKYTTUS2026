#1. Print numbers from 1 to 10.

for i in range(1, 11):
    print(i)

#1.2 Display multiplication table for a given number.

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x",i,"=",num*i)

#1.3 Find a factorial of a number.

num = int(input("Enter a number: "))

fact = 1
for i in range(1,num+1):
    fact *=i
print("factorial of",num,"is:", fact )

#1.4 Generate the first N fibonacci numbers.

n = int(input("Enter the fibonacci number: "))

a,b = 0,1
for i in range(n):
    print(a,end=" ")
    a,b = b , a + b

#1.5 check if a number is prime.

num = int(input("Enter a number: "))

if num <= 1:
    print("Number is not prime ")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not prime ")
            break
    else:
        print("number is prime ")

#1.6 Reverse a number.(eg. 123->321)

num = int(input("Enter a number: "))

rev = 0
while num >  0:
    digit = num % 10
    rev = rev *10 + digit
    num //=  10
print("Reverse number:",rev)

#1.7 count digit in a number.

num = int(input("Enter a number: "))

count = 0
while num > 0 :
    count += 1
    num //= 10
print("count digit is:",count)

# 1.8 find sum of even number between 1-100

sum_even = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print("sum of even number between 1-100 is: ",sum_even)

#1.9 print a pyramid pattern.

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# 1.10 find all divisors of a number.

num = int(input("Enter a number: "))

print("Divisors of ",num,"are:")
for i in range(1, num+1):
    if num % i == 0:
        print(i)