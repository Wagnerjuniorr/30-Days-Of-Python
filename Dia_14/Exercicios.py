from functools import reduce
# Exercises: Day 14
# Exercises: Level 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Explain the difference between map, filter, and reduce.
# Map is used when we want to iterate and transform all the items using a function
countries_with_uppercase = map(lambda name:name.upper(), countries)
print(list(countries_with_uppercase))
# Filter is used when we want to iterate over something and we want only the item with certain condition applied
countries_with_big_name = filter(lambda name:len(name)>6, countries)
print(list(countries_with_big_name))
# Reduce instead of maps and filters, it return a single value instead of an iterable
def add_two_nums(x, y):
    return x+y
sum_of_numbers = reduce(add_two_nums, numbers)
print(sum_of_numbers)

# Explain the difference between higher order function, closure and decorator

# Higher Order function are used when you want to return a function depending on the users choice or a function that can take order function as arguments
def square(n):
    return n**2
def cube(n):
    return n**3
def higher_order(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
result = higher_order('square')
print(result(2))
result = higher_order('cube')
print(result(2))

# Closure is when are two function, one outside and one inside each other, then the nested function returns something. 
# The nested function needs to refers to a variable outside its scope(outside function)
def multiply_2():  
    two = 2
    def multiply(num):
        return num*two
    return multiply
closure_result = multiply_2()
print(closure_result(5))

# Decorator is a designt pattern used to change the return value of a fucntion without chaging it structure
def upper_case_name(function):
    def wrapper():
        func = function()
        make_Upper_Case = func.upper()
        return make_Upper_Case
    return wrapper
@upper_case_name
def name():
    return 'Wagner Moreira Cavalcante Junior'
MyName = name()
print(MyName)

# HOF: Função que aceita ou retorna outra função
# Closure: Função aninhada que 'lembra' variáveis do escopo após a função externa ter retornado
# Decorator: Uma HOF que usa o padrão closure para modificcar/envolver outra função
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Define a call function before map, filter or reduce, see examples.
def add_dream_country(country):
    return country + ' is my dream country'
dream = map(add_dream_country, countries )
print(list(dream))
def starts_with_an_A(name):
    if name[0]=='A':
        return True
    return False
A_name = filter(starts_with_an_A,names)
print(list(A_name))
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers)
print(total)

# Use for loop to print each country in the countries list.
for country in countries:
    print(country)
# Use for to print each name in the names list.
for name in names:
    print(name)
# Use for to print each number in the numbers list.
for num in numbers:
    print(num)

# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
upper_map = map(lambda country: country.upper(),countries)
print(list(upper_map))
# Use map to create a new list by changing each number to its square in the numbers list
square_map = map(lambda num: num**2, numbers)
print(list(square_map))
# Use map to change each name to uppercase in the names list
countries = map(lambda country: country.upper(),countries)
print(list(countries))
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# Use filter to filter out countries containing 'land'.
def only_land(country):
    if 'land' in country:
        return True
    return False
land_countries = filter(only_land, countries)
print(list(land_countries))
# Use filter to filter out countries having exactly six characters.
def we_hate_six_character_countries(country):
    if len(country)==6:
        return False
    return True
no_six = filter(we_hate_six_character_countries, countries)
print(list(no_six))
# Use filter to filter out countries containing six letters and more in the country list.
def we_hate_six_character_or_more_countries(country):
    if len(country)>=6:
        return False
    return True
no_six_or_above = filter(we_hate_six_character_or_more_countries, countries)
print(list(no_six_or_above))
# Use filter to filter out countries starting with an 'E'
def no_E_countries(country):
    if country[0] == 'E':
        return False
    return True
countries_with_no_E = filter(no_E_countries, countries)
print(list(countries_with_no_E))
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
def only_land(country):
    return 'land' in country
land_upper_countries = list(map(lambda country: country.upper(), filter(only_land, countries)))
print(land_upper_countries)
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

string_and_ints =[2,'a',1,'b',3]
string_and_ints = filter(lambda item: type(item) == str, string_and_ints)
print(list(string_and_ints))
# Use reduce to sum all the numbers in the numbers list.
sum_nums = reduce(lambda x,y: x+y,numbers)
print(sum_nums)
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
concatenate_countries = reduce(lambda All_countries, country:(All_countries+','+country), countries )
print(concatenate_countries)
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from Countries_list import countries
def categorize_countries(countries):
    land_countries = []
    ia_countries = []
    island_countries = []
    stan_countries = []
    other_countries = []

    for country in countries:
        if 'land' in country:
            if 'island' in country:
                island_countries.append(country)
            land_countries.append(country)
        elif 'ia' in country:
            ia_countries.append(country)
        elif 'stan' in country:
            stan_countries.append(country)
        else:
            other_countries.append(country)
    return land_countries, island_countries, ia_countries, stan_countries, other_countries

all_countries = categorize_countries(countries)
print(all_countries)