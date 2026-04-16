#Step 31: A Complete Function Example
# A Complete Function Example
#let's creat a well-structured function:

def calculate_bmi(weight_kg,height_m):
    """Calculate Body Mass Index (BMI)"""
    if height_m <= 0:
        return None
    bmi = weight_kg / (height_m ** 2)
    return round(bmi,1)

#use the function
my_bmi = calculate_bmi(70,1.75)
print(f'BMI : {my_bmi}')

#Handle edge case
invalid = calculate_bmi(70,0)
print(invalid)

# Step 32: Functions Calling Other Functions
# Functions can call other functions:
'''def square(n):
    return n*n

def sum_of_square(a,b):
    return square(a) + square(b)

resutl = sum_of_square(3,4)
print(resutl)

def is_even(n):
    return n % 2 == 0

def count_evens(numbers):
    count = 0
    for n in numbers:
        if is_even(n):
            count += 1
    return count

print(count_evens([1,2,3,4,5,6,7,8,9,10]))



#String Utilities

def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_words(text):
    """Count the number of words in a string."""
    words = text.split()
    return len(words)

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def is_palindrome(text):
    """Check if a string is a palindrome (ignore case and spaces)."""
    cleaned = text.lower().replace(" ","")
    return cleaned == cleaned[::-1]

#Test the functions

print("string utilities".title().center(50,'='))
print('='*40)

test_string = 'Hello World'
print(f'\nOriginal: "{test_string}"')
print(f'Vowels: {count_vowels(test_string)}')
print(f'Worlds: {count_words(test_string)}')
print(f'Reversed: {reverse_string(test_string)}')

#Palindrome test
words = ['radar', 'hello','level','python','a man a plan a canal panma']
print('\npalindrome check:'.title())
for word in words:
    result = "YES" if is_palindrome(word) else 'No'
    print(f'    "{word}": {result}')
print('='*50)'''

#Application 3: Math helpers
'''def factorial(n):
    """Calculate the factorial of n."""
    if n < 0:
        return None
    if n ==0 or n == 1:
        return 1
    result = 1
    for i in range(2,n+1):
        result = result*i
    return result

def is_prime(n):
    """check if a number is prime"""
    if n<2:
        return False
    if n == 2:
        return True
    if n % 2==0:
        return False
    for i in range(3, int(n**0.5) +1,2):
        if n % i == 0:
            return False
        
    return True

def get_factors(n):
    """Get all factors of a number."""
    factors =[]
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors

#test the functions
print('math helpers'.title().center(50))
print('='*50)

#Factorials
print('\nFactorials:')
for i in range(8):
    print(f'    {i}! = {factorial(i)}')

#prime Checking
print('\nPrime Numbers (1-38):')
primes = [n for n in range(1,31) if is_prime(n)]
print(f'    {primes}')

#factors
print('\nFactors:')
for n in [12,24,36]:
    print(f'    Factors of {n}: {get_factors(n)}')

print('='*50)'''


#Application 4: list Operations
'''
def get_average(numbers):
    """Calculate the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def get_median(numbers):
    """Calculate the median of a list of numbers."""
    if len(numbers) == 0:
        return 0
    sorted_num = sorted(numbers)
    n = len(sorted_num)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_num[mid-1] + sorted_num[mid] )/2
    else:
        return sorted_num[mid]
    
def remove_duplicates(items):
    """Remove duplicates while preserving order."""
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

def find_common(list1,list2):
    """Find the elements between two lists."""
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

#Test the functions
print('List Operations'.center(50))
print('='*40)

numbers = [5,2,2,8,9,5,8,3]
print(f'\nOriginal list: {numbers}')
print(f'Average: {get_average(numbers):.2f}')
print(f'Median: {get_median(numbers)}')
print(f'Without duplicates: {remove_duplicates(numbers)}')

list_a = [1,2,3,4,5]
list_b = [4,5,6,7,8]
print(f'\nList A: {list_a}')
print(f'\nList B: {list_b}')
print(f'Common elements : {find_common(list_a, list_b)}')'''

#Task 1: basic Greeting function
"""
1. Takes a name as a parameter
2. Returns a greeting string (don't print it)
3. Test it with multiple names
"""
#Solution⬇️
'''def create_greeting(name:str)->str:
    """Create a personalized greeting"""
    return f'Hello, {name}! Welcome!'

#test the function
print("Basic Greeting Function")
print('='*40)

names = ['Alice','Bob','Carol','David']

for name in names:
    greeting = create_greeting(name)
    print(greeting)

#Use return value in another operation

message = create_greeting("Eve")
print(f'\nStored message: {message}')
print(f'Message length: {len(message)}')'''
# Task 2: Rectangle Calculator
# Create functions for rectangle calculations:

# calculate_area(width, height) - returns area
# calculate_perimeter(width, height) - returns perimeter
# Test with different dimensions
'''
def calculate_area(width,height):
    """Calculate the area of reactangle."""
    return width*height

def calculate_perimeter(width,height):
    """Calculate the permeter of a reactngle."""
    return 2*(width+height)


#Test the functions
print('rectangle calculator'.title().center(50))
print('='*50)

rectangles = [(5,3),(10,8),(7,7),(12,4)]

print(f'{'Width':<8} {'Height':<8} {'Area':<10} {"Perimeter":<10}')
print('-'*50)
for width, height in rectangles:
    area = calculate_area(width,height)
    perimeter = calculate_perimeter(width,height)
    print(f'{width:<8} {height:<8} {area:<10} {perimeter:<10}')

'''

# Task 3: Even/Odd Checker
# Create a function that:

# Takes a number as parameter
# Returns "even" or "odd"
# Test with a range of numbers

def check_even_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

#test the function
print('Even/Odd checker')
print('='*50)

for num in range(1,11):
    result = check_even_odd(num)
    print(f'{num} is {result}')

print('='*50)
#Use in filtering
print('\nEven numbers form 1-20')
evens = []
for num in range(1,21):
    if check_even_odd(num) == 'even':
        evens.append(num)
print(evens)

