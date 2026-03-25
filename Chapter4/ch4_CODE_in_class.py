# #Slide 3 - String from characters demo
# string = "How are you today"
# for char in string:
#     print(char)


## This will give an ERROR because an integer is not ITERABLE
# n = 123
# for digit in n:
#     print(digit)


#Slide 4 - exploring string indexes
name = 'Skywalker'
# print(name[0]) #The first letter is 'S'
# print(name[6])
#
# print(len(name))
#
# # print(name[9]) #Results in an index error because last index is at [8]
# print(name[8]) # The last letter
# print(name[len(name) - 1]) # ALSO the last letter
#
# print(name[-1]) # last character is 'r'
# print(name[-2]) #  Second to last character is 'e'


##Slide 5
data = 'Hi there, how are you!'
## Loop Through the indexes of the string (these are numbers)
# for char in range(len(data)):
    # print(char) # Displays the loop count
    # print(data[char]) # Display the letter at the index

## Loop through the elements of the string
# for char in data:
#     print(char) # Displays the charcter from the string


### YOUR TURN
# song = 'Harmony Hall'
# print(song[1])
# print(len(song))
#
# for i in range(len(song)):
#     print(song[i], end = ':)')
#
# for char in song:
#     print(char)
#
# print(song.upper()) # Makes everything


##Slide 7 - Mutable vs. Immutable Data
# mutable = ['G', 'O', 'O', 'D']
# print(mutable[0])
# mutable[0] = 'H'
# print(mutable)




# immutable = 'Good'
# print(immutable[0]) # First letter G
# # immutable[0] = 'H' # Can't change the 'G' to 'H'
#
# immutable = 'Hood' # This is okay



##Slide 9 - string slicing
name = 'myfile.txt'
# print(name[0:]) # full string
# print(name[0:1]) # Only the first character
# print(name[0:2]) # First two characters
# print(name[2:6]) # Character 2 to 5
# print(name[:2]) # This is the same as name[0:2]

# print(name[-3:-1]) # Start at third to last and go to last
# print(name[0::2]) # Start at the beginning and go every other letter


# print(name[100]) #ERROR
# print(name[0:100]) # This is okay
# print(name[-3:-1] + name[2:5]) # Last three characters combined with the character 2 to 5



##Slide 9 - Try to run your own experiments with the string below
my_string = "Give a man a program, frustrate him for a day. " \
            "Teach a man to program, frustrate him for a lifetime."



##Slide 10 - Your turn - Move Two Letters
# message = input("Please enter a word: ")
# print(message[-2:] + message[:-2])



##Slide 11 - String Methods
# superhero = 'incredible HULK'
# all_upper = superhero.upper()
# print(all_upper)
#
# print(superhero.lower())
#
# print("how is your day today".title())
# print(superhero.casefold()) # Ignores case sensitivity
# print(superhero.split())



##Slide 12 - More String Methods
address = '123 Fake St'
greeting = 'hello'
#
# print(address.islower()) # False beause not all character are lowercase
# print(greeting.islower()) # True
#
# print(address.isalnum()) # False
# print(address.isascii()) # True

# Check which characters are digits
# for char in address:
#     print(char, char.isdigit())


# for char in address:
#     print(char, char.islower())


# for char in address:


## IN_CLASS PRACTICE
message = input("Please enter a string: ")
lower_case_count = 0
only_uppercase = ""

for char in message:
    if char.islower():
        lower_case_count +=1
    if char.isupper():
        only_uppercase = only_uppercase + char

print(f"There are {lower_case_count} lower case letters")
print(only_uppercase)

##Slide 13 . Even more string methods
##Map a directory of files by using the split command
# string = "C:\\Users\\yuriy.drubinskiy\OneDrive - Garden City Community College\\Python Class\\Powerpoints and notes"



pass # Combining back into a single string


##Slide 13/14 - STRING METHODS SUMMARY
####Commands that let you access and see info about what string methods do
# greeting = 'hello'
# print(dir(greeting)) # A list of available methods for the 'string' object
# print(help(str)) # A more detailed description of each available method




##Slide 15 - Testing string logic with 'in'
# text = """A long time ago in a galaxy far far away..
# It is a period of civil war.
# Rebel spaceships, striking
# from a hidden base, have won
# their first victory against
# the evil Galactic Empire."""
#
pass #True
pass # False
pass #TRUE because Ignores case-sensitivity in the string


pass # show all charaters from character 60 to character 69
pass #Since war first appears at character 67, we can see what characters 60-69 are



##Slide 16
## The variable below defines a list data structure. We will lean more about this in chapter 5
# fileList = ['myfile.txt', 'myprogram.exe', 'yourfile.txt', 'dont_open.txt']




##Slide 17 - mini task; counting letters







#Slide 21 - Writing Text to a File





## In class practice
"""
Create a text file using Python.

 Write about how cool your programming instructor is…
(or any other text you want) 

"""


#Slide 23 - Writing Numbers to a File





##Slide 24 - Reading Text from a File



## Since the text file is broken up into lines, readline() adds an extra carrige return (\n)
## This is useful if you are searching for a specific line or need to take some action based on the contents of a line
pass #As long as there's data to read, read it



##Slide 25 - Reading Numbers from a File