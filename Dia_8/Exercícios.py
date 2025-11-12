# Create an empty dictionary called dog
dog = {
    'Name':'Koda',
    'Breed':'Coitado'
}
# Add name, color, breed, legs, age to the dog dictionary
dog['Color'] ='White'
dog['age']=69
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'la',
    'last_name':'bubu',
    'gender':'male',
    'age':69,
    'maritial_status':'single',
    'skills':['English','karate','Python'],
    'Country':'BRAZIL',
    'Address':{'labububuo':'lalal',
               'lalala':'bibibi'}
}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))
# Modify the skills values by adding one or two skills
student['skills'].extend(['Paito','Futebol'])
# Get the dictionary keys as a list
keys = student.keys()
print(keys)
# Get the dictionary values as a list
values = student.values()
print(values)
# Change the dictionary to a list of tuples using items() method
student = student.items()
print(student)

# Delete one of the items in the dictionary
student = dict(student)
del student['skills']
print(student.get('skills'))
# Delete one of the dictionaries
del student
