"""
Author: Moises Pleytez

Purpose: Practice mathematical expressions.

"""

age = int(input("How old are you? ")) + 1
print(f"On your next birthday, you will be {age}\n")

eggs_quantity = int(input("How many egg cartoons do you have? ")) * 12
print(f"You have {eggs_quantity} eggs\n")

cookies_quantity = float(input("How many cookies do you have? "))
people_quantity = int(input("How many people are there? "))

assignment_cookies = cookies_quantity / people_quantity

print(f"Each person may have {assignment_cookies} cookies")