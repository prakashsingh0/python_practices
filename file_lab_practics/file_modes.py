# file_modes.py
#Under standing different file modes

print('File MOdes in Python')
print('='*50)
print("""
Common File MOdes:
-----------------
      'r' - Read (default). file must exist.
      'w' - Write. Creates new file or truncates existing .
      'a' - Append. create new file or appends to exixting.
      'x' - Exclusive creation. Fails if file exists.

      'r+' - Read and write . file must exist//
      'w+' - Write and read. Creates new or truncates.
      'a+' - Append and read. Creates new or appends.


      Binary Modes (add 'b'):
      'rb' - Read binary
      'wb'- Write binary
      'ab' - Append binary
""")

#Demonstrate 'w' mode - Creates/Truncates
print('\n --- MOde \'w\' (Write) ---')
file = open('modes_demo.txt', 'w')
file.write("Line 1 - original\n")
file.write("Line 2 - original\n")
file.close()
print('Create file with 2 lines.')

#read and show

file = open('modes_demo.txt','r')
print(f'Content: {file.read()}')
file.close()


#demonstrate 'w' mode again - truncates!
print('\n--- Mode \'w\' again (truncates!) ---')
file = open('modes_demo.txt','w')
file.write('New content - old content is GONE!\n')
file.close()

file = open('modes_demo.txt','r')
print(f'Content: {file.read()}')
file.close()


#Demonstrate 'a' mode - appends

print('\n---Mode \'a\' (Append) ---')
file = open('modes_demo.txt','a')
file.write('This line was appended. \n')
file.write('and this one too.')
file.close()

file = open('modes_demo.txt','r')
print(f'Contents: {file.read()}')
file.close()

#Demonstrate 'r+' mode - read and write
print("\n --- Mode 'r+' (read/write) ---")
file = open('modes_demo.txt','r+')
content = file.read()
print(f'Read {len(content)} characters')
file.write('Added at the end with r+ \n') #Write at current postion (end)
file.close()

file = open('modes_demo.txt','r')
print('Final content:')
print(file.read())
file.close()