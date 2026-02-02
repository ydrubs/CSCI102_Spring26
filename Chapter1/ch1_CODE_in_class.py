### Slide 5 - Simple Hello World Program
# greeting = "Good morning!"
# print(greeting)
#
# print(id(greeting)) # Where does var live in memory

###Slide 15 - Data types
# hello = "hello" # String
# print(type(hello))
#
# a = 67 # int
# print(type(a))
#
# b = 1.0
# print(type(b))
#
# c = True
# print(type(c))

# d = "5"
# print(type(d))
# print(d)
#
# f = int(d) # converts the string '5' to an integer 5
# print(type(f))


###Slide 17 - Getting Input
# name = input("Enter your name, please: ")
# print("hi", name)

# a = input("Enter the first number: ") # Inputs are ALWAYS strings
# b = input("Enter the second number: ")
#
# results = a + b
# print(results)

# re-cast to an int
# a = int(a)
# b = int(b)
# print(a + b)
#
# c = float(b)
# print(c)
# print(a + c)


##Slide 18 Activity

####Slide 19 Recasting Input
# age = int(input("Enter your age: "))
# next_year = age + 1
# print("You will be "  + str(next_year) + " years old next year.") # One ful string
# print("You are", age, "years old") # Three separate pieces of data
#

###Slide 22 Outputting multiple data
# x = 'Hi'
# y = 5
# z = True
#
# print("data:" , x, y, z) # Using commas to seperate data
# print(x + str(y) + str(z)) # Using + to concatenate data into one string
# print(f"The data is {x}, {y**2}, {z}") # Using f-strings



###Slide 23 Operations
x = 99
y = 100

print(x + y) # Addtion
print(x - y) #
print(x * y) #

print(x/y) # Regular division, always a FLOAT
print(x//y) # Quotient division


##Slide 28
##Run-Time error - Program stops execution when it encounters an error
# length = int(input("Enter the length: "))
# print(legnth) # Stops execution HERE

# a = '5'
# print(int(a)) # THIS is OKAY
#
# b = 'five'
# print(int(b))

# c = 0/5
# print(c)
#
# d = 5/0
# print(d)

##Syntax Error - Program does not execute at all
# length = int(input("Enter the length: "))
# print{legnth} # SYNTAX ERROR Here
#  print("hello") # Extra space


##Sementic Error
# length = int(input("Enter the length: "))
# print("The area of the square is ", 2*length)


# ##Slide 29
# print("Hello")
#
#
# a = 2
# b = 3
# print(a +)


##Slide 30
##Traceback
# def say(name):
#     print('Hello, ' + nam)
# #
# say('Michael')