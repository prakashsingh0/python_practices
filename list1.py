# Part 8: Practical Applications
# Step 32: Grade Tracker => track and display student grades
"""
print("=" * 50)
print(f"grade tracker".upper().center(50))
print("=" * 50)
print()


# pre-define grades
grades = [85, 92, 78, 95, 88, 76, 90]

print(f"Grades: {grades}")
print(f"Number of grades: {len(grades)}")
print()

total = 0
for grade in grades:
    total += grade
avg = total / len(grades)

print(f"Sum: {total}")
print(f"Average: {avg:.2f}")
a_count = 0
b_count = 0
c_count = 0
below_c = 0

for grade in grades:
    if grade >= 90:
        a_count += 1
    elif grade >= 80:
        b_count += 1
    elif grade >= 70:
        c_count += 1

    else:
        below_c += 1

print(f"Grade Distribution: ")
print(f" A(90-100): {a_count}")
print(f" B(80-90): {b_count}")
print(f" C(70-80): {c_count}")
print(f" Below C: {below_c}")
print('='*50)"""


# step 33: shopping list display => display a formatted shopping list
"""
print('='*50)
print('shopping list'.upper().center(50))
print('='*50)

shopping_list = ['Milk','Bread','Eggs','Butter','Cheese']
if len(shopping_list) ==0:
    print('Your shopping list is empty!')
else:
    print(f'You have {len(shopping_list)} items to buy:')
    print()
    
    for i in range(len(shopping_list)):
        print(f' {i+1}. {shopping_list[i]}')

    print()
    print('-'*50)
    print(f'First item: {shopping_list[0]}')
    print(f'Last item {shopping_list[-1]}')



print('='*50)
"""


# step 34: Finding values in Lists => Search for values in a list
"""print('='*50)
print('list search'.upper().center(50))
print('='*50)
print()

numbers = [10,25,30,45,50,65,70,85,90]
print(f'numbers: {numbers}')
print()

search = int(input('Enter a number to search for: '))

if search in numbers:
    for i in range(len(numbers)):
        if numbers[i] == search:
            print(f'found {search } at index {i}!')
            break
else:
    print(f'{search} not found in the list')

print()
print('='*50)"""

# Step 35: List Statistics => Calculate statistics for a list of numbers

"""
print('='*50)
print('list staticstics'.upper().center(50))
print('='*50)
print()


numbers = [23,45,12,67,34,89,21,56,78,43]
print(f'Numbers: {numbers}')
print()

#Calculate sum
total =0

for num in numbers:
    total += num


#calculate average
avg = total / len(numbers)

#find minimum
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

#find Max
maximum = numbers[0]

for num in numbers:
    if num>maximum:
        maximum = num


#Display results
print('='*50)
print('results'.upper().center(50))
print('='*50)
print(f'count: {len(numbers)}')
print(f'Sum: {total}')
print(f'Average: {avg:.2f}')
print(f'Minimum: {minimum}')
print(f'Maximum: {maximum}')
print(f'Range: {maximum - minimum}')
print('='*50)

"""
# Part 9: Practice Tasks
# Task 1: Name greeter => Greet each person in al list

"""print('Name Greeter')
print('='*50)

names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
print(f'Tatal people: {len(names)}')

print()
for name in names:
    print(f'Hello, {name}! Welcome')

print()
print('Everyone has been greeted!')
"""
# Task 2: Number Classifier => Classify numbers in a list
'''print("Number Classifier")
print("=" * 50)
numbers = [12, -5, 0, 18, -3, 7, 0, -8, 15]
print(f"Numbers: {numbers}")
print()


positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1
    
print(f'Positive numbers: {positive_count}')
print(f'Negative numbers: {negative_count}')
print(f'Zeros: {zero_count}')'''

#Task 3: Score updater => Add bonus points to all scores.
'''
print('Score Updater')
print('='*50)

scores = [75,82,68,91,77]

print(f'Original scores: {scores}')

bonus = 5
print(f'Adding {bonus} bonus points...')

for i in range(len(scores)):
    scores[i] += bonus

print(f'Updated Scores: {scores}')
'''

#Task 4: Word Length Counter => Count Characters in Each word.

'''print('word length counter'.title())
print('='*50)

words = ['Python', 'is', 'awesome', 'programming', 'language']

print(f'Words: {words}')
print()
total_chars = 0

for word in words:
    length = len(word)
    total_chars += length
    print(f"'{word}' has {length} characters")

print()
print(f'Total characters: {total_chars}')
print(f'Average word length: {total_chars / len(words):.1f}')
'''


#Task 5: Find maximum => Find the largest number without usering max()

'''print('find Maximum')
print('='*50)

numbers =[34,67,89,12,56,78,45]

print(f'Numbers: {numbers}')

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f'The aximum value of the list is : {maximum}')
'''

#Task 6: Element Checker => Check multiple values in a list
'''
print(f'Element Checker')
print('='*50)


available_colors = ['red', 'green', 'blue','yellow','orange']
print(f'Available : {available_colors}')
print()

check_colors = ['red','purple','green','pink']

for color in check_colors:
    if color in available_colors:
        print(f' {color} is available')
    else:
        print(f' {color} is not available')
     '''   


#Task 7: index finder => find all indices of a value

'''print(f'Index Finder')
print('='*50)


numbers = [5,2,8,9,2,1,7,2,6]

search = 2
print(f'List : {numbers}')

print(f'Searching for : {search}')
print()

found_indices = []
for i in range(len(numbers)):
    if numbers[i] == search:
        found_indices.append(i)

if len(found_indices) > 0:
    print(f'Found at indices: {found_indices}')
else:
    print('Not found')'''


#Task 8: Temperature converter (List) => Convert list of temperatures
'''
print('Temperature Converter (C to F)')
print('='*50)

celsius_temps = [0,10,20,30,40]

print(f'Celsius: {celsius_temps}')
print()

print('Conversions:')
for i in range(len(celsius_temps)):
    c = celsius_temps[i]
    f = (c * 9/5) + 32
    print(f' {c}C = {f}f')
    '''


#Task 9: Passing Students => identify passing and failing students

'''print('Passing students')
print('='*50)

students = ['Alice','Bob','Charlie','Diana','Eve']
scores = [85,58,92,67,73]

passing_threshold = 70

print('Student Results:')
print('-'*50)

for i in range(len(students)):
    if scores[i] >= passing_threshold:
        status = 'PASS'
    else:
        status = 'FAIL'
    print(f'{students[i]}: {scores[i]} - {status}')
'''

#Task 10: List Comparison => find common elements in two lists.

'''print('List Comparison')
print('='*50)

list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9]
print(f'List 1: {list1}')
print(f'List 2: {list2}')
print()
common = []
for item in list1:
    if item in list2:
        common.append(item)


print(f'common elements: {common}')
print(f'Count: {len(common)}')'''








