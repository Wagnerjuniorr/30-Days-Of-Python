import math
# 1 - Declare your age as integer variable
# 2 - #Declare your height as a float variable
# 3 - Declare a variable that store a complex number
# 4 - Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# 5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# 6 - Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# 7 - Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# 8 - Calculate the slope, x-intercept and y-intercept of y = 2x -2
# 9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# 10 - Compare the slopes in tasks 8 and 9.
# 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# 12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# 13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'
# 14 - I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# 15 - There is no 'on' in both dragon and python
# 16 - Find the length of the text python and convert the value to float and convert it to string
# 17 - Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# 18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# 19 - Check if type of '10' is equal to type of 10
# 20 - Check if int('9.8') is equal to 10
# 21 - Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?]
# 22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# 23 - Write a Python script that displays the following table

age = 20
altura = 1,74
num_complex = 4j

base = float(input("Qual é a base do triangulo? "))
altura = float(input("Qual é a altura do triangulo? "))
area_triangulo = 0.5 * base * altura
print("A área do triangulo é: ", area_triangulo)

side_a = int(input("Enter lado A: "))
side_b = int(input("Enter lado B: "))
side_c = int(input("Enter lado C: "))
perimeter = side_a + side_b + side_c
print("o perimetro do triangulo é: ", perimeter)

comprimento = float(input("Qual é o comprimento do retângulo? "))
largura = float(input("Qual é a largura do retângulo? "))
area_retangulo = comprimento * altura
print("Area do retangulo é: ", area_retangulo)

raio = float(input("raio: "))
area_circulo = 3.14 * raio ** 2
circumferencia = 2 * 3.14 * raio
print("Area e circumferencia do circulo: ", area_circulo, circumferencia)

#x = 0
x = 0
y = 2 * x - 2
print("A inclinação é: ", y)

#(m = y2-y1/x2-x1)
#ponto (2, 2) e o ponto (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10

inclinação = (y2 - y1)/(x2 - x1)
distancia_euclidiana = math.sqrt((x2 - x1)**2) + ((y2 - y1)**2)
print("inclinação e distancia euclidiana dos pontos(2, 2) e (6, 10)", inclinação, distancia_euclidiana)

print(y == inclinação)

x = int(input("Digite o valor de x: "))
y = (x**2) + (6*x) + 9
print("o valor de y é: ", y)
print("o valor para zera é -3")

print("Python e dragon tem o mesmo tamanho?")
print(not len('python') == len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full og jargon')

print(not 'on' in 'python' and 'on' in 'dragon')

tamanho_da_palavra_python = float(len('python'))
str(tamanho_da_palavra_python)

x = int(input("Qual o valor de x"))
print(x % 2 is 0)

print("Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.")
print(7 // 3 is 2.7)
print("Check if type of '10' is equal to type of 10")
print('10' is type(10))
print("Check if int('9.8') is equal to 10")
print(9.8 is 10)

horas = int(input("Enter hours: "))
rate = int(input("rate per hour: "))
ganho_semanal = horas * rate 
print("o ganho semanal é de: ", ganho_semanal)
anos_vividos = int(input("Digite quantos anos você viveu: "))
segundos_vividos = anos_vividos * 365 *24* 60* 60
print(f"Você viveu por {segundos_vividos} segundos" )

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
















