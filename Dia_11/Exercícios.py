import math
# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a + b
print(add_two_numbers(1,1))
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3.14 * r * r
print(area_of_circle(10))
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) is int:
           sum += num
        else:
           return 'Not all the items are int'
        
    return(sum)
print(add_all_nums(1,3,'a'))
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(Celsius):
    f = (Celsius *9/5) + 32
    return f
print(convert_celsius_to_fahrenheit(10))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ('dezembro', 'janeiro', 'fevereiro'):
        return 'Verão'
    elif month in ('março', 'abril', 'maio'):
        return 'Outono'
    elif month in ('junho', 'julho', 'agosto'):
        return 'Inverno'
    elif month in ('setembro', 'outubro', 'novembro'):
        return 'Primavera'
    else:
        return 'Mês inválido'
print(check_season(''))
# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(y1,y2,x1,x2):
    m = (y2-y1)/(x2-x1)
    return m
print(calculate_slope(1,2,3,4))
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    if a == 0:
        return "'O coeficiente 'a' não pode ser zero "
    delta = (b **2)-(4*a*c)

    if delta <0:
        return "A equação não possui raízes reais (Delta < 0)"
    elif delta == 0:
        x = -b / (2 *a)
        return(x,x)
    else:
        raiz_delta = math.sqrt(delta)

        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        return (x1, x2)

print(solve_quadratic_eqn(1,-5,6))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for i in list:
        print(i)
lista = ['a',1,True]
print_list(lista)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lista):
    start = 0
    end = len(lista) -1
    while start<end:
        lista[start],lista[end] = lista[end],lista[start]
        start += 1
        end -=1
    return lista
lista = [1,2,3,4,5]
print(reverse_list(lista))
# Another form to do so
def reverse_by_slicing(lista):
    return lista[::-1] 
# start vazio
# stop vazio
# step -1: indica que, ao pecorrer a lista do inciio ao fim, o python deve dar passos de -1, invertendo a ordem dos elementos
print(reverse_by_slicing(lista))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(uncaptilized_list):
    for word in uncaptilized_list:
        print(word.capitalize())
uncaptilized_list = ['oi','wagner','wWWWWWWWW']
capitalize_list_items(uncaptilized_list)

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(List_to_be_added_an_item, item):
    List_to_be_added_an_item.append(item)
    return List_to_be_added_an_item
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list_to_be_removed_an_item, item):
    list_to_be_removed_an_item.remove(item)
    return list_to_be_removed_an_item
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    sum = 0
    num = 0
    while num < n+1:
        sum += num
        num += 1
    return sum
print(sum_of_numbers(10))
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    num = 1
    sum = 0
    while num < n+1:
        sum += num
        num += 2
    return sum
print(sum_of_odds(11))
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_odds(n):
    num = 0
    sum = 0
    while num < n+1:
        sum += num
        num += 2
    return sum
print(sum_of_odds(10))

# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    if n % 2 == 0:
        evens = n / 2+1
        odds = n / 2
    return int(evens), int(odds)
print(evens_and_odds(100)) 

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    num = 1
    factorial_num = 1
    while num < n+1:
        factorial_num *= num
        num += 1
    return factorial_num
print(factorial(5))
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
empty =[]
def is_empty(data):
    return not data
# se 'data' for True (não vazia), o not inverte para false
# se 'data' dor False(vazia), o not inverte para True
# Em Python, a avaliação booleana de coleções funciona assim:
# Vazio: Listas, tuplas, dicionários, strings e conjuntos vazios ([], (), {}, "", set()) são avaliados como False.
# Não Vazio: Coleções com qualquer elemento dentro são avaliadas como True.
print(is_empty(lista))
print(is_empty(empty))
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
def calculate_mean(list_of_numbers):
    sum = 0
    for num in list_of_numbers:
        sum += num
    sum /= len(list_of_numbers) 
    return sum
print(calculate_mean(list_of_numbers=list_of_numbers))

def calculate_median(list_of_numbers):
    median = 0
    middle = 0
    if len(list_of_numbers)%2 == 0:
        middle = len(list_of_numbers)//2
        median += list_of_numbers[middle]
        median += list_of_numbers[middle-1]
    else:
        middle = len(list_of_numbers)//2
        median = list_of_numbers[middle]
    return median
print(calculate_median(list_of_numbers))
def calculate_mode(list_of_numbers):
    dct= {}
    check_mode_number = 0
    mode = 0
    for n in list_of_numbers:
        if n in dct:
            dct[n] += 1
        else:
            dct[n] = 1
    for key,value in dct.items():
        if check_mode_number < value:
            check_mode_number = value
            mode = key
    return 'The mode is', mode
print(calculate_mode(list_of_numbers))

def calculate_range(list_of_numbers):
    maximun = max(list_of_numbers)
    minimun = min(list_of_numbers)
    return maximun - minimun
print(calculate_range(list_of_numbers))

def calculate_variance(list_of_numbers):
    mean = calculate_mean(list_of_numbers)#primeiro devemos pegar a média da lista
    soma = 0
    for num in list_of_numbers: 
        desvio = mean - num # Depois devemos calcular o desvio de cada ponto ( o quão longe cada valor está da média)
        desvio = desvio * desvio # Elevar ao quadrado cada desvio( para tirar o símbolo de negativo )
        soma += desvio # Somar todos os desvios ao quadrado #poderia ter feito isso na linha superior mas não quis
    variance = soma / len(list_of_numbers) 
    return variance
print(calculate_variance(list_of_numbers))

def calculate_std(list_of_numbers):
    variance = calculate_variance(list_of_numbers)
    desvio_padrao = math.sqrt(variance)
    return desvio_padrao
print(calculate_std(list_of_numbers))

# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num  <= 1: # se for menor que 1 n é primo
        return False
    if num == 2: # se for == a 2 é primo 
        return True
    if num % 2 == 0: # e for divisivel por 2 não é primo
        return False
    
    limite = int(math.sqrt(num)) # aqui pegamos a raíz do num
    for i in range(3,limite + 1, 2): # aqui iteramos por todos os números impares pulando de 2 em 2 e dividimos até chegar na raíz
        if num % i ==0 :
            return False
    return True
print(is_prime(503))

# Write a functions which checks if all items are unique in the list.
def is_unique(list_of_numbers):
    dct = {}
    for n in list_of_numbers:
        if n in dct:
            dct[n] += 1
        else:
            dct[n] = 1
    for key,value in dct.items():
        if value > 1: # se o valor for maior que 1, quer dizer que esse item se repitiu mais de uma vez e não único
            not_unique_item = key
            return 'This list is not unique', not_unique_item 
    return 'This list is unique'
fruits= ['banana','uva','morango','banana',1]
print(is_unique(fruits)) 

# Write a function which checks if all the items of the list are of the same data type.
def is_same_data_type(list_of_numbers):
    n = 0
    while n < len(list_of_numbers)-1:
        if type(list_of_numbers[n]) == type(list_of_numbers[n+1]):
            n += 1
            continue
        else: 
            return 'This list not have the same data type'
    return 'This list have the same data type'
print(is_same_data_type(fruits))

# Write a function which check if provided variable is a valid python variable
def is_valid(variable):
    if variable[0].isdigit():
            return 'not valid'
    for valid in variable:
        if valid == '-':
            return 'not valid'
        elif valid == ' ':
            return 'not valid'
    if variable == 'if':
        return 'not valid'
    if variable == 'for':
        return 'not valid'
    if variable == 'while':
        return 'not valid'
    if variable == 'class':
        return 'not valid'
    if variable == 'def':
        return 'not valid'
    if variable == 'True':
        return 'not valid'
    if variable == 'False':
        return 'not valid'
    if variable == 'None':
        return 'not valid'
    return 'It is valid'
#i did only some keywords because yeah
print(is_valid('foroar'))





