"""
A DICTIONARY is a Python data type that links to pieces of data together inside of curly-brackets {}
    The first piece of data is called the KEY
    The second piece of data is called the VALUE
"""

#Define a dictionary
cars = {} # Empty Dictionary we can add entries to
cars = {'Ford':"Fusion", 'Toyota': "Camry", 'Jeep':"Wrangler"} # Example dictionary of car makes and models

# We can use the .keys() and the .values() method to view the keys and values separately
print(cars.keys()) # Shows the makes
print(cars.values()) # Shows the models


# We can add to a dictionary by specifying the KEY and setting it equal to a value
cars['Chevy'] = 'Corvette'
print(cars)

# car_make = input("Enter the make of the car: ") # Create a dictionary entry from user input
# car_model = input("Enter the model of the car:")

# cars[car_make] = car_model
# print(cars)

# --- Dictionary are NOT ORDERED meaning we CAN'T use their INDEX to access them or manipulate them
# print(cars[0]) #This gives an Error because we can't use indexes
# print[0] = 'Fiat' # This ALSO gives an error, need to use KEY to create a dictionary element
print(cars['Ford']) # This is okay because we reference a key


# --- Create a dictionary using a loop
for i in range(2):
    cars["Mercedes"] = 'Benz'
    cars["Alpha"] = "Romeo"
print(cars)

# --- Loop through only keys:
for key in cars.keys():
    print(key)

# --- Loop through both keys and values:
key_lst = []
value_lst = []

for key, value in cars.items(): # Looks at BOTH keys and values
    key_lst.append(key)
    value_lst.append(value)

print(key_lst)
print(value_lst)


# Dictionaries KEYS have to be UNIQUE, otherwise, the LAST entry will overwrite the previous similar one
cars['Ford'] = 'F150' # Replaces another Ford model with F150
print(cars)

cars['Ford'] = ['F150', 'Fusion', 'Mustang']
print(cars)

print(cars['Ford'][0]) # Gives F150



# We can perform operations on dictionary keys as long as we are using compatible data types:
# d = {'a': 13, 'b': 7, 'c' : 12}
# print(sum(d.values())) # Add up all the values
# print(sum(d.keys())) # Error because can't add strings

# --- in-class Practice 1
"""
1)Create a dictionary of states and their capital cities that includes:
          1) Kansas – Topeka 2) Texas – Austin 3) Arkansas – Little Rock

2) Write a line of code that accesses and prints only capital cities in the above dictionary
2b) Add the state Nebraska and its capital Lincoln
3) Write a for loop that converts the city in each dictionary all capital letters and print the dictionary
"""
# 1
places = {'Kansas': "Topeka", "Texas": 'Austin', "Arkansas": 'Little Rock'}

#2a
print(places.values())

#2b
places["Nebraska"] = "Lincoln"
print(places)

#3
for state, city in places.items():
    print(state, city)
    places[state] = city.upper()

print(places)


""" 4)	Explain - Why does the following cause an error: 

    colors = {'Red': 5, 'Blue': 3}
    print(colors[0])   # Error
    
    ANSWER: Dictionary entries can't be access with an index

"""



# --- in-class Practice 2
"""
Given list l1 and list l2 below -

Create a single dictionary where the keys are the elements in list 1 and
the values are the elements in list 2
"""
# l1 = ['a', 'b', 'c']
# l2 = [1, 2, 3]

