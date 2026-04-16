# step 26: Building a Simple Validator
# sinmple age and license validator

"""age = int(input('Enter Your age: '))
has_license = input('Do you fave a license? (yes/no: )').lower().strip() == 'yes'

print()
print('='*50)
print('eligibility check'.upper().center(50))
print('='*50)

can_drive = age>=16
car_drive_with_adult = age >=15
can_rent_car = age >= 21 and has_license
can_rent_luxury_car = age >= 25 and has_license

print(f'Age: {age}')
print(f'Has license: {has_license}')
print('-'*50)
print(f'Can drive: {can_drive}')
print(f'Can drive with adult: {car_drive_with_adult}')
print(f'Can rent car: {can_rent_car}')
print(f'can Rent luxury car: {can_rent_luxury_car}')
print('='*50)"""

# STEP 27: Grade Checker

"""print('='*50)
print('grade checker'.upper().center(50))
print('='*50)

score = float(input('enter your score (0-100): '))
passing_score = 60

passed = score >=60
excellent = score >=90
good = 90 > score >=80
average = 80> score >=70
needs_improvement = score < passing_score

print()
print('='*50)
print('grade analysis'.upper().center(50))
print('='*50)
print(f'Your score: {score}')
print(f'Passeing Score: {passing_score}')
print('-'*50)
print(f'Passed: {passed}')
print(f'Excellent (90+): {excellent}')
print(f'good (80+): {good}')
print(f'Average ((70+): {average})')
print(f'Needs Improvement: {needs_improvement}')
print('='*50)"""

# Number Comparison
"""num1 = float(input('Enter first numbers: '))
num2 = float(input('Enter Second number: '))

equal = num1 == num2
not_equal = num2 != num1
first_greater = num1 > num2
first_less = num1 < num2
first_greater_equal = num1 >= num2
first_less_equal = num1 <= num2


print('='*50)

print(f'{num1} == {num2} {equal}')
print(f'{num1} != {num2}: {not_equal}')
print(f'{num1} > {num2}: {first_greater}')
print(f'{num1} < {num2}: {first_less}')
print(f'{num1} >= {num2}: {first_greater_equal}')
print(f'{num1} <= {num2}: {first_less_equal}')

print('='*50)"""

# Step 29: Range Checker => Check if number is in range

"""print('='*50)
print('range checker'.upper().center(50))
print('='*50)


number = float(input('Enter a number: '))
min_value = float(input('Enter minimum value: '))
max_value = float(input('Enter maximum value: '))

in_range = min_value <= number <= max_value
below_range = number < min_value
above_range = number > max_value
at_minimum = number == min_value
at_maximum = number == max_value


print('='*50)
print('range checker'.upper().center(50))
print('='*50)
print(f'Number: {number}')
print(f'Range : {min_value} to {max_value}')
print('-'*50)
print(f'In range: {in_range}')
print(f'Below range: {below_range}')
print(f'Above Range: {above_range}')
print(f'At minimum: {at_minimum}')
print(f'At maximum: {at_maximum}')
print('='*50)"""

# step 30: Password Validator => validate password requirements

"""print('='*50)
print('password validator'.upper().center(50))
print('='*50)
print()

print('Password Requirements:')
print(' - At least 8 characters')
print('  - Contains uppercase letter')
print('  - Contains uppercase letter')
print('  - Contains lowercase letter')
print('  - Contains number')
print()

password = input('Enter password to validate: ')

# check requirements
long_enough = len(password) >= 8
#check for uppercase - string changes when converted to lowercase
has_upper = password != password.lower()
#check for lowercase - string changes when converted to uppercase
has_lower = password != password.upper()
#check for digits - look for common digits
has_digit = ('0' in password or '1' in password or '2' in password or 
             '3' in password or '4' in password or '5' in password or
             '6' in password or '7' in password or '8' in password or 
             '9' in password)

#check for common weak passwords
is_common = password.lower() in ['password','12345678','qwerty']

# Overall validity
is_valid = long_enough and has_digit and has_lower and has_upper and not is_common

print()
print('='*50)
print('validation results'.upper().center(50))
print('='*50)
print(f'Length >= 8: {long_enough} ({len(password)} chars)')
print(f'Has uppercase: {has_upper}')
print(f'Has lowercase: {has_lower}')
print(f'Has digit: {has_digit}')
print(f'Not common: {not is_common}')
print('-'*50)
print(f'Password Valid: {is_valid}')

print('='*50)"""

# Step 31: Email Validator => Basic email validation

"""print('='*50)
print('email validator'.upper().center(50))
print('='*50)
print()

email = input('Enter email address: ').strip().lower()


#basic Check

has_at = '@' in email
has_dot = '.' in email
has_one_at = email.count('@') == 1
not_empty = len(email) > 0


#More details checks

starts_or_ends_with_at  = email.startswith('@') or email.endswith('@')
start_or_ends_with_dot =  email.startswith('.') or email.endswith('.')
has_consecutive_dots = '..' in email
has_space = ' ' in email

#Check minimum length

min_length = len(email) >= 5  #AT least a@b.c

#Overall validity (basic check)
is_valid = (has_at and has_one_at and has_dot and not_empty 
            and not starts_or_ends_with_at and not start_or_ends_with_dot and 
            not has_consecutive_dots and not has_space and min_length)

print()
print('='*50)
print('valiation results'.upper().center(50))
print('='*50)

print(f'Email: {email}')
print('-'*50)
print(f'has @ symbol: {has_at}')
print(f'Has only one @: {has_one_at}')
print(f'Has . symbol: {has_dot}')
print(f'Not empty: {not_empty}')
print(f'Min length (>=): {min_length}')
print(f'No @ at start/end: {not starts_or_ends_with_at}')
print(f'No . at start/end: {not start_or_ends_with_dot}')
print(f'No consecutive dots: {not has_consecutive_dots}')
print(f'No spaces: {not has_space}')
print('-'*50)
print(f'Email Valid: {is_valid}')
print('='*50)"""

# PART 8: Practice Tasks
# Task 1: Temperature Range Checker
"""
print('temperature comfort checker'.title().center(50))
print('='*50)

temp = float(input('Enter temperature (F): '))
too_cold = temp < 60
cold = 60 <= temp < 70
comfortable= 70 <= temp <=78
warm = 78 < temp <=85
too_warm = temp > 85

print()
print(f'Temperatur: {temp}')
print(f'Too Cold (<60): {too_cold}')
print(f'Cold(60-69): {cold}')
print(f'Comfortable (70-78): {comfortable}')
print(f'Warm (79): {warm}')
print(f'Too Warm (> 85): {too_warm}')"""

# Task 2: Voting Eligibility => Check if person can vote.
"""print('Votting Eligibility Cheker')
print('='*50)

age = int(input('Enter Your age: '))
is_citizen = input('Are you citizen? (yes/no): ').lower() == 'yes'

eligible = age >= 18 and is_citizen
too_young = age<18
not_citizen = not is_citizen

print()
print(f'Age: {age}')
print(f'Citizen: {is_citizen}')
print('-'*50)
print(f'Eligiable to vote: {eligible}')
print(f'Too young: {too_young}')
print(f'Not a citizen: {not_citizen}')"""

# Task 3: Triangle Validator => Check if three sides can form a triangle

# Rule: Sum of any two sides must be greater then the third side
'''
print("Triangle Validator")
print("=" * 50)

a = float(input("Enter side a: "))
b = float(input("Enter side B: "))
c = float(input("Enter side c: "))

# Check Triangle inequality theorem
c1 = a + b > c
c2 = a + c > b
c3 = b + c > a

is_triangle = c1 and c2 and c3 

#Check types (only meaningful if it's a valid triangle)

is_equilateral = a == b == c
is_isocseles = (a==b) or (b==c) or (a==c)
is_scalene = a != b and b != c and a != c

print()
print(f'Sides: {a}, {b}, {c}')
print('-'*50)
print(f'Condition 1 (a+b > c): {c1}')
print(f'condition 2 (a+c > b): {c2}')
print(f'Condition 3 (b+c < a): {c3}')
print(f'Valid triangle: {is_triangle}')
print(f'Equilateral (all equal): {is_equilateral}')
print(f'Isosceles (two equal): {is_isocseles}')
print(f'Scalene ( all different): {is_scalene}')'''


#Task $: Leap Year Checker => check if a year is a leap year.
'''
print('leap year cheker'.title().center(50))
print('='*50)

year = int(input('Enter a year: '))

didsible_by_4 = year % 4==0
didsible_by_100 = year % 100 == 0
didsible_by_400 = year % 400 == 0

is_leap_year = didsible_by_4 and (not didsible_by_100 or didsible_by_400)

print()
print(f'Year: {year}')
print(f' Divisible by 4: {didsible_by_4}')
print(f' Divisible by 100: {didsible_by_100}')
print(f' Divisible by 400: {didsible_by_400}')
print('-'*50)
print(f'Leap Year: {is_leap_year}')'''

#Task 5: Username Validator => validate username requirements
#Requirements: (1) 3-20 characters (2) only letters, numbers, underscores (3) Doesn't start with number
'''
print('username validator'.title())
print('='*50)

username = input('Enter username: ').strip()

length_valid = 3 <= len(username) <= 20
has_no_space = ' ' not in username
has_no_spacial = not ('!' in username or '@' in username or '#' in username or '$' in username or '%' in username or '&' in username)


#check if starts with digit (check first character)
first_char = username[:1] #Gets first character, or empty string if username is empty

start_with_digit = first_char.isdigit()

is_valid = length_valid and has_no_space and has_no_spacial and not start_with_digit

print()
print(f'username: {username}')
print(f'Length (3-20): {length_valid} ({len(username)} chars)')
print('No spaces: {}'.format(has_no_space))
print('No special chars: {}'.format(has_no_spacial))
print('Doesn\'t start with number: {}'.format(not start_with_digit))
print('-'*50)
print(f'Username Valid: {is_valid}')'''


#Task 6: Grade Letter Calculator => Determine letter grade from score
'''
print('Grade Letter cacluator'.title())
print('='*50)

score = float(input('Enter Score (0-100)'))

valid_score = 0 <= score <=100
is_A = score >=90
is_B = 80 <= score <90
is_C = 70 <= score <80
is_D = 60 <= score <70
is_F = score <60

print()
print(f'Score: {score}')
print(f'Valid score: {valid_score}')
print(f'-'*50)
print(f'A {is_A}')
print(f'B {is_B}')
print(f'C {is_C}')
print(f'D {is_D}')
print(f'F {is_F}')'''

#Task 7: BMI Catagory checker => check BMI category
# Task 7: BMI Category Checker

'''print("BMI Category Checker")
print("=" * 50)

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

underweight = bmi < 18.5
normal = 18.5 <= bmi < 25
overweight = 25 <= bmi < 30
obese = bmi >= 30

print()
print(f"BMI: {bmi:.2f}")
print("-" * 50)
print(f"Underweight (< 18.5): {underweight}")
print(f"Normal (18.5-24.9): {normal}")
print(f"Overweight (25-29.9): {overweight}")
print(f"Obese (>= 30): {obese}")'''


# Task 8: File Type checker => check file type from extension
'''
print('file type checker'.title().center(50))
print('='*50)

filename = input('Enter filename: ').lower()

#checker extension
is_image = filename.endswith(('.jpg', '.png', '.gif', '.bmp'))
is_document = filename.endswith(('.doc', '.docx', '.pdf', '.txt'))
is_video = filename.endswith(('.mp4', '.avi', '.mov', '.mkv'))
is_audio = filename.endswith(('.mp3', '.wav', '.flac'))
is_python = filename.endswith('.py')

has_extension = '.' in filename


print()
print(f'Filename: {filename}')
print(f'Has extension: {has_extension}')
print('-'*50)
print(f'Image file: {is_image}')
print(f'Document file : {is_document}')
print(f'Video file: {is_video}')
print(f'Audio file: {is_audio}')
print(f'Python file: {is_python}')'''

#Task 9: Discount Eligibility => check if customer qualifies for discounts.

'''print('discount eligibility checker'.title())
print('='*50)

purchase_amount = float(input('Enter purcher anount: $'))
is_member = input('Are you a member? (yes/no)').lower() == 'yes'
is_first_purchase = input('First purchase? (yes/no)').lower() == 'yes'

#discount conditions
bulk_discount = purchase_amount >= 100
member_discount = is_member
first_time_discount = is_first_purchase
special_discount = purchase_amount >= 500

#Any discount eligible

any_discount = bulk_discount or member_discount or first_time_discount

print()
print('='*50)
print('discount eligibility'.upper().center(50))
print('='*50)
print(f'Purchase: ${purchase_amount:.2f}')
print(f'Member: {is_member}')
print(f'First Purchase: {is_first_purchase}')
print('-'*50)
print(f'Bulk discount: {bulk_discount}')
print(f'Member Discount: {member_discount}')
print(f'First-Time Discount: {first_time_discount}')
print(f'Special Discount (>= $500): {special_discount}')
print(f'-'*50)
print(f'Qualifies for discount: {any_discount}')
print(f'='*50)
'''

#Task 10: Time validator => Validate time format (HH:MM)
print('Time Validator (24-hour format)')
print('='*50)

time_str = input('Enter time (HH:MM)')

#check basic format

has_colon = ':' in time_str
correct_length = len(time_str) == 5 #HH:MM is exaclty 5 characters

#Check if colon is in the right position (index 2)
#Get character at position 2
char_at_2 = time_str[2:3]
colon_in_middle = char_at_2 == ':'

#Extract hour and minute parts using string slicing
hour_str = time_str[:2] #First 2 characters
minute_str = time_str[3:5] #Characters 3 and 4 (after colon)

#Check if parts contain only digits
hours_is_digit = hour_str.isdigit() and len(hour_str) == 2
minutes_is_digit = minute_str.isdigit() and len(minute_str) == 2

#check if vlaues are in valid range (we can safely use int() here or just compare as strings)
#For simplicity with no conditionals, we'll check the Boolean for digit validity

hours_valid = hours_is_digit #We'll display this as "hours format valid"
minutes_valid = minutes_is_digit #we'll display this as "minutes format valid"

#Overall format validity
is_valid = (has_colon and correct_length and colon_in_middle and hours_is_digit and minutes_is_digit)

print()
print(f'Time: {time_str}')
print(f'Has colon: {has_colon}')
print(f'Correct length (5): {correct_length}')
print(f'colon at postion 2 : {colon_in_middle}')
print(f'Hours format valid (2 digits): {hours_is_digit}')
print(f'Minutes format valid (2 digits): {minutes_is_digit}')
print('-'*50)
print(f'Valid time format: {is_valid}')

















