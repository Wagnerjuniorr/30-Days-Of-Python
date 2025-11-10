# Set is a collection of items. 
# The mathematic definition of a set can be applied also in Python.
# Set is a collection of unordered and un-indexed dinstic elements.
# In python set is used to store unique items,
# and it is possible to find the union, intersection, difference, symmetice difference, subet, super set and disjoint set among sets

# Creating a set
# Empty set
st = set()

st = {'item1','item2','item3','item4'}
fruits = {'banana','orange','mango','lemon'}

# len
print(len(fruits))

# Acessing items in a Set
# We use loops to access items, we will see this in loop section
# Checkin an item
# to check if an item exist in a list we use in membership operator
print('mango' in fruits) # True

# Adding items to set 
st.add('item5')
fruits.add('lime')
# Add multiple items using update()
st.update(['item5','item6','item7'])
fruits = {'banana','orange','mango','lemon'}
vegetables = {'tomato','potato','cabbage','onion','carrot'}
fruits.update(vegetables)


# Removing items from a set
# We can remove an item from a set using remove()
# If the item is not found remove() method will raise erros
# discard() method doesn't raise any erros
st.remove('item2')
# the pop() methods remove a RANDOM item from a list and it returns the removed item
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop() # removes a random item from a set
print(fruits)
# if we are interested in the removed item
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)

# Clearing items in a set
st.clear()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)

# Deleting a set
del st
del fruits

# Converting List to set
# We cannnot convert a list to set and set to list
# Converting list to set removes duplicates and only unique items will be reserved
lst = ['item1','item2','item3','item4','item1']
print(lst)
st = set(lst)
print(st)
fruits = ['banana','orange','mango','lemon','orange','banana']
fruits = set(fruits)

# Joining sets
# We can join two sets using the union() or update() method
# Union method returns a new set
st1 = {'item1','item2','item3','item4','item8'}
st2 = {'item5','item6','item7','item8'}
print(st1.union(st2))
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

# update method inserts a set into a given set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# Finding Intersection items
# Intersection returns a set of items which are both the sets
st1 = {'item1','item2','item3','item4'}
st2 = {'item3','item2'}
print(st1.intersection(st2))


whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,7,10}
print(whole_numbers.intersection(even_numbers))

# Checking a subset and Super set
# A set can be a subset or super set of others sets:
# Subset: issubset()
# Super set: issuperset
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1)) # True
print(st1.issuperset(st2)) # True

# Checking the difference between two sets
print(st2.difference(st1))
print(st1.difference(st2))

# Finding Symmetric Difference Between two sets
# It returns the symmetric difference between two sets
# ir means that it returns a set that contains all items from both sets,
# except items that are present in both sets, mathematically, (A\B) ∪ (B\A)
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) #{'item1','item4'}
whole_numbers ={0,1,2,3,4,5,6,7,8,9,10}
some_numbers = {1,2,3,4,5}
print(whole_numbers.symmetric_difference(some_numbers))

#Joining sets
#If two sets do not have a common item or items we call them disjoint sets. 
# We can check if two sets are joint or disjoint using isdisjoint()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))

even_numbers = {0,2,4,6,8}
numbers = {0,2,4,6,8}
odd_numbers = {1,3,5,7,9}
print(even_numbers.isdisjoint(odd_numbers))
print(even_numbers.isdisjoint(numbers))
