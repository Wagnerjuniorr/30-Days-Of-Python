# By default, statements in Pythn script are sequentially from top to bottom
# If the processing logic require so, the sequential flow of execution can be altered in two way
#   Conditional execution: a block of none or more statement will be executed if a certain expression is true
#   Repetitive execution: a blocl of one or more statements will be repetively executed as long as a certain expression is true
#   In this section, we will cover if, else, elif.

# if condition
# In python we use the key word if to check if a condition is true and to execute the block of code
# Remember the indentation ather the colon ':'
a = 3
if a > 0:
    print('A is a positive number')
# if the condition is true the block of code after the colon will be executede. 
# However, if its not true, we see nothing printed
# To see the result of a falsy condition, we should have another block, which is else

# if else
# if condition is true the first block will be executede, if not the else condition will run
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
# How abount if out condition is more than two.
# we could use elif

# if elif else
# we make decision not by checkin one or two condition but multiple conditions
if a>0:
    print('A is a positive number')
elif a<0:
    print('A is a negative number')
else:
    print('A is zero')

# Short hand
a = 3
# this is not recomended to do because its hard to read 
print('A is positive') if a > 0 else print('A is negative')

# Nested conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive number and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# we can avoid writing nested condition by using logical operator and
# if condition and logical operators
# if condition and condition:
#   code

a = 0
if a > 0 and a % 2 == 0:
    print('A is an even number and a positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# if and Or logical operators
user = 'James'
access_level = 6
if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied')