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
# n_people = int(input("How many people do you want to add: ")) #Get input about number
# freinds = [] # Create an empty list to hold the people
#
# for i in range(n_people): #Loop through however many people we said we wanted to add
#     new_freind = input("Who do you want to add: ")
#     freinds.append(new_freind)
#
# print(freinds)




## This example generates n random numbers between 1 and 365 and puts them into a list
# import random
# number_lst = []
# n = 21
#
# for i in range(n):
#     number = random.randint(1,365)
#     number_lst.append(number)
#
# print(number_lst)
#
#

## By converting to a 'set' data type we can see if there are any duplicates (like for the birthday problem)
# number_set = set(number_lst)
# print(number_set)
# print(len(number_lst))
# print(len(number_set))



##Slide 10 - Skill Review for exercise 5.1 - Stopping a loop when the 'enter' key is pressed.
# while True:
#     data = input("Enter some data: ")
#     if data == '':
#         break

# l = [1.3, 5.5, 7.3] # some list of numbers
# Find the sum of the list above
# l_sum = sum(l)
# print(l_sum)


#Slide 12 - Different operations and list slicing techniques that are possible
first = [1,2,3,4,5,6]
# first_modified = first[2:4] # returns second and third element as a new list (not the fourth)
# print(first_modified)



## Searching through a list
# print(1 in first)# find an element in a list, TRUE
# print('1' in first)# FALSE
# print(int('1') in first) # TRUE

## SKIP FOR NOW Equality vs equivalency of data:
# second = list(range(1,5))
# print(second)

pass #True because elements are not the same
pass #False because not the same place in memory


## Setting a new list equal to a previous list manipulates both lists




## Application: Searching through names in a database
# import random
#
names = ["Cenard Bennett", "Javier Bustillos", "Antonio Cruz", "Jezter Fernandez", "Keagan Harms",
         "Kemish Hernandez", "Aaron Martinez", "Troy McMullin", "William Miller", "Alfredo Ramirez",
         "Austin Randle", "Brysan Sprowls", "Tradon Valdez"
         ]
#
# random_student = random.choice(names) # Choose a random student
# print(random_student)
#
# print('Bob' in names) # False
#
# print(f'{random.randint(-10,10)} Fake extra credit point goes to {random_student}')


##Slide 13 - Changing elements in a list
# first = [1,2,3,4]
# first[0] = 10
# first[3] = 67
# # first[4] = 'Erorr' # ERROR
# print(first)
#
# names[0] = "George Washington"
# print(names)


##Slide 14 - Manipulating through looping
# numbers = [2,3,4,5]
# for i in range(len(numbers)): # Looping using the index of the list
#     numbers[i] = numbers[i] ** 2
# print(numbers)


# Looping using the elements of the list to build a new list
# new_list = []
# for n in numbers:
#     new_list.append(n**2)
# print(new_list)


## Loop in order to manipulate each string element
# sentence = "Python is a good beginner programming language"
# sentence = sentence.split() # Split into individual words and make a list
# print(sentence)
# print(len(sentence))
#
# for i in range(len(sentence)): #Loop through each element in the list of string by index
#     sentence[i] = sentence[i].upper() #Change each word to upper case and save it into the same position
# print(sentence)


## Slide 15 - adding elements by index, without replacing data
# print(names)
# print(names[0])
# names[0] = "Bob"
# print(names)

# names.insert(1, "Spongebob")
# print(names)

# new_students = ["Larry", "Curly", "Moe"]
# names.extend(new_students)
# print(names)
#
# more_ppl = ['A', 'B', 'C']
# names = names + more_ppl
# print(names)

##Slide 16 - removing elements
# names.pop()
# print(names)
#
# item = names.pop()
# print(names)
# print(item)
#
# another_item = names.pop(1)
# print(names)
# print(another_item)


## Remove an element using its name by first finding its position (index)
# some_person = names.index("Javier Bustillos")
# print(some_person)


# --- To prevent an index error if the element is not found, we can write a conditional:
# person = "Javier Bustillos"
# if person in names:
#     person_index = names.index(person)
#     print(person_index)
# else:
#     print(f"{person} is not in the list")



## Slide 18 practice exercise - IN CLASS
# from random import randint
# print(randint(0,1))
#
#
# lst = []
# for i in range(10):
#     lst.append(randint(0,1))
# print(lst)
#
# lst2 = []
# for i in range(len(lst)):
#     if lst[i] == 1:
#         lst2.append("valid")
#     else:
#         lst2.append(lst[i])
# print(lst2)

##Slide 20 - searching and sorting
## Building a list from conditions in another list (keep numbers greater than 15 in a new list)
# from random import randint
#
# lst = []
# for i in range(20):
#     lst.append(randint(1,20))
# print(lst)

# lst2 = [] # Only numbers greater than 15 from first list go here
# for number in lst:
#     if number > 15:
#         lst2.append(number)
#
# print(lst2)




## Slide 21
##Given a list of 20 random integers between 1 and 20, create a new list of all integers that appear more than once.
# from random import randint
# lst = []
# for i in range(20):
#     lst.append(randint(1,20))
# print(lst)

# delete_me = [1,1, 2, 'hi', 'hi']
# print(delete_me.count('hi'))

# lst2 = []
# for number in lst:
#     if lst.count(number) > 1:
#         if number not in lst2:
#             lst2.append(number)
# print(lst2)



##Given TWO lists of random numbers between 1 and 20 create a new list that has the common elements of both lists
# from random import randint
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
# print(lst2)
#
# common_lst = []
# for number in lst:
#     if number in lst2: # Check if that number is also in the second list
#         common_lst.append(number)
# print(common_lst)

# --- SKIP THIS PART
pass # prevents double counting the same element (unless the same element appears multiple times on both lists)




#Slide 22 - Sorting a list - NOTICE how sort() vs. sorted() behave HERE
lst = [4,10,2,1,7]

# Using Sort()
# lst.sort()
# print(lst)
#
# lst.sort(reverse=True)
# print(lst)
#
# letters = ['cat', 'caa', 'h', 'b', 'A', 'M', 'B', 'a']
# letters.sort()
# print(letters)


# --- Using Sorted()
lst2 = [4,10,2,1,7]

# new_lst2 = sorted(lst2) # This returns the list sorted in numeric order
# print(lst2) # Notice that this returns the original list - not the sorted one
#
# print(new_lst2) # This gives us the correct sorted list



##Slide 24 - Intro to Tuples
# cards = () #Empty tuple container
# print(type(cards))
#
# cards = (2,3,4,5,'Jack') #Tuples of card ranks
# card_full_tuple = ((2, 'hearts'), ('Ace', 'Spades'))#Tuple of tuples
# card_full_list = ([2, 'hearts'], ['Ace', 'Spades']) #Tuple of lists


# Get element info from a tuple (similar to lists and string)
# print(cards[0]) # Prints 2
# print(card_full_tuple[0][1]) # Prints Hearts



# --- Demonstrates you can't modify a tuple like you can a list, unless you run the line above
# cards[0] = 'Ace'
# card_full_list[0][1] = 'Diamonds'
# print(card_full_list)


##SLide 26
### Application: Building a deck of cards by combining tuples
# import random
#
# suit_tuple = ('hearts', 'diamomds', 'spades', 'clubs')
# rank_tuple = ('2', '3', '4', '5', '6', '7', '8','9', '10', 'jack', 'queen', 'king', 'ace')
#
# deck = []
# for suit in suit_tuple:
#     for rank in rank_tuple:
#
#         card = (rank, suit)#Temporary variable to store the current card in loop
#         print(card)# Show the card for debugging
#         deck.append(card) # Add this card to the deck list
# print(deck)
#
# random.shuffle(deck)
# print(deck)
#
# draw_card = random.choice(deck)
# print(draw_card)
#
# card_index = deck.index(draw_card)
# print(card_index)
#
# deck.pop(card_index) # remove the card you drew from the deck
#
# first_card = deck[0]
# print(first_card)

##Slide 27 (IN_CLASS_TUPLE PRACTICE - point slope form)
"""
Given two ordered pairs as tuples, write a script that:
    1) unpacks them into individual variables such as x1, x2, y1, and y2
    2) Calculates the slope of the line containing those points
"""
# p1 = (2,6)
# p2 = (9,1)
#
# x1 = p1[0]
# y1 = p1[1]
#
# x2 = p2[0]
# y2 = p2[1]
#
# slope = (y2-y1)/(x2-x1)
# print(slope)
# print(round(slope,2))
# print(f"{x2-x1}/{y2-y1}")
#

##Slide 29
# #Defining a simple function
# def greeting():
#     print("Hi Everyone")

# greeting() # Need parenthesis to trigger the function


# def greeting():
#     print("I am a function")
#     return "Hi Everyone"
#
# result = greeting() # Call greeting() and store the output as a variable
# print(result)



##Slide 31
##Pass arguments into a function (no limit on amount or data type)
# first name and last name are considered POSITIONAL arguments
# def greeting(name):
#     name = name + ' Dole'
#     return f'Hi {name}'

# Pass the corresponding parameters into the function
# result = greeting("Bob")
# print(result)

# greeting()# If you call a function that expects parameters but does not get them, you get an ERROR

# def greeting(first_name, last_name):
#     return f'Call me {last_name}, {first_name}, {last_name}'
#
# result = greeting('James', 'Bond') # POSITIONAL PARAMETERS
# print(result)

##Slide 32
##Pass default values into a function (order of keyword parameters vs. positional parameters matters!)
## positional parameters need to be defines FIRST!
# def greeting(first_name = 'James', last_name = 'Bond'): # These are KEYWORD Parameters
#     return f'Call me {last_name}, {first_name}, {last_name}'


# Returns the default parameters
# result = greeting()
# print(result)

# Returns name as "James" instead of 'John'
# result = greeting("Bob")
# print(result)

# result2 = greeting(first_name='Steve')
# print(result2)

# Returns a last name of "James" instead of "Doe"
# result3 = greeting(last_name='Doe')
# print(result3)


## Using BOTH POSITIONAL and KEYWORD
# def greeting(location, first_name = 'James', last_name = 'Bond'): # These are KEYWORD Parameters
#     location = "Great" + location
#     return f'Call me {last_name}, {first_name}, {last_name}'
#
# result4 = greeting("Britain", last_name='Doe')
# print(result4)

# ERROR because POSITIONAL comes before KEYWORD
# def greeting(first_name = 'James', last_name = 'Bond', location): # These are KEYWORD Parameters
#     location = "Great" + location
#     return f'Call me {last_name}, {first_name}, {last_name}'

# def addition(a,b):
#     return a+b
#
# n = addition(3,4)
# print(n)
#
# n2 = addition('Whats', ' up')
# print(n2)

##Try it:
"""Write a function called find_bigger that accepts two decimal numbers 
   and returns the bigger of the two"""
# def find_bigger(n1, n2):
#     if n1 > n2:
#         return n1 # Function EXITS as SOON as it sees a valid return
#
#     return n2 # Only works if the above return does not trigger
#
# compare = find_bigger(4.1, 3.6)
# print(compare)
#
#


##Slide 33
"""Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise."""
# Returns True only is a string is a valid integer
a = '3'
# print(a.isnumeric())

# def only_ints(n1, n2):
#     if str(n1).isnumeric() and str(n2).isnumeric():
#         return True
#     return False
#
# result = only_ints(1, 1.23)
# print(result)


# ##Slide 34
## Write a function that removes digits from a string and returns it back with only alphabetic characters.
#
# print('1.23'.isnumeric())
# print('1.23'.isdigit())

# def remove_digits(data):
#     new_word = ""
#     for c in data:
#         if not c.isnumeric():
#             new_word += c
#
#     return new_word
#
#
# message = input("Please enter a message: ")
# result = remove_digits(message)
# print(result)




##Slide 35
##Write a function that accepts an integer and returns the sum of its digits
number = 123
# print(number[0]) # ERROR
# number = str(number)
# print(number[0])
#
# number = list(number)
# print(number)

def sum_digits(n):
    n = list(str(n))
    total = 0
    print(n)
    for digit in n:
        total +=int(digit)
        # print(digit)

    return total

result = sum_digits(999)
print(result)



###########Extra Example
"""Write a function that takes an integer and returns all integers within a range whose sum of digits is equal to the integer passed in.
For example if 11 is passed in then 29,38,47,etc.. are returned because 2+9=11, 3+8=11, etc..."""