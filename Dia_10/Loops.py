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



