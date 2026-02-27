##Slide 5 - One way selection statement
# name = input("Enter you name, please: ")
# if name == 'admin':
#     print("Access granted")
#
# print("Hello eveyone")


#Slide 6 - If/else statement
# name = input("Enter you name, please: ")
# if name == 'admin' or name == 'Liam':
#     print("Access granted")
#
# else:
#     print("Wrong credentials")
#
# print("Hello eveyone")





##Slide 7: Multi-way selection
# number = int(input('Enter the numeric grade: '))

# if number > 89:
#     print("Good job!")
#     letter = 'A'
# elif number > 79:
#     print("Pretty good")
#     letter = 'B'
# elif number > 69:
#     print("Ok")
#     letter = 'C'
# else:
#     letter ='F'
#
# print(f'Your letter grade is {letter}')

# if number > 89:
#     print("Good job!")
#     letter = 'A'
# elif number > 79:
#     print("Pretty good")
#     letter = 'B'
# elif number > 69:
#     print("Ok")
#     letter = 'C'
# else:
#     letter ='F'
#
# print(f'Your letter grade is {letter}')




## Slide 8 ACTIVITY



##Slide 9
# x = 10
# y = 5
# z = 2

# print(x == y) # FALSE
# print(x == y + 5) # TRUE
# print(y != z) # TRUE
# print(x < 5) # FALSE
#



##Slide 11
# a = True
# b = False
#
# print(a and b) # FALSE
# print (a or b) # TRUE
# print (not a) # FALSE




# #Write your own challening logic statement, make it as long as you want
# print(a and not b or b and not a or (a and not b)) # True

# --- SKIP




##slide 12 - Evaluating Logic statements
# grade = float(input("Enter your grade: "))
#
# if grade >=90 and grade < 101:
#     print("Nice job!")
# elif grade < 90 and grade >=80:
#     print("not bad")
# else:
#     print("Unacceptable!")
#
# if grade > 90 and grade < 70:
#     print("You're on the edge of a bell curve")


## Slide 13 Activity
# valid_username = 'user123'
# is_active = False
# user = input("Enter your username, please: ")

# if user == valid_username and is_active:
#     print("access granted")
# elif user == valid_username and not is_active:
#     print("access denied")
# else:
#     print("No user found")


##Slide 16 - using a for loop
# passes = 10
# message = 'Hello'

# for eachPass in range(5):
#     print(message)

# i = 'sup'
# for i in range(100):
#     print(i, message)
#
# print(i, type(i))


## using a conditional in a for loop
# name = 'Bob'
#
# for i in range(5):
#     user = input("Enter your name: ")
#     if name == user:
#         print("Welcome")
#     else:
#         print("Go away!")


##Slide 18  - Looping through an algorithm
number = 1

# THIS IS SILLY AND INEFFICIANT
# number = number + 3
# print(number)
# number = number + 3
# print(number)
# number = number + 3
# print(number)
# number = number + 3
# print(number)
# number = number + 3
# print(number)

# passes = 10
# for i in range(passes):
#     print(number)
#     number = number + 3
#
# print(number)





##Slide 19 - Another example
# total = 1
# product = 5
# number_of_loops = 50

# for i in range(number_of_loops):
#     print(total)
#     total = total * product
# print(total)
#



##Slide 20 - Using the loop counter in the loop
# for i in range(11):
#     i = i * 2
#     print(i)
#
#
# for i in range(11):
#     i = i ** 2
#     print(i)

##Equivelant to the following but twice as long
# count = 0
#
# for i in range(11):
#     print(count)
#     count = (count + 1) ** 2
# print(count)



##Checkpoint Activity
"""
Write a for loop that counts 20 ‘Mississippis’, such as -
1 Mississippi
2 Mississippi
...
...
20 Mississippi
"""""
# for i in range(20):
#     print(i + 1, 'Mississippi')
#
# iterations = 20
# for i in range(iterations + 1):
#     print(i, 'Mississippi')





##Slide22 - Controlling the loop range
# for i in range(1,21): # Now i STARTS at 1
#     print(i)


##SLide 23 - Controlling the loop range; counting by...
## Count by threes
# for i in range(1,101,3):
#     print(i)



## Count backwards from 100
# for i in range(100, 0, -1):
#     print(i)
#

##Slide 24 - Augmented Assignment
a = 5
b = 7

# a = a + b
# print(a)

a += b # Augmented assignment is the more conventional way to reassign variables
# print(a)

a -= b
a *= b
a %=b



### FIZZ BUZZ Exercise (in-class)
# for i in range(1,101):
#
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#
#     elif i % 3 == 0:
#         print("Fizz")
#
#     elif i % 5 == 0:
#         print("Buzz")
#
#     else:
#         print(i)

## EXTRA - Looping over elements of a data set rather then a range
name = input("Enter your name, please: ")
greeting = f"Hello {name}, how is your day?"

string_length = len(greeting)
print(string_length)

# --- Loop using a counter
# for i in range(string_length):
#     print(greeting[i])

# --- Looping over a letter
# for letter in greeting:
#     print(letter)

##Slide 27 - The while Loop
""" Ask for a number and add until you hit 1000 """


pass # while loop is an entry-controlled loop





##slide 29 ACTIVITY






##Slide 30 - While Loop for entering data
# theSum = 0.0
# data = input('Enter a number or just enter to quit: ')

pass # Loop triggers if a string is not empty




##Slide 31 - Breaking a loop






##Slide 33 - While loop to validate data

pass # Runs forever (until break)




## Slide 34 - The While and the Boolean flag





## Slide 35 - Common while loop logic errors
##  Fail to break loop

# while True:
#     number = int(input('Enter the numeric grade: '))
#     if number >= 0 and number <= 100:
#         print(number)
#         # NEED TO ADD 'break'
#
#     else:
#         print('Error: grade must be between 100 and 0')


################infinite Loop, not updating variable
# a = 0
# count = 0
# while a < 1000:
#     count += 1
#     print(a, count)

###############Did not test for a = 500 condition
# a = 0
#
# while a < 1000:
#     a +=1
#     if a < 500:
#         print("Boom", a)
#     if a > 500:
#         print('Pow', a)
    ###Doesn't test a = 500


##Slide 36 - Importing Modules -> Random




pass # Don't have to reference random this way






##Slide 37
##Dice rolling simulator - generate 10 random numbers between 1 and 6





## Guess the number game