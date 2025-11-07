# A tuple ia a collection of different data types which is ordered and unchageable (IMMUTABLE).
# Tubples are written with round brackets, (). 
# Once a tuple is created, we cannot change its value.
# We cannot se add, insert, remove methods in a tuple because ir is not modifiable
# Unlike list, tuple has few methods
# Methods related to tuples:

# tuple(): to create empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
#   operator: to join two or more tuple and to create a new tuple

# Creating a Tuple
empty_tuple = ()
# or
empty_tuple = tuple()
# with values
tpl = ('item1','item2','item3')
fruits = ('banana','orange','mango','lemon')

# tuple lenght
print(len(fruits))

# Accessing Tuple Items
# Positive Indexing Simliar to the list data type we use positive or negative indexing to acess tuple items
first_fruit = fruits[0]
print(first_fruit)
last_fruit = fruits[len(fruits)-1]
print(last_fruit)

# Negative Indexing
# Means the beginning from the end, -1 refers to the last item, -2 refers to the second last 
first_fruit = fruits[-4]
last_fruit = fruits[-1]

# Slicing tuples
# We can slice out a sub-tuple by specifying a range of indexes where to start an where to end
# The return value will be a new tuple with the specified items
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]
# Range of Negative indexes
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]

# Change Tuples to List
# We can change tuples to list and list to tuples
# Tuple is immutable if we cant to modify a tuple we should change it to a list
fruits = list(fruits)
fruits[0] = 'apple'
print('list', fruits) # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print('tuple', fruits) # ('apple', 'orange', 'mango', 'lemon')

# Checking an item in a tuple
# We can check if an item existis or not in a tuple using in, it returns a boolean
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)

# Joining Tuples
# We can joing two or more tuple using + operator
vegetables = ('tomato', 'potato', 'cabbage','onio','carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Deleting Tuples
# it is not possible to remove a single item in a tuple but it is possible to delete the tuple itseld using del
del fruits
