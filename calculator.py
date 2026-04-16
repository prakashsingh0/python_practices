"""print("=============================")
print("1. Addition \n2. Substraction \n3. Multiplication \n4. Division")
print("=============================")
operator = int(input("Choose Operator : "))

value1= float(input("Enter first number : "))
value2 = float(input("Enter first number : "))

if operator == 1:
    print(value1 + value2)
elif operator == 2:
    print(value1 - value2)
elif operator == 3:
    print(value1 * value2)
elif operator == 4:
    print(value1 / value2)
else:
    print("Please Choose a vailid number")
 """



#play with variable

"""width = 40
height = 10
area = width * height

perimeter = 2 * (width + height)

print("Area", area)

print("perimete", perimeter)"""

# task:5 temperature calculator
'''celsius = 25
farhenheit = (celsius * 9/5) + 32

print("temperature in Farhenheit : ", farhenheit)
'''


#Task 6: Circle Calculations
#Objective: Calculate circumference and area of a circle.

'''PI = 3.14159
radius = 7

circumference = 2 * PI * radius

area = PI*radius**2

print(f"Redius : {radius}")

print(f"Circumference : {circumference}")

print(f"Area : {area}")'''


#Task 7: Shopping Cart Total
#Objective: Calculate shopping cart total with tax.
'''
item1 = 29.99
item2 = 15.50
item3 = 8.99

subtotal = item1+item2+item3

tax_rate = 0.08
tax = subtotal*tax_rate
total = subtotal + tax


print(f"Subtotal : {subtotal}")

print(f"Tax : {tax}")

print(f"Total : {total}")
'''

#Task 8: Seconds Conversion
#Objective: Convert seconds to hours, minutes, and seconds.

# Task 8: Seconds Conversion
'''total_seconds = 3725

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60

seconds = remaining_seconds % 60

print("Hours : {}".format(hours))
print(f"Minuts : {minutes}")
print("Second : {}".format(seconds))
'''
#Task 9: Average Calculator
#Objective: Calculate the average of five numbers.

'''num1 = 34
num2 = 45
num3 = 89
num4 = 90
num5 = 21

total = num1 + num2 + num3 + num4 + num5

average = total /5

print(f"Number {num1} {num2} {num3} {num4} {num5}")
print("Average : {}".format(average))

print("Total : {}".format(total))'''

#Task 10: Using In-Place Operators
#Objective: Practice in-place operators.

'''score = 0
print(f"Initial Score : {score}")

score +=10
print(f"After gaining 10 point : {score}")

score +=15
print(f"After gaining 10 point : {score}")

score -= 5 
print(f"After losing 5 point : {score}")

score *=2 
print(f"After doubling : {score}")

score //= 3
print("After Integer Devision by 3 : {}".format(score))'''


#Task 11: Compound Interest
#Objective: Calculate compound interest.
#Formula: A = P(1 + r)^t

'''principal = 1000
rate = 0.05
time = 5

amount = principal*(1+rate) ** time

print(f"Principal : {principal}")
print(f"Rate : {rate}")
print(f"Time : {time}")
print(f"Total Amount : {amount}")'''

#Task 12: Even or Odd Checker
#Objective: Use modulo to check if numbers are even or odd.

num1 = 15
num2 = 28
num3 = 101

print(f"{num1} % 2 = {num1%2}")
print(f"{num2} % 2 = {num2%2}")
print("{} % 2 = {}".format(num3,num3%2))
