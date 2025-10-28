print('Hello, World!') # it prints the value Hello, World!
len('Hello, World!') #it counts the number of characters including space
type('Hello, World!') #it checks the data type
str(10) #it convets number to string
int('10') #it converts to number
float('10') # it convets integer to decimal
input('Enter yout name:') #it takes user input
min(20, 30, 40 ,50) #gives the minimum value
max(20, 30, 40, 50) #gives the maximum value
min([20, 30, 40, 50]) #it takes list as an argument and return min 
max([20, 30, 40, 50]) #it takes list as an argument and return max
sum([20, 30, 40, 50]) #it takes only list as an argument ant return sum 

#Regras da nomenclatura de variáveis em Python
#O nome de uma variável deve começar com um letra ou underline
#O nome de uma variável não pode começar com um número
#Um nome de variável só pode contet caracteres alfanuméricos (A-Z, 0-9) e sublinhados (_)
#O interpretador Python diferencia de minúsuclas(nome, nome, nome e PRIMEIRO NOME) são váriaveis diferentes então tome cuidado com isso
#As variáveis seguem a convenção snake_case (todas as letras minúsculas e palavras separadas por sublinhados)
#O sinal de igual (=) é usado para atribuir valores às variáveis

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
    'city':'Helsinki'
}

print('Hello, World!') #The text Hello, World! is an argument
print('Hello', ',','World', '!') #it can take multiple arguments
print(len('Hello, World')) #it takes only one argument

# Printin the values stored in the variables
print('First name: ', first_name)
print('First name length: ', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ',country)
print('Citya: ', city)
print('Age: ', age )
print('Married: ', is_married)
print('Skills: ', skills)
print('Person info: ', person_info)

#Declarando múlitplas variáveis em um linha
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh','Finlad',250, True
print(first_name, last_name, country, age, is_married)

#input()
first_name = input('What is your name: ')
age = input('How old are you: ')
print(first_name)
print(age)


#Checando o tipo de dados e Casting
first_name = 'Asabeneh' #str
last_name = 'Yetayeh' #str
country = 'Finland' #str
city = 'Helsinki' #str
age = 250 #int

#printing out types
print(type('Asebeneh')) #str
print(type(first_name)) #str
print(type(10)) #int
print(type(3.14)) #float
print(type(1 +1j)) #complex
print(type(True)) #bool
print(type([1, 2, 3, 4])) #list
print(type({'name':'Asabeneh', 'age':250,'is_married':True}))   # dict
print(type((1, 2)))                                             # tuple
print(type(zip([1, 2],[3,3])))                                  # set

#Type Casting: Podemos converter um tipo de dados em outro tipo de dado
#Nós podemos usar esses tipos para fazer o casting int(), float(), str(), list, set quando fazemos operação aritiméticas
#Os números das strings devem ser primeiro convertidos para int ou float, caso contrário, retornará um erro
#Sec concaternamos um número com um string, o número deverá ser primeiro convertido em uma string.

#int to float
num_int = 10
print('num_int', num_int)       #10
num_float = float(num_int)
print('num_float:', num_float)  #10.0

#float to int
gravity = 9.81
print(int(gravity)) #9

#int to str
num_int = 10
print(num_int)
num_str = str(num_int) #'10'
print(num_str)

#str to int or float
num_str = '10'
print('num_int', int(num_str)) #10
print('num_float:', float(num_str)) #10

#str to list
first_name = 'Asabeneh'
print(first_name) #'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list) #['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

#Numeros
#Inteiros são considerados os(negativos, zero e positivos) sem parte decimal
#Floats são números com parte decimal
#Complexos são números imaginários representados com j ou J


