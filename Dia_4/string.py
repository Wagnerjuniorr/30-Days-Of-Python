# Text is a strng data type. Any data type written as a text is a string
# Any data under single, double or triple quotes are strings
# These are different string methods and built-in functions to deal with string data types
# to check the length of a string use the len() method

#CREATE A STRING
letter = 'p' # could be a single letter or a bunch of text
print(letter)
print(len(letter))
greetings = 'Hello, World!' # Could be made using single or double quotes, "Hello, World!"
print(greetings)
print(len(greetings))

#Multiline string is created using triple single(''') or triple double(""")
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python'''
print(multiline_string)
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String concatenation
# We can connect string together. 
# Merging or connecting strings is called concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name 
print(full_name)

# Escape Sequences In Strings
# In python and other programming languages \ followed by a character is an scape sequence.
# \n #
# new line
# \t
# tab
# \\: 
# Black slash
# \' 
# single quote (')
# \"
# Double quote(")
print('I hope everyone is enjoying the Python Challenge. \nAre you?') # line break
print('Days\tTopics\tExercises') # adding tab spaces or 4 spaces
print('Day 1\t5\t5')
print('Dat 2\t6\t20')
print('This is a backlash symbol(\\)') # to write a backslash
print('In every programming languague it starts with \"Hello, World!\\"') #to write a double quorte inside a single quote

#String formmating
#In Python there are many ways of formatting strings. 
#The "%" operator is used to format a set of variables enclosed in a "tuple" (fixed size list), 
# together with a format string,
# which contains normal text together with "argument specifiers",
# special symbols like "%s", "%d" , "%f", "%.number of digitsf."
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f = floating point numbers
#"%.number of digitsf" - Floating point numbers with fixed precision

#String only
first_name = 'Asabeneh'
last_name = 'Yeteyeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
print(formated_string)

python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

#New Style String Formatting (str.format)
#Python version 3
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4 
b = 3
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
#strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}'. format(radius, area)
print(formated_string)

# String intepolation / f-String (Python 3.6+)
# another new string formatting is string interpolation, f-string. 
# Strings star with f and we can inject the data in their corresponding positions 
a = 4
b = 3
print(f'{a} + {b} = {a+b}')
print(f'{a} / {b} = {a / b:.2f}')


# PYTHON STRINGS AS SEQUENCES OF CHARACTERS
# Python strings are sequences of characters, and share their basic methods os access with other python ordered sequences of objects - list and tuples
# The simplest way of extracting single character from strings is to unpack them into corresponding variables
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)
last_index  = len(language)- 1
last_letter = language[last_index]
print(last_letter)
#if we want to start from right end we can use negative indexing. -1 is the last index
language = 'python'
last_letter = language[-1]
print(last_letter) # n

# Slicing Python Strings
# In python we can slice strings into substrings
language = 'python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) # pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three =language[-3:]
print(last_three) # hon
last_three = language[3:]
print(last_three) # hon

#Reversing a String
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

#Skipping Character While Slicing
#ele vai dando pulos de 2 em 2 e mantendo o 2°
language = 'python'
skipped_chars = language[0:6:2]
print(skipped_chars) # pto:6:2

#captilize
#converts the firts character of the string to capital letter
challenge = "oi"
print(challenge.capitalize()) #Oi

#count
#return ocurrences of a substring in string
challenge = 'thirty dayrs of python'
print(challenge.count('y')) # 3
#count(substring, start= , end=)
print(challenge.count('y', 7, 14)) # 1

# endswith
# checks if a string ends with a specified ending
challenge = 'thirty dayrs of python'
print(challenge.endswith('on')) # TRUE

# expandtabs()
# Replace tab character with spaces, default tab size is 8, it takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find()
# Return the index of the list first occurence of a substring, if not returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# rfind()
# Return the index of the last occurrnce of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

# format
#formats string inrto a nicer output
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

# index()
# Returns the lowest index of a substring, 
# additional aruments indicate starting and ending index (default 0 and string lenth -1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7

# rindex
# Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex('on', 8)) # 19

# isalnum()
# checks alphanumerc character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha()
#checks if all string elements are alphabet
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

#isdecimal
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

#isdigits()
#checks if all characters in a string are numbers(0-9 and some unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

#isnumeric
#just like isdigit(), just accepts more symbols , like ½
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

#isidentifier()
#checks for a valid identifier - it checks if a string is a valir variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower
# Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper()
# Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

#join()
#return a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

#strip()
#removes all given character from the begining and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

#replace
#replaces a substring with given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

#split()
#splits the string using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

#title
#return a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

#swapcase()
#converts all uppercase character to lowercase and all lowercase to uppercase
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

#startswith()
#checks if a strig starts with the specified string
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False



