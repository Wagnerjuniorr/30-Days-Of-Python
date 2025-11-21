# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id.
import random, string
def random_user_id():
    all_possible_alphanumeric_digits = string.ascii_letters + string.digits
    n, count = 0, 0
    user_id = ''
    while count < 5:
        n = random.randint(0,61)
        user_id += all_possible_alphanumeric_digits[n] 
        count += 1

    return user_id
print(random_user_id())
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    all_possible_alphanumeric_digits = string.ascii_letters + string.digits
    number_of_char = int(input('Number of char: '))
    number_of_IDs = int(input('Number of IDs: '))
    list_of_IDs = []
    n = 0
    while n < number_of_IDs:
        # usa random.choices para selecionar number_of_char caracteres aleatórios
        # usa "".join() para transformar a lista de caracteres em uma única string
        user_id = "".join(random.choices(all_possible_alphanumeric_digits,k=number_of_char))
        list_of_IDs.append(user_id)
        n += 1
    return list_of_IDs
print(user_id_gen_by_user()) 

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    n = 0
    rgb = []
    while n < 3:
        rgb.append(random.randint(0,255))
        n += 1
    return rgb
print(rgb_color_gen())

# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(number_of_colors):
    hexa = string.hexdigits
    list_of_hexa = []
    for n in range(number_of_colors):
        hexa_id = '#' + "".join(random.choices(hexa,k=6)) 
        list_of_hexa.append(hexa_id)
    return list_of_hexa
print(list_of_hexa_colors(10))
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_color(number_of_colors):
    list_of_rgb = []
    for n in range(number_of_colors):
        list_of_rgb.append(rgb_color_gen())
    return list_of_rgb
print(list_of_rgb_color(10))


# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(rgb_hex,number):
    if rgb_hex == 'rgb':
        print(list_of_rgb_color(number))
    elif rgb_hex == 'hexa':
        print(list_of_hexa_colors(number))
    else:
        print('undefined')
generate_colors('hexa',5)

# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lista):
    random.shuffle(lista)
    print(lista)
numbers = [10,23,431,321,'aa']
shuffle_list(numbers)
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random_unique_numbers():
    seven_unique = ''
    # enquanto o tamanho da string for menor que 7
    while len(seven_unique) <7:
        number = str(random.randint(0,9))
        # verifica se o numero já está na string
        if number not in seven_unique:
            seven_unique += number
        # se n for único o while continua rodando sem contador manual
    return seven_unique
print(seven_random_unique_numbers())
            
