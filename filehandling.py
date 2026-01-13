#1 WAP to read a file and display its content.

file_name = input("Enter the file name to read: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()   
        print("\nFile Content:\n")
        print(content)

except FileNotFoundError:
    print("File not found. Please check the file name.")

#2 WAP to count the number of lines in a file.

file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()      
        line_count = len(lines)       

    print("Number of lines in the file:", line_count)

except FileNotFoundError:
    print("File not found. Please check the file name.")

#3 WAP to count how many times each word appear in file.

file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        text = file.read()   

    text = text.lower()
    words = text.split()
    word_count = {}

    for word in words:
        word = word.strip(".,!?;:\"()[]{}")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print("\nWord Frequency in the file:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print("File not found. Please check the file name.")

#4 WAP to writes 5 user entered sentences to a file.

file_name = input("Enter the file name to write: ")

with open(file_name, 'w') as file:
    for i in range(1, 6):
        sentence = input(f"Enter sentence {i}: ")
        file.write(sentence + "\n")   

print(f"5 sentences have been written to {file_name}")

#5 WAP to append a list of a strings to an existing file.

file_name = input("Enter the file name to append: ")

lines_to_append = [
    "This is the first new line.",
    "Python makes file handling easy.",
    "Appending text to files is simple.",
    "Always make sure the file exists.",
    "End of appended lines."
]

try:
    with open(file_name, 'a') as file:
        for line in lines_to_append:
            file.write(line + "\n") 

    print(f"{len(lines_to_append)} lines have been appended to {file_name}")

except FileNotFoundError:
    print("File not found. Please check the file name.")

#6 WAP to read a file and print only lines containing a specific word.

file_name = input("Enter the file name: ")
word_to_search = input("Enter the word to search: ").lower()

try:
    with open(file_name, 'r') as file:
        print(f"\nLines containing '{word_to_search}':\n")
        for line in file:
            if word_to_search in line.lower():
                print(line, end='')  

except FileNotFoundError:
    print("File not found. Please check the file name.")

#7 WAP to replace a specific word in a file and save changes.

file_name = input("Enter the file name: ")

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()

    content = content.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(content)

    print(f"All occurrences of '{old_word}' have been replaced with '{new_word}' in {file_name}.")

except FileNotFoundError:
    print("File not found. Please check the file name.")

#8 WAP to merge the contents of two text files into third file.

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
file3 = input("Enter third file name (merged file): ")

try:
    with open(file3, 'w') as f3:
        with open(file1, 'r') as f1:
            f3.write(f1.read())
            f3.write("\n")   

        with open(file2, 'r') as f2:
            f3.write(f2.read())

    print(f"Contents of '{file1}' and '{file2}' have been merged into '{file3}'.")

except FileNotFoundError:
    print("One of the files was not found. Please check the file names.")

#9 WAP to read csv file and display its content in a formated way.

import csv
try:
    with open("data.csv", "r") as file:
        csv_reader = csv.reader(file)
        
        print("CSV File Content:\n")
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print("Error: CSV file not found.")

#10 WAP to backup a file by copying its contents into another file.

source_file = input("Enter source file name: ")
backup_file = input("Enter backup file name: ")

try:
    with open(source_file, 'r') as src:
        content = src.read()

    with open(backup_file, 'w') as backup:
        backup.write(content)

    print(f"Backup created successfully as '{backup_file}'")

except FileNotFoundError:
    print("Source file not found. Please check the file name.")
