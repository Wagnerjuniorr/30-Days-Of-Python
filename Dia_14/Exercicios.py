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
