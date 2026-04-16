# print("What is your name?")
# name = input()
# print(f'Hello, {name}!')

# name = input("what is your name: ")

# print(f'Hello, {name}!')
# age = input("Enter your age: ")
# print(age)
# print(type(age))

# num1 = input("Enter Frst number: ")
# num2 = input('Enter second number: ')

# result = num1 + num2
# print(result)

"""print("Welcom to the Greeting Program!")
print('-'*40)

name = input("What is your name? : ")
age = input("How old are you? : ")
city = input('Where do you live? : ')
print("\n" + '='*40)
print('YOUR INFOMATION'.center(40,' '))
print('='*40)
print('Name: {}'.format(name))
print(f'Age: {age}')
print(f'City: {city}')
print(f'\nNice to meet you, {name} from {city}!')"""

# age_str = input("Enter your age: ")
# age = int(age_str)
# print(type(age))

# age =int(input('Enter your age: '))
# next_year = age+1
# print(f"next year you will be {next_year}")

# height = float(input('Enter your height in meters : '))
# print(f'Your height is {height} meters')
# print(type(height))


"""print("=" * 40)
print("simple calculator".title().center(40, " "))
print("=" * 40)
print()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print()
print('result:'.upper())
print(f'{num1} + {num2} = {num1+num2}.rjust(30)')
print(f'{num1} - {num2} = {num1-num2}.rjust(30)')
print(f'{num1} * {num2} = {num1*num2}.rjust(30)')
print(f'{num1} / {num2} = {num1/num2}.rjust(30)')
"""
# check input before converting
"""agr_str = input("Enter your age: ")
print(f'You entered: "{agr_str}"')
print(f'Is it all degits? "{agr_str.isdigit()}"')"""

# work with None
"""middle_name = None
print(middle_name)
print(type(middle_name))"""

# useing None for optional informatino

"""print("Creat Your Profile")
print('-'*40)

name = input("Enter your name: ")
email = input("Enter yor email: ")

phone = input("Enter Your phone (or press Enter to skip)")
website = input('enter your website (or press Enter to skip)')

phone = phone or None
website = website or None

#display profile

print('YOUR PROFIL'.center(40,'='))
print(F'Name : {name}')
print(f'Email: {email}')
print(f'Phone: {phone}')
print(f'Website: {website}')"""

"""name = 'shiv'
middle_name=None
last_name = 'dev'

middle_part = f'{middle_name}' if middle_name else ''

print(f'full name : {name}{middle_part} {last_name}')"""

# temperature converter
"""print('='*50)
print('TEMPERATURE CONVERT'.center(50))
print('='*50)
print()
celsius = float(input('Enter temperatur in celsius: '))
fahrenheit = (celsius*9/5) +32

print()
print('-'*50)
print(f'{celsius}C = {fahrenheit}F')
print('-'*50)"""

# step 17: BMI Calculator

"""print('='*50)
print('BMI CALCULATOR'.center(50))
print('='*50)
print()

name = input("enter Your name: ")
weight = float(input('Enter Your weight (kg): '))
height = float(input('Enter your height (m): '))

#formula : BMI = WEIGHT/HEIGHT^2

bmi = weight/(height**2)
print()
print('='*50)
print(f'BMI RESULT FOR {name.upper()}'.center(50))
print('='*50)
print(f'Weight: {weight}')
print(f'Height: {height}')
print(f'BMI: {bmi:.2f}')
print('='*50)

#Information about BMI categories
print('\nBMI Categories:')
print('Below 18.5 underweight')
print('15.5 - 24.9 Normal')
print('25.0 - 29.9: Overweight')
print('30.0 and above: Obese')"""


# Step 18: Tip Calculator

"""print("=" * 50)
print("TIP CALCULATOR".center(50))
print("=" * 50)
print()

# get bill information
bill_amount = float(input("Enter bill amount: $"))
tip_percentage = float(input("Enter tip percentage (e.g., 15 for 15%)"))
num_people = int(input("number fo people splitting the bill"))

# Calculate tip and totals
tip_amount = bill_amount * (tip_percentage / 100)
total_with_tip = bill_amount + tip_amount
per_person = total_with_tip / num_people

#display result
print('='*50)
print('BILL BREAKDOWN'.center(50))
print('='*50)

print(f'Bill Amount:         ${bill_amount:>10.2f}')

print(f'Tip ({tip_percentage}%):       ${tip_amount:>10.2f}')
print('-'*50)
print(f'Total:               ${total_with_tip:>10.2f}')
print('='*50)
print(f'Per person: ({num_people}):     ${per_person:>10.2f}')
print('='*50)
"""

# step 19: Age calculator

"""print("=" * 50)
print("AGE CALCULATOR".center(50))
print("=" * 50)
print()
#GET birth year
current_year = 2026
birth_year = int(input('Enter Your birth year: '))

#calculator age
age = current_year - birth_year

#calculator in different units
age_months = age*12 
age_weeks = age*52
age_days = age*365
age_hours = age_days *24
age_minuts = age_hours*60
print()
print("=" * 50)
print("YOUR AGE IN DIFFERENT UNITS".center(50))
print("=" * 50)
print(f'years:  {age:>15,}')
print(f'Months: {age_months:>15,}')
print(f'Weeks:  {age_weeks:>15,}')
print(f'Days:   {age_days:>15,}')
print(f'Hours:  {age_hours:>15,}')
print(f'Minuts: {age_minuts:>15,}')
print('='*50)"""


# Step 20: Shopping Cart Total
"""print("=" * 50)
print("SHOPPING CART CALCULATOR".center(50))
print("=" * 50)
print()

# get items
print("Enter item prices (we'll get 3 items)")
print()
item1_name = input("Item 1 name : ")
item1_price = float(input("Item 1 price: $"))

item2_name = input("Item 2 name: ")
item2_price = float(input("item 2 price"))

item3_name = input("Item 3 name: ")
item3_price = float(input("Item 3 price"))


# calculate totals
subtotal = item1_price + item2_price + item3_price
tax_rate = 0.08
tax = subtotal * tax_rate
total = subtotal + tax
#Display receipt
print()
print("=" * 50)
print("RECEIPT".center(50))
print("=" * 50)

print(f'{item1_name.ljust(30)} ${item1_price:>8.2f}')
print(f'{item2_name.ljust(30)} ${item2_price:>8.2f}')
print(f'{item3_name.ljust(30)} ${item3_price:>8.2f}')
print('-'*50)
print(f'{"Subtoal:".ljust(30)} ${subtotal:>8.2f}')
print(f"{'tax (8%):'.ljust(30)} ${tax:>8.2f}")
print('='*50)
print(f'{"TOTAL:".ljust(30)} ${total:>8.2f}')
print('='*50)"""


# part 5: Combining input with string methods

# step 21: cleaning User input with strip()
"""print('Create Your username')
print()
username = input('Enter Username')
print("You entered: '{}'".format(username))
#clean the username
username = username.strip()
print(f'After cleaning: "{username}"')"""


# step 22: Converting input to consistent case

"""email = input('Enter your email: ')
print(f'Original: {email}')

#Normalize to lowercase
email = email.lower()
print(f'Normalized: {email}')"""

# step 23: checking email format
"""while True:
    email = input('Enter Your email: ').strip().lower()

    #check for basic email components
    has_at = "@" in email
    has_dot = '.' in email
    at_count= email.count('@')

    print()
    print("=" * 50)
    print("EMAIL FORMAT CHECK".center(50))
    print("=" * 50)
    print(f'Email: {email}')
    print(f'has @ symbol: {has_at}')
    print(f'has dot symbol: {has_dot}')
    print(f'Number of @ symbol: {at_count}')
    print('='*50)

    if has_at and has_dot and at_count==1:
        print(f'mail Id : {email}')
        break
    else:
        print('Please Enter valid email id')"""

# Step 24: Name formatter

"""print("=" * 50)
print("NAME FORMATTER".center(50).title())
print("=" * 50)

full_name = input('Enter Your Full Name: ')

#Clean and format
full_name = full_name.strip().title()

print(f'\nFormatted name: {full_name}')

#EXTRACT PART
parts = full_name.split()


print(f'Number of name parts: {len(parts)}')
print(f'First Part: {parts[0]}')
print(f'Last part: {parts[-1]}')

#create initials
initials = ""
for part in parts:
    initials += part[0]

print(f'Initials: {initials}')"""

# Step 25: Word Counter
"""print("=" * 50)
print("WORD COUNTER".center(50).title())
print("=" * 50)

text = input("Enter some text: ")

# count different things
words = text.split()
word_count = len(words)
char_count = len(text)
char_no_spaces = len(text.replace(" ", ""))

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    vowel_count += vowels.count(char)

print()
print("=" * 50)
print("STATISTICS".center(50).title())
print("=" * 50)
print(f"Words:  {word_count:>10}")
print(f"Characters: {char_count:>10}")
print(f"Chars (no spaces): {char_no_spaces:>10}")
print(f"Vowels: {vowel_count:>10}")
print(f"spaces: {char_count - char_no_spaces}")"""

# Step 26: Phone number Formatter

"""print("=" * 50)
print("phone number formatter".center(50).title())
print("=" * 50)
print()

phone = input('Enter phone number (digits only): ')

#remove any non-digit characters
phone_digit = ''
for char in phone:
    phone_digit += char if char.isdigit() else ''

print(f'Original input: {phone}')
print(f'Digits only: {phone_digit}')
print(f'Number of digits : {len(phone_digit)}')

#Format as (xxx) xxx-xxxx (for 10 digit numbers)
area_code = phone_digit[0:3]
prefix = phone_digit[3:6]
line_number = phone_digit[6:10]

formatted = f'({area_code}) {prefix}-{line_number}'
print(f'Formatted: {formatted}')"""

# step 27: Passowrd Strength Checker
"""print("=" * 50)
print("password strength checker".center(50).title())
print("=" * 50)

password = input('Enter a password to check: ')

#check various criteria
length = len(password)
has_upper = password != password.lower()
has_lower = password != password.upper()
has_digit = any(char.isdigit() for char in password)

#Count different character types
upper_count = sum(1 for char in password if char.isupper())
lower_count = sum(1 for char in password if char.islower())
digit_count = sum(1 for char in password if char.isdigit())
special_count = sum(1 for char in password if char.isalnum())

print()
print("=" * 50)
print("password strength analysis".center(50).upper())
print("=" * 50)
print(f'length: {length} characters')
print(f'has uppercase: {has_upper}')
print(f'has lowercase: {has_lower}')
print(f'has digit : {has_digit}')
print('-'*50)
print(f'Uppercase letters: {upper_count}')
print(f'Lowercase letters: {lower_count}')
print(f'Digits: {digit_count}')
print(f'Special characters: {special_count}')
print('='*50)"""


# Part 6: Practice Tasks

# task 1: Distance converter => convert kilometers to miles

"""print('='*50)
print("distance converter kilometer into miles".upper())
print('='*50)


kilometers = float(input("Enter distance in kilometers: "))

#convert into miles
miles = (kilometers* 0.621371)


print('\n{} km = miles {}'.format(kilometers,miles))"""


# TASK 2: CIRCLE AREA CALCULATOR => Calculate circle form radius.
# formula : area = pi * radius^2

"""print('='*50)
print('cricle area calculator'.center(50).upper())
print('='*50)

PI = 3.14159

radius = float(input('Enter radius of the circle: '))

area = PI * (radius**2)
circumference = 2 * PI * radius

print(f'\nradius: {radius}')
print(f'Area = {area:.2f}')
print(f'Circumference ; {circumference:.2f}')
print('='*50)"""


# TASK 3: Grade Average Calculator => calculate average of three grades.
"""print('grade average calculator'.center(50).title())
print('='*50)

grade1 = float(input('Enter grade 1: '))
grade2 = float(input('Enter grade 2: '))
grade3 = float(input('Enter grade 3: '))

avg = (grade1 + grade2 + grade3) /3

print('-'*50)
print(f'\n Grades: {grade1} {grade2} {grade3}')

print('-'*50)
print(f'Agerage: {avg:.2f}')"""

# TASK 4: Second converter => convert second to hours, minutes, and second

"""print("Seconds to time convert".center(50).title())
print("=" * 50)

total_second = float(input("enter number of seconds: "))

hours = total_second // 3600
remaining = total_second % 3600
minuts = remaining // 60
seconds = remaining % 60

print(f'\n{total_second} Seconds equals: ')
print(f'{hours} hours, {minuts} minuts, {seconds} seconds')"""


# Task 5: Compound Interest Calculator
# formola : A = P(1+r)^t

"""print('compound interest calculator'.title())
print('='*50)

principal = float(input('Enter principal amount: $'))
rate = float(input('Enter annual interest rate (e.g, 5 for 5%): '))
years = int(input('Enter number of years: '))

#convert rate to decimal

rate_decimal = rate /100

#Calculate final amount
amount = principal * ((1+rate_decimal)**years)
interest = amount - principal

print()
print('='*50)
print('investment summary'.upper().center(50))
print('='*50)
print(f'Principal : ${principal:>10.2f}')
print(f'Interest Rate: {rate:>10.2f}')
print(f'Time Period: {years:>10} Years')
print('-'*50)
print(f'Final Amount: ${amount:>10.2f}')
print(f'Interest Earned ${interest:>10.2f}')
print('='*50)"""


# nums = [3,2, 4]
# target =6
# def find_indecies(nums,target):
#     for i in range(len(nums)):

#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:

#                 return [i,j]

# print(find_indecies(nums,target))


# TASK 6: Fuel Efficiency calculator => Calculate miles par gallon.
"""print("fuel efficiency calculator".title())
print("=" * 50)

miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons of fuel used: "))

mpg = miles_driven / gallons_used
cost_per_gallon = float(input("Enter cost per gallon: $"))
total_cost = gallons_used + cost_per_gallon
cost_per_mile = total_cost / miles_driven

print()
print('='*50)
print('fuel efficiency report'.upper().center(50))
print('='*50)
print(f'Miles Driven:       {miles_driven:>10.2f}')
print(f'Gallons Used:       {gallons_used:>10.2f}')
print(f'Miles per Gallon:   {mpg:>10.2f}')
print(f'Total Fuel Cost:    ${total_cost:>10.2f}')
print(f'Cost Per Mile:      ${cost_per_gallon:>9.2f}')
print('='*50)"""

# TASK Username Generator => Generate username from name.

"""print('Username Generator')
print('='*50)

first_name = input('Enter your first name: ').strip().lower()
last_name = input('Enter your last name: ').strip().lower()
birth_year = input('Enter your birth year: ').strip()


#Generate username options
username1 = first_name + last_name
username2 = first_name[0] + last_name
username3 = first_name + last_name + birth_year[-2]
username4 = first_name+'_'+last_name

print()
print('='*50)
print('generated usernames'.upper().center(50))
print('='*50)
print(f'1. {username1.replace(' ', '_')}')
print(f'2. {username2.replace(' ', '_')}')
print(f'3. {username3.replace(' ', '_')}')
print(f'4. {username4.replace(' ', '_')}')
print('='*50)"""

# Tesk 8: Text Statistics => Analyze text input
"""print('text statistics analyzer'.upper())
print('='*50)

text = input('Enter some text: ')

#Calculate statistics 
total_charts = len(text)
letters_only = sum(1 for char in text if char.isalpha())
digits_only = sum(1 for char in text if char.isdigit())
spaces = text.count(' ')
words = len(text.split())
uppercase = sum(1 for char in text if char.isupper())
lowercase = sum(1 for char in text if char.islower())

print()
print('='*50)
print('text analysis'.upper().center(50))
print('='*50)
print(f'Total Characters:   {total_charts:>10}')
print(f'Letters:    {letters_only}')
print(f'Digigs: {digits_only}')
print(f'Spacess: {spaces}')
print(f'Words: {words}')
print(f'Uppercase Letters: {uppercase}')
print(f'Lowercase Letters:  {lowercase}')
print('='*50)"""


# TASK 9: Discount Calculator => Calculate sale price with discount

'''print("discount calculator".title())
print("=" * 50)

original_price = float(input("Enter original price: $"))
discount_percent = float(input("Etner discount percentrage: "))

discount_amount = original_price * (discount_percent / 100)
sale_price = original_price - discount_amount
savings = discount_amount

print()
print('='*50)
print('sale details'.upper().center(50))
print('='*50)
print(f'Orignal Price: ${original_price:>10.2f}')
print(f'Discount: {discount_percent:>10.2f}')
print(f'You save: ${savings:>10.2f}')
print('-'*50)
print(f'Sale Price: ${sale_price:>10.2f}')
print('='*50)'''


#TASK 10: Initial Extractor => Extract initials from full name
print('Initial Extractor')
print('='*50)

full_name = input('Enter your full name: ').strip().title()
parts = full_name.split()
initials = ''
for part in parts:
    initials += part[0]

print(f'\nFull Name: {full_name}')
print(f'Initials: {initials}')

