# we've seen different pytohn data types
# We usually store our data in different file formats.
# In addition to handling files, we will also see different file formarts(.txt, .json, .xml, .csv, .tsv, excel)
# First let us get familiar with handling file with commom file format(.txt)

# File handling is an important part of programming which allows us to create, read, update and delete files
# In python to handle data we use open() built-in func

# Syntax
# open('filename', mode) # mode(r,a,w,x,t,b)
# r - Read - Deafaul value. Opens a file for reading, it returns an error if the file does not exists
# a - append - Opens a file for appendind, creates the file if does not exists
# w - write - Opens a file for writting, create the file if does not exist
# x - Create - Create the specified file, returns an error if the file does not exists
# t - Text - Default value. Text mode
# b - Binary - Binary mode (e.g. images)

# Opening files for reading
# the default mode of open is reading, so we do not have to specify 'r' or 'rt'
# I have create and save a file named reading_file_example.txt int the files directory. 
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
# As u can see in the example above, I printed the opened file and it gave some information about it
# An opened file has to be clodes with clese()

# read()
# read the whole text as a string. if we want to limit the number of character we want to read, we can limite by passing int value 
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
# Instead of printing all the text, let us print the first 10 character of the txt file
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# readline(): read only the first lines
f = open('./files/reading_file_example.txt')
line = f.readlines()
print(type(line))
print(line)
f.close()
# Another way to get all the line as a list is using splitlines()
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# After we open a file, we should close(pq libera recursos do sistema, torna o programa mais prevsisivel e seguro)
# There is a chacing to forget to do so
# There is a new way of opening files using with - closes the files by itself
with open('./files/reading_file_example.txt')as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# Opening files for writting and updating
# to write to an existing file, we must add a mode as a parametr to open() funcions
# "a" 
# "w"
# Let us append some text to the file we have been reading
with open('./files/reading_file_example.txt','a') as f:
    f.write(' This text has to be appened at the end')
# The method below creates a new file, if the file does not exists
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly create file')

# Deleting Files
# If we want to remove a file we use os module
# if the file foes not exists, the remove will raise an errror, so it is good to use a condition like this
import os

if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exists')

# File Types
# JSON
# JSON stands for JavaScript Object Notation.
# Actually, it is stringfied JavaScript object or Python dictionary
person_dct = {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript","React","Python"]
}
# json is a string in python
# thats why he put ''' here
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
# Changing JSON to Dictionary
# to change JSON to a dictionary, first we import the json modeule and thein wwe use laods methods
import json
# Lets change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Changing Dictionary to JSON
# To change a dictionary to a JSON we use dumps method from the json module.
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# lets convert it to json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

# Savind as JSON file
# for writing a json file, we use json.dump() methods, it can take dictionary, outputfile, ensure_ascii and indent
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# 1- Onde vamos salvar o arquivo, 2-w: write, enconding = Unicode Transformation Format- 8 bit
with open('./files/json_example.json','w', encoding='utf-8') as f:
    json.dump(person, f , ensure_ascii=False, indent=4)

# File with csv Extension
# CSV stands for comma separated values.
# CSV is a simple file format used to store tabular data
import csv
# abre o arquivo localizado em bla bla; with garante que o arquivo será fechado assim que o bloco de códido terminar
with open('./files/csv_example.csv') as f:
    # aqui é criado o objeto que vai 'iterar' sobre as linhas do arquivo, 
    # Delimiter diz ao python que cada coluna vai ser limita por uma ,
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    # dentro desse loop, cada row(linha) é tratada como uma lista de string
    for row in csv_reader:
        # o código identifica a primeira lina(nome, cidade, país) junta os elemento com "," e os imprime
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        # para todas as outras linhas ele assume que são dados de professores
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

# File with xlsl Extension
# To read excel files we need to isntall xlrd package. 
# We will cover this after we cover package installing using pip
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets())
# print(excel_book.sheet_names())     

# File with XML extension
# In XML the tags are not predefined.
# The first line is an XML declaration
# The person tag is the root of the XML
# The person has a gender attibute
import xml.etree.ElementTree as ET
# lendo o arquivo
# parse le o arquivo fisico que está na pasta files
# ele carrega todo o conteýdo e criar um objeto chamado tree
tree = ET.parse('./files/xml_example.xml')
# Capturando a raiz (tag principal)
root = tree.getroot()
# exibindo a tag raiz
print('Root tag:', root.tag)
# verificando atributos
print('Attribute:', root.attrib)
# Como xml é um árvore, a raz tem filhos(tags que estão abaixo dela)
for child in root:
    print('field: ', child.tag)
    
                                                    