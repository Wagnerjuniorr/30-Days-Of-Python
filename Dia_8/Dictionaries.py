# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type
# Creating a dictionary
# To create a dictionary we use curly brackets, {} or the dict() func
# syntax 
empyt_dict = {}
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
person ={
    'first_name':'Asabeneh',
    'Last_name':'Yetayeh',
    'age':'250',
    'country':'Finland',
    'is_married':'True',
    'skills':['Javascript','React','Node','MongoDB','Python'],
    'addres':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
# This dictionaty accepts any data type

# lenght
print(len(dct))
print(len(person))

# Acessing Dictionary Items
# We can access Dictionary items by referring to its key name
print(dct['key1'])
print(dct['key2'])
print(person['first_name'])
print(person['age'])
print(person['addres']['street'])
# Accessing an item by key name raises an error if the key does not exist.
# To avoid this error we have to check if a key exist or we can use the get method()
# The get method returns None, which is NoneType object data type, if the key does not exist
print(person.get('first_name'))
print(person.get('hair'))

# Adding items to a Dictionaty
dct['key5'] = 'value5'
person['job_title'] = 'Instructor'
# Here we use append cuz 'skills' is a list
person['skills'].append('Html')
print(person)

# Modifyig items in a Dictionary
dct['key1'] = 'value-one'
person['first_name'] = 'Wagner'
person['age'] = 69

# Checking Keys in a Dictionary
# In operator
print('key1' in dct)
print('key19' in dct)

# Removing Key and Values Pairs from a Dictionary
# pop(key): removes the item with the specified key name
# popitem(): removes the last item
# del: removes an item with specified key name
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') #removes the item key1
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() #removes the last item
del dct['key2']

person.pop('first_name')
person.popitem()
del person['is_married']
print(person)

# Changing Dictionary to a list of items
# the items() method changes dictionary to a list of tuples
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) 

# Clearing a Dictionary
print(dct.clear())

# Delting a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a Dictionary
# We can copy a dictionary using a copy() method.
# Using copy avoids mutation of the original dicitionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()

# Getting Dictionary Keys as a List
# The keys() methods give us all the keys of a dictionary as a list
keys = dct.keys()
print(keys)

# Getting Dictionary Values as a List
values = dct.values()
print(values)