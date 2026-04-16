# name = 'Alice'
# print(name)

# message = 'hello world'
# print(message)

# count = 0
# for i in message.lower():
#     if i in 'aeiou':
#         count += 1

# print(count)

# for num in range(10, 0, -1):
#     print('*' * num )
# for i in range(2,10):
#     print('*' * i)

# print(type(message))

# print(type(count))

# message1 = 'hello\nworld'
# print(message1)

# path = "C:\\Users\\Alice\\Documents"
# print(path)

# message = 'It\'s a beautiful day'
# print(message)

# quote = "She said , \"Hello!\""
# print(quote)

# message = "It's a beautiful day"
# quote = 'She said, "Hello!"'
# print(message)
# print(quote)

# message = 'hello\rworld'
# print(message)

# Part 3: String Concatenation
# Concept Overview
# Concatenation means combining (joining) strings together to create a new string.

# Step 9: Using the + Operator

# first_name = "john"
# last_name = 'Doe'
# full_name = first_name + last_name
# print(full_name)

# Adding Spaces:
"""first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(full_name)"""


# Step 10: Concatenating Multiple Strings

"""greeting = "Hello"
name = "Alice"

message = greeting + ", " + name + "!"
print(message)"""

"""street = '123 main st'
city = 'Boston'
state = "MA"
zip_code = '02101'
address = street + ", " + city + ', ' + state + ' ' + zip_code
print(address)"""

# Using the += Operator
# '+=' operator adds to an existing string

"""message = 'Hello'
message += ' world'
print(message)
"""
"""story = "Once upon a time, "
story += 'there was a python programmer. '
story += 'She wrote amazing code!'
print(story)"""

# step 12: Repeating String
# You can repeat string using the '*' operator:

"""laugh = 'ha'
print(laugh * 5)"""

"""separator = '-' * 50
print(separator)

print('Python! ' * 3)"""

# Convert number to strings first:
"""
age = 25
message = 'I am ' + str(age) + ' Years old'
print(message)"""

# Part 4: String Formatting (F-Strings)
# Concept Overview
# F-strings (formatted string literals) are the modern, best way to format string in Python (Python 3.6+)
# They let you embed variable directly inside strings!

# Step 14: Basic F-String Syntax
# Put an 'f' before the opening quote, then use `{variable_name}` to insert variables:

"""name = "Alice"
message = f'Hello, {name}!'
print(message)
"""

"""age = 25
message = f'I am {age} years old'
print(message)

"""
# Notes: F-string automatically convert numbers to strings!
# Step 15: multiple Variable in f-Strings
"""first_name = 'John'
last_name = 'Doe'
age = 30
message = f'My name is {first_name} {last_name} and I am {age} years old.'
print(message)"""

"""item = 'laptop'
price = 999.99
quantity = 2
message = f'You ordered {quantity} {item} for ${price} each.'
print(message)"""

# Step 16: Expressions in F-Strings
# You can put calculation and expressions in side the curly braces:
"""length = 10
width = 5
message = f'The area is {length * width} square meters'
print(message)"""

"""price = 100
tax_rate = 0.08
message = f'Total price: ${price + (price*tax_rate)}'

print(message)
"""

"""num1 = 15
num2 = 7
message = f'{num1} + {num2} = {num1 + num2}'
print(message)"""

# Step 17: formatting Numbers in F-Strings
# you can control how numbers are displayed
# limiting decimal places:
"""
price = 19.5559567
message = f'Price: ${price:.2f}'
print(message)"""

# Explanation: `:.2f` means "format as float with 2 decimal places"

"""pi = 3.14159265359
print(f'Pi to 2 decimals : {pi:.2f}')

print(f'Pi to 4 decimals : {pi:.4f}')"""

# Adding commas to large number
"""population = 1000000000
message = f'Population : {population:,}'
print(message)
salary = 75000
print(f'Salary: ${salary:,}')"""

# Step 18: Old-Style String Formatting (.format())
# Before f-string, python used the `.format()` method:

"""name = 'Alice'
age = 35
message = 'My name is {} and I am {} years old'.format(name, age)
print(message)"""

# With named placeholders:
"""message = 'Hello, {name}. You are {age} years old.'.format(name='BOb',age=25)
print(message)
"""
# Note: F-string are preferred because ther're  more readable and faster!

# Part 5: String indexing
# concept overview
# Each character in a string has a position (index). you can access individual characters using their index.
# Important : indexing starts at 0 (not 1)!
# String: P y t h o n
# index:  0 1 2 3 4 5

# Step 19: Accessing Characters by index

# use square brackets `[]` with the index number:
"""word = 'Python'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])"""
# Explanation: Index 5 is the last character (6 characters total, but indexing starts at 0)
# Step 20 : index Visualization
"""message = "Hello"
print(f"Character at index 0: {message[0]}")
print(f"Character at index 1: {message[1]}")

print(f"Character at index 2: {message[2]}")

print(f"Character at index 3: {message[3]}")

print(f"Character at index 4: {message[4]}")"""

# Step 21: Negative indexing
# Negative indices count from the end of the string

"""
String:   P  y  t  h  o  n
Positive: 0  1  2  3  4  5
Negative: -6 -5 -4 -3 -2 -1
"""
"""word = 'Python'
print(word[-1])"""
# Explanation: -1 is the last character
"""word = 'Python'
print(word[-2])"""
# Explanation: -2 is the second-to-last character

# Step 22: using indexing in practice
# Getting the first and last character:

"""name = 'Alexander'
first_letter = name[0]
last_letter = name[-1]

print(f'First: {first_letter}, Last: {last_letter}')"""

# Creating initials

"""first_name = 'John'
last_name = "Doe"
initials = first_name[0] + last_name[0]

print(initials)"""

# Step 23: Index Out of range Error
# BAD : Accessing an index that doesn't exist:

"""word = 'hi' 
print(word[5])"""

# Explanation : "hi" only has indices 0 and 1 (or -2 and -1)

# Good: Stay within valid indices:

"""word = 'Hi'
print(word[0])

print(word[1])

print(word[-1])

print(word[-2])
"""

# Part 6: convertin Data types
"""Concept Overview
Sometimes you need to convert between different data types:
=> Convert numbers to strings for display
=> Convert string to numbers for calculations
"""
# Step 24: Convertin to string - str()
# The `str()` function converts any value to a string:

"""age = 25
age_str = str(age)
print(age_str)
print(type(age_str))

price = 19.99
message = "The price is $" + str(price)
print(message)

x = 10
y = 20
result = str(x) + str(y)
print(result)"""
# Notice: This concatenates the strings "10" and "20", not adding the numbers!


# step 25: Converting to integer - int()
# The `int()` function converts stirngs (and floats) to integers:
"""
age_str = "25"
age = int(age_str)
print(age)
print(type(age))

num_str = '100'
num = int(num_str)
print(num)
print(type(num))"""

# Converting floats tto integers (truncates decimal):

"""price = 19.19
whole_price = int(price)
print(whole_price)
"""
# Notice: The decimal part is removed (not rounded!)

# Step 26: Converting to Float - float()
# The `float()` function converts strings (and integers) to floats:

"""price_str = '19.99'
price = float(price_str)
print(price)
print(type(price))

whole_number = 10
decimal_number = float(whole_number)
print(decimal_number)
print(type(decimal_number))
"""

# Step 27: Conversion Errors
# BAD : Converting invalid strings:
"""text = 'hello'
print(int(text))
"""
# Explanation : "hello" cannot be converted to a number!

# BAD : converting Stings with decimals to int:
"""
price = '19.99'
print(int(price))
"""
# Good : convert to float first, then to int:
"""num = float('19.99')
result = int(num)
print(result)"""

# Part: Essential String Methods
"""
Concept Overview
Strings have many built-in methods (functions) that perform useful operations
Syntax:
    `string_variable.method_name()`
Important: String methods do NOT change the original string (Strings are immutable). They return a NEW string
"""
# Step 28: upper() - Convert to UpperCase
# The `upper()` method converts all lowercase letters in a string to uppercase letters.
"""message = "hello world"
uppercase = message.upper()
print(uppercase)
print(message) #Original unchanged"""

"""
WHAT IT DOES:
=> Takes every lowercase letter (a-z) and converts it ot uppercase(A-Z)
=> Numbers, symbols, and spaces remain unchanged
=> Return a NEW string (original is not modified)
=> If the string is already uppercase, it return a copy
"""
# name = 'alice'
# print(name.upper())

# Practical use - case-insensitive comparison:
"""user_input = "YES"
if user_input.upper() == "YES":
    print("User agreed!")"""
"""
WHY USE upper():
=> User input validation: Compare user input regardless of case (YES,yes, Yes all become YES)
=> Display formatting: Show text in all caps for emphasis or titles
=> Data normalization: Store data consistently (e.g., country codes: "US", "UK" )
=> Searching: find text regardless of case by convertin both search term text
"""

# Step : lower() - Convert to Lowercase
# The `lower()` method converts all uppercase letters in a string to lowecase letters.

"""message = "HELLO WORLD"
lower_case = message.lower()
print(lower_case)
print(message)
"""
# NOTES
"""
WHAT IT DOES:
=> Takes every uppercase letter (A-Z) and converts it to lowercase (a-z)
=> Numbers, symbols, and spaces remain unchanged
=. If the string is already lowercase, it returns a copy
"""
"""
email = "User@EXAMPLE.COM"
normalized_email = email.lower()
print(normalized_email)
"""
# NOTES;
"""
WHY USE lower():
=> Email normalization: Store emails in lowercase for consistency (alice@email.com vs ALICE@EMAIL.COM should be the same)
=> Case-insensitive comparisons: Make comparisons work regarless of case
=> URL processing: URLs are oftern lowercase
=> Username storage: Store usernames consistently
=> Search functionality: Convert both search term and text to lowercase for matching
"""
# Common use case:
"""username = input("Enter username: ")
username = username.lower() 
print(username)"""

# Step 30: capitalize() - Capitalize First Letter
# The `capitalize()` method converts the first character to uppercase and all other characters to lowercase.

"""sentence = 'hello world'
capitalized = sentence.capitalize()
print(capitalized)
"""
# NOTES:
"""
WHAT IT DOES:
=> Makes the FIRST character uppercase
=> Makes ALL remaing characters lowercase
=> Return a NEW string
=> If the first character is not a letter, not change occurs
NOTICE: Only the FIRST letter is capitalized, rest are lowercase
"""
"""word = "pYtHoN"
print(word.capitalize())
"""
# NOTES:
"""
WHY USE capitalize():
=> Sentence formatting: Start stentences with a capital letter
=> Name formatting: Simple title case for single words
=> User input normalization: Fix user input that's all caps mixed case
"""
# important difference:
"""capitalized = 'HELLO WORLD' 
print(capitalized.capitalize()) #ONLY first letter capitalized
titled = 'HELLO WORLD'
print(titled.title()) #Each word capitalized"""

# step 31: title() - capitalize each Word
# The `title()` method converts the first character of each word to uppercase and all other character to lowercase.

"""book = 'the lord of the rings'
title_case = book.title()
print(title_case)
print(book)"""
# NOTES:
"""
What it does:
=> Capitalize the first letter of EVERY word
=> makes all other letters lowercase
=>Words are separated by spaces or punctuation
=> Return a NEW string
=>> Explanation: Each word starts with a capital letter
"""
# name = "john doe"
# print(name.title())
"""
Why use title():
=> Book titles: Format book, movie, or article titles
=> Names:  Format full names properly ("john smith"-->"John Smith" )
=> Headings: Create properly formatted headings
=> Addresses: Format street names and cities
"""

# Important notes:
"""
title_case = "i'm learning python".title()
print(title_case)"""
# The apsostrophe causes the next letter to be capitalized (m-->M), which may not be desired!

# Step:32 strip() - Remove Whitespace
# The `strip()` method removes spaces, tabs,and newlines form both ends:
"""
message = "    Hello World      "
cleaned = message.strip()
print(cleaned)
print(f"Original length: {len(message)}")
print(f"Cleaned length: {len(cleaned)}")

user_input = "  alice  \n"
username = user_input.strip()
print(username)"""
# Explanation: Very useful for cleaning user input!

# Variations:
"""
text = "    python      "
print(text.lstrip()) #Remove lift whitespace
print(text.rstrip()) #remove right whitespace
print(text.strip())  #Remove both sides whitespace"""

# NOTES:
"""
Method variations explained:
=> lstrip() - "Left strip" - removes whitespace from the LEFT (beginning) only
=> rstrip() - "Right strip" - removes whitespace from the RIGHT (end) only
=> strip() - Removes whitespace from BOTH sides

WHY USE strip():
=> Clean user input: Remove accidental spaces users type
=> File processing: Clean lines read form files
=> Data validation: Ensure clean data before comparisons
=> Form data: Clean form submissions
"""
# Comman pattern:
"""name = input("Enter you name: ")
name = name.strip()
print(name)
"""
# Step 33: replace() - Replace substrings
# The `replace()` method replace all occurrences of a substring with another substring.

"""message = 'i love Java'
new_message = message.lower().replace('java','python').upper()

print(new_message)"""
# NOTES:
"""
What it does:
=> Searches for ALL occurrences of the first string
=> Replaces them with the second string
=> Returns a NEW string
=> Original string is unchanged
=> Case-sensitive (won't replace "java" when looking for "Java)

"""
"""
text = 'hello world world world'
replaced = text.replace('world','Python')
print(replaced)
#NOtes: Replaces ALL occurrences by default"""

# Limiting Replacements:
"""text = 'apple apple apple'
replaced = text.replace('apple' , 'orange',2)
print(replaced)"""
# NOTES:
"""
The optional third parameter: Limits how many replacemnents to make (replaces from left to right)

WHY USE replace():
=> Text correction: Fix common typos or errors
=> Data cleaning: Remove or replace unwanted characters
=> String  manipulation: Transform text data
=> Formatting: Replace placeholders with actual values
"""
# Common users:
"""message = 'hello world'
print(message.replace(" ", ""))

text = 'line1\nline2\nline3\nline4'
print(text)
print(text.replace("\n", " "))"""

# step34: split() - split String into list
# The `split()` method breaks a string into a list of words or substrings.
"""sentence = 'Hello World Python'
words = sentence.split()
print(words)
print(type(words))
text = 'hello'
print(text.split())"""

# NOTES:
"""
What it does:
=>Breaks a string into multiple parts 
=> Returns a LIST of strings
=> By default, split on ANY whitespace (spaces, tabs, newlines)
=> Consecutive whitespace is treated as one separator
=> You can specify a different separator
# Explanation: By default, split on spaces
"""
# Splitting on specific characters:
"""csv_data = "apple,banana,orange"
fruits = csv_data.split(",")
print(fruits)"""
# Custom separator: The comma `,` is used to split the string
"""date = '2024-12-15'
parts = date.split("-")
print(parts)

year = parts[0]
month = parts[1]
day = parts[2]

print(f"year:{year}, month: {month}, day: {day}".title())
"""
# NOTES:
"""
WHY use split():
=> Parse data: Break apart CSV data, dates, paths, etc.
=> Prodess input: Split user input into words or tokens
=> Count words: Get a list of words to count them
=> Extract parts: Get specifc parts of strctured text
"""
# common patterns:
"""#Split on multiple spaces (consecutive spaces treated as one)
print("word1    word2       word3".split())
#Split into maximum 2 parts
print("one,two,three,four".split(',',2))"""

# Step 35: join() - Join List into String
# The `join()` method combines a list of strings into a single string, with a separator between each item.
"""words = ['Hello', 'World', 'Python']
sentance = " ".join(words)
print(sentance)"""

# NOTES:
"""
What it does:
=> Takes LIST of strings
=> Combines them into ONE string
=> Puts the separator (the string you call join on) between each item
=> Return a NEW string
# Explanation: Join list items with a space betweeb them
# Important: The separator is the string that `join()` is called on!
    `separator.join(list_of_strings)`
"""
# Example
"""fruits = ['apple', 'banana', 'orange']
csv = ', '.join(fruits)
print(csv)"""
# The separator is `", "` (comma and space)
"""letters = ['p','y','t','h','o','n']
word = "".join(letters)
print(word.title())"""
# Empty Separator: use`""` to join with nothing in between
"""
Why use join():
=> Build strings efficiently: More efficient than repeated concatenation
=> Create CSV data: Combine values with commas
=> Format output: Create formatted strings from lists
=> Reverse split(): Rebuild a string from parts
"""
# Common patterns:
# Create a path
"""print("/".join(['folder','subfolder','file.text']))
# Create a sentence with newlines
print("\n".join(['line1','line2','line3']))


url = str("https://skillopia.com/student/courses/672b658aaad1c640a53d3275/learn?lab=6916cf1be043930febe112e9".split("//"))
new_url = url.split('/')
for i in new_url:
    print(i)"""

# Note: All items in the list must be strings! This won't work:

# Step 36: find() - Find substring Position
# The `find()` method searches for a substring and returns the index (position) where it first appears.

"""text = 'Hello World'
position = text.find('World')
print(position)"""

# NOTES:
"""
What it does:
=> Searches for the substring from left to right
=> Return the INDEX of the first occurrence
=> Case-sensitive search
=> you can spcify where to start searching (optional)
# Explanation: "World" starts at index 6
"""
# Example:
"""
email = 'user@example.com'
at_postion = email.find('@')
print(at_postion)
"""
# Use Case: Finding the @ symbol in an email split userame and domain
# When substring is not found
"""text = "Hello World"
position = text.find('Python')
print(position)"""
# Explanation: Returns -1 when substring doesn't exist

# NOTES:
"""
Why use find():
=> Check id substring exists: Use `if text.find("word") != -1:`
=> Extract parts: Find position to split or extract text
=> Validation: Check if email has @, URL has http://, etc.
=> ParsingL find position of special characters
"""
# Advanced Usage:
"""#Find starting from a specific position
print("apple apple apple".find("apple", 6)) #start searching form index6
#Find the last occurrence (use rfind instead)
print("apple apple apple".rfind("apple"))"""

# Note: There's also an `index()` method that works like `find()`, but raises an error instead of returning -1 when the substring isn't found

# Step 37: count() - Count Occurrence
# The `count()` method counts how many times a substring appears in a string.
"""text = 'apple apple orange apple'
count = text.count("apple")
print(count)"""

# NOTES:
"""
What it does:
=> Searches the enire string
=> Counts ALL non-overlapping occurrences
=> Case-sensitive
=> Returns an integer (0 if not found)
"""
# Example:
"""sentence = "The quick brown for jumps over the lazy dog"
count = sentence.count('the')
print(count)
"""
# Notice: case-sensitive "The" and "the" are different

# Case-insensitive counting:
"""sentence = "The quick brown for jumps over the lazy dog"
count = sentence.lower().count('the')
print(count)"""
# Technique: Convert to lowercase first, then count
# NOTES:
"""
Why use count():
=> Frequency analysis: Count how often words appear
=> Data validation: Count how many times a character appears
=> statistics: Analyze text patterns
=> Quality checks: Count punctuation, vowerls, etc.
"""
# Exaples:
"""# Count a single character
print("Mississippi".count("s"))
# Count a substring
print("la la la la la la".count("la "))
# Count in a specific range (optional start and end positions)
print("abcabcabc".count("abc",3,9)) #Count between index 3 and 9

"""
# Step 38: startswith() and endswith()
# These methods check if a string begins or ends with a specific substring.

"""filename = 'document.pdf'
print(filename.endswith(".pdf"))
print(filename.endswith('.txt'))"""
# NOTES:
"""
What they do:
=> `startswith(substring)` - Return True if string starts with substring
=> `endswith(substring)` - Return True if string end with substring
=> Both are case-sensitive
=> Return Boolean values (True or False)
"""
# Example:
"""url = 'https://www.example.com'
print(url.startswith('https://'))
print(url.startswith('http://'))"""

# Practical use - file validation:
"""filename = 'photo.jpg'
valid_extensions = ['.jpg','png','.gif']
for ext in valid_extensions:
    if filename.endswith(ext):
        print(f'Valid image file: {filename}')
        break"""
# NOTES:
"""
Why use startswith() and endswith():
=> File type checking: Validate file extensions
=> URL validation: check protocol (http:// vs https://)
=> Prefix/suffix matching: Check if text has specific patterns
=> path handling: Check if path starts with specific directory
=> Data validation: Verify format of strings
"""
"""#check multiple possibilities (tuple)
print('hello.py'.endswith(('.py','.pyc','.pyw')))
#Case-insensitive check
url = 'HTTP://example.com'
print(url.lower().startswith('http://'))
#Advanced use:
#Specify start/end positions
print("document.pdf",0,12) #Check only first 12 characters
"""
# Step 39: String Test Methods
# These methods test the content of a string and return `True` and `False`.
# isdigit()- Check if all characters are digits:
"""print("123456".isdigit())
print("123456acb".isdigit())
print("".isdigit())"""
# NOTES:
"""
What it does:
=> Returns True if ALL characters are digits (0-9)
=> Returns False if string is empty
=> Return False if there are any non-digit characters (including space, perods, or minus signs)

Why use isdigit():
=> Validate numeric input: Check if user enterd only numbers
=> Data cleaning: Verify data before convertin to int
=> Phone numbers: Check if input contains only digits
"""
# Example use case:
"""user_age = input("Enter your age : ")
if user_age.isdigit():
    age = int(user_age)
    print(f"You are {age} years old")
else:
    print("Please enter only numbers")
"""
# isalpha() - Check if all characters aare letters:

"""print("hello".isalpha())
print("hello123".isalpha())
print("Hello world".isalpha())"""

# NOTES:
"""
What it does:
=> Return True if ALL characters are letters (a-z, A-Z)
=> Return False for numbers, spaces, or punctuation
=> Return False if string is empty
#Notice: Spaces are not letters!
Why use isalpha():
=> Name validation: Check if name contains only letters
=> Text analysis: Filter words that are pure alphabetic
=> Data validation: Ensure no numbers or symbols
"""
# isalnum() - check if all characters are letters or digits:
"""print("Hello123".isalnum())
print("Hello 123".isalnum())"""

# NOTES:
"""
What it does
=> Returns True if ALL characters are either letters or digits
=> No spaces, punctuation, or special characters allowed
=> Combination of isalpha() and isdigit()
Why use isalnum():
=> Username validation: Usernames often allow only letters and numbers
=> Password checking: Check if password contains only alphanumeric characters
=> Code generation: Validate generated codes
"""
# isspace() - Check if all characters are whitespace:
"""print("   ".isspace())
print("   a   ".isspace())"""
# NOTES:
"""
What it does:
=> Returns True if ALL characters are whitespace (spaces, tabs, newlines)
=> Returns False if string is empty
=> Returns False if there's any non-whitespace character

# Why use isspace():
=> empty input detection: Check if user just pressed Enter/Space
=> Datacleaning: Identify whitespace-only entries
=> Validataion: Reject whitespace-only input
"""
# Example:
"""name = input("Enter name: ")
if not name or name.isspace():
    print("Name canot be mepty!")"""

# inlower() and isupper():
"""print("hello".islower())
print("HELLO".isupper())
print("HELLO".islower())
print("hello".isupper())"""

# NOTES:
"""
What they do:
=> `islower()` - Return True if ALL letters are lowercase (ignores numbers/symbols)
=> `isupper()` - Return True if ALL letters are uppercase (ignores numbers/symbols) 
=> At least one letter must be present
=> Numbers and symbols are ignored
"""
# Important notes:
"""print('hello123'.islower())
print('HELLO123'.isupper())
print('123'.islower())
print('123'.isupper())"""
# NOTES:
"""
Why use islower() and isupper():
=> Format checking: Verify text is in expected case
=> Data validation: Ensure consistent formatting
=> Text analysis: Categorize text by case
"""
# Step 40: len() - String Length
# `len()` function returns the number of characters in a string.
"""message = "hello"
length = len(message)
print(length)"""
# NOTES:
"""
What it does:
=> Counts ALL characters (including spaces, punctuation, and special characters)
=> Returns an integer
=> Empty string has length 0
#Notes: `len()` is a function, not a method (you don't call it with a dot)
"""
"""password = 'MySecurePassword123'
print(f'Password length: {len(password)}')
#Check password length:
password1 = 'abc'
if len(password1) < 8:
    print("password too short! Must be at least 8 characters.")"""

# NOTES:
"""
Why use len():
=> Validation: Check if input meets length requirements
=> Limits: Enforce maximun character counts (tweets, forms, etc.)
=> Analysis: Count characters for statistics
=> Iteration: Know how many characters to loop through
"""
# print(len('hello\n'))
# Note : Each escape sequence like `\n` count as ONE character, eve though it looks like two in the code!

# Part : Multi-line Strings
# Concept Overview
# multi-line strings span miltiple lines, use triple quotes (""" or ''')

# Step Create multi-line Strings
"""poem = '''
Roses are red
Violets are blue
Python is awesome
and so are you
'''
print(poem)"""

# Step 42: Multi-Line Strings in Code
'''email_template = """
Dear {name},

Thank you for your purchase of {item}.
your order total is ${price}.


Best regards,
The Team
""" 
message = email_template.format(name='Alice', item='Laptop', price=999.99)
print(message)'''

# Part 9: Raw Strings
"""
Concept Overview
=> Raw Strings ignore escape sequences. Put an `r` before the opening quote.
"""
# file_path = r'C:\Users\Alice\Documents\file.txt'
# print(file_path)

# pattern = r'\d{3}-\d{3}-\d{4}' #phone number pattern
# print(pattern)

# word = "Python"
# new_word = "J"+word[1:]
# print(new_word)

# word = 'python'
# new_word = word.replace('p','J')
# print(new_word)
# print(word)

# title = "Python"
# print(title.center(50, '-'))
# print(title.ljust(25, "*"))
# print(title.rjust(25, "="))

# Create table
# print("Name".ljust(15), "age".rjust(5))
# print("Prakash".ljust(15), "24".rjust(5))

# Center a tiltle
# print("MENU".center(40,"="))

# text = "Hello World"
# print(text.swapcase())

# zfill()

# number = "42"
# print(number.zfill(5))
# name = "prakash"
# print(name.zfill(10))
# invoice = '123'
# print(f'Invoice : {invoice.zfill(6)}')

# for i in range(1,4):
#     filename = f'image_{str(i).zfill(3)}.jpg'
#     print(filename)

# print("-5".zfill(5))
# print('+5'.zfill(5))

# url = 'https://www.example.com'
# print(url.removeprefix("https://"))
# filename = 'docutment.txt'
# print(filename.removesuffix('.txt'))
# print("report.pdf".removesuffix('.pdf'))
# print('report.pdf'.removesuffix('txt'))
# print(url.removeprefix('https://').removeprefix('www.'))

# email = "user@example.com"
# parts = email.partition('@')
# print(parts)
# print(email.split('@'))

# path = 'folder/subfolder/file.txt'
# print(path.rpartition('/'))

# email = 'john.doe@company.com'
# username,sep,domain = email.partition("@")
# print(f'User: {username}, Domain: {domain}')

# filename = 'document.final.pdf'
# name, sep, ext = filename.rpartition('.')
# print(f'Name : {name}, Extension: {ext}')

# text = 'Name:\tAlice'
# print(text.expandtabs(4))
# print('a\tb\tc'.expandtabs())
# print('a\tb\tc'.expandtabs(2))
# print('Name:\t\tAge:\t\tCity'.expandtabs(10))

# TASK 1 personal Introduction
# first_name = 'Prakash'
# last_name = 'Singh'
# age = 24
# city = 'mumbai'
# occupation = 'Software Engineer'

# introduction = f'Hello! My name is {first_name} {last_name}. I am {age} years old, and I work as a {occupation} in {city}'
# print(introduction)

# TASK 2 String Formatting practice
"""product = 'laptop'
price = 999.99
quantity = 3
tax_rate = 0.08

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f'Product: {product.title()}')
print(f'Price per item: ${price:.2f}')
print(f'Quantity: {quantity}')
print(f'Subtotal: {subtotal}')
print(f'Tax (%8): ${tax}')
print(f"total: ${total:.2f}")"""


# TASK 3 String methods practics => upper(), lower() and title()
"""message = "python is AMAZING and easy TO learn"

print('Original:',message)
print('Uppercase:',message.upper())
print('Lowercase:' , message.lower())
print('Title case',message.title())
print('Capitalized:',message.capitalize())
print('Swapcase:',message.swapcase())"""

# TASK 4 Email Cleaner => strip() and lower() to clear user input
# email1 = 'ALICE@EXAMPLE.COM  '
# email2 = 'Bob@Example.Com   \n'
# email3 = '  charlie@EXAMPLE.COM'
# clean_email1 = email1.strip().lower()
# clean_email2 = email2.strip().lower()
# clean_email3 = email3.strip().lower()

# print(f'Email1 : "{clean_email1}"')
# print(f'Email2 : "{clean_email2}"')
# print(f'Email3 : "{clean_email3}"')

# TASK 5: Word Counter : use split() and len() to count words.

"""sentence = "Python is a powerfull and versatile programming language"

words = sentence.split()
word_count = len(words)
char_count = len(sentence)

print(f'Sentence: {sentence}')
print(f"Number of words: {word_count}")
print(f"Number of characters: {char_count}")"""

# TASK 6: Replace Words : use replace() method.
"""
original = "I love Java because Java is powerfull and Java is popular"

modified = original.replace("Java", "Python")

print("Original : ", original)
print(f"Modified: {modified}")
"""

# TASK 7: Name Extractor : Use split() to extract parts
"""
full_name = "Alice marie Johnson"

parts = full_name.split()

first_name = parts[0]
middle_name = parts[1]
last_name = parts[2]

print(f"fist name : {first_name}")
print(f'Middle name : {middle_name}')
print(f"Last name : {last_name}")

print(f"Initials: {first_name[0]}{middle_name[0]}{last_name[0]}".upper())"""

# TASK 8: CSV Data Parser : Parse comma-separated data.
"""csv_line = "John,Doe,30,Engineer,New York"
fields = csv_line.split(',')

first_name = fields[0]
last_name = fields[1]
age = fields[2]
job = fields[3]
city = fields[4]

print(f"First name : {first_name}")
print(f"Last name : {last_name}")
print(f"Age : {age}")
print(f"Job : {job}")
print(f"City : {city}")"""

# TASK 9: File Extension Checker => use endswith to check file types

"""file1 = 'document.pdf'
file2 = 'photo.jpg'
file3 = 'script.py'
file4 = 'data.txt'
file5 = 'script.c'

files = [file1,file2,file3,file4,file5]
for file in files:
    if file.endswith(".pdf"):
        print(f"{file } is a Pdf documnet")
    elif file.endswith('jpg'):
        print(f'{file} is an image file')
    elif file.endswith('py'):
        print(f'{file} is a python file')
    elif file.endswith('txt'):
        print(f'{file} is a txt file')
    else:
        print(f"{file} is another type of file")

"""

# TASK 10: password validator : use string method to validate password

"""password = 'MyPassword123'

length_check = len(password) >= 8

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)

print(f'Password : {password}')
print(f"Has uppercase : {has_upper}")
print(f'Has lowercase: {has_lower}')
print(f'Has digit: {has_digit}')
print(f'Valid : {length_check and has_upper and has_lower and has_digit}')
"""

# TASK 11: Text Alignment : use center(), ljust(), rjust()

"""title = 'PYTHON'

subtitle =' Programming Language'

print(title.center(30,'='))
print(subtitle.center(30))
print("First Name".ljust(5) , 'Prakash'.rjust(20))
print("Last name".title().ljust(5), "singh".title().rjust(19))
print("Age".ljust(5),'24'.rjust(20))
print('=' * 30)"""

# TASK 12: Count Vowels : Use count() method.
"""text = 'hello Word, Python is Amazing!'
text_lower = text.lower()

count_a = text_lower.count('a')
count_e = text_lower.count('e')
count_i = text_lower.count('i')
count_o = text_lower.count('o')
count_u = text_lower.count('u')

total_vowels =  count_a + count_e+count_i+count_o+count_u
print(f'Text: {text}')
print(f'a:{count_a}, e: {count_e}, i: {count_i}, o: {count_o}, u: {count_u}')
print(f'Total vowels: {total_vowels}')"""

# TASK 13: URL Parser : Extrat parts form a URL
"""url = "https://www.example.com/products/items123"

protocol_end = url.find("://")
protocol = url[:protocol_end]

remaining = url[protocol_end + 3 :]
domain_end = remaining.find('/')
domain = remaining[:domain_end]
path = remaining[domain_end:]

print(f'full URL: {url}')
print('Protocol : {}'.format(protocol))
print('Domain : {}'.format(domain))
print(f'Path: {path}')

print(f'End domain": {domain_end}')
"""
# TASK 14: String Reversal => reverse a string useing indexing

"""word = 'Python'
reversed_word = word[::-1]

print(f'Original: {word}')
print(f'Reversed: {reversed_word}')"""

# TASK: multi-Line Receipt => Create a formatted receipt.
'''store_name = "python store"
item1 = "laptop"
price1 = 999.99
item2 = "Mouse"
price2 = 29.99
item3 = "keyboard"
price3 = 79.99

subtotal = price1 + price2 + price3
tax = subtotal * 0.08
total = subtotal + tax

receipt = f"""
{'=' * 40}
{store_name.title().center(40)}
{'=' * 40}
{item1.title().ljust(30)} ${price1:>7.2f}
{item2.title().ljust(30)} ${price2:>7.2f}
{item3.title().ljust(30)} ${price3:>7.2f}

{'-' * 40}
{'Subtotal:'.ljust(30)} ${subtotal:>7.2f}
{'Tax (8%):'.ljust(30)} ${tax:>7.2f}
{'Total:'.ljust(30)} ${total:>7.2f}
{'=' * 40}


Thank you for shopping with us!
"""

print(receipt)'''


DATA = """
BEGIN:VCARD
VERSION:3.0
N:Iron;Hr;Raipur;;
FN:Hr Raipur Iron
TEL;type=Mobile;waid=917377374674:+91 73773 74674
X-WA-BIZ-DESCRIPTION:Association for the Steel Traders of Raipur Chhattisgarh
X-WA-BIZ-NAME:Hr Raipur Iron
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Mishra;Hr Sakhamabari;Sudhir;;
FN:Hr Sakhamabari Sudhir Mishra
TEL;type=Mobile;waid=919669302444:+91 96693 02444
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Mishra;Siupl Hr;Ajay;;
FN:Siupl Hr Ajay Mishra
TEL;type=Home;waid=918224060207:+91 82240 60207
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raigarh;Hr;Salasar;;
FN:Hr Salasar Raigarh
TEL;type=Mobile:+91 77140 61978
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raigarh;Hr;Singhal;;
FN:Hr Singhal Raigarh
TEL;type=Mobile;waid=919981260070:+91 99812 60070
X-WA-BIZ-DESCRIPTION:Success has a simple formula: do your best, and people may like it.”
X-WA-BIZ-NAME:Hr Singhal Raigarh
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Bajrang;Power;;
FN:Hr Bajrang Power Raipur
TEL;type=Mobile:+91 77142 88035
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Concorit;tmt;;
FN:Hr Concorit tmt Raipur
TEL;type=Mobile;waid=917389913151:+91 73899 13151
X-WA-BIZ-NAME:Hr Concorit tmt Raipur
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Ishwar;Ispat;;
FN:Hr Ishwar Ispat Raipur
TEL;type=Mobile;waid=916262322006:+91 62623 22006
X-WA-BIZ-DESCRIPTION:BANK DETAIL

ISHWAR ISPAT INDUSTRIES PVT.LTD
PUNJAB NATIONAL BANK
A/C.NO.-7484008700000431
IFSC CODE..PUNB0748400
DEVENDRA NAGAR BRANCH, RAIPUR (C.G)
X-WA-BIZ-NAME:Hr Ishwar Ispat Raipur
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Maruti;Ferroes;;
FN:Hr Maruti Ferroes Raipur
TEL;type=Mobile:+91 80 4581 1752
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Nandan;Tmt;;
FN:Hr Nandan Tmt Raipur
TEL;type=Mobile:+91 99812 07292
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Santurn;Ferrous;;
FN:Hr Santurn Ferrous Raipur
TEL;type=Mobile:+91 77140 93970
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Sarthak;Tmt;;
FN:Hr Sarthak Tmt Raipur
TEL;type=Mobile;waid=919300000722:+91 93000 00722
X-WA-BIZ-NAME:Hr Sarthak Tmt Raipur
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Shristhi;Tmt;;
FN:Hr Shristhi Tmt Raipur
TEL;type=Mobile;waid=919893021933:+91 98930 21933
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Sourbh;Roling;;
FN:Hr Sourbh Roling Raipur
TEL;type=Mobile:+91 77142 23000
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr Vandana;Global;;
FN:Hr Vandana Global Raipur
TEL;type=Mobile:+91 77142 35555
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr;Bhagvati;;
FN:Hr Bhagvati Raipur
TEL;type=Mobile:+91 77140 41346
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr;Khudargadhi;;
FN:Hr Khudargadhi Raipur
TEL;type=Mobile:+91 77149 17475
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr;Lingraj;;
FN:Hr Lingraj Raipur
TEL;type=Mobile;waid=917999060824:+91 79990 60824
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr;Mahamaya;;
FN:Hr Mahamaya Raipur
TEL;type=Mobile:+91 77149 10058
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr;Resmi;;
FN:Hr Resmi Raipur
TEL;type=Mobile:+91 77123 25449
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr;Sks;;
FN:Hr Sks Raipur
TEL;type=Mobile:+91 22 3080 7000
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Raipur;Hr;Vandana;;
FN:Hr Vandana Raipur
TEL;type=Mobile:+91 77125 35244
END:VCARD

BEGIN:VCARD
VERSION:3.0
N:Raipur;Sapna Steel;Hr;;
FN:Sapna Steel  Hr Raipur
TEL;type=Mobile;waid=919907122431:+91 99071 22431

END:VCARD
""".lower()
# cards = DATA.split("end:vcard")

# # print(card)
# for card in cards:

#     FN = card.find("fn:")
#     TEL = card.find("tel")
#     NAME = card[FN + 3 : TEL]
#     description = card.find("description:",TEL)
#     end_d = card.find("x-wa-biz-name:")
#     # print(description)
#     # print(end_d)
#     company = card[description + 12 : end_d] if description != -1 else ''
   
#     equal = card.find("+91")
#     number = card[equal + 4 : equal + 17]
#     # print(NAME)
#     print(f"Name         : {NAME.rjust(30)} ")
#     print(f'Phone number : {number.rjust(30)}')
#     print(f'company name : {company.rjust(30)}')
#     print('-'*50)










