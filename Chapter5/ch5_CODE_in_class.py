##Slide 5 - Defining lists

fruits = ['apples', 'oranges', 'cherries'] # Three element list
profile = [24, 3.2, 'hello', True] # Lists can mix data types

coordinates = [[-3,1], [0,3]] # Lists can contain other lists
freinds = [] # Lists can be empty


# print(len(fruits)) # lists have a length
# print(profile[1]) # Lists can be indexed
# print(profile[4]) # ERROR because profile only has elements 0 to 3

# print(profile[-1]) # Last element
# print(profile[len(profile)-1]) # Also does the same thing (with more effort)
#
# print(coordinates[0][0], coordinates[0][1]) # Elements of sublists can be accessed from within a list



# --- Lists can store the result of other operation
# import math
# x= 2
# lst = [x, x+2, math.sqrt(x), 'h' + 'i']
#
# print(lst)


#Slide 6 - Your turn


##Slide 7
# --- Iterable data types can be recast as lists
my_numbers = range(100)
my_numbers = list(my_numbers)
#
# print(my_numbers)
# print(max(my_numbers)) # The biggst number in the list
# print(min(my_numbers)) # The lowest number
# print(sum(my_numbers))


## Build a list from a string
# message = 'Hello how are you?'
# message_lst = list(message)
# print(message_lst)
#
#

## Other list operations
# print(len(message_lst)) # Check the number of elements in a list
# letters = [1,2,3]
# new_lst = message_lst + letters # Combine two list swith a '+' sign
#
# print(new_lst)


#Slide 8
## This example allows you to add people to a roster by looping through the number of people that get added
n_people = int(input("How many people do you want to add: ")) #Get input about number
freinds = [] # Create an empty list to hold the people

for i in range(n_people): #Loop through however many people we said we wanted to add
    new_freind = input("Who do you want to add: ")
    freinds.append(new_freind)

print(freinds)




## This example generates n random numbers between 1 and 365 and puts them into a list




## By converting to a 'set' data type we can see if there are any duplicates (like for the birthday problem)




##Slide 10 - Skill Review for exercise 5.1 - Stopping a loop when the 'enter' key is pressed.




#Slide 12 - Different operations and list slicing techniques that are possible
pass # first = [1,2,3,4]
pass # returns second and third element as a new list (not the fourth)




## Searching through a list
# find an element in a list, TRUE
# FALSE
# TRUE
# FALSE


## Equality vs equivalency of data:
# second = list(range(1,5))
# print(second)

pass #True because elements are not the same
pass #False because not the same place in memory


## Setting a new list equal to a previous list manipulates both lists




## Application: Searching through names in a database
import random

names = ["Cenard Bennett", "Javier Bustillos", "Antonio Cruz", "Jezter Fernandez", "Keagan Harms",
         "Kemish Hernandez", "Aaron Martinez", "Troy McMullin", "William Miller", "Alfredo Ramirez",
         "Austin Randle", "Brysan Sprowls", "Tradon Valdez"
         ]

pass # Choose a random student



##Slide 13 - Changing elements in a list
# first = [1,2,3,4]




##Slide 14 - Manipulating through looping
# numbers = [2,3,4,5]
# Looping using the index of the list




# Looping using the elements of the list to build a new list



## Loop in order to manipulate each string element
pass # sentence = "Python is a good beginner programming language"
pass # Split into individual words and make a list



pass #Loop through each element in the list of string by index
    #Change each word to upper case and save it into the same position



##Slide 15 - adding elements by index, without replacing data





##Slide 16 - removing elements





## Remove an element using its name by first finding its position (index)
# some_person = csci102_Roster.index("Stephen")
# print(some_person)


# --- To prevent an index error if the element is not found, we can write a conditional:




## Slide 18 practice exercise - IN CLASS




##Slide 20 - searching and sorting
## Building a list from conditions in another list (keep numbers greater than 15 in a new list)







## Slide 21
##Given a list of 20 random integers between 1 and 20, create a new list of all integers that appear more then once.






##Given TWO lists of random numbers between 1 and 20 create a new list that has the common elements of both lists
# lst = []
# for i in range(20):
#     lst.append(randint(1,20))
# print(lst)
#
#
# lst2 = []
# for i in range(20):
#     lst2.append(randint(1,20))
#
# print(lst)
# print(lst2)


pass # prevents double counting the same element (unless the same element appears multiple times on both lists)




##Slide 22 - Sorting a list - NOTICE how sort() vs. sorted() behave HERE
# lst = [4,10,2,1,7]

# Using Sort()



# letters = ['c', 'h', 'b', 'A', 'M', 'B']



# --- Using Sorted()
# lst2 = [4,10,2,1,7]

pass # This returns the list sorted in numeric order
pass # Notice that this returns the original list - not the sorted one

pass # This gives us the correct sorted list



##Slide 24 - Intro to Tuples
pass #Empty tuple container

#Tuples of card ranks
#Tuple of tuples
#Tuple of lists


# Get element info from a tiple (similar to lists and string)



# --- Demonstrates you can't modify a tuple like you can a list, unless you run the line above
pass

pass # If we change the cards tuple to a list we can manipulate elements


# Since the third element [2] in the first tuple is a list, it can be modified. We are not modifying the tuple itself



##SLide 26
### Application: Building a deck of cards by combining tuples
import random

# suit_tuple = ('hearts', 'diamomds', 'spades', 'clubs')
# rank_tuple = ('2', '3', '4', '5', '6', '7', '8','9', '10', 'jack', 'queen', 'king', 'ace')

# deck = []

        #Temporary variable to store the current card in loop
        # Show the card for debugging
        # Add this card to the deck list




##Slide 27 (IN_CLASS_TUPLE PRACTICE - point slope form)
"""
Given two ordered pairs as tuples, write a script that:
    1) unpacks them into individual variables such as x1, x2, y1, and y2
    2) Calculates the slope of the line containing those points
"""
p1 = (2,6)
p2 = (9,1)




##Slide 29
##Defining a simple function



# Need parenthesis to trigger the function



##Slide 31
##Pass arguments into a function (no limit on amount or data type)
# first name and last name are considered POSITIONAL arguments


# Pass the corresponding parameters into the function


# If you call a function that expects parameters but does not get them, you get an ERROR





##Slide 32
##Pass default values into a function (order of keyword parameters vs. positional parameters matters!)
## positional parameters need to be defines FIRST!

# These are KEYWORD Parameters


# Returns the default parameters


# Returns name as "James" instead of 'John'


# Returns a last name of "James" instead of "Doe"


# Without a parameter name they take the value based on the order (position) they are declared




## Using BOTH POSITIONAL and KEYWORD




# ERROR because POSITIONAL comes before KEYWORD



##Try it:
"""Write a function called find_bigger that accepts two decimal number and returns the bigger of the two"""





##Slide 33
"""Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise."""
# Returns True only is a string is a valid integer




# ##Slide 34
## Write a function that removes digits from a string and returns it back with only alphabetic characters.





##Slide 35
##Write a function that accepts an integer and returns the sum of its digits





###########Extra Example
"""Write a function that takes an integer and returns all integers within a range whose sum of digits is equal to the integer passed in.
For example if 11 is passed in then 29,38,47,etc.. are returned because 2+9=11, 3+8=11, etc..."""