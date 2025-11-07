# ### Exercises: Level 1
# 
# 1. Declare an empty list
# 2. Declare a list with more than 5 items
# 3. Find the length of your list
# 4. Get the first item, the middle item and the last item of the list
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# 7. Print the list using _print()_
# 8. Print the number of companies in the list
# 9. Print the first, middle and last company
# 10. Print the list after modifying one of the companies
# 11. Add an IT company to it_companies
# 12. Insert an IT company in the middle of the companies list
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
# 14. Join the it_companies with a string '#;&nbsp; '
# 15. Check if a certain company exists in the it_companies list.
# 16. Sort the list using sort() method
# 17. Reverse the list in descending order using reverse() method
# 18. Slice out the first 3 companies from the list
# 19. Slice out the last 3 companies from the list
# 20. Slice out the middle IT company or companies from the list
# 21. Remove the first IT company from the list
# 22. Remove the middle IT company or companies from the list
# 23. Remove the last IT company from the list
# 24. Remove all IT companies from the list
# 25. Destroy the IT companies list
# 26. Join the following lists:
# 
#     ```py
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
#     ```
# 
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
# 
# ### Exercises: Level 2
# 
# 1. The following is a list of 10 students ages:
# 
# ```sh
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ```
# 
# - Sort the list and find the min and max age
# - Add the min age and the max age again to the list
# - Find the median age (one middle item or two middle items divided by two)
# - Find the average age (sum of all items divided by their number )
# - Find the range of the ages (max minus min)
# - Compare the value of (min - average) and (max - average), use _abs()_ method
# 
# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

#Declare an empty list
empty_list = []
print(empty_list)
#Declare a list with more than 5 items
items = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']
#Find the length of your list
print(len(items))
#Get the first item, the middle item and the last item of the list
item_zero = items[0]
item_middle = items[4]
item_last = items[len(items)-1]
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Wagner', 20, 175, 'alone?','bla bla bla']
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple','IBM','Oracle','Amazon']
#Print the list using print()
print(it_companies)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
print(it_companies[0])
print(it_companies[4])
print(it_companies[len(it_companies)- 1])
#Print the list after modifying one of the companies
it_companies[0] = 'Ceub'
print(it_companies)
#Ad_d an IT company to it_companies
it_companies.append('Meta')
#Insert an IT company in the middle of the companies list
it_companies.insert(2,'Flamengo')
#Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())
#Join the it_companies with a string '#;  '
it_companies_hashed = '#'.join(it_companies)
print(it_companies_hashed)
#Check if a certain company exists in the it_companies list.
does_exist = 'IBM' in it_companies
print(does_exist)
#Sort the list using sort() method
it_companies.sort()
print(it_companies)
#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#Slice out the first 3 companies from the list
print(it_companies[3:])
#Slice out the last 3 companies from the list
print(it_companies[0:6])
#Slice out the middle IT company or companies from the list
middle = len(it_companies)//2
print(it_companies[:middle] + it_companies[middle +1:]) #list[start:end]  # start is inclusive, end is exclusive
#Remove the first IT company from the list
it_companies.remove('Oracle')
print(it_companies)
#Remove the middle IT company or companies from the list
it_companies.pop(5)
print(it_companies)
#Remove the last IT company from the list
it_companies.pop()
#Remove all IT companies from the list
it_companies.clear()
#Destroy the IT companies list
del it_companies
#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
Programming_Languages = front_end + back_end

Full_stack = Programming_Languages.copy()

Full_stack.insert(5, 'Python')
Full_stack.insert(5,'SQL')
print(Full_stack)

#Exercises: Level 2
#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
#Ad_d the min age and the max age again to the list
#Find the median age (one middle item or two middle items divided by two)
#Find the average age (sum of all items divided by their number )
#Find the range of the ages (max minus min)
#Compare the value of (min - average) and (max - average), use abs() method

ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[len(ages) -1] 
print(min_age)
print(max_age)
middle = len(ages) //2
print(ages[middle])
average =sum(ages) / len(ages)
print(average)
range_of_the_ages = ages[len(ages)-1] - ages[0]
print(range_of_the_ages)
print(abs(ages[0]- average))
print(abs(ages[len(ages) -1]-average))

#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

middle = len(countries)//2
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(middle)
first_half = countries[:96]
print(first_half)
second_half = countries[96:]
print(second_half)
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
print(countries.index('China'))
print(countries.index('Russia'))
print(countries.index('United States'))
print(countries.index('Finland'))
print(countries.index('Sweden'))
print(countries.index('Norway'))
print(countries.index('Denmark'))
China, Russia, United_States, *scandic_countries = countries[35], countries[141], countries[183], countries[59], countries[165], countries[128], countries[46],
print(China)
print(Russia)
print(United_States)
print(scandic_countries)