# Exercises: Level 1
# Create an empty tuple
empty_tuple = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
irmaos = ('La','bu','bu')
irmas = ('Vanessa','Care')
# Join brothers and sisters tuples and assign it to siblings
todos_os_irmaos = irmaos + irmas
# How many siblings do you have?
print(len(todos_os_irmaos))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
todos_os_irmaos = list(todos_os_irmaos)
todos_os_irmaos.append('laa')
todos_os_irmaos.append('bubbububu')
family = todos_os_irmaos
family = tuple(family)
print(family)

# Exercises: Level 2
# Unpack siblings and parents from family_members
irmãos, pais = family[0:5],family[5:]
print(irmãos)
print(pais)
# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Leite', 'Queijo')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_tp)//2
item_do_meio = food_stuff_tp[middle]
# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt = food_stuff_lt[3:]
print(food_stuff_lt)
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)



