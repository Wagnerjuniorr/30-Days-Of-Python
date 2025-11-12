# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))
print(age)
if age >= 18:
    print("Your are old enough to drive")
else:
    difference = 18 - age
    print("You need {} more years to learn to drive".format(difference))
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
your_age = int(input("Enter your age: "))
my_age = 20
if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are a year older than me")
    else:   
        print("You are {} years older than me".format(difference))
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("Im a year older than you")
    else:
        print("Im {} years older than you".format(difference))
else:
    print("We are the same age")
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
if number_one > number_two:
    print("{} is greater than {}".format(number_one, number_two))
elif number_two > number_one:
    print("{} is greater than {}".format(number_two, number_one))
else:
    print("{} and {} are equals".format(number_one, number_two))

# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
score = int(input("What was your score? "))
if score > 90 and score <= 100:
    print("You got A")
elif score > 70 and score < 89:
    print("You got B")
elif score > 60 and score < 69:
    print("You got C")
elif score > 50 and score < 59:
    print("You got D")
elif score > 0 and score < 49:
    print("You got F")
elif score > 100:
    print("You are lying")

# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

season = input("What season are we in? ")
if season == 'Autumn':
    print("We are probably in September, October or November")
elif season == 'Winter':
    print("We are probably in December, January or February")
elif season == 'Spring':
    print("We are probably in March, April or May")
elif season == 'Summer':
    print("We are probably in June, July or August")
else:
    print("You probrably typed somethin wrong")

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Type a fruit: ')
does_exist = new_fruit in fruits
if does_exist == True:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print(fruits)

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if person.get('skills') == None:
    print('skill issue')
else:
    middle = len(person['skills']) // 2
    print(person['skills'][middle])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if person.get('skills') == None:
    print('skills issue')
elif 'Python' in person.get('skills', []):
    print('Has python')
else: 
    print('Does not have PAITO')

# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
skills = person.get('skills',[])
if len(person['skills'])==2 and 'JavaScript' in skills and 'React'in skills:
        print('He is a front end dev')
elif len(person['skills'])==3 and 'Node' in skills and 'Python'in skills and 'MongoDB'in skills:
        print('He is a backend dev')
elif len(person['skills'])==3 and 'Node' in skills and 'React'in skills and 'MongoDB'in skills:
        print('He is a fullstack dev')
else:
    print('unkown title')

# If the person is married and if he lives in Finland, print the information in the following format:
if person.get('is_married') == True and person.get('country') == 'Finland':
    print('{} {} lives in {}. He is married '.format(person['first_name'],person['last_name'],person['country']))
