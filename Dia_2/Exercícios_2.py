#Exercicios: Level 2
#1-Verifique o tipo de dados de todas as suas variáveis ​​usando a função integrada type()
#2-Usando a função integrada len(), encontre o comprimento do seu primeiro nome
#3-Compare o comprimento do seu nome e do seu sobrenome
#4-Declare 5 como num_one e 4 como num_two
    #Adicione num_one e num_two e atribua o valor a uma variável total
    #Subtraia num_two de num_one e atribua o valor a uma variável diff
    #Multiplique num_two e num_one e atribua o valor a um produto variável
    #Divida num_one por num_two e atribua o valor a uma divisão variável
    #Use a divisão de módulo para encontrar num_dois dividido por num_um e atribua o valor a uma variável restante
    #Calcule num_one elevado a num_two e atribua o valor a uma variável exp
    #Encontre a divisão mínima de num_one por num_two e atribua o valor a uma variável floor_division
#5-O raio de um círculo é de 30 metros.
    #Calcule a área de um círculo e atribua o valor a um nome de variável de area_of_circle
    #Calcule a circunferência de um círculo e atribua o valor a um nome de variável circum_of_circle
    #Pegue o raio como entrada do usuário e calcule a área.
#6-Use a função de entrada integrada para obter nome, sobrenome, país e idade de um usuário e armazenar o valor em seus nomes de variáveis ​​correspondentes
#7-Execute help('keywords') no Python shell ou em seu arquivo para verificar as palavras ou palavras-chave reservadas do Python

print(type('oi'))
print(type(69))
print(type(3.14))
print(type(1 + 1j))
print(type(True))
print(type([6, 6, 9]))
print(type({'nome':'Wagner','idade':69}))
print(type((6, 9)))
print(type(zip([6,9],[9,6])))

print(len('Wagner'))
print(len('Moreira'))

num_one = 5
num_two = 4
var_total = num_one + num_two
var_diff = num_one - num_two
var_product = num_one * num_two
var_division = num_one / num_two
num_modulo = num_one % num_two
var_exp = num_one ** num_two
num_floor_division = num_one // num_two
print(var_total)
print(var_diff)
print(var_product)
print(var_division)
print(num_modulo)
print(var_exp)
print(num_floor_division)

Area = 3.14 * 30 ** 2
Circunferencia = 2 * 3.14 * 30
print(Area)
print(Circunferencia)
raio = int(input('Digite o raio do cículo em metros: '))
Area_usuario = 3.14 * raio ** 2
print(Area_usuario)

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
pais = input('Digite seu país: ')
idade = input('Digite sua idade: ')
print(nome)
print(sobrenome)
print(pais)
print(idade)
help('keywords')
