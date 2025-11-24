# List Comprehension in Python is a compact way of creating a list from a sequence. 
# I s a short way to create a new list. 
# List comprehension is conderably faster than processing a list using the for loop

# syntax
# [i for i in tireable if expression]
# For instance, if you want to change a string to a list of characters
# You cant use a couple methods. Here is some of them
# one way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst)) # list
print(lst) 

# second way: list comprehension
lst = [i for i in language]
print(type(lst))
print(lst)

numbers = [i for i in range(11)] # to generate numbers from 0 to 10
# nova_lista = [EXPRESSÃO FOR ITEM IN INTERÁVEL]
#                   1    /          2
print(numbers)
squares = [i * i for i in range(11)]
print(squares) 
# it is also possible to make a list of tuples
numbers = [(i, i*i) for i in range(11)]
print(numbers) # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Lis comprehension can be combined with if expression
even_numbers = [i for i in range(21) if i %2 == 0]
# nova_lista = [EXPRESSÃO FOR ITEM IN INTERÁVEL IF CONDIÇÃO]
#                   1    /          2          /    3, Opcional
print(even_numbers)
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)
# flattening a two dimensional array
list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
flattned_list = [ number for row in list_of_list for number in row]
print(flattned_list)
# Loop 1
# for row in list_of_list é o loop principal, ele itera sobre list_of_list, tratando cada sub-list como uma row(list)
# Loop 2
# number in row, para cada rwo do loop externo, este loop itera sobre os elementos individuais dentro daquela row, extraindo o number
# o primeiro number é um append implicto (por o primeiro item fica jogado)
# ele precisa estar ali porque essa posição permite que voce não apenas pegue o valor, mas também o transfome antes de adiociona-lo


# Lambda Function
# Lambda function is a small anonymous function without a name. 
# It can take any number of arguments, but can only have one expression
# Lambda function is similar to anonymous functions in javascript. 
# we need it when we wan to write an anonymous function inside another function

# Creating a lambda Function
# to create a lambada function we use lambda keyword followed by a parameter(s), followed by an expression
# Lambda does not use return but it explicitly returns the expression
def add_two_nums(a,b):
    return a+b
print(add_two_nums(2,3))
# Lets change the above function to a lambda function
add_two_nums = lambda a,b: a + b
print(add_two_nums(2,3))
#self invoking lambda function
print((lambda a,b:a + b)(2,3)) # 5 - need to encapsulate it in print() to see the result in the console
square = lambda x : x ** 2
print(square(3))
cube = lambda x:x ** 3
print(cube(3)) # 27
# a lambda function permite criar uma pequena função que não tem nome (por isso, anonima) e que pode ser definida em uma única linha de código
# seu papel é ser uma função descártavel e imediata para tarefas simples que exigiriam a definição formal de uma função completa(def)
# lambda argumento1, argumento2,...: EXPRESSÃO
# keyword      ARGUMENTOS       Corpo da função de retorno
# se quiser usa-la novamente, deve atribuí-la a uma variavel
# não pode conter comandos como if/else complexos, for ou multiplas linhas
# CONTINUANDO
multiple_variables = lambda a,b,c: a ** 2 -3 * b + 4 * c
print(multiple_variables(5,5,3))
# Lambda function inside another function
def power(x):
    return lambda n : x ** n
cube = power(2)(3) # function power now need 2 argumentes to run , in separate rounded brackets
# ali na verdade são duas chamadas de função, uma sendo o x(2) e a outra sendo n(3) utilizando uma função anonima
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)

# Exemmplo 2 sort
# As funções de ordenação usam o argumento key para definir o critério de ordenação.
# Cenário: ordernar uma lista de tuplas pelo segundo elemento de cada tupla
# Usando lambda: define a chabe de ordenação como índice 1 (idade)
people = [('Alice',30), ('Bob',25),('Charlie', 38)]
people_sorted = sorted(people, key=lambda p: p[1])
print(people_sorted)