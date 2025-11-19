# A module is a file containning a set of codes or a set of functions which can be included to an application
# A modeula could be a file containning a single variable, a function or a big code base

# Creating a Module
# To create a modeule we write our code in a python script and we save it a .py file
# Create a file named mymodule.py inside your project folder. 
import mymodule
print(mymodule.generate_full_name('Asabenh','Yeteyah'))

# We can have many functions in a file and we can import all the fucntions differently
from mymodule import generate_full_name, sum_of_numbers, sum_two_nums
print(generate_full_name('Asabeneh','Yetayeh'))
print(sum_two_nums(1,9))

# Import Functions from a module and Renaming
# We can rename the name of the module
from mymodule import generate_full_name as fullname, sum_of_numbers as total
print(fullname('Asabeneh','Yeteyah'))
print(total(9))

# Import Built-in Modules
# Like other programming languages we can also import modules by importing the file/function using the  key word import.
# Lets import the common module we will use most of the time
# Some of the common built-in modules: math, datetime, os, sys, random, statistics, collections, json, re

# OS module
# Using Python os module it is possible to automaticaly perform many operating systems tasks
# The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing the current directory

import os
# Creating a directory
## os.mkdir('directory_name')
# Changing the current directory
## os.chdir('path')
# Getting current working directory
## os.getcwd()
# Removing directory
## os.rmdir()