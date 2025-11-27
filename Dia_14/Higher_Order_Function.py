# In python function are treated as first cllas citzen, allowing you to perform the following operations on functions
# a functiona can take one or moe functions as parameters
# a function can be returned as a result of another function
# a function can be modified
# a function can be assigned to a variable

# In this section, we will cover:
# Handling function as parameters
# Returnin funtions as return value from another functions
# Using python closures and decorators

# Function as a parameter
def sum_numbers(nums): # normal func
    return sum(nums) # a sad function abusing the built-in sum function 
def higher_order_function(f,lst): # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1,2,3,4,5])
print(result)

# Function as a return value
def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    elif type == 'add':
        return lambda x, y : x + y
result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result =higher_order_function('absolute')
print(result(-3))
result = higher_order_function('add')
print(result(1,3))
# Nesse exemplo vimos que a função higher orde function retorna diferente funções dependendo do resultado
# result vira uma cópia das funções acima, ou no caso do lambda vira um cópia da funç]ao anonima

# Python Closures
# Python allow a nested function to acess the outer scope of the enclosing function. 
# This is known as a closure
# In python closure is created by a nesting a function inside snother eccapsulating function and then returnin the inner function
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(5))

def add_buzz():
    buzz = 'buzz'
    def add(ans):
        return ans + buzz
    return add
closure_result = add_buzz()
print(closure_result('oiiiii'))

# Python decorators
# A decorator is a design pattern in Python that allows user to add new functionality to an existing object without modifying its structure
# Decorator are usually called before the definition of a function you want to decorate
# CREATING DECORATORS
# to create a decorator function, we need outer function with inner wrapper function

def greetings():
    return 'welcome to python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greetings)
print(g())

# Let us implment the example above with a decorator
def uppercase_decorator(function):
    def wrapper():
        # aqui a função greetings é renomeada para func
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greetings():
    return 'Welcome to Python'
print(greetings())

# Applying multiple decorator to a single function
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_decorator(function):
    def wrapper():
        func = function()
        split_func = func.split()
        return split_func
    return wrapper

# POR ALGUM MOTIVO, os decoradores são executados de baixo pra cima(dentro pra fora), por isso, é importante inverter a ordem nesse exemplo oq se não 
# o split_decorator retornará uma lista o que impede o uppercase_decorator de funcionar
@split_decorator
@uppercase_decorator
def greetings():
    return 'Welcome to Python'
print(greetings())

# tentativa de entender essa parada
def string_decorator(function):
    def wraper():
        func = function()
        list_to_string = ", ".join([str(number)for number in func])
        return list_to_string
    return wraper
def prefix_decorator(function):
    def wrapper():
        func = function()
        string_prefix = 'A lista é: ' + func
        return string_prefix
    return wrapper
def exclamation_decorator(function):
    def wrapper():
        func = function()
        string_exclamation = func + '!'
        return string_exclamation
    return wrapper
@exclamation_decorator
@prefix_decorator
@string_decorator
def get_numbers():
    return [1,2,3,4]
print(get_numbers())

# Accepting Parameters in Decorators Functions
# Most fo the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1,para2,para3):
        function(para1,para2,para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters
@decorator_with_parameters
def print_full_name(first_name,last_name,country):
    print("I am {} {}. I love to teach".format(first_name, last_name, country))

print_full_name('PO','IA','CACA')





nums = [3,1,3]
target = 6
def sum_of_index_to_target(lista,target):
    i , j = 0, 1
    index = []
    while i<len(lista):
        while j<len(lista):
            if target == lista[i]+lista[j]:
                index.append(i)
                index.append(j)
                return index
            j += 1
    i += 1        
print(sum_of_index_to_target(nums, target))