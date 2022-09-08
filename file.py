# variable declaration
# Data Types - Primitive - Numbers
num1 = 42

# variable declaration
# Data Types - Primitive - Float
num2 = 2.3

# variable declaration
# Data Types - Primitive - Bool
boolean = True

# variable declaration
# Data Types - Primitive - Strings
string = 'Hello World'

# variable declaration
# Data Types - Composite - List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable declaration
# Data Types - Composite - Dict
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable declaration
# Data Types - Composite - Tuple
fruit = ('blueberry', 'strawberry', 'banana')

# log statement
# type check
print(type(fruit))

# log statement
# Data Types - Composite - List - access value
print(pizza_toppings[1])

# Data Types - Composite - List- add value
pizza_toppings.append('Mushrooms')

# log statement
# Data Types - Composite - Dict - access value
print(person['name'])

# Data Types - Composite - Dict - change value
person['name'] = 'George'

# Data Types - Composite - Dict - initialize
person['eye_color'] = 'blue'

# log statement
# access value
print(fruit[2])

# conditional if
if num1 > 45:
    print("It's greater")
# conditional else
else:
    print("It's lower")

# conditional if
# length check
if len(string) < 5:
    # log statement
    print("It's a short word!")
# conditional else if
# length check
elif len(string) > 15:
    # log statement
    print("It's a long word!")
# conditional else  
else:
    # log statement
    print("Just right!")

# for loop start
for x in range(5):
    # log statement
    print(x)

# for loop start
for x in range(2,5):
    # log statement
    print(x)

# for loop start
for x in range(2,10,3):
    # log statement
    print(x)

# variable declaration
x = 0

# while loop start
while(x < 5):
    # log statement
    print(x)
    # while loop - increment
    x += 1

# Data Types - Composite - List - delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

# log statement
print(person)

# Data Types - Composite - Dict - delete value
person.pop('eye_color')

# log statement
print(person)

# for loop - start
for topping in pizza_toppings:
    # conditional if
    if topping == 'Pepperoni':
        # for loop - continue
        continue
    # log statement
    print('After 1st if statement')
    # conditional if
    if topping == 'Olives':
        #for loop break
        break

# function
def print_hello_ten_times():
    # for loop - start
    for num in range(10):
        # log statement
        print('Hello')

# function (call function)
print_hello_ten_times()

# function
# x = function parameter
def print_hello_x_times(x):
    # for loop - start
    for num in range(x):
        # log statement
        print('Hello')

# function
# 4 = function argument
print_hello_x_times(4)

# function
# x = function parameter
def print_hello_x_or_ten_times(x = 10):
    # for loop - start
    for num in range(x):
        # log statement
        print('Hello')

# function (call function)
print_hello_x_or_ten_times()

# function (call function)
# 4 = function argument
print_hello_x_or_ten_times(4)

# comment multiline
"""
Bonus section
"""

# log statement
# NameError: name <variable name> is not defined
# TODO: print(num3)

# variable declaration
num3 = 72

# TypeError: 'tuple' object does not support item assignment
fruit[0] = 'cranberry'

# KeyError: 'favorite_team'
print(person['favorite_team'])

# IndexError: list index out of range
print(pizza_toppings[7])

# IndentationError: unexpected indent
   print(boolean)

# AttributeError: 'tuple' object has no attribute 'append'
fruit.append('raspberry')

# AttributeError: 'tuple' object has no attribute 'pop'
fruit.pop(1)