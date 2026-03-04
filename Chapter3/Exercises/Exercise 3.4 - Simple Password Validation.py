"""
Exercise 3.4 - Simple Password validation

Write a program that asks the user to enter a password.
    The program should continuosly ask the user for a password as long as the password is NOT 'password123'

    There is ALSO one caveat -  Every three incorrect entries, the program should ask the user "Are you sure you are not a robot":

        If the user responds with 'y' they can continue to put in the password.
        If they respond with 'n' the loop (and program) stops, you can give a funny message if you want.

    Example Input:
        Please enter a valid password: password123

    Example output:
        Access granted!

    Another example running the program:
        Please enter a valid password: password
        Incorrect password, please try again.

        Please enter a valid password: Password123
        Incorrect password, please try again.

        Please enter a valid password: I don't know
        Incorrect password, please try again.

        Are you sure you are not a robot (y or n): n
        Program terminated.

    One more example:
        Please enter a valid password: password
        Incorrect password, please try again.

        Please enter a valid password: password1
        Incorrect password, please try again.

        Please enter a valid password: password12
        Incorrect password, please try again.

        Are you sure you are not a robot (y or n): y

        Please enter a valid password: password123
        Access granted!

    SUGGESTION:
        1) You will need a counter to keep track of how many times the password was entered to decide the next action
        2) You might consider using a nested conditional where
            ...if it is the third incorrect guess the program asks if you are human,
            otherwise it just says incorrect password and asks again
"""
