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