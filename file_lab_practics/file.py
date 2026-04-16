print('basic file operations'.capitalize())
print('='*50)

#create a simple text file first
#Open kfile for writing 

file = open('example.txt', 'w')

#Write some content
file.write("Hello, World!\n")
file.write("This is a test file. \n")
file.write("Python file I/O is useful! \n")

#IMPORTANT: always close the file
file.close()

print("File created adnd closed successfully!")

#Now open and read the file

file = open("example.txt", 'r')

#read entire content 
content = file.read()

#close the file

file.close()


print('\nfile content:')
print('-'*50)
print(content)
print('-'*50)



#check what heppens if you forget to  close
print('\nNote: Forgetting to close files can cause:')
print(' - Data not being written properly')
print(' - Memory leaks')
print(' - File lock issues (especially on windows)')
print(' - Resource exhaustion with many files')