# Statistics is a branch of mathematics that is rocommended to be perequisite for data science and machine learning
# After completing this challenge, you may go onto the web development, data analysis, machine learning and data science path

# DATA
# Data is any set of characters that is gathered and transleted for some purpose, usually analysis
# It can be any character, including text and numbers, pictures, sound, or video
# If data is not put in a context, it doesnt make any sense to a human or computer
# to make sense from data we need to work on the data using different tools
# The work flow of data analysis, data science or machine learning starts from data
# there are structured and unstructed data

# Statistics module
# the module is not intendeed to be a competitor to third-party libraries such as numpy, Scipy, or proprietary full-featured statistic packages aimed at professional statisticians such as Minitab, SAS and Matlab
# it is aimend at the lavel of graphing and scientific calculators

# Numpy
# is the core library for scientific computing in Python
# it provides a high-performance multidimensional array object, and workong tools with arrays
# So far, we have been using vscode but from now on i would recommend using Jupyter Notebool
# To access jupyter lets install anaconda
# if you are using anaconda most of the common packages are included and you dont have to installs packages if you installed anaconda

# Importing numpy
import numpy as np
# check the version
print('numpy',np.__version__)
# checking the avaible methods
print(dir(np))

# Creating numpy array using 
# Creating int numpy arrays
python_list = [1,2,3,4,5]
print('Type', type(python_list))
print(python_list)
two_dimensional_list = [[0,1,2],[3,4,5],[6,7,8]]
print(two_dimensional_list)
# Creating Numpy array from python list
numpy_array_from_list = np.array(python_list)
print('Tipo:',type (numpy_array_from_list))
print(numpy_array_from_list)

# Creting float numpy arrays
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2) # ([1., 2., 3., 4., 5.])

# Creating boolean numpy arrays
numpy_bool_array = np.array([0,1,-1,0,0], dtype=bool) # false true true false false 0 = false 0 != true
print(numpy_bool_array)

# Creating multidimensional array using numpy
two_dimensional_list = [[0,1,2],[3,4,5],[6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# Converting numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensioal array: ', numpy_two_dimensional_list.tolist())

# Creating numpy array from tuple
python_tuple = (1,2,3,4,5)
print(type(python_tuple))
print('python tuple: ', python_tuple)
numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print('numpy array from tuple', numpy_array_from_tuple)

# Shape
# The shape method provides the shape of the array as a tuple
# The first is the row and the second is the column
# if the array is just one dimensional it returns the size of the array
nums = np.array([1,2,3,4,5])
print(nums)
print('shape of nums', nums.shape) # (5,) is a tuple one dimensional
print(numpy_two_dimensional_list)
print('shape of numpy two dimensional list: ', numpy_two_dimensional_list.shape) # (3, 3) row and collumn
three_by_four_array = np.array([[0,1,2,3],
                               [4,5,6,7,],
                               [8,9,10,11]])
print(three_by_four_array.shape) # (3,4)

# Data type of numpy array
# type of data types: str, int, float, complex, bool, list, None
int_list = [-3,-2,1,0,1,2,3]
int_array = np.array(int_list)
float_array = np.array(int_list, dtype= float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# Size of a numpy array
# if numpy to know the number of items in a numpy array list we use size
numpy_array_from_list = np.array([1,2,3,4,5])
two_dimensional_list = np.array([[0,1,2],
                                 [3,4,5],
                                 [6,7,8]])
print('The size', numpy_array_from_list.size)
print('The size', two_dimensional_list.size)

# Mathematical Operation using numpy
# Numpt array is not like exactly like python list
# to do mathematical operation in python list we have to loop through the items but numpy can allow to do any mathematical operation without looping 
# Addition
numpy_array_from_list = np.array([1,2,3,4,5])
print('original array', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print('plus ten',ten_plus_original)
# Subtraction
ten_minus_original = numpy_array_from_list - 10
print('minus ten', ten_minus_original)

# Convertinh types
# we can convert data types of numpy array
# int to float
numpy_int_arr = np.array([1,2,3,4], dtype= float)
print(numpy_int_arr)
# float to int
numpy_int_arr = np.array([1,2,3,4], dtype= int)
print(numpy_int_arr)
# int to str 
array_strings = numpy_int_arr.astype('U') # U = unicode melhor para o pt-br
print(array_strings.dtype)

# Getting items from a numpt array
two_dimensional_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
first_row = two_dimensional_array[0]
print('first_row', first_row)
first_column = two_dimensional_array[:,0]
print('First column: ', first_column)

# Slicing Numpy array
first_two_rows_and_columns = two_dimensional_array[0:2,0:2]
print('complete\n',two_dimensional_array)
print('sliced\n', first_two_rows_and_columns)

# How to reverse the rows and the whole array
print(two_dimensional_array[::1,::-1])

# How to change values
print(two_dimensional_array)
two_dimensional_array[1,1] = 55
two_dimensional_array[1,2] = 44
print(two_dimensional_array)

# array of zeros
numpy_zeros = np.zeros((3,3), dtype=int, order='C')

# Reshape
first_shape = np.array([(1,2,3), (4,5,6)])
print('first shape\n', first_shape)
reshaped = first_shape.reshape(3,2)
print('reshaped\n', reshaped)

# flatten
flattened = reshaped.flatten()
print('flattened', flattened)

# Horizontal stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print('wrong way', np_list_one + np_list_two)
print('Horizontal Append', np.hstack((np_list_one, np_list_two)))
## Vertical Stack
print('Vertical Append:\n', np.vstack((np_list_one, np_list_two)))

# Generating random Numbers
random_float = np.random.random()
print(random_float)
random_float = np.random.random(2)
print(random_float)
# generating a random int between 0 and 10
random_int = np.random.randint(0,11)
print(random_int)
# Genaraint a random int and creating a one row array
random_int = np.random.randint(0,11, size=4)
print(random_int)

# mu sigma size
normal_array = np.random.normal(79,15,(3,5))
print(normal_array)

# Numpy and Statistics
# import matplotlib.pyplot as plt
# import seaborn as sns
# print(sns.set())
# print(plt.hist(normal_array, color= 'grey', bins=50))

# Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype = float))
print(four_by_four_matrix)

# Numpy.arange()
# What is arrange
# sometimes, you want to create values that are evenly spaced within a difned interval
# for instance, you want to create values from 1 to 10
lst = range(0,11,2)
print(lst)
for l  in lst:
    print(l)

# similar to range arange numpy.arange(start, stop , step)
whole_number = np.arange(0,20,1)
print(whole_number)

# Creating sequence of numers using linspace
floats_numbers = np.linspace(1.0, 5.0, num= 10)
print(floats_numbers)

# Logspace
# returns even spaced numbers on a log scale
# Logspace has the same parameters as np.linspace
log_space = np.logspace(2,4.0, num=4)
print(log_space)

# Check de size of an array
x = np.array([1,23,], dtype=np.complex128)
print(x)
print(x.itemsize)

# Indexing and sliciin numpy arrays in python
np_list = np.array([(1,2,3),(4,5,6)])
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])
print('First column: ', np_list[:,0])

# Numpy Statiscal funcions with example
# Numpy has quite useful statistical functions for finding minium, maximum, median, percetile, std and variace
np_normal_dis = np.random.normal(5,0.5,100)
print(np_normal_dis)
## min , max, meanm median, sd
print('min: ', two_dimensional_array.min())
print('max: ', two_dimensional_array.max())
print('mean: ', two_dimensional_array.mean())
print('sd: ', two_dimensional_array.std())

print(two_dimensional_array)
print('Column with minimum: ', np.amin(two_dimensional_array, axis=0))
print('Column with maximum: ', np.amax(two_dimensional_array, axis=0))
print('=== Row ===')
print('Row with minimum: ', np.amin(two_dimensional_array, axis=1))
print('Row with maximum: ', np.amax(two_dimensional_array, axis=1))

# How to create reapeating sequences
a = [1,2,3]
# Reapeat whole of 'a' two times
print('Tile:    ', np.tile(a,2))
# Repeat eache element of 'a' two times
print('Reapeat: ', np.repeat(a,2))

import scipy.stats as stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, std, number os samples
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

# Linear Algebra
# dot product
## Linear Algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,6])
## 1*4+2*5 + 3*6
print(np.dot(f,g))

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
print(np.matmul(h, i))

new_list = [ x + 2 for x in range(0,11)]
print(new_list)
np_arr = np.array(range(0,11))
print(np_arr + 2)

# We use linear equation for quantities which have linear relationship
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

# arrays support vectorized operation while lists dont
# Once an array is created, you cannot change its size . You will have to create a new array or overwrite the existing one
# Every array has one and olny one dtype. All items in it should be of that dtype
# An equivalent numpy array occupies much less space than a python list of list # Enquanto python tenta ser flexivel, numpy tenta ser eficiente na alocação de memória
# Numpy arrays supprt boolean indexind