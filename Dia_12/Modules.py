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
# Creating a directory // Make a directory no caminho atual de trabalho ou no caminho especificado
## os.mkdir('teste')
# Changing the current directory // Change Directory, altera o diretório atual para o caminho especificado
## os.chdir('teste')
# Getting current working directory // Retorna uma string contendo o caminho completo para o diretório do script
## os.getcwd()
# Removing directory // Exclui um diretório no mcianho especificado
## os.rmdir('teste')

# o arquivo __pycache__ só foi criado porque estou em usando module

# Sys Module
# The sys module provides functions and variables used to manipulate different parts of the Python runtime enviroment
# Functions sys.argv returns a lsit of command lines arguments passed to a Python script.
# The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line
import sys
#print(sys.argv[0],sys.argv[1],sys.argv[2]) # This line would print out: filnename argument1 argument2
## print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1],sys.argv[2]))
# The script:
# To use the script u need to acess a terminal, cd to where the Modules.py is, and use this command:
## python Modules.py[argv[0]] Asabeneh(argv[1]) 30DaysOfPython(argv[2])
# Output:
## Welcome Asabeneh. Enjoy  30DayOfPython challenge! 

#Some useful sys commands:
# Exist sys
# sys.exit() # se eu usar esse comando nada depois dele será exibido
# To know ther largest interger variable it takes
print(sys.maxsize)
# To know envioroment path // sys path é uma variável que contém uma lista de todos os diretórios onde o Python procura por módulo quando voce usa o comando import
for path in sys.path:
    print(f"={path}")
#to know the version of the python you are using
print(sys.version)


# Statics Module
# The statics module provides functions for mathematical statistics of numeric data.
# the popular statiscal func which are definied in this module: mean, median, mode, stdev etc
from statistics import * # import all the statistics modules
ages = [20,20,4,24,25,22,26,20,23,22,26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# Math module
# Module containing many mathematical operations and constants
import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

# to check what functions the module has got, we can use hel(math), or dir(math). 
# This will display the available functions in the module.

# if we want to import only 1 func:
from math import pi
print(pi)
# if we want to import multiple funcs at once
from math import pi, sqrt, pow, floor, ceil, log10

# if we want to import all:
from math import *
# if we want to rename
from math import pi as PI
print(PI)

# String Module
from string import ascii_letters, digits, punctuation
print(ascii_letters)
print(digits)
print(punctuation)

# Random Module
# the rangom module gives a random number between 0 and 0.9999 
# (esse intervalo é assim porque ele é de fácil escalonamento, a lógica por trás do random() facilita que vc consiga gera número negativos, numero intereiros positivos etc)
# There are many more func in this module, it is important to read all the documentation
from random import random, randint
print(random()) 
print(randint(5,20)) # it returns a random interger between [5,20] inclusive