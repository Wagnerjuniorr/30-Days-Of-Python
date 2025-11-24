import string
# Exercises: Day 13
# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_positive_int =  [i for i in numbers if i>0]
print(only_positive_int)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists_of_list =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
two_dimesional_list = [sub_row for row in list_of_lists_of_list for sub_row in row]
flatten_list = [number for row in two_dimesional_list for number in row]
flatten_list = [number for list_ in list_of_lists_of_list for sublist in list_ for number in sublist]
print(flatten_list)
flatten_list = [number for list_ in list_of_lists_of_list for sublist in list_ for number in sublist]
print(flatten_list)

# Using list comprehension create the following list of tuples:
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
number_lst = [(i, 1 , i , i**2 , i**3 , i**4 ,i**5) for i in range(11)]
print(number_lst)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

updated_countries_list = [[country.upper(), country[:3].upper(),city.upper()] for sub_list in countries for country,city in sub_list] 
# for sublist in countries acessa o primeiro nivel de colchete [(Finland, Helsinki)]
# for country, city in sublist avessa a tupla dentro da sublista. Ele usa o desempacotamento de tupla(country, city) para extrair os dois calores de uma vez
print(updated_countries_list)

# change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
updated_countries_list =[{'country':key.upper(), 'city':value.upper()}for sub_list in countries for key,value in sub_list]
print(updated_countries_list)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# aqui primeiro achato a lista para uma tupla, depois eu pego os dois valores dentro dessa duplas e os concateno 
concatened_strings = [[name+' '+second_name] for separete_names in names for name, second_name in separete_names ]
print(concatened_strings)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
calculate_slope = lambda x1,y1,x2,y2: (y2-y1)/(x2-x1)
result = calculate_slope(1,5,3,11)
print(result)
calculate_intercept = lambda m,x,y:y -(m*x)
b_result = calculate_intercept(result,1,5)
print(b_result)