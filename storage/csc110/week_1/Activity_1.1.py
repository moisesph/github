"""
Author: Moises Pleytez

Purpose: Say the name like James

"""

first_name = input(f"What is your first name? ")
last_name = input(f"What is your last name? ")

print (f"Your name is {last_name.capitalize()},")
print (f"{first_name.capitalize()} {last_name.capitalize()}")

# Be aware that there are many ways to do the formatting of that line, such as:
# print("Your name is " + last + ", " + first + " " + last + ".")
# print("Your name is {}, {} {}.".format(last, first, last))
# print("Your name is {0}, {1} {0}.".format(last, first))

""" 
I could make it like # This is for the the first part of the activity
print(f"Your name is {last}, {first} {last}.")

# This is for the the second part, where we adjust the capitalization
print(f"Your name is {last.title()}, {first.title()} {last.title()}.")

"""