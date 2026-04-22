print('Different ways to read files')
print('='*50)

#First create a test file

with open('sample.txt','w') as f:
    f.write("Line 1: Hello, world!\n")
    f.write('Line 2: python is awesome!\n')
    f.write('line 3: Fiule I/O is important. \n')
    f.write("Line 4: This is the fourth line.\n")
    f.write("Line 5: The end of our sample file.\n")

print('Test file cread with 5 lines.\n')

# Method 1: read() - reads entire file as string
print("--- Method 1: read() ---")

file = open('sample.txt','r')

content = file.read()

file.close()

print(f'Type : {type(content)}')
print(f'Length: {len(content)}')

print("content:")
print(content)

# Method 2: read(n) - read n characters
print("\n--- Method 2: read(n) - Read n characters ---")

file = open('sample.txt','r')
chunk1 = file.read(10) #First 10 characters
chunk2 = file.read(10) # next 10 characters
file.close()

print(f'First 10 chars: "{chunk1}"')
print(f'Next 10 characters: "{chunk2}"')


#Method 3: readline() - read one line at a time
print('\n--- Method 3: readline()---')

file = open('sample.txt','r')

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
file.close()
print(f"Line 1: {line1!r}")
print(f"Line 2: {line2!r}")
print(f"Line 3: {line3!r}")
print("Note: Lines include the newline character \\n")

# Method 4: readlines() - read all lines into a list
print("\n--- Method 4: readlines() ---")
file = open('sample.txt','r')
lines = file.readlines()
file.close()
print(f'Type: {type(lines)}')
print(f'Number of lines: {len(lines)}')
print(f'Lines list:')
for i, line in enumerate(lines,1):
    print(f'{i}:{line!r}')


# Method 5: Iterate over file object (most memory efficient)
print("\n--- Method 5: Iterate over file object ---")
file = open('sample.txt','r')

print("Reading line by line:")
line_count = 0
for line in file:
   line_count += 1
   print(f'{line.strip()}')
file.close()
print(f'Total lines: {line_count}')
print('This is the most memory-efficient method for large files')



