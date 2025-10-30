"""
Author: Moises Pleytez

purpose: Check if the person is elegible for a loan

"""

print ("Please rate the following questions regarding your reality from 1 - 10 stars: ")

loan = int(input("How much dollars would you like to get as a loan? "))
history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

if loan >= 5:

    if history >= 7 and income >= 7:
        qualify = True   

    elif (history >= 7 or income >= 7) and down_payment >= 5:
        qualify = True
        
    elif not history >=7 or income >=7: 
        qualify = False

    elif history >= 7 and income>= 7:
        qualify = False


if not loan >= 5: 


    if income >= 7 or down_payment >= 7: 
        qualify = True   

    elif income >= 4 and down_payment >= 4: 
        qualify = True 

    elif loan < 4: 
        qualify = False

    else: 
        qualify = False


if qualify: 
    print("You qualify!")
else:
    print("You don't qualify :(")