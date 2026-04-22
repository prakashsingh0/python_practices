# lab25_file_position.py
# Understanding file position and seeking

print("File Position and Seeking")
print("=" * 50)

#Create a test file

with open('position_demo.txt','w') as f:
    f.write('ABCDEFGHIJ') #10 characters, no newline
print('File content: \'ABCDEFGHIJ\' (10 CHARACTERS)')


#Open for reading

file = open('position_demo.txt','r')

#tell() get current position
print(f'\n--- file position with tell() ---')
print(f'Initial position: {file.tell()}')
#Read some characters
chars = file.read(3)
print(f'read 3 characters : \'{chars}\'')
print(f'Position now: {file.tell()}')
chars = file.read(2)
print(f'read 2 characters : \'{chars}\'')
print(f'Position now: {file.tell()}')

#seek() - move to a specific position
# seek() - move to a specific position
print(f"\n--- Moving with seek() ---")

# seek(0) - go back to beginning
file.seek(0)
print(f'After seek(0): position = {file.tell()}')
print(f'Read all: "{file.read()}"')
# seek(5) - go back to position 5
file.seek(5)
print(f'\nAfter seek(5): position = {file.tell()}')
print(f'Read form there: "{file.read()}"')

#seek with offset from end (mode 2)
file.seek(0,2) # 0 bytes from end

print(f'\nAfter seek(0,2) [end]: Position = {file.tell()}')

#seek with offset from current (mode 1)

file.seek(0)
file.read(3)
print(f'\nAt position {file.tell()}, seek(2,1) moves +2 from current')

#Note: seeking from current position only works in binary mode
file.close()












