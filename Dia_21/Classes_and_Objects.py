# Python is an object oriented programming language
# Everything in python is an object, with its properties an methods
# A number, string, list, dictionary, tuple, set etc
# We create class to create an object
# A class is like an object constructor, or a "Blueprint for creating objects
# We instantiate a class to create an object
# The class defines attibutes and behavior of the object, while the object, the other hand, represents the class

# We have been working with classes and object right from the beggining of this challenge
# Every element in a python program is an object of a class
num = 10
print(type(num)) # <class 'int'>

# Creating a Class
# to create a class we need the key word class followed by the name and colon
# Class name should be CamelCase
class Person:
    pass
print(Person)

# Creating an Object
# We can create an object by calling the class
p = Person()
print(p)

# Class Constructor
# In the examples above, we have created an object from the Person class.
# However, a class without a constructor is not really useful in aplication
# Let us use constructor function to make our class useful
# Like the constructor function in Java or JavaScript, Python  has also a built-in init() constructor function
# The init constructor function has self parametes which is a reference to the current instance of the class 
class Person:
    def __init__(self, name):
        # self allow to attach parameter to the class
        self.name = name
p = Person('Asabeneh')
print(p.name)
print(p)

# Let add more parameters do the constructor
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
p = Person('wagner', 'moreira',69, 'br','bsb')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

# Objects Methods
# Objectcs can have  methods. The methods are functionas wich belonh to the object
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname}{self.lastname} is {self.age} years old. Ge lives in {self.city}, {self.country}'
p = Person('wagner', 'moreira',69, 'br','bsb') # eu tive que declarar p novamente
print(p.person_info())

# Object Default Methods
# Sometimes, you may want to have a dedfault value sfor your object methods
# If we give default values for the parameters in the constructor, we can avoid errors when we call our class without parametes
class Person:
    def __init__(self, firstname = 'wagner', lastname='moreira',age=69, country='br',city= 'bsb'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
p1 = Person()
print(p1.person_info())
p2 = Person('RATATA','BLA',2121,'OOOO','AA')
print(p2.person_info())

# Method to Modify Class Default Values
# In the example below, the person class, all the constructor parameters have deafult values
# In addition to that, we havve skills parameter, which we can access using a method
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self,skill):
          self.skills.append(skill)
p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p2 = Person('RATATA','BLA',2121,'OOOO','AA')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# Inheritance
# Using inheritance we can reuse parent class code
# Inheritance allows to define a class that inherits all the methods and propoerties from parent clas
# The parent class or super or base class is the class which fives all the methods and properties
# Child class is the class tha inherits from another or parent class
class Student(Person):
    pass
s1 = Student('Eyob','Yetayeh',30,'Finland','Helsinki')
# Memsmo sem adicionar nada na classe student, eu consegui criar alunos
# Isso porque o python foi buscar o "molde"(o constructor __init__) la na classe pai(Persond)
s2 = Student('Lidiya','Teklemariam',28,'Finland','Espoo')
# Quando eu chamo o método person_info o python percebe que student n tem esse método, então ele sobe um nível
print(s1.person_info())
s1.add_skill('JavaScript')
print(s1.skills)

print(s2.person_info())
s2.add_skill('IDK')
s2.add_skill('MARKETING')
print(s2.skills)
# We did not call the init() constructor in the child class
# if we didnt call it when we can still access all the properties from the parent
# but if we do call the constructor we can access the parent properties by calling super
# we can add a new method to the child or we can overide the parent class methods by creating the sanme method name int the child class
# when we add the init() function, the child class will no longer inherit the parents init()function

# Se voce não crair um __init__ no filho: Ele sua o do pai automaticamente
# Se voce cirar um __init__ no filho: ele atropela(sobrescreve) o do pai. Se voce fizer isso e ainda quiser as caracteristicas do pai, precisa usar o comando super()


# Overriding parent method
class Student(Person):
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki',gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}'
s1 = Student('Roberto','alvaraz',20,'idk','idkcity','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# We can use super() built-in function or the parent name Person to automatically inherit the methods and properties from its parent
# In the example above we overrde the parent method
# The child method has a different feature
# it can identify, if the gender is male or femlae and assign the proper pronoun(he/she)