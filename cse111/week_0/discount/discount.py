from datetime import datetime 

DISCOUNT_DAYS= [1,2,3]
DISCOUNT_RATE = .1
TAX_RATE = .06
subtotal = 0
today = 0
discount = 0
quantity = 1


while quantity != 0:
    quantity = int(input("Please enter the quantity of items: "))
    if quantity != 0:
        price = float(input("How much it is? $"))
        subtotal = quantity * price


tax = round(subtotal * TAX_RATE,2)
today = datetime.now()
day = today.weekday()


if day in DISCOUNT_DAYS: 
    if subtotal >= 50:
        discount = round(subtotal * DISCOUNT_RATE,2)
        subtotal = round(subtotal - discount,2)

    else: 
        add_more = round(50 - subtotal,2)
        print(f"You can get a discount if you add {add_more:.2f}$ more")

total = round(subtotal + tax,2)

print(f"Subtotal Order {subtotal:.2f}")
print(f"Discount {discount:.2f}")
print(f"Tax {tax:.2f}")
print(f"total Due {total:.2f}")