# A regular expression or RegEX is a special text string that helps to find patterns in data
# A RegEx can be used to check if some pattern existis in a different data type
# To use RegEx in python first we should imoprt the RegEx module which is called re

# The re Module
import re
# Methods in re Module
# To find a pattern we use different set of re character sets that allows to search for a match in a string
# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None
# re.search(): returns a match object if there is one anywhere in the string, including multline strings
# re.split(): takes a string, splits it at the match points, returns a list
# re.sub(): replaces one or many matches within a string

# match
# re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern, re.I is case ignore

import re
txt = 'I love to teach python and javaScript'
# it returns an object with span, and match
match = re.match('I love to teach', txt, re.I) # I = IGNORECASE (ao usar re.I vc está dizendo para o python ignorar a diferenças de minusculas e maiusculas)
print(match)
span = match.span() # span é o intervalo de indices (ele é retornado como uma tupla) primerio num é inclusivo e o último exclusivo (15 é onde para)
print(span)
# Lets find the star and stop position from the span
start, end = span
print(start, end)
print(start, end)
substring = txt[start:end]
print(substring)
# the match function returns an object only if the text starts with the pattern
txt = 'I love to teach python an javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)

# Search
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# it returns an object with span and match
match = re.search('first', txt, re.I)
print(match) 
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)
# Search is a much better function because it search for a pattern throught the entire text
# findall checks for the pattern throught the entire text and returns all the matches

# Searching for All the Matches Using Findall
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# it returns a list
matches = re.findall('language', txt, re.I)
print(matches)
matches = re.findall('python', txt, re.I)
print(matches)
# both lowercase and uppercase letter are included
# if we do not have the re.I flad, then we will have to write out pattern differently 
matches = re.findall('Python|python',txt)
print(matches)
# Or
matches = re.findall('[Pp]ython', txt)
print(matches)

# Replacing a Substring
match_replaced = re.sub('[Pp]ython','JavaScript', txt,re.I) # it seems that case ignore does not works with re.sub
# re.sub segue essa estrutura : re.sub(pattern, repl, string, count=0, flags=0)
# Quando eu coloquei re.I ele interpretou como count(4 argumento)
# Como o valor da constante re.I é 2, ele na verade estava substituindo no max 2 vezes
# funcinou mas n deveria
# outros me´todos
match_replaced = re.sub('python', 'JavaScript', txt, flags=re.I)
match_replaced = re.sub('python', 'JavaScript', txt, 0, re.I)
print(match_replaced)

# Spliting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n',txt)) # splitting using \n - end of line symbol

# Writing RegEx Patterns
# to declare a string we use a single or double quote 
# to declare RegEx variable r". The following pattern only identifies apple with lowercase
# to make case INSESITIVE we either should rewrite out pattern or we should add a flag
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)
# to make case insensitive
matches = re.findall(regex_pattern, txt, re.I)
print(matches)
# or
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)

# []: A set o cheracters
# [a-c]: means, a or b or c
# [A-C]: means, A or B or C
# [0-3]: means, 0 or 1 or 3
# [A-Za-z0-9] any single charecter, that is a to z, A to z or 0 to 9

# \: uses to escape special characters
# \d means: matcch where the string contains digits(numbers from 0-9)
# \D means: match where the string does not contain digits

# .: any character except new line character(\n)

# ^: starts with
# r'^substring' , a sentence that starts with a word substring
# r'[^abc] means not a, not b, not c

# $: ends with
# r'substring$' eg r'love$', sentence that ends with a word love

# *: zero or more times
# r'[a]*' means a optional or it can occur many times

# +: one or more times
# r'[a]+' means at least once (or more)

# ?: zero or one time
# r'[a]?' means zero times or once

# {3}: Exactly 3 characters
# {3,}: At least 3 characters
# {3,8}: 3 to 8 characters

# |: Either or
# r'apple|banana' means either apple or banana

# (): capture and group

# if we want to look for banana and apple, we write use |
regex_pattern = r'[Aa]pple|[Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern,txt)
print(matches)

# Escape character(\) in RegEx
regex_pattern = r'\d' # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

# One or more time(+)
regex_pattern = r'\d+' # + mean one or more times
matches = re.findall(regex_pattern, txt)
print(matches ) # ['6', '2019', '8', '2021']

# Period(.)
regex_pattern = r'[a].' # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'[a].+' # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches) # ['and banana are fruits']

# Zero or more times(*)
# The pattern could may not occur or it can occur many times
regex_pattern = r'[a].*' # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches) # ['and banana are fruits']

# Zero or one time(?)
# the pattern may not occur or it may occur once
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail' # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches) # ['e-mail', 'email', 'Email', 'E-mail']

# Quantifier in RegEx
# We can specify the lenght of the substring we are looking for
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}' # exactly four times
matches = re.findall(regex_pattern,txt)
print(matches)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

# Cart ^
# Starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This' # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches) # ['This']

# Negation
regex_pattern = r'[^A-Za-z ]+' # ^ in set character means neagtion, not A to z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches) # ['6,', '2019', '8', '2021']
