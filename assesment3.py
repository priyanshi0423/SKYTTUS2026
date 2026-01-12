
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

# 3. craete a tuples with 5 numbers.

tuple = (1, 2, 3, 4, 5)
print(tuple)

# acsess the third element in a tuple.

tuple = (1, 2, 3, 4, 5)
third_element = tuple[2]
print(third_element)

# unpack a tuple into separate variables.

tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = tuple
print(a, b, c, d, e)

# ceate a set of 5 fruits.

fruits = {"apple", "banana", "oranges", "grapes", "mango"}
print(fruits)

# add a new fruits in a set.

fruits = {"apple", "banana", "oranges", "grapes", "mango"}
fruits.add("watermelon")
print(fruits)

# remove an element from a set.

fruits = {"apple", "banana", "oranges", "grapes", "mango"}
fruits.remove("oranges")
print(fruits)

# find union of two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9,10}
result= set1.union(set2)
print(result)

# find intersection of two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {6, 5, 4, 7, 8, 9,10}
result= set1.intersection(set2)
print(result)

# check if one set is subset of another.

set1 = {1, 2, 3, 4, 5}
set2 = {6, 5, 4, 7, 8, 9,10}
result = set1.issubset(set2)
print(result)

# convert a list with duplicate values into a set to remove duplicates

list = [1, 2, 3, 4, 2, 3, 2, 4, 1, 3]
unique_list = set(list)
print(unique_list)

#4. create dictionary storing student name and marks.

students = {"priyanshi" :43,  "sonu": 50, "priya": 45, "jiya":46}
print(students)

# add a new key value pair to an existing dictionary.

students = {"priyanshi" :43,  "sonu": 50, "priya": 45, "jiya":46}
students["yashvi"] = 43
print(students)

# delete a key value pair from a dictionary.

students = {"priyanshi" :43,  "sonu": 50, "priya": 45, "jiya":46}
del students["priya"]
print(students)

# merge two dictionaries into one.

dict1 = {"priyanshi" :43,  "sonu": 50 }
dict2 = {"priya": 45, "jiya":46}
result = dict1.update(dict2)
print(dict1)

# check if a key exists in a dictionary.

students = {"priyanshi" :43,  "sonu": 50, "priya": 45, "jiya":46}
if "priya" in students:
  print("key exists")
else:
  print("key is not exists")

# count word frequency in a given string using dictionary.

sentence = " python is easy and python is powerful"
words = sentence.split()
word_frequency = {}
for word in words:
  if word in word_frequency:
    word_frequency[word] += 1
  else:
    word_frequency[word] = 1
print(word_frequency)

# find the key with the maximum values in the dictionary.

students = {"priyanshi" :43,  "sonu": 50, "priya": 45, "jiya":46}
max_key = max(students, key=students.get)
print("Key with maximum value:", max_key)
print("Maximum value:", students[max_key])

# reverse key and value in a dictionary.

students = {"priyanshi" :43,  "sonu": 50, "priya": 45, "jiya":46}
reversed_dict = {value: key for key, value in students.items()}
print(reversed_dict)

# update the value for specific key.

students = {"priyanshi" :43,  "sonu": 50, "priya": 45, "jiya":46}
students["priya"] = 50
print(students)

# convert a list of tuples into a dictionary.

students = [("priyanshi" ,43), ("sonu",50) , ("priya", 45), ("jiya",46)]
students_dict = dict(students)
print(students_dict)