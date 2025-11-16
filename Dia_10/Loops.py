# Loops
# In order to handle repetitive task programming language use loops
# Python programming language also provides the following type of two loops
# while loop
# for loop

# while loop
# it is used to execute a block of statements repeatedly until giben condition
# when the condition becomes false, the lines of code after the loop will continued to be executed
count = 0
while count <5:
    print(count)
    count = count + 1

# in the above while loop, the condition becomews false when count is 5
# that when  the loop stops
# if we are intested to run block of code onde the condition is no longer true, we can use else
print('while else loop')
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
# the above loop condition will be false when count is 5

# Break and Continue - Part 1
# Break: We use break when we like to get out of or stop the loop
count = 0
print('break and continue')
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# continue: with the continue statement we can skil the current iteration, and continue with the next
count = 0
while count<5:
    if count == 3:
        count = count +1
        continue
    print(count)
    count = count + 1
# the above whie loop only prints 0,1,2 and 4 (skips 3)

# for loop
# Loop is used for iterating over a sequence(that is either a list, a tuple, a dictionary, a set, or a string)
numbers = [0,1,2,3,4,5]
for number in numbers: # number is a temporary name to refer to the list items, valid only inside this loop
    print(number)      # the number will be printed linbe by line, from 0 to 5
# for loop with a string
language = 'Python'
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])
# for loop with a tuple
numbers = ( 0,1,2,3,4,5)
for number in numbers:
    print(number)

# for loop with a dictionary looping through gives you the key of the dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)
for key, value in person.items():
    print(key, value)# this way we get both keys and values

# Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


# Break and Continue - Part 2
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
for number in numbers:
    print(number)
    if number == 3:
        continue
    if number !=5:
        print('Next number should be', number + 1)  
    else: 
        print("loop's end")
print('outside loop')
# In the example, if the number is equals to 3, the step after the condition will be jumped and the rest of the iteration will continue (nmumber 4)


# The range function
# The range() function is used to list numbers. 
# The range (start, end, step) takes three parameters.
# It starts from 0 and the increments is 1.
# The range sequence neeeds at least 1 argument (end).
lst = list(range(11))
print(lst)
st = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst)
st = set(range(1,11,2))
print(st)
for number in range(11):
    print(number)

# Nester for loop
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# for else
# if we want to execute a messagen when loop end, we use else
for number in range(11):
    print(number)
else:
    print('The loops stops at', number)

# Pass
# In python when statement is required (after semicolon), but we don't like to execute any code there, 
# we can write the word pass to avoid erros
# Alse can be used as a placeholder, for future
for number in range(6):
    pass