# So far we lhave senn many built-in Python Functions.
# In ths section, we will focus o custom fucntions
# Defining a Function
# A function is a reusable block of code or programming statements designed to perform a certain task
# Python provides the def key word

# Declaring and calling a Function
# When we make a function, we call it declaring a function
# When we use it, we call it or invoke it
# Funcs can have or not parameters

# Function whithout parameters
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # Calling a function

# Function returninf a Value - Part 1
# Function can also return values, if a function does not have a return satement, the value of the function is None
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name)

# Function with parameters
# Single Paramenters: if our function takes a parametes we should call our function with an argument
def greetings(name):
    message = name + ', welcome'
    return message
print(greetings('Asabeneh'))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
print(sum_of_numbers(10))

# two parametes: If our function takes parameters we should call it with arguments
def generate_full_name(first_name, last_name):
    space = ' '
    full_name =first_name + space + last_name
    return full_name
print('Full Name:', generate_full_name('Asabeneh','Yeteyah'))

# Passing Arguments with key and Value
# if we pass the arguments with key and value, the order of ther arguments does not matter.
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(lastname='Yetayeh',firstname='Asabeneh')

# Function Returnin a Value - Part 2
# if the func is not return a value, then is returning None by default
# we can return any kind of data type from a function
def print_name(firstname):
    return firstname
print_name('Asabeneh')

def add_two_numbers (num1,num2):
    total = num1 + num2
    return total
print(add_two_numbers(2,3))

#list
def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Function with Default Paramerters
# Sometimes we pass default values as parametes, when we invke the function.
# if we do not passa arguments when calling the function, their default values will be used
def greetings (name = 'Peter'):
    message = name + ', welcome'
    return message
print(greetings())
print(greetings('Asabeneh'))

def weight_of_object(mass,gravity=9.81):
    weigth = str(mass * gravity)+ ' N'
    return weigth
print('Weight of an object in Newtons', weight_of_object(100))
print('Weight of an object in Newtons', weight_of_object(100, 1.62)) # Moon

# Arbitrary Number of arguments
# if we do not know the number of arguments we pass to out function, we can create a func which can take arbritrary number of arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total +=num
    return total
print(sum_all_nums(2,3,5))

# Default and Arbritary Number of Paramets in Functions
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

# Function as a parameters of another function
# Higher-Order Function
def square_number (n):
    return n * n
def do_something(f,x):
    return f(x)
print(do_something(square_number, 3))




                                        