
#1.Take a string input and print it's length.

a = str(input("Enter a Name: "))
print(len(a))

# convert sentences to lowercase.

sentences = input("Enter a Sentence: ")
print(sentences.lower())

# Replace spaces with underscores in a string

a = input("Enter a sentence: ")
print(a.replace(" ","_"))

# Extract the first and last character of a string.
a = str(input("Enter a Name: "))
print("First character:",a[0])
print("Last character:",a[-1])

# Reverse a string using slicing.

a = "priyanshi"
print(a[::-1])

# Cont how many times a letter appers in a string.

a = "priyanshi"
print(a.count("i"))

# check if a word is present in a Sentence.

sentences = input("Enter a Sentence: ")
word = input("Enter a Word: ")

if word in sentences:
  print("word is present in sentence")
else:
  print("word is not present in sentence")

# Take name & age and print using f-string formatting.

Name = "priyanshi"
age = 21
print(f"My name is {Name} and I am {age} years old.")

# Remove extra spaces from start and end of a string.

a = "  Hello My Name Is Priyanshi   "
print(a.strip())

# join a list of a words into a single string with -between them

a = ["My", "Name", "is", "Priyanshi"]
print(" ".join(a))

# 2.Create a list of your 5 favourite movies.

list = ["3idiots", "golmaal", "singham", "bahubali", "KGF"]
print(list)

# add a new movie to the list.

list = ["3idiots", "golmaal", "singham", "bahubali", "KGF"]
list.append("K3")
print(list)

# Remove the first movie from the list.

list = ["3idiots", "golmaal", "singham", "bahubali", "KGF"]
list.pop(0)
print(list)

# sort a list of numbers in ascending order.

numbers = [4, 6, 7, 3, 2, 1, 8, 10, 9]
numbers.sort()
print(numbers)

# Reverse a list

list = ["3idiots", "golmaal", "singham", "bahubali", "KGF"]
list.reverse()
print(list)

# Find the largest number in a list.

numbers = [4, 6, 7, 3, 2, 1, 8, 10, 9]
print(max(numbers))

# merge two lists into one.

list1 = ["3idiots", "golmaal", "singham", "bahubali", "KGF"]
list2 = ["k3", "golmaal2", "bahubali2"]
result = list1 + list2
print(result)

# access the last elements of a list without using index numbers.

list = ["3idiots", "golmaal", "singham", "bahubali", "KGF"]
last_element = list.pop()
print(last_element)

# create a nested list and access a specific inner element.

nested_list = [[4, 6, 7], [3, 2, 1], [8, 10, 9]]
print(nested_list[1][1])

# count how many times an element appears in a list.

list = [1, 2, 3, 4, 2, 3, 2, 4, 1, 3]
print(list.count(3))

