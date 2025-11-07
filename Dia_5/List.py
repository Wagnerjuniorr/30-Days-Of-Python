#There are four collection data types in Python
#List: is a collection which is oredered and chegeable(modifiable). Allows duplicate members
#Tuple: is a collection which is ordered and unchangeable or unmodifiable(ummutable). Allow duplicate members
#Set: is a collection which is unored, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are now allowed


#A list can be empty or it may have different data type items

#How to Create a list
#Using Buil-in func
mylist = list()
empty_list = list()
print(len(empty_list))

#Using square brackets
lst= []
empty_list = [] #this is an empty list, no item in the list
print(len(empty_list))

#list with values
fruits = ['banana', 'orange', 'mango', 'lemon']
web_techs = ['HTML', 'CSS', 'JS','React','Redux','Node','MongoDB']
print('Fruits', fruits)
print('Number of fruits: ',len(fruits))
print('web technologies', web_techs)
print('Number of web technologies', len(web_techs))

#list can have items of differente data types
lst = ['Asabeneh', 250, True,{'country':'Finland','city':'Helsinki'}]

#Acessing list items using positive indexing
first_fruit =fruits[0]
print(first_fruit) #banana
#last_index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
#Acessing using negative index
first_fruit = fruits[-4]
print('Using negative index of -4 to banana:', first_fruit)

#UNPACKING LIST ITEMS
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest =lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

#Slicing items from a list
#Positive indexin: We can specify a range of positive indexes by specifying the start, end an step, the return value will be a new list
#default values start = 0, end = len(lst) -1, step = 1
all_fruits = fruits[0:4]
#this one is will return somethin identical to the one above
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
print(orange_and_mango)
orange_and_lemon = fruits[::2]  # here we used a 3rd argument, step. 
                                # it will take every 2cnd item - ['banana','mango']
print(orange_and_lemon)

#Negative Indexing. We can specify a range indexes by specifying the start, end and step
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1]
reverse_fruits = fruits[::-1]
print(reverse_fruits)


#MODIFYNG LIST
#REMEMBER: list is MUTABLE 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado' 
print(fruits)
fruits = ['banana', 'orange', 'mango', 'lemon']

#Checking items in a list
#Using IN operator
does_exist = 'banana' in fruits
print(does_exist) #True

#Adding items to a list
#To add intem to the end of an existing list we use the method append()
#syntax
#lst = list()
#lst.append(item)
fruits.append('apple')
print(fruits)

#Inserting Items into a List
#We can use inset() method to insert a single item at a specified index in a list
#Not that items are shifted to the right. 
#The insert() methods takes two arguments: index and an item to insert
#sytanx 
# lst = ['item1', 'item2]
# lst.insert(index, tem)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2,'apple') #insert apple between orange and mango
print(fruits)

#Removing items from a list
#the remove method removes a specified item from a list
#syntax
# lst = ['item1', 'item2']
# lst.remove(item)

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana') #this method removes the first occurrnce of the item on the list

#Removinf items using Pop
#The pop() removes the specified index, (or the last item if index is not specified)
#syntax
# lst = ['item1','item2']
# lst.pop() #last item
# lst.pop(index)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

#Removing items using Del
#The dell keyword removez the specified index and it can alse be used to delete items within index range
#it can alse delete the list completely
#syntax
#lst = ['item1', 'item2']
#del lst(0)
#del lst
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]

#Clearing List Items
#the clear() method empties the list
#syntax
#lst = ['item1','item2']
#lst.clear()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

#Copying a list
#Is possible to copy a list by reassigning it to a new variable in the following way:
#list2 = list1.
#Now, list2 is a reference of list1, 
# any changes we make in list2 will also modify the original, list1
#but there are a lots of case in wihich we do not like to nodify the original instead we like to have a different copy
#one way of avoiding the problem abose is using copy()
# syntax
# lst = ['item1', 'item2']
# lst_copy = lst.copy()

fruits = ['banana','orange','mango','lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

#Joinnig List
#There are several ways to join or concatenate two or more list in Python
#Plus operator
#syntax
#list3 = list1 + list2
positive_numbers = [1,2,3,4,5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)

#joining using extend() method
#The extend() method allows to appedn list in a list
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers', negative_numbers)

#Counting Items in a List
print(fruits.count('orange')) # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

#Finding Index of an item
print(fruits.index('orange'))
print(ages.index(24))

#Reversing a List
fruits.reverse()
print(fruits)
fruits = ['banana', 'orange', 'mango', 'lemon']

# Sorting List Items
# to sort list we can use sort() method or sorted() built-in functions. 
# The sort() method reorders the list items in ascending order and modifies the original list
# If an argument of sort() method reverse is equal to true, it will arrange the list in descending order

fruits.sort()
print('Fruits sorted in alphabetical order:', fruits)
fruits.sort(reverse=True)
print('Fruits sorted in reverse alphabetical order:', fruits)

#sorted() returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
fruits = sorted(fruits, reverse=True) #i think in this example, he wanted to show that we can also modify the original list
print(fruits)

