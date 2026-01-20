#string_operations

def to_upper(text):
    "covert string to uppercase"
    return text.upper()

def to_lower(text):
    "covert string to lowercase"
    return text.lower()

def reverse_string(text):
    "Reverse the given string"
    return text[::-1]

def count_characters(text):
    "count total characters in string"
    return len(text)

def is_palindrome(text):
    "check if string is palindrome"
    cleaned = text.lower().replace(" "," ")
    return cleaned == cleaned[::-1]

def count_vowels(text):
    "count number of vowels in string"
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count