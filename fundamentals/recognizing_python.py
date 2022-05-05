num1 = 42   # variable declaration, initalize number
num2 = 2.3   # variable declaration, initialize float
boolean = True # variable declaration , initialize boolean
string = 'Hello World'  # variable declaration initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')  # variable declarartion , intialize tuple
print(type(fruit)) # log statement , type check fruit
print(pizza_toppings[1])  # log statement, access value from list [1] = 'Sausage
pizza_toppings.append('Mushrooms')  # adding value to list
print(person['name'])  # log statement, accessing value from dictionary specifically [name]
person['name'] = 'George'  # changing the key value to 'George'
person['eye_color'] = 'blue'  # adding a key value pair to the dictionary
print(fruit[2])  # accessing the value from the tuple

if num1 > 45:      # conditional 42 > 45
    print("It's greater")  # log statement
else:              # conditinal
    print("It's lower")   # og statement

if len(string) < 5:     # conditional, length check of the value of string
    print("It's a short word!")     # log statement
elif len(string) > 15:  # conditional, length check of the value of string
    print("It's a long word!")     # log statement
else:                   # conditional
    print("Just right!") # log statement

for x in range(5):      # for loop start at 0, increment by 1 and stop at 5
    print(x)            # log statement
for x in range(2,5):    # for loop start at 2, increment by 1 and stop at 5
    print(x)            # log statement
for x in range(2,10,3): # for loop start at 2, increment by 3 and stop at 10
    print(x)            # log statement
x = 0                   # variable declaration, initialize number
while(x < 5):           # while loop start 0, increment by 1 and stop at 5
    print(x)            # logs the value of x
    x += 1              # increments by 1

pizza_toppings.pop()   # removes the last value from the list
pizza_toppings.pop(1)  # removes the second value from the list

print(person)          # log the dictinary person
person.pop('eye_color')  # removes the key 'eye_color' from the dictionary
print(person)          # log the dictionary person

for topping in pizza_toppings:  # for loop starts
    if topping == 'Pepperoni':  # conditional if topping equals 'Pepperoni'
        continue                # continue with the foor loop
    print('After 1st if statement') # log statement
    if topping == 'Olives':     # conditional if topping equals 'Olives'
        break                   # break stop for loop

def print_hello_ten_times():    # function name , parameters are empty
    for num in range(10):       # for loop starts at 0, increments by 1 ans stops at 10
        print('Hello')          # log statement

print_hello_ten_times()         # function with empty parameters

def print_hello_x_times(x):     # function name, parameter is x
    for num in range(x):        # for loop starts at 0, increments by 1 and ends at 4
        print('Hello')          # log statement

print_hello_x_times(4)          # function, parameter is 4

def print_hello_x_or_ten_times(x = 10): # function name, parameter is x = 10
    for num in range(x):        # for loop starts at 0, increments by 1 and ends at 10
        print('Hello')          # log statement

print_hello_x_or_ten_times()    # function, parameter is empty
print_hello_x_or_ten_times(4)   # function, parameter is 4


"""
Bonus section
"""

# print(num3)       #  Num3Error: num3 <variable num3> is not defined
# num3 = 72         # variable declaration, intialize number
# fruit[0] = 'cranberry'        # TypeError: 'tuple' object does not accept item assignment
# print(person['favorite_team'])  # KeyError: 'favorite team'
# print(pizza_toppings[7])      # IndexError: list index out of range
#   print(boolean)          # IndentationError: unexpected indent
# fruit.append('raspberry')       # AtttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)              # AttributeError: 'tuple' object has no attribute 'pop'