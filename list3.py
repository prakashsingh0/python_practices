# Practical Applications
# Application 1: tic-tac-toe board
# Create an empty tic-tac-toe board

"""board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

board[0][0] = 'X'
board[1][1] = 'O'
board[0][2] = 'X'


def display_board():
    print(' 0   1   2')
    for i in range(3):
        print(f'{i} {board[i][0]} | {board[i][1]} | {board[i][2]}')
        if i < 2:
            print(' --+---+--')



display_board()"""


# Application 2: Grade report Generator
# Student grade data

"""Students = [
    ['Alice', 85, 90, 88,92],
    ['Bob', 78, 82, 80,85],
    ['Carol', 92, 95, 91,88],
    ['David', 70, 75, 72,78]
]

print('='*50)
print('student grade report'.upper().center(50))
print('='*50)
print(f'{'Name':<10}    {'Test1':<7}    {'Test2':<7}    {'Test3':<7}    {'Test4':<7}    {'Avg':<7}')
print('-'*50)


for student in Students:
    name = student[0]
    grades = student[1:] #All elements except the first (name)
    #Calculate average
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    print(f'{name:<10}   {student[1]:<7}    {student[2]:<7}     {student[3]:<7}    {student[4]:<7}    {average:<7.1f} ')
"""

# Application 3: Matrix Operations
# Two matrieces to add
"""
matrix_a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix_b = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

#Create result matrix with zeros
result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#Add the matrices
for i in range(3):
    for j in range(3):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]


print('Matrix A + Matrix B = ')
for row in result:
    print(row)"""


# application 4: Sales Data analysis
# Sales data: [Product, Q1,Q2,Q3,Q4]
"""
sales = [
    ["Laptops", 150, 200, 180, 220],
    ["Phones", 300, 350, 400, 380],
    ["Tables", 100, 120, 110, 130],
]

print('annual sales report'.upper())
print('='*55)

#Calculate and display totals for each product
for product in sales:
    name = product[0]
    quarterly = product[1:]
    yearly_total = 0
    for q in quarterly:
        yearly_total += q
    print(f'{name}: {quarterly} --> Total: {yearly_total}')


q1_total = 0
for product in sales:
    q1_total += product[2]

print(f'\nQ1 Total (all products): {q1_total}')
"""

# Practice Tasks
# Task 1: List Slicer
# Create a program that:
#
# Has a list of 10 numbers: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# Asks the user for start and stop indices
# Displays the slice
# Continues until user enters -1 for start

'''numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print("list slicer".title())
print("=" * 40)
print(f"Full list: {numbers}")
print("Indices: 0 1 2 3 4 5 6 7 8 9")
print()

while True:
    start_input = input("Enter start index (-1 to quit): ")
    start = int(start_input)

    if start == -1:
        print("Goodbye!")
        break
    stop_input = input("Enter stop index: ")
    stop = int(stop_input)

    result = numbers[start: stop]
    print(f"Numbers[{start}:{stop}] = {result}")
    print()'''

#Task 2: Every Nth Element
#Create a program that :
# Has a list of letters: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Asks the user for a step value
# Displays every nth element
# Shows both forward and reversed versions
'''
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print('Every Nth element selector'.title())
print('='*40)
print(f'Letters: {letters}')
print()

step_input = input('Enter step value (e.g., 2 for every 2nd ): ')
step = int(step_input)

if step > 0:
    forword = letters[::step]
    backword = letters[::-step]
    print(f'\nEvery {step} element(s):')
    print(f'Forward: {forword}')
    print(f'Backword: {backword}')
else:
    print('Step must be greater then 0')
'''




# Task 3: Value Swapper
# Create a program that:

# Has a list of 5 numbers
# Asks the user for two indices to swap
# Performs the swap and displays the result
# Continues until user enters -1
'''numbers = [10,20,30,40,50]
print('Value Swapper')
print('='*50)
while True:
    print(f'\nCurrect list: {numbers}')
    print('Indices:     0   1   2   3   4')

    first_input = input('\nFirst index to swap (-1 to quit): ')
    first = int(first_input)
    if first == -1:
        print('Final List:',numbers)
        print('GoodBye!')
        break
    second_input = input('Second index to swap: ')
    second = int(second_input)
    if first< 0 or first > 4 or second<0 or second >4:
        print('Invalid index! use 0-4')
    else:
        #Perform the swap
        numbers[first],numbers[second] = numbers[second],numbers[first]
        print(f'Swapped indices {first} and {second}')
'''
#Task 4: List Unpacker
#Create a program that:
# 1. Has a list of 5 test scores
# 2. Unpacks the first score, middle scores, and last score
# 3. Display lowest score removed, highest score removed, and average of middle
'''
scores = [72,85,88,95]
print('Score Analyzer with unpacking')
print('='*50)
print(f'All Scores: {scores}')
print()

#Unpack first, middle and last
first, *middle, last = scores
print(f'First score (dropped): {first}')
print(f'Last score (droped): {last}')
print(f'Middle scores: {middle}')

total = 0
for score in middle:
    total += score
average = total / len(middle)
print(f'\nAverage of middle {len(middle)} scores: {average:.1f}')
'''

# Task 5: 3x3 Matrix Creator
# Create a program that:

# 1. Asks the user to enter 9 numbers (one at a time)
# 2. Builds a 3x3 matrix from these numbers
# 3. Displays the matrix in a nice format
# 4. Shows the sum of each row
'''
print('3x3 Matrix Creator')
print('='*50)
print('Enter 9 numbers to fill the matrix (row by row): ')
print()

matrix = []

for row_num in range(3):
    row = []
    for col_num in range(3):
        prompt = f'Enter value for row {row_num}, column {col_num}:'
        value_input = input(prompt)
        value = int(value_input)
        row.append(value)
    matrix.append(row)

print('\nYour matrix:')
print('-'*50)
for row in matrix:
    print(f' {row[0]:4} {row[1]:4}  {row[2]:4}')
print('-'*50)
'''

#Task 6: Nested List navigator
# Create a program that:
#1. Has a nested list representing a seating chart (3 rows, 4 seats each)
#2. Asks user for row and seat number
#3. Shows who is sitting there
#4. Allows user to change the name at a seat
#5. Displays updated seating chart

seats = [
    ['Alice','Bob','Carol','David'],
    ['Eve','Frank','Grace','Henry'],
    ['Ivy','Jack','Kate','Leo']
]


print('seating hart navigator'.title().center(50))
print('='*50)

while True:
    print('\nCurrent Seating Chart:')
    print(' seat 0  seat 1  seat 3')
    for i in range(3):
        print(f'Row {i} {seats[i][0]:<9} {seats[i][1]:<9} {seats[i][2]:<9} {seats[i][3]:<9}')

    print('\nOptions:')
    print('1. Check a seat')
    print('2. Change aname')
    print('3. Exit')

    choice = input('Enter choice (1-3): ')
    
    if choice == '1':
        row_input = input('Enter row (0-1):')
        row = input(row_input)
        seat_input = input('Enter seat (0-3): ')
        seat = int(seat_input)
        if row >= 0 and row <= 2 and seat >=0 and seat <= 3:
            print(f'Person at row {row}, seat {seat}: {seats[row][seat]}')
        else:
            print('Invalid row or seat numbers!')

    elif choice == '2':
        row_input = input('Enter row (0-1):')
        row = input(row_input)
        seat_input = input('Enter seat (0-3): ')
        seat = int(seat_input)
        if row >= 0 and row <= 2 and seat >=0 and seat <= 3:
            old_name = seats[row][seat]
            new_name = input('Enter new name: ')
            seats[row][seat] = new_name
            print(f'Change {old_name} to {new_name}')
        else:
            print('Invalid row or seat number!')
    elif choice == '3':
        print('Goodbye!')
        break
    else:
        print('Invalid choice')





