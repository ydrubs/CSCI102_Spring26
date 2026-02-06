"""
This is example code for Chapter 2
This is code we did in class
"""

##Slide 2 - Example of comments and docstrings

# --- demo of an in-line comment
age = 115 # age of the oldest ever living person


"""Sometimes there is a need to explain or document a portrion of code beyond one line.
For this we can use a docstring to extend to multiple lines.
Docstrings are also used to attribute programs and explain functions."""

# --- Slide 4 - code literals - how data types are represented to the programming language
# a = 4
# b = '4'
# print(a,b)
# print(a + a, b + b, str(a) + str(int(b)))


##Slide 5 - place value representation
# liams_number = 84,000
# print(liams_number)
#
# print(1,234) # This prints two separate pieces of data
#
# liams_number_part2 = 848_120_000
# print(liams_number_part2)



##Slide 7 - String literals
# print("that's") # use double quotes of a single quote is part of the string

# --  Often the choice of single or double quote does not matter
# print("A double quoted string")
# print('does the same thing as a single quoted string')

# -- Perhaps an exception
# print('However, there\'ll be times when a string needs to include a single quote within it, so a double quote is useful')


## Multiline strings look similar to docstrings
# welcomeText = '''Welcome to my game!
#
# I will think of a number from 1 to 100, and you must try
# to guess it. I'll tell you if your guess is too small
# or too large.
#
#
#         # Enter an integer between 1 and 100 when prompted.'''
#
#
# print(welcomeText)


##Slide 8 - Escape characters
# print('Hello. How are you?')
# #
# print("1. hello " + 'there') #Substitute one of the escape chars for the '#'
# print("2. hello\b " + ' there')
# print("3. hello\n " + '  there')
# print("4. hello\t " + ' there')
# print("5. hello\\" + ' there')
# print("6. hello\'"" " + ' there')
# print("7.hello\"" + ' there')




##Slide 10 - End of line arguments
# print("Hello")# Drops to new line
# print("there")
#
# seperator = ' --#-- '
# print('hello', end = seperator)
# print('there')




##Slide 11 - separator arguments
# name = 'Yoda'
# age = 900
# home_planet = 'Dagobah'
#
# ## using sep
# print(name, age, home_planet)
# print(name, age, home_planet, sep = ', ')
# print(name, age, home_planet, sep = ' *** ')
#
# ##  combine sep and end
# print(name, age, home_planet, sep=", ", end=' :) ')
# print("The End")

## Acvivity - sep and end
# Add to the command below in order to have each color appear on a seperate line
# print('red', 'green', 'blue', sep='\n')


# Reformat the following to have them show up on the same line seperated by a '%' character
# print('red', end='%')
# print('blue', end='%')
# print('green')

this_is_my_super_freindly_greeting_to_you = 'hello'

carType = 'Sedan'

car_type = 'Sedan'


###Activity from slide 13
## Three valid Variables
# HITHERE = 'Hello'
# hiThere = 'Hello'
# hi_th0re = 'Hello'
# hi_there = 'hello' # most conventional

## Three Invalid variables
# 1hi_there = 'hello'
# if = 'hello'
# hi! = 'Hello'


##Slide 14 - variable assignment through concatenation
# first_name = "Obi-Wan"
# last_name = "Kenobi"
#
# print(f"Hi I am {first_name} {last_name}")
#
# full_name = first_name + ' ' + last_name
# print(f"Hi I am {full_name}")


## Reassigning Variables to new values
# x = 125
# y = x / 5   # y defined in terms of x
# print(x,y)


# x = 100   # redefining x
# print(x, y)



# y = 2 * y   # redefining y by modifying
# print(x, y)


##Slide 15 - Review Concatenation vs. comma seperation
# first_name = "Yuriy"
# last_name = "Drubinskiy"
#
# print(first_name + last_name) # Concatenation results in ONE SINGLE string
# print(first_name, last_name) # comma seperated arguments - two different pieces of data


## Slide 16 - The * string operation
# s1 = 'waaz'
# s2 = 'a'
# s3 = 'p'
#
# print('hello ' * 5)
# print((s1 + s2*10 + s3) * 3)


### ACTIVITY slide 17 - Write a print statement that outputs the string seen in slide 17 of the powerpoint
# print(('^' * 10 + '\n') + (('#' * 10 + '\n')*3) + ('^' * 10 + '\n'))


##Slide 18 - Examples of math operations
# print(4 ** 2)  #Exponents
# print(9//10) # QUOTIENT - Always drops decimal
# print(9 % 2) # Modulus (mod) - Remainder
#
# print(15 % 4) # 3
#
# print(2**2**3) # NOT 32
# print(4**3)


# a = 1
pass # Increment and reassign to itself




## Slide 20 Mixed-Mode Arithmetic
a = 6
b = 3
print(a/b) # True division Results in a float
print(a//b) # Quotient Division rounds down to an int


c = 0.7
d = 0.3
print(c + d) # Addition using at least one float always results in a float

f = str(33)
print(f + str(1))




## SLide 23 rounding floats
# g = 3.4415926
#
# g1 = round(g, 0)
# print(g1)
#
# g2 = round(g, 1)
# print(g2)
#
# g3 = round(g, 2)
# print('$' + str(g3))
#



##Slide 24 - Character operations
s1 = "Mary"
s2 = "Freddy"

print(len(s1)) #Get the lenght of string s1 and s2

print(ord("M")) # Get the ASCII code of the character

# IMPORTANT SKILLS
# print(chr(67)) #Get the character from the ASCII code
# print(chr(67+1)) # The letter D
# print(ord(chr(67+1)))

# lower_to_upper = chr(int(ord('a')-32))
# print(lower_to_upper)

## Playing around with some character codes in unicode
print(chr(0x265e))
print(chr(0x250C))
print(chr(203850))
print(int(0x265e))
print(chr(9822))

# print('The ASCII code for the letter \'a\' is ' + str(ord('a')))

for i in range (100000):
    print(chr((i)), end = '\n ')