# Part 7: Practical Applications
# Step 26: Dynamic shopping List => Interactive shopping list manager

"""print('='*50)
print('shopping list manager'.upper().center(30))
print('='*50)

shopping_list = []

running = True

while running:
    print()
    print('='*50)
    print('menu'.upper().center(50))
    print('='*50)
    print('1. View list')
    print('2. Add item')
    print('3. Remove item')
    print('4. Sort list')
    print('5. Clear list')
    print('6. Exit')
    print('='*50)

    choice = input('Choose option (1-6): ')

    if choice == '1':
        if len(shopping_list) == 0:
            print('List is empty')
        else:
            print('Your Shopping List:')
            for i in range(len(shopping_list)):
                print(f'{i+1}. {shopping_list[i]}')

    elif choice == '2':
        item = input('Enter item: ').strip()
        if len(item) > 0:
             shopping_list.append(item)
             print(f'Added \'{item}\' to list')
        else:
            print('Invalid item!')
    elif choice == '3':
        if len(shopping_list) ==0:
            print('List is empty!')
        else:
             item = input('Enter item to remove: ')
             if item in shopping_list:
                 shopping_list.remove(item)
                 print('Item removed from list: {item}')
             else:
                 print('Invalid item')
    elif choice == '4':
        if len(shopping_list) > 0:
            shopping_list.sort()
            print('List sorted alphabetically!')
        else:
            print('List is empty!')
    elif choice == '5':
        if len(shopping_list) > 0:
            confirm = input('Clear all items? (yes/no): ').lower()
            if confirm == 'yes':
                shopping_list.clear()
                print('List cleard!')
            else:
                print('List is already empty!')

    elif choice == '6':
        print()
        print('Final shopping list:')
        if len(shopping_list) > 0:
            print(', '.join(shopping_list))
        else:
            print('(empty)')
        print('Goodbye!')
        running = False

    else:
        print('Invalid choice!')

print('='*50)
"""

# Step 27: Score analyzer => Analyze a list of scores
"""
print("=" * 50)
print("score analyzer".upper().center(50))
print("=" * 50)

scores = []
print("Enter scores (type 'done' when finished):")

while True:
    user_input = input(f"Score {len(scores) + 1}: ")

    if user_input.lower() == "done":
        break

    if user_input.isdigit():
        score = int(user_input)
        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Score must be  0-100!")
    else:
        print("Invalid input!")

if len(scores) == 0:
    print("No scores Entered!")

else:
    print("=" * 50)
    print("analysis".upper().center(50))
    print("=" * 50)

    # calculate statistics
    total = 0
    for score in scores:
        total += score

    average = total / len(scores)

    # Make a copy for sorting
    sorted_scores = sorted(scores)

    minimum = sorted_scores[0]
    maximum = sorted_scores[-1]

    # Find median
    middle = len(sorted_scores) // 2
    if len(sorted_scores) % 2 == 0:
        median = (sorted_scores[middle - 1] + sorted_scores[middle]) / 2
    else:
        median = sorted_scores[middle]
    

    print(f'Scores enterd: {scores}')
    print(f'Sorted scores: {sorted_scores}')
    print(f'count: {len(scores)}')
    print(f'Sum {total}')
    print(f'Average: {average}')
    print(f'Minimum: {minimum}')
    print(f'Maximum: {maximum}')
    print(f'Median: {median}')
    print(f'Range: {maximum - minimum}')

    #count passing/failing

    passing = 0
    for score in scores:
        if score >= 60:
            passing += 1
    
    print(f'Passing (>=60): {passing}')
    print(f'Failing (<60): {len(scores) - passing}')

    print('='*50)
"""

# Step 28: Word Frequency Counter => Count word frequencies
"""print('='*50)
print('word frequency conunter'.upper().center(50))
print('='*50)
print()

text = input('Enter text to analyze: ')

#split into words and clean
words = text.lower().split()

#Remove punctuation from each word
clean_words = []
for word in words:
    clean_word = ''
    for char in word:
        if char.isalnum():
            clean_word += char
    if len(clean_word) > 0:
        clean_words.append(clean_word)

print()
print(f'Total words: {len(clean_words)}')
print(f'Words: {clean_words}')
print()

#Find unique words and their counts
unique_words = []
for word in clean_words:
    if word not in unique_words:
        unique_words.append(word)

print(f'Unique words: {len(unique_words)}')
print()

#count and display
print('Word Frequenies:')
print('='*50)
for word in unique_words:
    count = clean_words.count(word)
    print(f' "{word}": {count}')

print('='*50)
"""

# Step 29: To-Do List with Priorities
"""
print('='*50)
print('to-do list manager'.upper().center(50))
print('='*50)

tasks = []
priorities = []

running = True
while running:
    print()
    print('Menu'.center(50,'-'))
    print('1. Add task')
    print('2. View tasks')
    print('3. Complete task')
    print('4. Sort by priority')
    print('5. Exit')

    choice = input('Choose (1-5): ')

    if choice == '1':
        task = input('Enter task: ').strip()
        if len(task) > 0:
            priority = input('Priority (1=High, 2=Medium, 3=Low): ')
            if priority in ['1','2','3']:
                tasks.append(task)
                priorities.append(int(priority))
                print(f'Added: \'{task}\'')
            else:
                print('Invalid priority!')
        else:
            print('Invalid task!')
    elif choice == '2':
        if len(tasks) == 0:
            print('No tasks!')
        else:
            print()
            print('Your Tasks:')
            print('-'*40)
            for i in range(len(tasks)):
                if priorities[i] == 1:
                    p = 'HIGH'
                elif priorities[i] == 2:
                    p = 'MEDIUM'
                else:
                    P = 'LOW'
                print(f' {i+1}.[{p}] {tasks[i]}')

    elif choice == '3':
        if len(tasks) == 0:
            print('No tasks!')
        else:
            task_num = input('Task nunmber to complete: ')
            if task_num.isdigit():
                index = int(task_num) - 1
                if 0 <= index < len(tasks):
                    completed = tasks.pop(index)
                    priorities.pop(index)
                    print(f"Completed: '{completed}")
                else:
                    print('Invalid task number!')
            else:
                print('Invalid input!')
    elif choice == '4':
        if len(tasks) > 0:
            #simple bubble sort by priority
            for i in range(len(tasks)):
                for j in range(len(tasks) -1):
                    if priorities[j] > priorities[j + 1]:
                        #Swap priorities
                        priorities[j], priorities[j + 1] = priorities[j + 1], priorities[j]
                        #Swap tasks
                        tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
            print('Tasks sorted by priority!')
        else:
            print('No tasks to sort!')

    elif choice == '5':
        print('GoodBye!')
        running = False

    else:
        print('Ivalid choice!')

print('='*50)
"""


# Part 8: Practice Tasks
# Task 1: Nunmber collector => Build a list of numbers and calculate statistics

"""print('number collector'.title())
print('='*50)

numbers = []

while True:
    user_input = input('Enter number (or done): ')
    if user_input.lower() == 'done':
        break
    if user_input.replace('-','').replace('.','').isdigit():
        numbers.append(float(user_input))


if len(numbers) > 0:
    print(f'Numbers: {numbers}')
    print(f' Count: {len(numbers)}')

    total= 0
    for num in numbers:
        total += num
print(f'Sum: {total}')
print(f'Average: {total / len(numbers):.2f}')
sorted_nums = sorted(numbers)
print(f'Min: {sorted_nums[0]}')
print(f'Max: {sorted_nums[-1]}')
"""


# Task 2: Remove Duplicates => Create a new list without duplicate value
"""
print("Remove Duplicates")
print("=" * 50)
original = [1,2,3,2,4,3,5,1,6,2]

print(f'Original: {original}')

unique = []

# for num in original:
#     if num not in unique:
#         unique.append(num)

# aur

for num in original:
    if num in unique:
        continue
    else:
        unique.append(num)

print(f'Unique: {unique}')
print(f'Removed {len(original) - len(unique)}')
"""

# Task 3: Reverse List without reverse() => Reverse a list without using reverse() method.

"""print("Reverse List")
print("=" * 50)
original = [1,2,3,4,5]
print(f'Original: {original}')
#Method 1 slice
reverse = original[::-1]
print(f'Reverse: {reverse}')
#Method 2: new list with insert at beginning
reverse_list = []
for item in original:
    reverse_list.insert(0,item)
print(f'Reverse: {reverse_list}')
#Method 3: Loop backwards
reverse_list2 = []
for i in range(len(original) -1, -1, -1):
    reverse_list2.append(original[i])
print(f'Reverse: {reverse_list2}')"""

# Task 4: merge and Sort => Merge two sorted lists into one sorted list
"""
print('Merge and Sort Lists')
print('='*50)

list1 = [1,4,7,10]
list2 = [2,5,8,11]

print(f'List 1: {list1}')
print(f'List 2: {list2}')

merged = []
merged.extend(list1)
merged.extend(list2)
print(f'Merged: {merged}')


merged.sort()
print(f'Sorted: {merged}')"""


# Task 5: Find Second Largest => Find the second largest number in a list
"""
print('Find Second Largest')
print('='*50)

numbers = [5,2,8,1,9,3,7]
print(f'Numbers: {numbers}')

#Method 1: sort and get second
sorted_nums = sorted(numbers, reverse=True)
second_largest = sorted_nums[1]
print(f'Second largest: {second_largest}')

# Method 2: without sorting
largest = numbers[0]

second = numbers[0]
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(f'Second largest (method 2) : {second}')"""


# Task 6: List Rotation => Rotate list elements by n positions

"""print('List rotation')
print('='*50)

original = [1,2,3,4,5]
n=2 #Rotate by 2 position

print(f'Original: {original}')
print(f'Rotate by: {n}')

#Rotate left
rotated_left = original[n:] + original[:n]
print(f'Rotated left: {rotated_left}')

#Rotate right
rotated_right = original[-n:] + original[:-n]
print(f'Rotated right: {rotated_right}')
"""

# Task 7: Interleave Lists => Combine two lists by alternating elements.
"""
print('Interleave Lists')
print('='*50)

list1 = ['a','b','c','d']
list2 = [1,2,3,4]


print(f'List 1: {list1}')
print(f'List 2: {list2}')

interleaved = []
for i in range(len(list1)):
    interleaved.append(list1[i])
    interleaved.append(list2[i])

print(f'Interleaved: {interleaved}')"""


# Task 8: Find common and Unique => Find common and unique elements between two lists.

'''print("Common and Unique elements")
print("=" * 50)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8,1]

print(f"List 1: {list1}")
print(f"List 2: {list2}")

#Method 1
common = []
unique = []

for num in list1:
    if num in list2:
        common.append(num)
    else:
        unique.append(num)

for num in list2:
    if num in list1 and num not in common:
        common.append(num)
    elif num not in unique and num not in common:
        unique.append(num)


print(f'Common method 1: {common}')
print(f'Unique method 1: {unique}')


#Common elements
common1 =[]
for item in list1:
    if item in list2 and item not in common1:
        common1.append(item)
print(f'Common Method 2: {common1}')


#Unique to list1
unique1 = []
for item in list1:
    if item not in list2:
        unique1.append(item)
print(f'Only in List 1: {unique1}')

# Unique to list2
unique2 = []
for item in list2:
    if item not in list1:
        unique2.append(item)

print(f'Only in list 2: {unique2}')
'''

#Task 9: Flatten nested list => Convert nested list to flat list
'''
print('Flatten Nested List')
print('='*50)

nested = [[1,2,3],[4,5],[6,7,8,9]]
print(f'Nested: {nested}')

flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
print(f'flat: {flat}')'''

#Task 10: List-Based Queue => Implement a simple queue (FIFO)
'''
print('QUEUE IMPLEMENTATION')
print('='*50)

queue = []
queue.append('Customer 1')
queue.append('Customer 2')
queue.append('Customer 3')
print(f'Queue: {queue}')

#Dequeue (remove from front)
served = queue.pop(0)
print(f'Served: {served}')
print(f'Queue: {queue}')

queue.append('Customer 4')
print(f'Added Customer 4: {queue}')

served = queue.pop(0)
print(f'Served: {served}')
print(f'Queue: {queue}')'''




























