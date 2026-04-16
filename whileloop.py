# Part 8: Practical Applications
# Step 24: Number Guessing Game => Guess the secret number
"""
print('='*50)
print('number guessing game'.upper().center(50))
print('='*50)
print()

secret_number = 42
attempts = 0
guessed = False

print("I'm thinking fo a number between 1 and 100")
print()

while not guessed:
    guess_input = input('Your guess: ')

    #validate input
    if not guess_input.isdigit():
        print('Please enter a valid number!')
        continue
    guess = int(guess_input)
    attempts += 1

    if guess < 1 or guess > 100:
        print('Guess must be between 1 and 100')
        continue

    if guess < secret_number:
        print('Too low! Try higher.')
    elif guess > secret_number:
        print('Too high! Try lower')
    else:
        guessed = True
        print()
        print('Conrrect!')
        print(f'You guessed it in {attempts} attempts!')

print()
print('='*50)

print('Thanks for playing')
print('='*50)"""


# step 25: login system with attempt limit => login with maximum attempts
"""
print("=" * 50)
print("secure login system".upper().center(50))
print("=" * 50)
print()

correct_username = "admin"
correct_password = "secure123"

max_attempts = 3
attempts = 0
logged_in = False

while attempts < max_attempts and not logged_in:
    print(f"Attempt {attempts + 1} of {max_attempts}")
    username = input('Username: ').strip()
    password = input('Password: ')
    if username == correct_username and password == correct_password:
        logged_in = True
        print()
        print("=" * 50)
        print("login successful!".upper().center(50))
        print("=" * 50)
        print(f'Welcome, {username}!')
    else:
        attempts += 1
        remaining = max_attempts - attempts

        if remaining > 0:
            print(f' Invalid credentials. {remaining} attempts remaining.')
            print()
        else:
            print("Invalid credentials")

if not logged_in:
    print()
    print('='*50)
    print('account locked'.upper().center(50))
    print('='*50)
    print('Too many failed attempts!')
 """

# Step 28: Simple calculator loop => Calculator that keeps running

"""print('='*50)
print('simple calculator'.upper().center(50))
print('='*50)
print()
print('Operations: +, -, *, /')
print('Type \'quit\' to exit')
print()

running = True

while True:
    num1_input = input('Enter first number (or \'quit\'): ')

    if num1_input.lower() == 'quit':
        break

    #Validate first number
    if not num1_input.replace('.','').replace('-','').isdigit():
        print('Invalid number!')
        continue

    num1 = float(num1_input)

    #get operation
    operation = input('Enter operation (+, -, *, /): ')

    if operation not in ['+', '-', '*', '/']:
        print('Invalid operation!')
        continue

    #Get second number

    num2_input = input('Enter second number: ')
    if not num2_input.replace('.','').replace('-','').isdigit():
        print('Invalid number!')
        continue
    num2 = float(num2_input)

    #Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1* num2
    elif operation == '/':
        if num2 == 0:
            print('Erro: Cannot divide by zero!')
            continue
        result = num1 / num2

    print(f'Result: {num1} {operation} {num2} = {result}')

print('Thank you for using the calculator!')
"""

# Step 27: Average Calculator => Calculator average of numbers

'''print("=" * 50)
print("average calculator".upper().center(50))
print("=" * 50)
print()
print("Enter numbers to average.")
print("Type 'done' when finished.")
print()

total = 0
count = 0

while True:
    user_input = input(f"Number {count + 1}: ")
    if user_input.lower() == "done":
        break

    # Validate input
    if user_input.replace(".", "").replace("-", "").isdigit():
        number = float(user_input)
        total += number
        count += 1
    else:
        print("Invalid number! Please try again.")


# Calculate and display results
print()
print("=" * 50)
print("result".upper().center(50))
print("=" * 50)

if count == 0:
    print("No numbers entered!")
else:
    average = total / count
    print(f'Count: {count}')
    print(f'Sum: {total}')
    print(f'Average: {average:.2f}')

    #find min and max (simple approach)
    print()
    print('Enter the same numbers again to see min/max')
    #(we'll learn better ways with lists later)

print('='*50)
'''

#Step 28: Countdown timer => Simple countdown timer
'''
print('='*50)
print('countdown timer'.upper().center(50))
print('='*50)
print()

#Get countdown value
seconds_input = input('Enter seconds to countdown')

if not seconds_input.isdigit():
    print('Invalid input!')
else:
    seconds = int(seconds_input)
    print()
    print(f'Starting countdown for {seconds}...')
    print()

    while seconds > 0:
        print(f'{seconds}..', end=' ')
        seconds -= 1

    print()
    print()
    print('Time\'s up!')

print('='*50)
'''


#Step 29: Password Strength Checker loop => keep checking strong password
'''
print('='*50)
print('password strength checker'.upper().center(50))
print('='*50)
print()
print('Requirements:')
print(' - At least 8 characters')
print(' - At least one Uppercase letter')
print(' - At leaset one lowercase leter')
print(' - At least one digit')
print(' - At least one special character (!@#$%^&*)')
print()

strong_password = False
while not strong_password:
    password = input('Enter password: ')
    
    #check all requiremnets
    long_enouogh = len(password) >= 8
    has_upper = password != password.lower()
    has_lower = password != password.upper()

    #check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    #check for special character
    has_special = False
    special_chars = '!@#$%^&*'
    for char in password:
        if char in special_chars:
            has_special = True
            break

    
    #Display feedback
    print()
    if long_enouogh:
        print('Length OK')
    else:
        print('Too short')
    
    if has_upper:
        print('Has uppercase')
    else:
        print('Missing uppercase')

    if has_lower:
        print('Has lowercase')
    else:
        print('Missing lowercase')
        
    if has_digit:
        print('has Digit')
    else:
        print('missing digit')
    if has_special:
        print('Has Special character')
    else:
        print('Missing Special character')

    #Check if all requirements met 
    if long_enouogh and has_upper and has_lower and has_digit and has_special:
        strong_password = True
        print()
        print('='*50)
        print('password is strong!'.upper().center(50))
        print('='*50)
    else:
        print()
        print('Password is weak. Try again!')
        print()
        '''


#Step 30: Menu - Driven Contact Manager => simple contact menu (without lists)

'''print('='*50)
print('contact manager'.upper().center(50))
print('='*50)

#Store only one contact (we'll use lists later for multiple)
contact_name = ''
contact_phone = ''
has_contact = False
running = True
while running:
    print()
    print('='*50)
    print('menu'.upper().center(50))
    print('='*50)
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Delete Contact')
    print('4. Exit')
    print('='*50)

    choice = input('hoose option (1-4): ')

    if choice == '1':
        print()
        print('Add Contact'.center(50,'-'))
        contact_name = input('Enter name: ').strip()
        contact_phone = input('Enter phone: ').strip()
        
        if len(contact_name) > 0 and len(contact_phone) > 0:
            has_contact = True
            print('Contact added!')
        else:
            print('Invalid input!')

    elif choice == '2':
        print()
        print('View Contact'.center(50,'-'))
        if has_contact:

            print(f'Name : {contact_name}')
            print(f'Phone: {contact_phone}')
        else:
            print('No contact saved!')

    elif choice == '3':
        print()
        print('Delete Contact'.center(50,'-'))
        if has_contact:
            confirm = input(f'Delete {contact_name}? (yes/no): ')
            if confirm.lower() == 'yes':
                contact_name = ''
                contact_phone = ''
                has_contact = False
                print('Contact dleted!')
            else:
                print('Deletion cancelled')
        else:
            print('No canctact to delete!')

    elif choice == '4':
        print()
        print('Goodbye!')
        running = False
    else:
        print()
        print('Invalid choice')
print('='*50)
'''


#part 9: Practice Tasks
#Task 1: Higher or lower Game = > Guess if next is higher or lower




