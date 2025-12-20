import re
# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# aqui eu separo todas as palavras na variavel lista words sem pontuação e em lowercase
words = re.findall(r'\b\w+\b',paragraph.lower())
print(words)
most_frequent_word = {}
for w in words:
    if w not in most_frequent_word:
        most_frequent_word[w] = 1
    else: 
        most_frequent_word[w] +=1
most_frequent_word = sorted(most_frequent_word.items(), key=lambda kv:kv[1], reverse=True)
print(most_frequent_word)

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
# Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0','8', '4' ]
match = re.findall(r'-?\d+', str(points))
print(match)
positions = []
positions = [int(n) for n in match]
print(positions)
positions = sorted(positions)
distance = positions[len(positions) -1] - positions[0]
print(positions)

# Exercises: Level 2
# Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(string):
    Is_valid = False
    regex_pattern = r'^[0-9]|@|#|!|-'
    match = re.findall(regex_pattern, string)
    if match == []:
        Is_valid = True
    return Is_valid
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

# Exercises: Level 3
# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(string):
    bad_characters = ['%','@','#','$','&'] # '$ ' é um matacaractere, por isso é necessário escapa-lo
    for bd in bad_characters:
        string = re.sub(re.escape(bd),'', string)
    return string
sentence = clean_text(sentence)
def most_frequent_word(sentence):
    # words(list) recebe o texto inteiro em lowercase
    words = re.findall(r'\b\w+\b',sentence.lower())
    # é criada o dicionatio most frequent word
    most_frequent_word = {}
    # w pasa pela lista words
    for w in words:
        # se w não estiver em most_frequent_word, é criada a chave com o valor = 1
        if w not in most_frequent_word:
            most_frequent_word[w] = 1
        # se não o valor recebe +1
        else: 
            most_frequent_word[w] +=1
    # o dicionário é organizado de forma decreescente 
    most_frequent_word = sorted(most_frequent_word.items(), key=lambda kv:kv[1], reverse=True)[:3]
    return most_frequent_word
print(most_frequent_word(sentence))