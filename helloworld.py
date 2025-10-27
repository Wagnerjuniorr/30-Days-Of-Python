#COMENTÁRIOS
#This is the first comment
#This is the secont comment
#Python is eating the world

#DOCSTRING
"""This is multiline comment
"multiline comment takes multiples lines.
"python is eating the world
"""

#DATA TYPES
#STRING
#Se uma string tiver mais de uma frase, usamos aspas triplas
'Asababeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30 days of python'

#BOOLEAN (deve sempre estar em maiúsculo)
True # Is the light on? if it is on, the the value is true
False # Is the light on? if it is off, then the value is false

#LISTA
#A lista em python é uma coleção ordenada que permite armazenar itens de diferentes tipos de dados
#Uma lista é semelhante a um array em JavaScript
[0, 1, 2, 3, 4, 5] #all are the same data types
['Banana', 'Orange', 'Mango', 'Avocado'] #all the same data types - a list of string (fruits)
['Finland','Estonia','Sweden','Norway']#all the same data types - a list of strings(contries)
['Banana', 10, False, 9.81] #different data types in the list - strings, integer, boolean and float

#DICIONÁRIO
#Um objeto de dicionário em Phthon é uma coelção não ordenada de dados em formato de par de valores-chave
{
    'Fisrt_name': 'Asabeneh',
    'Last_name': 'Yetayeh',
    'Country': 'Finland',
    'Age': 250,
    'is_married': True,
    'Skills': ['JavaScript', 'React', 'Node', 'Python'],
}

#TUPLA
#Uma tupla é uma coleção rodenada de diferentes tipos de dados, como uma lista, mas as tuplas não podem ser modificadas(são imutáveis) depois de criadas.
#Eles são imutáveis 
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') #Names
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Saturn') #Planets

#SET
#O set é uma coleção de tipode de dados semelhantes a uma lista e uma tupla.
#Ao contrário de lista e da tupla, set não é uma coleção ordenada de itens.
#Como na matemática, o conjunto em Python armazena apenas itens exclusivos
{2, 4, 3, 5}
{3.14, 9.81, 2.7, 1.6}#order is not important in set

#Day 1 - 30DaysOfPython Challenge

print(2+3)  #addition(+)
print(3-1)  #subtraction(-)
print(2*3)  #multiplication(*)
print(3/2)  #division(/)
print(3**2) #exponentiation(**)
print(3%2)  #modulus(%)
print(3//2) #floor division(//)

#Checking data types 
print(type(10))       #int
print(type(3.14))     #float
print(type(1 +3j))  #complex
print (type('Asabeneh'))  #str
print(type([1,2, 3])) #List
print(type({'name': "Asabeneh"})) #Dictionary
print(type({9.8,3.14,2.7})) #Set 
print(type((9.8,3.14,2.7))) #Tuple                                                                                                                                                                                                                                                                                                                                                                                                                  