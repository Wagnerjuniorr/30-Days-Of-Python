#Booleanos  
#Um valor booleano representa um de dois estados: verdadeiro (True) ou falso (False).
#Diferente do java, em python os valores booleanos são escritos com a primeira letra maiúscula.
print(True)
print(False)

#Operadores lógicos
#O sinal de igual na matemática representa dois valores iguais, 
#mas em python signigica que estamos armazenando um valor em uma variável.

print('Adição ', 1 + 2)
print('Subtração ', 2 - 1)
print('Multiplicação ', 2 * 3)
print('Divisão ', 6 / 2)  #O resultado da divisão sempre será um número float
print('Divisão sem resto ', 7 // 2)
print('Modulo ', 7 % 2) #Resto da divisão
print('Potência ', 2 ** 3)

#Float
print('Floating Point Number, PI',3.14)
print('Floating Point Number, gravidade na Terra',9.8)

#Número complexos
print('Número complexo ', 2 + 3j)
print('Múltiplicação de número complexo ', (2 + 3j) * (1 + 2j))

#Vamos declarar uma variável e atribuir um tipo de dado númerico. 
#Não criar o hábito de declarar variáveis com caractere único 

a = 3
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponent = a ** b

#Poderia ter usado sum ao invés de total, mas sum é uma built-in function do python.
print(total) #Se você não ancexar uma string, o print irá exibir apenas o valor e você não saberá do que se trata.
print('a + b =', total)
print('a - b =', diff)
print('a * b =', product)
print('a / b =', division)
print('a % b =', remainder)
print('a // b =', floor_division)
print('a ** b =', exponent)

#Calculando a área de um círculo
raio = 10
area_circulo = 3.14 & raio ** 2
print('Área do círculo:', area_circulo)

#Calculando a área de um retângulo
largura = 10
altura = 20
area_do_retangulo = largura * altura
print('Área do retângulo:', area_do_retangulo)

#Calcuando o peso de um objeto
massa = 75  # em kg
gravidade = 9.81  # em m/s²
peso = massa * gravidade
print('Peso', peso)

#Calculando a densidade de um líquido
massa = 75 # em kg
volume = 0.075 # em m³
densidade = massa / volume
print('Densidade:', densidade)

#Operadores de comparação
print(3 > 2) #True, pois 3 é maior que 2
print(3>= 2) #True, pois 3 é maior igual a 2
print(3 < 2) #False, pois 3 é maior que 2
print(2 < 3) #True, pois 2 é menor que 3
print(2 <= 3) #True, pois 2 é menor igual a 3
print(3 == 2) #False, pois 3 não é igual a 2
print(3 != 2) #True, pois 3 não é igual a 2
print(len('mango') == len('avocado')) #False 
print(len('mango') != len('avocado')) #True
print(len('mango') < len('avocado')) #True
print(len('milk') == len('meat')) #True
print(len('milk') != len('meat')) #False
print(len('tomato') == len('potato')) #True
print(len('python') > len('dragon')) #False

# Compating something gives either a True or False
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)

# Além disso python também usa:
# is: Retorna True se ambas as variáveis forem o mesmo objeto (x is y)
# is not: Retorna True se ambas as variáveis não forem o mesmo objeto (x is not y)
# in: Retorna True se o valor especificado estiver presente no objeto (x in y)
# not in: Retorna True se o valor especificado não estiver presente no objeto (x not in y)

print('1 is 1: ', 1 is 1) #True
print('1 is not 2', 1 is not 2) #True
print('A in Asabeneh', 'A' in 'Asabeneh') #True
print('B in Asabeneh', 'B' in 'Asabeneh') #False - não tem B maiúsculo
print('coding' in 'coding for all') #True
print('a in an: ', 'a' in 'an') #True
print('4 is 2 **2: ', 4 is 2 ** 2)

#Operadores Lógicos
#Diferente de outras linguagens de programação, python usa palavras chave and, or e not para os operadores lógicos. Operadores Lógicos são usados para combinar estados
#and
#Retorna True se ambos estados forem verdadeiro x < 5 and x < 10
#or 
#Retorna True se um dos estados forem verdadeiro x < 5 or x < 4
#not
#Inverte o resultado, retorna False se o resultado for verdadeiro not(x < 5 and x < 10)

print(3 > 2 and 4 > 3) # True
print(3 > 2 and 4 < 3) # False 
print('True and True: ', True and True)
print(3 > 2 or 4 > 3) # True 
print(3 > 2 or 4 < 3) # True - porque um dos estados é verdade
print(3 < 2 or 4 < 3) # False - porque ambos estados são falso
print('True of False: ', True or False)
print(not 3 > 2) # False(True)
print(not True) # False
print(not False) # True
print(not not True) # True


