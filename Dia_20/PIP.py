# Pip stands for preferred installer program. 
# we use pip to isntall different pytho packages
# Package is a python module that can contain one or more modules or other packagges
# A module or modules that can isntall to out application is a package
# In programming, we do not have to write utility program, instead we install package and import tham to out applications

# Installing PIP
# pip install pip

# checking 
# pip --version

# Installing packages using pip
# Let us try install numpy, called numeric python
# It is one of the most popular packages in machine learning and data science community
# NumPy is the fundamental package for scientific computing with python
# It contains among other thing:
    # a powerful N-dimensional array object
    # sophiticated (broadcasting) functions 
    # tooll for integraing C/C++ and fortran code 
    # Useful linaer algebra, fourier transform, and random number capabilities
# pip intall numpy

# USING NUMPY
import numpy
print(numpy.version.version)
lst = [1, 2, 3,4, 5]
np_arr = numpy.array(lst)
print(np_arr)
print(len(np_arr))
print(np_arr * 2)
print(np_arr  + 2)

# Pandas is an open sourve, BSD-licensed library providing high-performance, 
# easy-to-use data structures anda data analysis tools
# Let us install the big brother of numpy, pandas
# pip install pandas

# wevbrowser module
# help us to open any website
# it is already installed by deafault
# if you like to open any number of websites at any time or if you lie to scheadule someting, this webbbrowser module can be used
import webbrowser

url_lists = [
]
for url in url_lists:
    webbrowser.open_new_tab(url)

# Uninstalling Packages
# pip uninstall packagename

# List of packages
# pip list

# Show package
# show information about package
# pip show packagename
# if we want more details, just add -- verbose
# pip show --verbose pandas

# Pip freeze
# Generate installed Pyton packages with their version an the output is suitable to use it in a requirement file
# A requirements.txt file is a file that should contain all the installed Python packages in a Python project
# pip freeze

# Reading from URL
# Sometimes, we would like to read from a website using url or from an API.
# API stands for application Program Interface.
# It is means to exchange structured data between servers primaly as json data
# To open a network connection, we need a package called requests 
# it allows to open networl connection and to implement CRUD(create, read, update and delete) operations
# In this section, we will cover only reading or getting part of a CRUD

# Até agora eu só sei manipular arquivos localmente .txt .csv etc
# O próximo passo é ler dados diretamente de um URL ou de uma API
# API é como se fosse um garçom que traz os pedidos da cozinha(servidor da internet) e traz comida(os dados)
# os dados são JSON
# para poder fazer pedidos é necessário a biblioteca requests
# open('arquivo.txt') vai virar requests.get('https...')

# pip install requests
# get(): open a network and fetch data from url - it returns a responde object
# status_code: after we fetched data, we can check the status of the operation(success, error, etc)
# headers: to cheack the headers types
# text: to extract the text from the fetched responde object
# json: to extract json data. 
import requests
url = 'https://www.w3.org/'
response = requests.get(url) # opening a network and fetching a website
print(response)
print(response.status_code)
print(response.headers)
print(response.text)

# Let us read from API.
# It is a meanos to exchange structure data between servers primaly a json data
url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
print(response)
print(response.status_code)
# countries = responde.json()
# print(countries[:1])

# Creating a Package
# We organize a large number of files in different folders and sub-folders bases on some criteria
# so that can we can find and manage them easily
# As you know, a module can contain mulitple objects, such as classes, functions, etc
# A package can contain one or moe relevatn modules
# A package is actually a folder containing one or more module files
# Create a new folder named mypackage inside 30DaysOfPython folder
# Create an empty init.py file in the mypackage folder.
# Create modules arithmetic.py and greet.py with following code
from mypackage import arithmetics
print(arithmetics.add_numbers(1,2,3,4,5))
from mypackage import greet
print(greet.greet_person('wagner','moreira'))
# The package folder contains a special file called init.py
# it stores the package content
# if we put ini.py in the package folder, python start recognizes it as a pacakge
# init.py exposes specified resources from its module to be imported to other python files
# An empyth ini file makes all function avaible when a package is imported

# Further information about packages
# Data base 
    # SQLAlchamy or SQLObject - object oriented access to several different database systems
    # pip install SQLAchemy
# Web Development
    # Django - High level framework
    # Flask - micro framework for python based on Werkzeug, Jinja 2
# HTML Parser
    # Beautiful Soup - HTML/XML parser designed for quick turnaround projects like scree-scraping, will accept bad markup
    # PyQuery - implements jQuert in Python; faster thaan BeutifulSoup
# XML Processing 
    # ElementTree - The Element type is a simple but flexible container object, designed to storre hierachical data structures,
    # such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
# GUI
    # PyQt - Bindings for the cross-platafrom Qt framework
    # Tklnter - The traditionao Python user interface toolkit
# Data Analysis, Data Science and Machine Learning
    # Numpy - is known as one of the most popular machine learning library in Python
    # Pandas: is data analysis, data science and a machine learning library in Python that provides data structures of high-level and wide variety of tools for analysis
    # SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
    # Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
    # TensorFlow: is a machine learning library built by Google.
    # Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
# Network
    # requests: is a package which can use to send requests to a server(GET, POST, DELETE, PUT)
