# Python uses try and axcept to handle erros gratefulls. 
# A graceful exit(or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "extis fracefully"
# In a controller manner as a result
# Often the program prints a decriptive error message to a terminal or log as part of the grateful exit, this makes our application more robust
# The cause fo an exception is often external to the program itself
# An example of exceptions could be an incrorrect input, wrong file name, unalbe to find a file, a mafunctiong IO device.
# Graceful handling errors prevent out applications from crashing

# Example
# Try:
# {run this code} "IF THINGS GO WELL"
# Except:
# {Execute this code when is an exception} "IF THINGS GO WRONG"
# Else: 
# {No exception? Run this code}
# Finally:
# {Always run this code}


try:
    print(10 +'5')
except:
    print('Something went wrong')

try:
    # name = input('Enter your name:')
    name = 'wagner'
    # year_born = input('Year you were born:')
    year_born = '1' # STRING
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}')
except:
    print('Something went wrong')
# In this example we do not know(actually i know) what error it was
try:
    # name = input('Enter your name:')
    name = 'wagner'
    # year_born = input('Year you were born:')
    year_born = '1' # STRING
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value Error occured')
except ZeroDivisionError:
    print('Zero division error occured')

# In this code above the output is going to be typeError. 
# Now, lets add an addictional block
try:
    # name = input('Enter your name:')
    name = 'wagner'
    # year_born = input('Year you were born:')
    year_born = '1' 
    age = 2019 - int(year_born) # INT
    print(f'You are {name}. And your age is {age}')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value Error occured')
except ZeroDivisionError:
    print('Zero division error occured')
else:
    print('I usually run with the try block') # this one always run if there is no exception
finally: 
    print('I always run')

# It is also shorten the above code as follows
try: 
    # name = input('Enter your name:')
    name = 'wagner'
    # year_born = input('Year you were born:')
    year_born = '1' 
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

# Packing and Unpacking Arguments in Python
# we use two operators:
# * for tuples
# ** for dictionaries

# Unpacking
def sum_of_five_nums(a,b,c,d,e):
    return a + b + c + d + e
lst = [1,2,3,4,5]
# print(sum_of_five_nums(lst)) 
# Type error: missing arguments: b,c,d,e
# This functoin takes numbers(not a list)
print(sum_of_five_nums(*lst))

# we can also use unpacking in the range built-in function that excepts a start and an end
numbers = range(2,7)
print(list(numbers))
args = [2,7]
numbers = range(*args)
print(list(numbers))

# a list or a tuple can also be unpacked like this
countries = ['Finland','Sweden','Norway','Denmark','Iceland']
fin, sw, nor, *rest = countries
print(fin,sw,nor,rest)
numbers = [1,2,3,4,5,6,7]
one, *middle, last = numbers
print(one,middle,last)

# Unpackin Dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'wagner','country':'brazil','city':'bsb','age':'69'}
print(unpacking_person_info(**dct))

# Packing
# Sometime we never know hoe many arguments need to be passed to a python. 
# We can use the packing method to allow out function to take unlimited number or arbitrary number of arguments
# Packing list
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6,7)) 

# Packing Dictionaries
def packing_person_info(**kwargs):
    # check the type of kwargws and its is a dict type
    # print(type(kwargs))
    # printing dictionaary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")# para cada par chave/ valor imprime uma linha "chave = valor"
    return kwargs # devolve a dict completa para quam chamou a função
print(packing_person_info(name="Asabeneh",country="Finland", city="Helsinki", age=250))

# Spreading in Python
lst_one = [1,2,3]
lst_two = [4,5,6,7]
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark','Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]# aqui vira uma lista só
print(nordic_countries)
nordic_countries = [country_lst_one, country_lst_two] # aqui vira uma lista de duas lista
print(nordic_countries)

# Enumerate
# if we are interested in an index of a list, we use enumerate built-in function to get the index of each intem in the list
for index, item in enumerate([20,30,40]):
    print(index,item)
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finalnd':
        print('The country {i} has been found at index {index}')

# Zip
# Sometime we would like to combine lists when looping through them.
# see the example below
fruits = ['banana','orange','mango','lemon','lime']
vegetables = ['Tomato', 'Potato','Cabbage','Onion','Carrot']
fruits_and_veges = []
for f , v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f,'veg':v})
print(fruits_and_veges)

