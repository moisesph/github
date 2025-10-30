"""
Author: Moises Pleytez

Purpose: Give the change to the customer of the meal

"""


child_price = float(input("What is the price of a child's meal? $"))
adult_price = float(input("What is the price of an adult's meal? $"))
child_quantity = int(input("How many children are there? "))
adult_quantity = int(input("How many adults are there? "))

subtotal_child =  child_quantity * child_price
subtotal_adult = adult_quantity * adult_price

subtotal = subtotal_child + subtotal_adult

print(f"\nSubtotal: ${subtotal:.2f}")


tax = float(input("\nWhat is the sales tax rate? %"))
sales_tax = tax * subtotal / 100
print(f"\nSales Tax: ${sales_tax:.2f}")


total = subtotal + sales_tax
print (f"Total: ${total:.2f}")

payment_amount = float(input("What is the payment amount? $"))
change = payment_amount - total 
print(f"\nChange: ${change:.2f} ")