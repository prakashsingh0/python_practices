'''print('Creaating Your First Class')
print('='*50)

#define a simple class
class Dog:
    """A Simple class representing a dog."""
    pass # 'pass' mean the class is empty now

#Create object (instances) from the class
dog1 = Dog()
dog2 = Dog()

print(f'\nDog1 is of type {type(dog1)}')
print(f'\nDog2 is of type: {type(dog2)}')
print(f'\nDog1 and  Dog2 are the same object: {dog1 is dog2}')
print(f'\nBut the are both Dog objects : {isinstance(dog1, Dog) and isinstance(dog2, Dog)}')
# WE can add attributes to objects directly
dog1.name = "Buddy"
dog1.age = 3
dog2.name = 'Mac'
dog2.age = 5

print(f'\ndog1 {dog1.name}, {dog1.age} yesrs old')
print(f'\ndog1 {dog2.name}, {dog2.age} yesrs old')'''

'''print('Adding methods to a class')
print('='*50)

class Dog:
    """A class representingg a dog with methods."""
    def bark(self):
        """Make the dog bark."""
        print('Woof! woof!')
    
    def sit(self):
        """Make the dog sit."""
        print('the dog sites down.')

    def roll_over(self):
        """Make the dog roll over."""
        print('The dog rolls over!')

#Create a dog object

my_dog = Dog()

#Call methods on the object

print('\nCalling methods on my_dog:')

my_dog.bark()
my_dog.sit()
my_dog.roll_over()

# We can stil add attributes
my_dog.name = "Buddy"
print(f'\n{my_dog.name} performs tricks!')
my_dog.bark()
'''

#The __init__ method
'''
print('The __init() method')
print('='*50)

class Dog:
     """A Dog class with initialization."""

     def __init__(self,name, age):
          """Initialize a new Dog object"""
          print(f' Creating a new Dog named {name}...')
          self.name = name
          self.age = age
        
     def bark(self):
          """Make the dog bark."""
          print(f'{self.name} says: Woof! Woof!')
    
     def describe(self):
          """Describe the dog."""
          print(f'{self.name} is {self.age} yesrs old')
#Create objects - init__ runs automatically
print('\nCreating dog1:')
dog1 = Dog('Buddy', 3)

print('\nCreating dog2:')
dog2 = Dog("Max",5)

#Using the objects

print('\n--- Dog Information ---')
dog1.describe()
dog1.bark()

print()
dog2.describe()
dog2.bark()'''


#Step 5: ___init___ with default parameters

'''print('___init___ with default parameters')
print('='*50)

class Student:
    """A Stundent class with default values"""
    def __init__(self,name, age=18,grade='Freshman'):
        """
        Initialize a Student.
        Agrs:
            name: Student's name (required)
            age: Student's age (default: 18)
            grade: Student's grade level (default: "Freshman")

        """
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = [] #Empty list for courses

    def display_info(self):
        """Display student information."""
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Grade: {self.grade}')
        print(f'Courses: {self.courses if self.courses else "None enrolled"}')
    
    def enroll(self,course):
        """Enroll in  course."""
        self.courses.append(course)
        print(f'{self.name} enrolled in {course}')


#Creating students with different parameters

print('\n--- Student 1: all parameters --')
student1 = Student("Alice", 20, "junior")
student1.display_info()

print('\n---Student 2: Using Defaults ---')
student2 = Student("Bob") # Using default age and grade
student2.display_info()

print('\n---Student 3: Partial parameters ---')
student3 = Student("Charlie", 19) # Using default grade only
student3.display_info()

#Enrolled in courses
print('\n--Course Enrollment---')
student1.enroll(input("Enter relavent course : "))
student1.enroll(input("Enter relavent course : "))
print(f'\n{student1.name}\'s course: {student1.courses}')
'''

# step 6: how self Works 
'''print("underStanding the \'self\' Parameter")
print('='*50)


class Person:
    """A Person class to demonstrate self."""
    def __init__(self, name):
        """Initialize with name."""
        print(f' __init__ called with self = {self}')
        self.name = name
    
    def greet(self):
        """Greet the person."""
        print(f'Greet called wtih self = {self}')
        print(f'Hello, my name is {self.name}')

    def introduce_to(self,other_person):
        """Introduxe self to another person."""
        print(f' {self.name}  says: Nice to meet you, {other_person.name}!')
        print(f' {other_person.name} says: Nice to meet you too, {self.name}')


#Create Person objects
print('\n Creating person1.:')
person1 = Person("Alice")

print('\nCreate person2:')
person2 = Person('Bob')

#Call methods
print('\n---Calling greet on person1 --')
person1.greet()

print('\n---Calling greet on person2 ---')
person2.greet()

#Introducing
print('\n--- Introducing person1 to person2 ---')
person1.introduce_to(person2)

#The manual way (equivalent but not recommended)
print('\n---Manual method call (understanding)---')
print('Person.greet(person1) is the same as person.greet()')

Person.greet(person1) #Explicitly passing person1 as self
'''

#Step 7: Using self to call Other Methods
'''
print("Using self to call other methods")
print('='*50)


class BankAccount:
    """A siple back account class."""

    def __init__(self,owner,balance=0):
        """Initialize account with owner and optional balance"""
        self.owner = owner
        self.balance = balance
        self.transaction_count = 0

    def deposite(self,amount):
        """Deposit money into the account."""
        if amount>0:
            self.balance += amount
            self._record_transaction() #call another method using self
            print(f'Deposited ${amount:.2f}. New balance: ${self.balance:.2f}')
        else:
            print('Deposite amount must be positive!')

    def withdraw(self,amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print(f'Insufficient funds! Balance: ${self.balance:.2f}')
            return False
        elif amount <= 0:
            print('Withdraw amount must be positive!')
            return False
        else:
            self.balance -= amount
            self._record_transaction() # Call another method using self
            print(f'Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}')
            return True
        
    def _record_transaction(self):
        """Record that a transaction occurred (internal method)."""
        self.transaction_count += 1
    def display_info(self):
        """Display account information."""
        print(f'\n---Account Information---')
        print(f'Ower: {self.owner}')
        print(f'Balance: ${self.balance:.2f}')
        print(f'Transactions: {self.transaction_count}')
    
    def transfer_to(self, other_account, amount):
        """Transfer money to another account."""
        print(f'\nTransferring ${amount:.2f} from {self.owner} to {other_account.owner}...')
        
        #Use self to withdraw from this account
        if self.withdraw(amount):
            #Use the other account object to deposit
            other_account.deposite(amount)
            print('Transfer successful')
        else:
            print('Transfer failed!')

# Create accounts
account1 = BankAccount('Alice',1000)
account2 = BankAccount('Bob', 500)

#Test operations
print('\n--- Testing operation ---'.title())
account1.deposite(200)
account1.withdraw(150)
account1.withdraw(2000) # Should fail

#Transfer
account1.transfer_to(account2, 300)

#Display final state
account1.display_info()
account2.display_info()
'''

# Step 8: Instance Variables
# Instance Variables - unique to each object

'''print("Instance Variables")
print('='*50)


class Cat:
    """A Cat with instance variables."""

    def __init__(self,name, color):
        """Each cat has its own name and color."""
        self.name = name #Instance variable
        self.color = color #Instance variable
        self.lives = 9 # Instance variable (same inital value, but uniue copy)

    def describe(self):
        """Describe the cat."""
        print(f'{self.name} is a {self.color} cat with {self.lives}')

    def lose_life(self):
        """The cat loses a life."""
        if self.lives > 0:
            self.lives -= 1
            print(f'{self.name} lost a life! {self.lives} lives  remaining.')
        else:
            print(f'{self.name} has no lives lieft!')


#Create two cats

cat1 = Cat('Whiskers','orange')
cat2 = Cat("shadow",'Black')

#Each cat has its own variables

print('\n--- Inital State ---')
cat1.describe()
cat2.describe()

#Modifying one cat doesn't affect the other
print('\n--- Whiskers has an adventure ---')
cat1.lose_life()
cat1.lose_life()

print('\n---final State ---')
cat1.describe()
cat2.describe() #Shadow still has 9 lives!

print('\n--- Proof they\' separete ---')
print(f'cat1.lives = {cat1.lives}')
print(f'cat2.lives = {cat2.lives}')
print(f'Same object? {cat1.lives is cat2.lives}')
'''

# Step 9: Class Variables
# Class variables - shared by all instances
'''
print('class variables'.title().center(50))
print('='*50)

class Employee:
    """An Employee class with class and instance variables."""
    # Class variables = shared by all employee
    company_name = 'TechCorp Inc.'
    total_employees = 0
    all_employees = []

    def __init__(self,name,position,salary):
        """Initialize an employee."""
        # Instance variables - unique to each employee
        self.name = name
        self.position = position
        self.salary = salary
        self.employee_id = Employee.total_employees + 1

        # Update class variables
        Employee.total_employees += 1
        Employee.all_employees.append(self)

    def display_info(self):
        """Display employee information."""
        print(f'ID: {self.employee_id}')
        print(f'Name: {self.name}')
        print(f'Position: {self.position}')
        print(f'Salary: ${self.salary:.2f}')
        print(f'Company: {Employee.company_name}')

    @classmethod
    def get_company_info(cls):
        """Display company-wide information."""
        print(f'\n{cls.company_name}'.center(20,'='))
        print(f'Total Employees: {cls.total_employees}')

    @classmethod
    def list_all_employees(cls):
        """List all employees."""
        print(f'\nAll employees at {cls.company_name}')
        for emp in cls.all_employees:
            print(f' - {emp.name} ({emp.position})')


# Create employees

print('\ncreating employees'.title().center(20,'-'))
print('='*50)
emp1 = Employee('Alice','Software Engineer',85000)
print(f'Created: {emp1.name}')

emp2 = Employee('Bob','Data Engineer',75000)
print(f'Created: {emp2.name}')

emp3 = Employee('Charlie','Project Manager',95000)
print(f'Created: {emp3.name}')

#Display company info (class variable)
Employee.get_company_info()

#List all employees
Employee.list_all_employees()

#display individual info
print('\nemployee details'.title().center(20,'-'))
emp1.display_info()

print()
emp2.display_info()

#Changing class variable affects all instances
print('\ncompany rebranding'.title().center(20,'-'))
Employee.company_name = 'InnovateTech LTD.'
print(f'emp1\'s company: {emp1.company_name}')
print(f'emp2\'s company: {emp2.company_name}')
print(f'emp3\'s company: {emp3.company_name}')
print('All show the new name!')
'''

# Step 10: Instance vs Class Variable Comparison
#lab23_variable_comparison.py
#comparing instance and class variables
"""
print("Instance vs class variables comparison".capitalize())
print('*'*50)


class Counter:
    """A class to demonstrate instace vs class variables"""

    #Class variable - shared counter
    class_count = 0

    def __init__(self,name):
        self.name = name

        #instance variable - each object has its own
        self.instance_count = 0

        Counter.class_count += 1

    def increament(self):
        """Increament both counters."""

        self.instance_count += 1
        Counter.class_count += 1
        print(f'{self.name}: instance = {self.instance_count}, class = {Counter.class_count}')


#Create counters

print('\n---Creating Counters ---')
counter_a = Counter('A')
counter_b = Counter('b')


print(f'After creating 2 counters:')
print(f' Class count: {Counter.class_count}') #2(one per __init__ call)

#Increment counter_a several times
print('\n--- Incrementing A ---')
counter_a.increament()
counter_a.increament()
counter_a.increament()

print('\n--- Incrementing B ---')
counter_b.increament()
counter_b.increament()


#Final comparison
print('\n--- Final State ---')
print(f'counter_a.instance_coun = {counter_a.instance_count}') #3
print(f'counter_a.instnace_count = {counter_b.instance_count}') #2
print(f'Counter.class_count = {Counter.class_count}') # 7 (2 init + 3 + 2)

# Important : Accessing class variable tthrough instance
print('\n--- Accessing class variable through instance ---'.capitalize())
print(f'counter_a.class_count = {counter_a.class_count}') #Works, but not recommended
print(f'counter_b.class_count = {counter_b.class_count}') #Same value
print('Note: Both shjow the same value because it\'s a class variable!')"""

# Part 6: Creating and Using Objects
# Step 11: A Complete Class Example

print()















          

