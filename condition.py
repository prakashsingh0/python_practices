#Part 7: Practical Applications
# Step 21: Number Guessing game


'''print('='*50)
print('number guessing game'.upper().center(50))
print('='*50)
print()

secret_number = 42
print('I\'m thinking of a number between 1 and 100.... ')
guess = int(input('What\'s your guess? '))


if guess == secret_number:
    print('Crrect! you guessed it!')
elif guess < secret_number:
    print('Too low! Try a higher number.')
else:
    print('too high! Try a lower number.')

print()
print(f'The secret number was {secret_number}')
'''

# Step 22: Age Category Classifier => Classify person by age category

'''print('age catagory classifier'.upper().center(50))
print('='*50)

age = int(input('Enter your age: '))

if age < 0:
    print('Eroor: Age canot be negative!')
elif age <= 2:
    print('You are an infant')
elif age <=12:
    print('You are a child')
elif age <=17:
    print('You are a teenager')
elif age <= 64:
    print('You are an adult')
else:
    print('You are a senior')


print()
print(f'Category determined for age: {age}')'''


# Step 23: Login Validator => validate login credentials

'''print('='*50)
print('logni system'.upper().center(50))
print('='*50)
print()

#Stord credentilas (in real apps, these would be in a databse)
correct_username = 'admin'
correct_password = 'secure123'

username = input('Username: ').strip()
password = input('Password: ')

print()
print('='*50)

if len(username) == 0:
    print('Error: Username cannot be empty')
elif len(password) == 0:
    print('Error: Password cannot be empty')
elif username == correct_username and password == correct_password:
    print('✔️ Login successful!')
    print(f'Welcome, {username}')
elif username == correct_username:
    print('Incorrect password')
else:
    print('Username not found')

print('='*50)
'''

#Step 24: Calculator with validation => simple calculator with error handing


print('='*50)
print('simple calculator'.upper().center(50))
print('='*50)
print()

num1 = float(input('Enter first number: '))
operation = input('Enter operation (+, -, *, /): ')
num2 = float(input('Enter Second number: '))

print()
print('='*50)

if operation == '+':
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
elif operation == '-':
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
elif operation == '*':
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
elif operation == '/':
    result = num1/num2
    print(f'{num1} / {num2} = {result}')
else:
    print('Please select valid Operation')
print('='*50)





