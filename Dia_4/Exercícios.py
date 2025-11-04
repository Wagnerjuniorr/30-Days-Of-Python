#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
#3. Declare a variable named company and assign it to an initial value "Coding For All".
#4. Print the variable company using _print()_.
#5. Print the length of the company string using _len()_ method and _print()_.
#6. Change all the characters to uppercase letters using _upper()_ method.
#7. Change all the characters to lowercase letters using _lower()_ method.
#8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
#9. Cut(slice) out the first word of _Coding For All_ string.
#10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
#11. Replace the word coding in the string 'Coding For All' to Python.
#12. Change Python for Everyone to Python for All using the replace method or other methods.
#13. Split the string 'Coding For All' using space as the separator (split()) .
#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
#15. What is the character at index 0 in the string _Coding For All_.
#16. What is the last index of the string _Coding For All_.
#17. What character is at index 10 in "Coding For All" string.
#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
#19. Create an acronym or an abbreviation for the name 'Coding For All'.
#20. Use index to determine the position of the first occurrence of C in Coding For All.
#21. Use index to determine the position of the first occurrence of F in Coding For All.
#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#28. Does '\'Coding For All' start with a substring _Coding_?
#29. Does 'Coding For All' end with a substring _coding_?
#30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
#31. Which one of the following variables return True when we use the method isidentifier():
#    - 30DaysOfPython
#    - thirty_days_of_python
#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
#33. Use the new line escape sequence to separate the following sentences.
#    ```py
#    I am enjoying this challenge.
#    I just wonder what is next.
#    ```
#34. Use a tab escape sequence to write the following lines.
#    ```py
#    Name      Age     Country   City
#    Asabeneh  250     Finland   Helsinki
#    ```
#35. Use the string formatting method to display the following:
#
#```sh
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
#```
#
#36. Make the following using string formatting methods:
#
#```sh
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
#```


concatened_string = 'Thirty'+ ' ' + 'Days' + ' ' + 'of' + ' ' + 'Python'
print(concatened_string)
concatened_string = 'Coding' + ' ' + 'for' + ' ' + 'all'
print(concatened_string)
company = 'company'
concatened_string = concatened_string + ' ' + company
print(concatened_string)
print(company)
print(len(company))
print(company.swapcase())
print(company.swapcase())
concatened_string = 'Coding' + ' ' + 'for' + ' ' + 'all'
print(concatened_string.capitalize())
print(concatened_string.title())
print(concatened_string.swapcase())
without_the_first_letter = concatened_string[7:]
print(without_the_first_letter)
print(concatened_string.find('Coding'))
concatened_string = concatened_string.replace('Coding', 'Python')
print(concatened_string.replace('all','everyone'))
concatened_string = 'Coding '  + 'for '+ 'all'
print(concatened_string)
print(concatened_string.split(' '))
big_techs = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(big_techs.split(','))
print(concatened_string[0])
print(concatened_string[-1])
print(concatened_string[10])
acronym = 'PFE'
acronym = 'CFE'
print(concatened_string.find('C'))
print(concatened_string.find('F'))
print(concatened_string.rfind('i'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))
sentece = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace(' because because because', ''))
print(sentence.find('because'))
substring = 'Coding'
print(concatened_string.startswith(substring))
print(concatened_string.endswith(substring))
DaysOfPython = '30DaysOfPython'
thirty_days_of_python = 'thirty_days_of_python'
print(DaysOfPython.isidentifier())
print(thirty_days_of_python.isidentifier())
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libraries_with_hash = '#'.join(libraries)
print(libraries_with_hash)
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\tAsabeneh\t250\tFinland\tHelsinki')
radius = 10
print('radius = {}'.format(radius))
print('area = {} * {} ** {}'.format(3.14,radius,2))
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with radius %d is %.2f meters square.' %(radius, area)
print(formated_string)
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {:.2f}'.format(a, b, a/b))
print('{} % {} = {}'.format(a, b, a%b))
print('{} // {} = {}'.format(a, b, a//b))
print('{} ** {} = {}'.format(a, b, a**b))

