# Exercises: Level 1
# Find the length of the set it_companies
it_companies = {'Google', 'Meta','Tesla','Nvidia'}
print(len(it_companies))
# a.dd 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Oracle','Amazon'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)
# What is the difference between remove and discard
it_companies.discard('daawdadaw')
# discard does not return and error if the item does not exist in the list

# Exercises: Level 2
# Join A and B
A = {1,2,3,4,5}
B = {6,7,8,9,10}
print(A.union(B))
# Find A intersection B
A = {1,2,3,4,5}
B = {5,6,7,8,9,10}
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
A = {1,2,3,4,5}
B = {6,7,8,9,10}
print(A.isdisjoint(B))
# Join A with B and B with A
A = {1,2,3,4,5}
B = {6,7,8,9,10}
print(B.union(A))
A = {1,2,3,4,5}
B = {6,7,8,9,10}
print(A.union(B))
# What is the symmetric difference between A and B
A = {1,2,3,4,5}
B = {6,7,8,9,10}
print(A.symmetric_difference(B))
# Delete the sets completely
del(A)
del(B)

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, 
# which one is bigger?
age_lst = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age_lst)
print(len(age_set))
print(len(age_lst))
# Explain the difference between the following data types: string, list, tuple and set
# string are a sequence of characters used to represent text
# List are a sequence of any type of variable that can be muttable 
# Tuple are a sequence of any type of variable that can not be muttable
# set are a unored sequence of any type of variable that can mutable but are unique

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
print(len(sentence.split()))
print(len(set(sentence.split())))